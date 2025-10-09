#!/usr/bin/env python3
"""
Repository Inventory and Duplicate Detection Script

Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

This script performs a comprehensive inventory of repository files, computes
SHA-1 hashes, and detects exact duplicates.

Outputs:
- repo_index.csv: Complete file inventory with metadata
- duplicates.csv: Detected exact duplicate files

Usage:
    python scripts/audit_inventory.py [--output-dir OUTPUT_DIR] [--exclude PATTERN]

Requirements:
    Python 3.7+
    Standard library only (no external dependencies)
"""

import os
import sys
import csv
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Tuple
from collections import defaultdict


def compute_sha1(filepath: Path) -> str:
    """
    Compute SHA-1 hash of a file.
    
    Args:
        filepath: Path to the file
        
    Returns:
        Hexadecimal SHA-1 hash string
    """
    sha1 = hashlib.sha1()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha1.update(chunk)
        return sha1.hexdigest()
    except (IOError, OSError) as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
        return "ERROR"


def get_file_metadata(filepath: Path, repo_root: Path) -> Dict:
    """
    Gather metadata about a file.
    
    Args:
        filepath: Path to the file
        repo_root: Root directory of the repository
        
    Returns:
        Dictionary containing file metadata
    """
    stat = filepath.stat()
    relative_path = filepath.relative_to(repo_root)
    
    return {
        'path': str(relative_path),
        'absolute_path': str(filepath),
        'size_bytes': stat.st_size,
        'modified_time': datetime.fromtimestamp(stat.st_mtime).isoformat(),
        'extension': filepath.suffix,
        'sha1': compute_sha1(filepath),
        'directory': str(relative_path.parent),
        'filename': filepath.name
    }


def should_exclude(path: Path, exclude_patterns: List[str]) -> bool:
    """
    Check if a path should be excluded based on patterns.
    
    Args:
        path: Path to check
        exclude_patterns: List of patterns to exclude
        
    Returns:
        True if path should be excluded, False otherwise
    """
    path_str = str(path)
    
    # Default exclusions
    default_excludes = {
        '.git', '__pycache__', 'node_modules', '.venv', 'venv',
        '.pytest_cache', '.mypy_cache', '.tox', 'dist', 'build',
        '.eggs', '*.pyc', '*.pyo', '*.pyd', '.DS_Store', 'Thumbs.db'
    }
    
    # Check default exclusions
    for exclude in default_excludes:
        if exclude.startswith('*.'):
            if path_str.endswith(exclude[1:]):
                return True
        elif exclude in path.parts:
            return True
    
    # Check custom exclusions
    for pattern in exclude_patterns:
        if pattern in path_str:
            return True
    
    return False


def inventory_repository(repo_root: Path, exclude_patterns: List[str] = None) -> List[Dict]:
    """
    Create a complete inventory of repository files.
    
    Args:
        repo_root: Root directory of the repository
        exclude_patterns: Optional list of patterns to exclude
        
    Returns:
        List of file metadata dictionaries
    """
    if exclude_patterns is None:
        exclude_patterns = []
    
    inventory = []
    
    print(f"Scanning repository: {repo_root}")
    
    for root, dirs, files in os.walk(repo_root):
        root_path = Path(root)
        
        # Filter out excluded directories (modify dirs in-place)
        dirs[:] = [d for d in dirs if not should_exclude(root_path / d, exclude_patterns)]
        
        for filename in files:
            filepath = root_path / filename
            
            if should_exclude(filepath, exclude_patterns):
                continue
            
            metadata = get_file_metadata(filepath, repo_root)
            inventory.append(metadata)
            
            if len(inventory) % 100 == 0:
                print(f"Processed {len(inventory)} files...", end='\r')
    
    print(f"\nTotal files inventoried: {len(inventory)}")
    return inventory


def find_duplicates(inventory: List[Dict]) -> List[Tuple[str, List[str]]]:
    """
    Find exact duplicate files based on SHA-1 hash.
    
    Args:
        inventory: List of file metadata dictionaries
        
    Returns:
        List of tuples (hash, [paths]) for duplicate files
    """
    hash_to_paths = defaultdict(list)
    
    for item in inventory:
        if item['sha1'] != 'ERROR' and item['size_bytes'] > 0:
            hash_to_paths[item['sha1']].append(item['path'])
    
    # Filter to only duplicates (more than one path per hash)
    duplicates = [(h, paths) for h, paths in hash_to_paths.items() if len(paths) > 1]
    
    print(f"Found {len(duplicates)} groups of duplicate files")
    return duplicates


def write_inventory_csv(inventory: List[Dict], output_path: Path):
    """
    Write inventory to CSV file.
    
    Args:
        inventory: List of file metadata dictionaries
        output_path: Path to output CSV file
    """
    if not inventory:
        print("No inventory data to write")
        return
    
    fieldnames = ['path', 'size_bytes', 'modified_time', 'extension', 
                  'sha1', 'directory', 'filename', 'absolute_path']
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in sorted(inventory, key=lambda x: x['path']):
            writer.writerow(item)
    
    print(f"Inventory written to: {output_path}")


def write_duplicates_csv(duplicates: List[Tuple[str, List[str]]], 
                        inventory: List[Dict], output_path: Path):
    """
    Write duplicates report to CSV file.
    
    Args:
        duplicates: List of (hash, paths) tuples
        inventory: Original inventory for size lookup
        output_path: Path to output CSV file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create hash to size mapping
    hash_to_size = {item['sha1']: item['size_bytes'] for item in inventory}
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sha1', 'size_bytes', 'duplicate_count', 'paths', 'wasted_bytes'])
        
        for sha1, paths in sorted(duplicates, key=lambda x: len(x[1]), reverse=True):
            size = hash_to_size.get(sha1, 0)
            duplicate_count = len(paths)
            wasted_bytes = size * (duplicate_count - 1)
            paths_str = '; '.join(sorted(paths))
            
            writer.writerow([sha1, size, duplicate_count, paths_str, wasted_bytes])
    
    print(f"Duplicates report written to: {output_path}")
    
    # Print summary
    total_wasted = sum(hash_to_size.get(h, 0) * (len(p) - 1) for h, p in duplicates)
    print(f"\nDuplicate Summary:")
    print(f"  Total duplicate groups: {len(duplicates)}")
    print(f"  Total wasted space: {total_wasted:,} bytes ({total_wasted / 1024 / 1024:.2f} MB)")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Inventory repository files and detect duplicates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage (outputs to artifacts/)
  python scripts/audit_inventory.py
  
  # Custom output directory
  python scripts/audit_inventory.py --output-dir outputs/
  
  # Exclude specific patterns
  python scripts/audit_inventory.py --exclude "temp" --exclude "backup"
        """
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='artifacts',
        help='Output directory for CSV files (default: artifacts/)'
    )
    
    parser.add_argument(
        '--exclude',
        action='append',
        default=[],
        help='Additional patterns to exclude (can be specified multiple times)'
    )
    
    parser.add_argument(
        '--repo-root',
        type=str,
        default='.',
        help='Repository root directory (default: current directory)'
    )
    
    args = parser.parse_args()
    
    repo_root = Path(args.repo_root).resolve()
    output_dir = Path(args.output_dir)
    
    if not repo_root.exists():
        print(f"Error: Repository root does not exist: {repo_root}", file=sys.stderr)
        sys.exit(1)
    
    print("=" * 70)
    print("Repository Audit Inventory")
    print("=" * 70)
    print(f"Repository: {repo_root}")
    print(f"Output directory: {output_dir}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)
    print()
    
    # Perform inventory
    inventory = inventory_repository(repo_root, args.exclude)
    
    # Find duplicates
    duplicates = find_duplicates(inventory)
    
    # Write outputs
    write_inventory_csv(inventory, output_dir / 'repo_index.csv')
    write_duplicates_csv(duplicates, inventory, output_dir / 'duplicates.csv')
    
    print("\n" + "=" * 70)
    print("Audit complete!")
    print("=" * 70)


if __name__ == '__main__':
    main()
