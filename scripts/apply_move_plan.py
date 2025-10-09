#!/usr/bin/env python3
"""
Apply Move Plan Script

Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

This script reads a proposed_move_plan.csv file and generates git operations
to reorganize repository files. Includes dry-run mode, safety checks, and
backup functionality.

Usage:
    python scripts/apply_move_plan.py [--plan PLAN_CSV] [--dry-run] [--backup]

Requirements:
    Python 3.7+
    git command-line tool

Safety Features:
    - Dry-run mode (default): Shows what would be done without making changes
    - Backup mode: Creates timestamped backup before applying changes
    - Validation checks: Verifies source files exist and targets don't
    - Interactive confirmation for destructive operations
    - Detailed logging of all operations
"""

import os
import sys
import csv
import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional


class MoveOperation:
    """Represents a single move/reorganization operation."""
    
    def __init__(self, current_path: str, proposed_path: str, 
                 confidence: str, reason: str, action: str):
        self.current_path = Path(current_path)
        self.proposed_path = Path(proposed_path)
        self.confidence = confidence
        self.reason = reason
        self.action = action.lower()
        self.status = "pending"
        self.error_message = None
    
    def __repr__(self):
        return f"MoveOperation({self.action}: {self.current_path} -> {self.proposed_path})"


def load_move_plan(plan_path: Path) -> List[MoveOperation]:
    """
    Load move plan from CSV file.
    
    Args:
        plan_path: Path to CSV file
        
    Returns:
        List of MoveOperation objects
    """
    operations = []
    
    try:
        with open(plan_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            required_columns = {'current_path', 'proposed_path', 'confidence', 'reason', 'action'}
            if not required_columns.issubset(reader.fieldnames):
                print(f"Error: CSV must contain columns: {required_columns}", file=sys.stderr)
                sys.exit(1)
            
            for row in reader:
                if row['current_path'].strip() and row['action'].strip():
                    operations.append(MoveOperation(
                        current_path=row['current_path'],
                        proposed_path=row['proposed_path'],
                        confidence=row['confidence'],
                        reason=row['reason'],
                        action=row['action']
                    ))
    
    except FileNotFoundError:
        print(f"Error: Plan file not found: {plan_path}", file=sys.stderr)
        sys.exit(1)
    except csv.Error as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)
    
    return operations


def validate_operations(operations: List[MoveOperation], repo_root: Path) -> Tuple[List[MoveOperation], List[str]]:
    """
    Validate move operations.
    
    Args:
        operations: List of MoveOperation objects
        repo_root: Repository root directory
        
    Returns:
        Tuple of (valid_operations, errors)
    """
    valid_ops = []
    errors = []
    
    for op in operations:
        # Check if action is valid
        valid_actions = {'move', 'delete', 'merge', 'propose'}
        if op.action not in valid_actions:
            errors.append(f"Invalid action '{op.action}' for {op.current_path}")
            continue
        
        # For 'propose' action, no file operations needed
        if op.action == 'propose':
            continue
        
        # Check if source exists
        source_full = repo_root / op.current_path
        if not source_full.exists():
            errors.append(f"Source does not exist: {op.current_path}")
            op.status = "error"
            op.error_message = "Source not found"
            continue
        
        # For move operations, check target doesn't exist
        if op.action == 'move':
            target_full = repo_root / op.proposed_path
            if target_full.exists():
                errors.append(f"Target already exists: {op.proposed_path}")
                op.status = "error"
                op.error_message = "Target already exists"
                continue
        
        valid_ops.append(op)
    
    return valid_ops, errors


def create_backup(repo_root: Path) -> Optional[Path]:
    """
    Create a backup of the repository.
    
    Args:
        repo_root: Repository root directory
        
    Returns:
        Path to backup directory or None if failed
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = repo_root.parent / f"backup_{repo_root.name}_{timestamp}"
    
    print(f"Creating backup at: {backup_dir}")
    
    try:
        # Copy entire repository
        shutil.copytree(repo_root, backup_dir, 
                       ignore=shutil.ignore_patterns('.git', '__pycache__', 'node_modules', 'venv'))
        print(f"✓ Backup created successfully")
        return backup_dir
    except (OSError, shutil.Error) as e:
        print(f"✗ Backup failed: {e}", file=sys.stderr)
        return None


def execute_git_mv(source: Path, target: Path, repo_root: Path, dry_run: bool = True) -> bool:
    """
    Execute git mv command.
    
    Args:
        source: Source file path (relative to repo)
        target: Target file path (relative to repo)
        repo_root: Repository root directory
        dry_run: If True, only print command without executing
        
    Returns:
        True if successful, False otherwise
    """
    # Create target directory if needed
    target_dir = target.parent
    
    if not dry_run:
        (repo_root / target_dir).mkdir(parents=True, exist_ok=True)
    
    # Build git mv command
    cmd = ['git', 'mv', str(source), str(target)]
    
    if dry_run:
        print(f"  [DRY-RUN] Would execute: {' '.join(cmd)}")
        return True
    else:
        print(f"  Executing: {' '.join(cmd)}")
        try:
            result = subprocess.run(
                cmd,
                cwd=repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"  ✓ Success")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Failed: {e.stderr}", file=sys.stderr)
            return False


def execute_git_rm(path: Path, repo_root: Path, dry_run: bool = True) -> bool:
    """
    Execute git rm command.
    
    Args:
        path: File path to remove (relative to repo)
        repo_root: Repository root directory
        dry_run: If True, only print command without executing
        
    Returns:
        True if successful, False otherwise
    """
    cmd = ['git', 'rm', str(path)]
    
    if dry_run:
        print(f"  [DRY-RUN] Would execute: {' '.join(cmd)}")
        return True
    else:
        print(f"  Executing: {' '.join(cmd)}")
        try:
            result = subprocess.run(
                cmd,
                cwd=repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"  ✓ Success")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Failed: {e.stderr}", file=sys.stderr)
            return False


def apply_operations(operations: List[MoveOperation], repo_root: Path, 
                    dry_run: bool = True) -> Dict[str, int]:
    """
    Apply move operations.
    
    Args:
        operations: List of valid MoveOperation objects
        repo_root: Repository root directory
        dry_run: If True, only simulate operations
        
    Returns:
        Dictionary with operation statistics
    """
    stats = {'success': 0, 'failed': 0, 'skipped': 0}
    
    for i, op in enumerate(operations, 1):
        print(f"\n[{i}/{len(operations)}] Processing: {op.current_path}")
        print(f"  Action: {op.action}")
        print(f"  Reason: {op.reason}")
        print(f"  Confidence: {op.confidence}")
        
        if op.action == 'move':
            print(f"  Target: {op.proposed_path}")
            success = execute_git_mv(op.current_path, op.proposed_path, repo_root, dry_run)
            if success:
                stats['success'] += 1
                op.status = "completed" if not dry_run else "simulated"
            else:
                stats['failed'] += 1
                op.status = "failed"
        
        elif op.action == 'delete':
            success = execute_git_rm(op.current_path, repo_root, dry_run)
            if success:
                stats['success'] += 1
                op.status = "completed" if not dry_run else "simulated"
            else:
                stats['failed'] += 1
                op.status = "failed"
        
        elif op.action == 'merge':
            print(f"  ⚠ MERGE action requires manual intervention")
            print(f"  Target: {op.proposed_path}")
            print(f"  Please manually merge content and then delete source")
            stats['skipped'] += 1
            op.status = "manual_required"
        
        else:
            print(f"  ℹ Skipping action '{op.action}'")
            stats['skipped'] += 1
            op.status = "skipped"
    
    return stats


def write_execution_log(operations: List[MoveOperation], stats: Dict[str, int], 
                       output_path: Path, dry_run: bool):
    """
    Write execution log to file.
    
    Args:
        operations: List of MoveOperation objects with status
        stats: Operation statistics
        output_path: Path to output log file
        dry_run: Whether this was a dry run
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Move Plan Execution Log\n")
        f.write(f"========================\n\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}\n")
        f.write(f"\nStatistics:\n")
        f.write(f"  Success: {stats['success']}\n")
        f.write(f"  Failed: {stats['failed']}\n")
        f.write(f"  Skipped: {stats['skipped']}\n")
        f.write(f"  Total: {sum(stats.values())}\n")
        f.write(f"\nOperations:\n")
        f.write(f"-----------\n\n")
        
        for op in operations:
            f.write(f"Action: {op.action}\n")
            f.write(f"Source: {op.current_path}\n")
            if op.proposed_path:
                f.write(f"Target: {op.proposed_path}\n")
            f.write(f"Status: {op.status}\n")
            if op.error_message:
                f.write(f"Error: {op.error_message}\n")
            f.write(f"Reason: {op.reason}\n")
            f.write(f"\n")
    
    print(f"\nExecution log written to: {output_path}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Apply repository reorganization plan',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run (safe, shows what would happen)
  python scripts/apply_move_plan.py --plan proposed_move_plan.csv --dry-run
  
  # Create backup and apply changes
  python scripts/apply_move_plan.py --plan proposed_move_plan.csv --backup --apply
  
  # Apply without confirmation (dangerous!)
  python scripts/apply_move_plan.py --plan proposed_move_plan.csv --apply --force

Safety Notes:
  - Always run with --dry-run first to review changes
  - Use --backup to create a backup before applying changes
  - Review the plan CSV carefully before applying
  - Operations are logged to artifacts/move_execution_log.txt
        """
    )
    
    parser.add_argument(
        '--plan',
        type=str,
        default='proposed_move_plan.csv',
        help='Path to move plan CSV file (default: proposed_move_plan.csv)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        default=True,
        help='Simulate operations without making changes (default)'
    )
    
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Actually apply the changes (use with caution!)'
    )
    
    parser.add_argument(
        '--backup',
        action='store_true',
        help='Create backup before applying changes'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Skip confirmation prompts (dangerous!)'
    )
    
    parser.add_argument(
        '--repo-root',
        type=str,
        default='.',
        help='Repository root directory (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Determine if this is a dry run
    dry_run = not args.apply
    
    plan_path = Path(args.plan)
    repo_root = Path(args.repo_root).resolve()
    
    if not plan_path.exists():
        print(f"Error: Plan file not found: {plan_path}", file=sys.stderr)
        sys.exit(1)
    
    print("=" * 70)
    print("Repository Reorganization Plan Application")
    print("=" * 70)
    print(f"Plan file: {plan_path}")
    print(f"Repository: {repo_root}")
    print(f"Mode: {'DRY-RUN (safe)' if dry_run else 'LIVE (will make changes!)'}")
    print(f"Backup: {'Yes' if args.backup else 'No'}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)
    print()
    
    # Load and validate operations
    print("Loading move plan...")
    operations = load_move_plan(plan_path)
    print(f"Loaded {len(operations)} operations\n")
    
    print("Validating operations...")
    valid_ops, errors = validate_operations(operations, repo_root)
    
    if errors:
        print(f"\n⚠ Validation errors found:")
        for error in errors:
            print(f"  - {error}")
        print(f"\n{len(valid_ops)} operations are valid, {len(errors)} have errors")
        
        if not args.force:
            response = input("\nContinue with valid operations only? (yes/no): ")
            if response.lower() != 'yes':
                print("Aborted by user")
                sys.exit(1)
    else:
        print(f"✓ All {len(valid_ops)} operations validated successfully\n")
    
    if not valid_ops:
        print("No valid operations to execute")
        sys.exit(0)
    
    # Create backup if requested
    if args.backup and not dry_run:
        backup_path = create_backup(repo_root)
        if not backup_path:
            print("Backup failed, aborting")
            sys.exit(1)
        print()
    
    # Confirm before applying
    if not dry_run and not args.force:
        print("⚠ WARNING: This will make REAL changes to your repository!")
        print(f"⚠ {len(valid_ops)} operations will be executed")
        response = input("\nAre you absolutely sure you want to continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted by user")
            sys.exit(1)
        print()
    
    # Apply operations
    print("=" * 70)
    print(f"{'Simulating' if dry_run else 'Applying'} operations...")
    print("=" * 70)
    
    stats = apply_operations(valid_ops, repo_root, dry_run)
    
    # Write execution log
    log_path = Path('artifacts') / 'move_execution_log.txt'
    write_execution_log(operations, stats, log_path, dry_run)
    
    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Success: {stats['success']}")
    print(f"Failed: {stats['failed']}")
    print(f"Skipped: {stats['skipped']}")
    print(f"Total: {sum(stats.values())}")
    
    if dry_run:
        print("\n✓ This was a DRY-RUN. No changes were made.")
        print("  To apply changes, run with --apply flag")
    else:
        print("\n✓ Operations completed!")
        print("  Review changes with: git status")
        print("  Create commit with: git commit -m 'Apply reorganization plan'")
    
    print("=" * 70)


if __name__ == '__main__':
    main()
