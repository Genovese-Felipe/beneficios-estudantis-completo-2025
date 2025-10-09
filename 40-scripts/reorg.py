#!/usr/bin/env python3
"""
Repository Reorganization and Deduplication Script

This script reorganizes the repository structure, identifies duplicates,
and maintains comprehensive logs of all operations.

Usage:
    python reorg.py [--dry-run] [--spec SPEC_FILE]
    python reorg.py --apply [--spec SPEC_FILE]
"""

import argparse
import csv
import hashlib
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install it with: pip install PyYAML")
    sys.exit(1)


class ReorgTool:
    """Repository reorganization and deduplication tool."""

    def __init__(self, spec_file: str, dry_run: bool = True):
        self.spec_file = spec_file
        self.dry_run = dry_run
        self.operations_log = []
        self.spec = None
        self.repo_root = Path(__file__).parent.parent
        self.start_time = datetime.utcnow()

    def load_spec(self) -> Dict:
        """Load the reorganization specification from YAML file."""
        spec_path = self.repo_root / self.spec_file
        if not spec_path.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_path}")

        with open(spec_path, 'r', encoding='utf-8') as f:
            self.spec = yaml.safe_load(f)

        # Override dry_run if specified on command line
        if not self.dry_run and self.spec.get('dry_run', True):
            print("Warning: Specification has dry_run: true but --apply was used.")
            print("Continuing with dry run mode for safety.")
            self.dry_run = True
        elif self.dry_run:
            self.spec['dry_run'] = True

        return self.spec

    def log_operation(self, operation: str, details: str):
        """Log an operation for audit trail."""
        timestamp = datetime.utcnow().isoformat() + 'Z'
        log_entry = f"{timestamp} - {operation}: {details}"
        self.operations_log.append(log_entry)
        print(f"  {operation}: {details}")

    def ensure_directories(self):
        """Create all required directories from specification."""
        print("\n=== Phase 1: Ensuring Directory Structure ===")
        create_dirs = self.spec.get('create_dirs', [])

        for dir_spec in create_dirs:
            dir_path = self.repo_root / dir_spec
            if dir_path.exists():
                self.log_operation("EXISTS", str(dir_path.relative_to(self.repo_root)))
            else:
                if not self.dry_run:
                    dir_path.mkdir(parents=True, exist_ok=True)
                self.log_operation("CREATE", str(dir_path.relative_to(self.repo_root)))

    def apply_moves(self):
        """Apply file moves according to specification."""
        print("\n=== Phase 2: Applying File Moves ===")
        move_rules = self.spec.get('move_rules', [])

        for rule in move_rules:
            source = self.repo_root / rule['source']
            destination = self.repo_root / rule['destination']

            if not source.exists():
                self.log_operation("SKIP", f"{rule['source']} (source not found)")
                continue

            # Handle directory moves
            if source.is_dir():
                if not self.dry_run:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(source), str(destination))
                self.log_operation("MOVE_DIR", f"{rule['source']} -> {rule['destination']}")
            else:
                # Handle file moves
                if not self.dry_run:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(source), str(destination))
                self.log_operation("MOVE_FILE", f"{rule['source']} -> {rule['destination']}")

    def compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA-256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def find_duplicates(self) -> Dict[str, List[Path]]:
        """Find duplicate files based on SHA-256 hash."""
        print("\n=== Phase 3: Detecting Duplicates ===")

        # Get exclusions from spec
        exclude_patterns = self.spec.get('dedup_config', {}).get('exclude_patterns', [])
        exclude_dirs = set(self.spec.get('dedup_config', {}).get('exclude_dirs', []))

        # Build hash table
        hash_table: Dict[str, List[Path]] = {}

        for root, dirs, files in os.walk(self.repo_root):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]

            for file in files:
                file_path = Path(root) / file

                # Skip if matches exclusion pattern
                skip = False
                for pattern in exclude_patterns:
                    if pattern in str(file_path):
                        skip = True
                        break
                if skip:
                    continue

                try:
                    file_hash = self.compute_file_hash(file_path)
                    if file_hash not in hash_table:
                        hash_table[file_hash] = []
                    hash_table[file_hash].append(file_path)
                except Exception as e:
                    self.log_operation("ERROR", f"Failed to hash {file_path}: {e}")

        # Filter to only duplicates (hash with multiple files)
        duplicates = {h: files for h, files in hash_table.items() if len(files) > 1}

        print(f"Found {len(duplicates)} sets of duplicate files")
        return duplicates

    def archive_duplicates(self, duplicates: Dict[str, List[Path]]):
        """Archive duplicate files."""
        print("\n=== Phase 4: Archiving Duplicates ===")

        archive_dir = self.repo_root / "90-archive" / "duplicates"
        index_file = archive_dir / "duplicates-index.csv"

        # Prepare CSV data
        csv_rows = []

        for file_hash, file_list in duplicates.items():
            if len(file_list) < 2:
                continue

            # Keep the first file, archive the rest
            original = file_list[0]
            duplicates_to_archive = file_list[1:]

            for dup in duplicates_to_archive:
                try:
                    # Prepare archive location preserving some path structure
                    rel_path = dup.relative_to(self.repo_root)
                    archive_path = archive_dir / rel_path

                    # Archive the file
                    if not self.dry_run:
                        archive_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(dup), str(archive_path))

                    # Record in index
                    csv_row = {
                        'original_path': str(original.relative_to(self.repo_root)),
                        'duplicate_path': str(rel_path),
                        'sha256_hash': file_hash,
                        'size_bytes': original.stat().st_size if original.exists() else 0,
                        'archived_date': datetime.utcnow().isoformat() + 'Z',
                        'detected_by': 'reorg.py'
                    }
                    csv_rows.append(csv_row)

                    self.log_operation(
                        "ARCHIVE_DUP",
                        f"{rel_path} -> 90-archive/duplicates/{rel_path}"
                    )

                except Exception as e:
                    self.log_operation("ERROR", f"Failed to archive {dup}: {e}")

        # Write to CSV index
        if csv_rows and not self.dry_run:
            # Read existing entries
            existing_rows = []
            if index_file.exists():
                with open(index_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    existing_rows = list(reader)

            # Write all entries
            with open(index_file, 'w', encoding='utf-8', newline='') as f:
                fieldnames = [
                    'original_path', 'duplicate_path', 'sha256_hash',
                    'size_bytes', 'archived_date', 'detected_by'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(existing_rows)
                writer.writerows(csv_rows)

        print(f"Would archive {len(csv_rows)} duplicate files" if self.dry_run else f"Archived {len(csv_rows)} duplicate files")

    def save_operations_log(self):
        """Save operations log to file."""
        print("\n=== Saving Operations Log ===")

        log_dir = self.repo_root / "21-github-and-copilot-tech" / "02-operations-logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = self.start_time.strftime("%Y%m%d-%H%M%S")
        log_file = log_dir / f"reorg-{timestamp}.log"

        mode_str = "DRY-RUN" if self.dry_run else "APPLIED"

        log_content = [
            f"Repository Reorganization Log - {mode_str}",
            f"Started: {self.start_time.isoformat()}Z",
            f"Completed: {datetime.utcnow().isoformat()}Z",
            f"Specification: {self.spec_file}",
            "",
            "=== Operations ===",
            ""
        ]
        log_content.extend(self.operations_log)

        if not self.dry_run:
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(log_content))
            print(f"Operations log saved to: {log_file.relative_to(self.repo_root)}")
        else:
            print(f"Would save operations log to: {log_file.relative_to(self.repo_root)}")
            print("\n=== Operations Log Preview ===")
            for line in log_content[-20:]:  # Show last 20 lines
                print(line)

    def run(self):
        """Execute the reorganization process."""
        print("=" * 60)
        print("Repository Reorganization Tool")
        print("=" * 60)
        print(f"Mode: {'DRY-RUN (no changes will be made)' if self.dry_run else 'APPLY (changes will be made)'}")
        print(f"Specification: {self.spec_file}")
        print(f"Repository root: {self.repo_root}")
        print("=" * 60)

        try:
            # Load specification
            print("\nLoading specification...")
            self.load_spec()
            print(f"Specification loaded: {len(self.spec.get('create_dirs', []))} dirs, "
                  f"{len(self.spec.get('move_rules', []))} move rules")

            # Phase 1: Ensure directories
            self.ensure_directories()

            # Phase 2: Apply moves
            if self.spec.get('move_rules'):
                self.apply_moves()

            # Phase 3 & 4: Find and archive duplicates
            if self.spec.get('dedup_config', {}).get('enabled', True):
                duplicates = self.find_duplicates()
                if duplicates:
                    self.archive_duplicates(duplicates)
            else:
                print("\n=== Deduplication Disabled ===")

            # Save operations log
            self.save_operations_log()

            print("\n" + "=" * 60)
            print("Reorganization completed successfully!")
            if self.dry_run:
                print("\nThis was a DRY RUN. No changes were made.")
                print("Review the output above and run with --apply to apply changes.")
            print("=" * 60)

            return 0

        except Exception as e:
            print(f"\n!!! ERROR: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            return 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Repository reorganization and deduplication tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run with default spec (no changes made)
  python reorg.py

  # Dry run with custom spec
  python reorg.py --spec custom-spec.yaml

  # Apply changes (after reviewing dry run)
  python reorg.py --apply
        """
    )

    parser.add_argument(
        '--spec',
        default='reorg-spec.yaml',
        help='Path to reorganization specification file (default: reorg-spec.yaml)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        default=True,
        help='Preview changes without applying them (default)'
    )

    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes (use after reviewing dry-run results)'
    )

    args = parser.parse_args()

    # Determine mode
    dry_run = not args.apply

    # Run reorganization
    tool = ReorgTool(spec_file=args.spec, dry_run=dry_run)
    return tool.run()


if __name__ == '__main__':
    sys.exit(main())
