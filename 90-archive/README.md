# 90-archive

## Overview

This directory serves as the permanent storage location for deprecated, duplicate, and legacy content that is no longer actively used but must be retained for historical, reference, or compliance purposes.

## Purpose

- **Historical Preservation**: Maintain record of past content and decisions
- **Deduplication**: Store redundant copies identified during cleanup
- **Legacy Support**: Retain outdated content that may still be referenced
- **Compliance**: Meet retention requirements for certain materials

## Directory Structure

### duplicates/
Exact duplicate files identified through content-based hashing (SHA-256) during repository reorganization and cleanup operations.

**Contents:**
- Duplicate file copies (maintaining original paths in metadata)
- `duplicates-index.csv`: Comprehensive record of all duplicates
- Organized by detection date if volume grows

**Index Format:**
```csv
original_path,duplicate_path,sha256_hash,size_bytes,archived_date,detected_by
```

### legacy/
Content that is outdated or superseded but retained for reference purposes.

**Contents:**
- Deprecated documentation versions
- Old scripts and tools no longer in use
- Previous organizational structures
- Historical analyses and reports
- Superseded templates

**Organization:**
- By date (YYYY-MM-DD-description/)
- By content type (docs/, scripts/, data/)
- With README explaining context

## Archive Policies

### What Gets Archived

**Duplicates:**
- Exact file copies detected by hash comparison
- Redundant content identified manually
- Multiple versions of same document (keeping latest)

**Legacy:**
- Replaced or superseded documentation
- Deprecated scripts and tools
- Old organizational structures
- Content no longer reflecting current state
- Historical versions for reference

### What NOT to Archive

- Active content still in use
- Unique files (even if old)
- Legally required current documentation
- Content that should be deleted (use git history instead)

## Archival Process

### Automated Archival (via reorg.py)

1. **Duplicate Detection**:
   - Compute SHA-256 hash for all files
   - Identify files with matching hashes
   - Keep one copy in active location
   - Move duplicates to `90-archive/duplicates/`
   - Log in `duplicates-index.csv`

2. **Documentation**:
   - Original file location preserved in index
   - Hash value recorded for verification
   - Timestamp of archival
   - Detection method noted

### Manual Archival

1. **Identify content** for archival
2. **Document reason** for archival
3. **Create dated subdirectory** in appropriate location
4. **Move content** with original structure preserved
5. **Add README** explaining context
6. **Update references** in active documentation
7. **Log in operations logs**

## Usage Guidelines

### For Maintenance
- **Regular cleanup**: Quarterly review of archive
- **Compression**: Consider compressing old archives
- **Metadata**: Maintain comprehensive indices
- **Access tracking**: Monitor if archived content is accessed

### For Recovery
- Check `duplicates-index.csv` to find duplicate copies
- Review legacy/ subdirectory READMEs for context
- Verify content hash before restoring duplicates
- Document restoration in operations logs

### For AI Assistants
- Consult `ai_assistant_guide.yaml` for area-specific guidance
- Never delete archived content without explicit instruction
- Always update indices when archiving content
- Preserve original metadata and context

## Duplicate Index

### duplicates-index.csv

**Purpose**: Comprehensive record of all duplicate files for auditability and potential recovery.

**Schema**:
- `original_path`: Path where unique copy is retained
- `duplicate_path`: Path where duplicate was found (before archival)
- `sha256_hash`: SHA-256 hash for content verification
- `size_bytes`: File size in bytes
- `archived_date`: ISO 8601 timestamp of archival
- `detected_by`: Tool or process that identified duplicate

**Maintenance**:
- Append-only (never delete entries)
- Updated automatically by deduplication scripts
- Manually updated for manual archival
- Backed up with repository

## Recovery Procedures

### Restoring Duplicates
```bash
# Verify hash of archived file
sha256sum 90-archive/duplicates/path/to/file

# Compare with index
grep <hash> 90-archive/duplicates/duplicates-index.csv

# If verified, restore to new location
cp 90-archive/duplicates/path/to/file new/location/
```

### Restoring Legacy Content
1. Locate in legacy/ subdirectories
2. Review README for context and reason for archival
3. Assess if content is still applicable
4. Update content if needed before restoration
5. Move to appropriate active location
6. Document restoration in operations logs

## Retention Policy

### Duplicates
- **Immediate term**: Retain all duplicates for 1 year
- **Long term**: After 1 year, may delete if confirmed unnecessary
- **Verification**: Periodic hash verification to ensure integrity

### Legacy
- **Permanent retention** unless:
  - Content is provably obsolete with no historical value
  - Superseded by newer content with full coverage
  - Storage constraints require cleanup (rare)

### Compliance
- Follow organizational retention policies
- Consider legal/regulatory requirements
- Document any deletions from archive

## Storage Optimization

As archive grows, consider:
- **Compression**: Use tar.gz or zip for old archives
- **Deduplication**: Internal deduplication within archive
- **External storage**: Move very old archives to cold storage
- **Documentation**: Always maintain indices even if files moved

## Relationship to Other Areas

### 00-governance-and-origins
- Archival follows governance protocols
- Historical decisions preserved in archive

### 40-scripts
- reorg.py and other scripts populate this archive
- Scripts may reference archive for verification

### All Active Areas
- Content from any area may be archived
- Cross-reference updates needed when archiving

## Metadata Standards

### Directory READMEs in legacy/
Required sections:
- **Date Archived**: When content was moved
- **Reason**: Why content was archived
- **Superseded By**: Link to replacement if applicable
- **Original Location**: Where content lived before
- **Notes**: Any additional context

### File Naming
- Preserve original names when possible
- Add date prefix if needed: YYYY-MM-DD-original-name
- Maintain directory structure for context

## Audit Trail

All archival operations should be logged in:
```
21-github-and-copilot-tech/02-operations-logs/
```

Include:
- What was archived
- Why it was archived  
- Where it came from
- Where it went
- Who/what performed archival
- Date and time

## Future Enhancements

- Automated compression of old archives
- Archive statistics dashboard
- Search functionality across archive
- Automated retention policy enforcement
- Integration with backup systems

---

**Last Updated**: 2025-01-09  
**Status**: Initial Setup - Ready for Use  
**Maintained By**: Repository Maintenance Team

**Note**: This archive is append-only. Content is added but rarely removed. Preservation is the priority.
