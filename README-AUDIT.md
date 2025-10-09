# Repository Audit & Reorganization Toolkit

**Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09**  
*Note: Copilot is powered by AI; mistakes are possible. Review carefully.*

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Prerequisites](#prerequisites)
4. [Scripts Reference](#scripts-reference)
5. [Workflow Guide](#workflow-guide)
6. [Safety & Verification](#safety--verification)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [FAQ](#faq)

---

## Overview

### English

This toolkit provides comprehensive auditing and reorganization capabilities for the repository. It enables maintainers to:

- **Inventory all files** with SHA-1 hash tracking for exact duplicate detection
- **Normalize conversations** from various formats into structured JSONL
- **Detect semantic duplicates** using AI-powered embeddings
- **Plan reorganizations** with CSV-based move plans
- **Execute moves safely** with dry-run, backup, and validation features

**Key Principle**: This PR is **additive only** - it provides tools without moving existing content. Actual reorganization happens in future PRs using these tools.

### Português

Este toolkit fornece capacidades abrangentes de auditoria e reorganização para o repositório. Permite aos mantenedores:

- **Inventariar todos os arquivos** com rastreamento de hash SHA-1 para detecção de duplicatas exatas
- **Normalizar conversas** de vários formatos para JSONL estruturado
- **Detectar duplicatas semânticas** usando embeddings alimentados por IA
- **Planejar reorganizações** com planos de movimentação baseados em CSV
- **Executar movimentações com segurança** com recursos de simulação, backup e validação

**Princípio Chave**: Este PR é **apenas aditivo** - fornece ferramentas sem mover conteúdo existente. A reorganização real acontece em PRs futuros usando estas ferramentas.

---

## Quick Start

```bash
# 1. Clone the repository (if not already)
git clone https://github.com/Genovese-Felipe/beneficios-estudantis-completo-2025.git
cd beneficios-estudantis-completo-2025

# 2. Run file inventory
python scripts/audit_inventory.py

# 3. Review outputs
cat artifacts/repo_index.csv       # All files
cat artifacts/duplicates.csv       # Exact duplicates

# 4. Normalize conversations
python scripts/normalize_conversations.py

# 5. Review conversation data
cat artifacts/conversations.jsonl

# 6. (Optional) Detect semantic duplicates - requires installation
# pip install sentence-transformers numpy scipy
# python scripts/deduplicate_semantic.py

# 7. Create/edit move plan
nano proposed_move_plan.csv

# 8. Test move plan (DRY RUN - safe)
python scripts/apply_move_plan.py --plan proposed_move_plan.csv --dry-run

# 9. Review dry-run output
cat artifacts/move_execution_log.txt

# 10. Apply moves (ONLY after verification)
# python scripts/apply_move_plan.py --plan proposed_move_plan.csv --apply --backup
```

---

## Prerequisites

### Required

- **Python 3.7+**: All scripts require Python 3.7 or later
- **Git**: For move operations (`git mv`, `git rm`)
- **Standard Library**: No external dependencies for basic operations

### Optional (for advanced features)

For semantic duplicate detection:

```bash
pip install sentence-transformers numpy scipy

# Optional: For faster similarity search
pip install faiss-cpu
# or
pip install hnswlib
```

### Checking Requirements

```bash
# Check Python version
python --version  # Should be 3.7+

# Check Git
git --version

# Check if optional packages installed
python -c "import sentence_transformers; print('✓ sentence-transformers installed')"
python -c "import numpy; print('✓ numpy installed')"
python -c "import scipy; print('✓ scipy installed')"
```

---

## Scripts Reference

### 1. audit_inventory.py

**Purpose**: Create complete file inventory with hash-based duplicate detection

**What it does**:
- Scans all repository files (excluding .git, node_modules, etc.)
- Computes SHA-1 hash for each file
- Generates comprehensive CSV inventory
- Identifies exact duplicate files
- Calculates wasted space from duplication

**Outputs**:
- `artifacts/repo_index.csv`: Complete file inventory
- `artifacts/duplicates.csv`: Duplicate file groups

**Usage**:
```bash
# Basic usage
python scripts/audit_inventory.py

# Custom output directory
python scripts/audit_inventory.py --output-dir outputs/

# Exclude additional patterns
python scripts/audit_inventory.py --exclude "temp" --exclude "backup"

# Scan different repository
python scripts/audit_inventory.py --repo-root /path/to/repo
```

**Expected Runtime**: 1-5 seconds for typical repositories (< 1000 files)

**CSV Format** (repo_index.csv):
```csv
path,size_bytes,modified_time,extension,sha1,directory,filename,absolute_path
README.md,9495,2025-10-09T12:00:00,.md,abc123...,.,README.md,/full/path/README.md
```

**CSV Format** (duplicates.csv):
```csv
sha1,size_bytes,duplicate_count,paths,wasted_bytes
abc123...,5000,3,"file1.md; file2.md; file3.md",10000
```

---

### 2. normalize_conversations.py

**Purpose**: Parse and normalize conversation data into structured JSONL format

**What it does**:
- Scans markdown files in specified directory (default: 99-REGISTROS-HISTORICOS/)
- Detects conversation patterns (User:, Assistant:, Q:, A:)
- Extracts messages with role attribution
- Exports to JSON Lines format for easy processing
- Generates metadata summary

**Outputs**:
- `artifacts/conversations.jsonl`: Normalized conversation data (one JSON per line)
- `artifacts/conversations_metadata.json`: Statistics and summary

**Usage**:
```bash
# Basic usage (processes 99-REGISTROS-HISTORICOS/)
python scripts/normalize_conversations.py

# Custom input directory
python scripts/normalize_conversations.py --input-dir conversations/

# Custom output directory
python scripts/normalize_conversations.py --output-dir outputs/
```

**Expected Runtime**: 1-10 seconds depending on conversation count

**JSONL Format** (conversations.jsonl):
```json
{"conversation_id": "repo-reorg", "source_file": "99-REGISTROS-HISTORICOS/discussion.md", "messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}], "extracted_at": "2025-10-09T12:00:00", "metadata": {"message_count": 10}}
```

**Supported Patterns**:
- `## User:` / `## Assistant:`
- `**User**:` / `**Assistant**:`
- `Q:` / `A:`
- `Question:` / `Answer:`

---

### 3. deduplicate_semantic.py

**Purpose**: Find semantically similar documents using AI embeddings

**What it does**:
- Loads documents from repo_index.csv or directory
- Generates embeddings using sentence-transformers
- Computes cosine similarity between documents
- Identifies near-duplicates above threshold
- Provides recommendations for consolidation

**Outputs**:
- `artifacts/semantic_duplicates.csv`: Similar document pairs

**Usage**:
```bash
# Process from repo_index.csv
python scripts/deduplicate_semantic.py --input artifacts/repo_index.csv

# Process from directory
python scripts/deduplicate_semantic.py --input .

# Custom similarity threshold (0-1, higher = more similar)
python scripts/deduplicate_semantic.py --threshold 0.90

# Use different model
python scripts/deduplicate_semantic.py --model all-mpnet-base-v2

# Use FAISS for faster search (if installed)
python scripts/deduplicate_semantic.py --use-faiss
```

**Expected Runtime**: 
- Small repos (<100 docs): 10-30 seconds
- Medium repos (100-500 docs): 1-3 minutes
- Large repos (>500 docs): 5-10 minutes

**Dependencies**:
```bash
pip install sentence-transformers numpy scipy
# Optional for speed:
pip install faiss-cpu
```

**CSV Format** (semantic_duplicates.csv):
```csv
document1,document2,similarity,size1,size2,recommendation
doc1.md,doc2.md,0.9523,5000,4800,Very likely duplicate - review for merge/delete
```

**Similarity Thresholds**:
- `> 0.95`: Very likely duplicate
- `0.90-0.95`: Likely duplicate
- `0.85-0.90`: Possibly similar
- `< 0.85`: Different content

---

### 4. apply_move_plan.py

**Purpose**: Execute repository reorganization with safety checks

**What it does**:
- Reads proposed_move_plan.csv
- Validates all operations (source exists, target doesn't)
- Executes git mv/rm commands
- Creates backups (optional)
- Logs all operations
- Provides dry-run mode for testing

**Inputs**:
- `proposed_move_plan.csv`: CSV with move operations

**Outputs**:
- `artifacts/move_execution_log.txt`: Operation log
- Modified repository structure (if --apply used)

**Usage**:
```bash
# DRY RUN (safe - shows what would happen)
python scripts/apply_move_plan.py --plan proposed_move_plan.csv --dry-run

# Create backup and apply changes
python scripts/apply_move_plan.py --plan proposed_move_plan.csv --apply --backup

# Apply without confirmation (use with caution!)
python scripts/apply_move_plan.py --apply --force

# Custom plan file
python scripts/apply_move_plan.py --plan custom_plan.csv --dry-run
```

**Expected Runtime**: 
- Dry-run: <1 second
- Real execution: 1-10 seconds depending on operation count

**Safety Features**:
- ✅ Dry-run enabled by default
- ✅ Backup creation before changes
- ✅ Validation of all operations
- ✅ Detailed logging
- ✅ Rollback instructions

**Move Plan CSV Format**:
```csv
current_path,proposed_path,confidence,reason,action
old/file.md,new/file.md,high,Better organization,move
duplicate.md,,high,Exact duplicate of other file,delete
file1.md,file2.md,medium,Merge content,merge
```

**Actions**:
- `move`: Execute git mv
- `delete`: Execute git rm
- `merge`: Manual intervention required
- `propose`: Documentation only, no action

---

## Workflow Guide

### Phase 1: Understanding Current State

```bash
# Step 1: Run inventory
python scripts/audit_inventory.py

# Step 2: Review outputs
wc -l artifacts/repo_index.csv          # How many files?
cat artifacts/duplicates.csv            # Any duplicates?

# Step 3: Normalize conversations
python scripts/normalize_conversations.py

# Step 4: Review conversation data
head -n 5 artifacts/conversations.jsonl
cat artifacts/conversations_metadata.json
```

**Expected Outputs**:
- Complete file list with hashes
- Duplicate file groups (if any)
- Normalized conversation data
- Understanding of repository content

---

### Phase 2: Analyzing Content

```bash
# Step 1: Identify exact duplicates
# Review artifacts/duplicates.csv manually
# Decide which copies to keep

# Step 2: (Optional) Find semantic duplicates
pip install sentence-transformers numpy scipy
python scripts/deduplicate_semantic.py --input artifacts/repo_index.csv

# Step 3: Review semantic similarities
cat artifacts/semantic_duplicates.csv
# Look for high-similarity pairs (>0.90)

# Step 4: Read historical context
# Review normalized conversations to understand past decisions
grep -i "reorganization" artifacts/conversations.jsonl
```

**Decision Points**:
- Which duplicates to remove?
- Which similar documents to merge?
- Which directories to rename/restructure?

---

### Phase 3: Planning Reorganization

```bash
# Step 1: Create/edit move plan
nano proposed_move_plan.csv

# Step 2: Add operations with format:
# current_path,proposed_path,confidence,reason,action

# Step 3: Review plan
cat proposed_move_plan.csv
wc -l proposed_move_plan.csv  # How many operations?

# Step 4: Validate plan syntax
python -c "
import csv
with open('proposed_move_plan.csv') as f:
    reader = csv.DictReader(f)
    print(f'Valid CSV with {len(list(reader))} operations')
"
```

**Planning Tips**:
- Start with high-confidence moves only
- Group related changes
- Consider impact on existing links
- Document rationale clearly

---

### Phase 4: Testing (Dry Run)

```bash
# Step 1: Run in dry-run mode (SAFE)
python scripts/apply_move_plan.py --plan proposed_move_plan.csv --dry-run

# Step 2: Review what would happen
cat artifacts/move_execution_log.txt

# Step 3: Check for issues
# Look for validation errors in output
# Verify proposed paths make sense

# Step 4: Iterate if needed
# Edit proposed_move_plan.csv
# Re-run dry-run
# Repeat until satisfactory
```

**What to Look For**:
- ✅ All validations pass
- ✅ Paths look correct
- ✅ No surprising operations
- ❌ Any error messages

---

### Phase 5: Backup

```bash
# Option 1: Git branch (RECOMMENDED)
git checkout -b backup/before-reorg-$(date +%Y%m%d)
git push -u origin backup/before-reorg-$(date +%Y%m%d)
git checkout feature/reorg-audit-20251009  # Back to work branch

# Option 2: Local copy
cp -r . ../backup-$(date +%Y%m%d)

# Option 3: Built-in backup (during apply)
# The --backup flag creates automatic backup
```

**Verification**:
```bash
# Check backup exists
ls -la ../backup-*/

# Or check backup branch
git branch -a | grep backup
```

---

### Phase 6: Execution

```bash
# Step 1: Final review
cat proposed_move_plan.csv
cat artifacts/move_execution_log.txt  # From last dry-run

# Step 2: Apply changes WITH BACKUP
python scripts/apply_move_plan.py --plan proposed_move_plan.csv --apply --backup

# Step 3: Review git status
git status
git diff --stat

# Step 4: Verify operations
ls -R  # Check directory structure
# Test a few moved files manually
```

**Expected Output**:
- Git shows moved/deleted files
- Directory structure updated
- Execution log created

---

### Phase 7: Verification & Cleanup

```bash
# Step 1: Check for broken links
# (Manual review or use link checker tool)
grep -r "](.*\.md)" --include="*.md" | grep -v "http"

# Step 2: Verify no content lost
# Compare file counts
ls -R | wc -l  # Should match expected count

# Step 3: Test major workflows
# Open main README, follow links
# Check that documentation renders correctly

# Step 4: Update related documentation
# Edit README.md, GUIA-COMPLETO.md as needed
# Update any broken relative paths

# Step 5: Commit changes
git add .
git commit -m "refactor: apply repository reorganization plan

- Moved 99-REGISTROS-HISTORICOS to 00-foundation-origins
- Removed duplicate files
- Updated directory structure per proposed_move_plan.csv

See docs/CHANGELOG-AUDIT.md for details"

# Step 6: Push and create PR
git push -u origin feature/reorg-audit-20251009
```

---

## Safety & Verification

### Before Making Changes

✅ **Always run dry-run first**
```bash
python scripts/apply_move_plan.py --dry-run
```

✅ **Create backup**
```bash
git checkout -b backup/$(date +%Y%m%d)
git push origin backup/$(date +%Y%m%d)
```

✅ **Validate move plan**
```bash
# Check CSV syntax
python -c "import csv; list(csv.DictReader(open('proposed_move_plan.csv')))"

# Review operations manually
cat proposed_move_plan.csv
```

✅ **Review audit outputs**
```bash
cat artifacts/repo_index.csv
cat artifacts/duplicates.csv
```

### After Making Changes

✅ **Verify git status**
```bash
git status
git diff --stat
```

✅ **Check file count**
```bash
# Before: note count from repo_index.csv
# After: verify similar count (accounting for deletions)
find . -type f ! -path "./.git/*" | wc -l
```

✅ **Test links**
```bash
# Check markdown internal links
grep -r "](.*\.md)" --include="*.md"
```

✅ **Review moved files**
```bash
# Spot check moved files exist in new location
ls -la 00-foundation-origins/conversations/
```

### Rollback Procedures

If something goes wrong:

**Git-based rollback**:
```bash
# View recent commits
git log --oneline -10

# Revert specific commit
git revert <commit-sha>

# Or reset to before changes (DESTRUCTIVE)
git reset --hard <commit-before-changes>
```

**Backup restoration**:
```bash
# From backup branch
git checkout backup/before-reorg-20251009
git checkout -b recovery
# Cherry-pick good commits if needed

# From local copy
rm -rf ./*  # ⚠️ DANGEROUS
cp -r ../backup-20251009/* .
git status
```

---

## Examples

### Example 1: Finding and Removing Exact Duplicates

```bash
# Run inventory
python scripts/audit_inventory.py

# Review duplicates
cat artifacts/duplicates.csv

# Example output:
# sha1,size_bytes,duplicate_count,paths,wasted_bytes
# abc123,5000,2,"file1.md; file2.md",5000

# Create move plan to remove duplicate
echo "current_path,proposed_path,confidence,reason,action" > proposed_move_plan.csv
echo "file2.md,,high,Exact duplicate of file1.md,delete" >> proposed_move_plan.csv

# Test and apply
python scripts/apply_move_plan.py --dry-run
python scripts/apply_move_plan.py --apply --backup

# Commit
git commit -m "chore: remove duplicate file2.md"
```

---

### Example 2: Reorganizing Historical Records

```bash
# Normalize conversations first
python scripts/normalize_conversations.py

# Create move plan for 99-REGISTROS-HISTORICOS → 00-foundation-origins
cat > proposed_move_plan.csv << EOF
current_path,proposed_path,confidence,reason,action
99-REGISTROS-HISTORICOS/README.md,00-foundation-origins/conversations/README.md,high,Restructure for better organization,move
99-REGISTROS-HISTORICOS/conversation1.md,00-foundation-origins/conversations/raw/2025-01-08-conversation1.md,high,Move to raw conversations with date,move
EOF

# Test
python scripts/apply_move_plan.py --dry-run

# Review
cat artifacts/move_execution_log.txt

# Apply if satisfied
python scripts/apply_move_plan.py --apply --backup
```

---

### Example 3: Finding Semantic Duplicates

```bash
# Install dependencies
pip install sentence-transformers numpy scipy

# Run semantic analysis
python scripts/deduplicate_semantic.py --input artifacts/repo_index.csv --threshold 0.88

# Review results
cat artifacts/semantic_duplicates.csv

# Example output:
# document1,document2,similarity,size1,size2,recommendation
# guide1.md,guide2.md,0.9234,10000,9500,Likely duplicate - review content carefully

# Manual review: compare the files
diff guide1.md guide2.md

# Decide: merge, keep separate, or delete one
# Create move plan accordingly
```

---

### Example 4: Complete Workflow

```bash
# Phase 1: Audit
python scripts/audit_inventory.py
python scripts/normalize_conversations.py
python scripts/deduplicate_semantic.py --input artifacts/repo_index.csv

# Phase 2: Analyze outputs
cat artifacts/repo_index.csv | wc -l           # File count
cat artifacts/duplicates.csv                   # Exact dupes
cat artifacts/semantic_duplicates.csv          # Similar content
cat artifacts/conversations_metadata.json      # Conversation stats

# Phase 3: Create comprehensive plan
nano proposed_move_plan.csv
# Add all operations: moves, deletes, merges

# Phase 4: Test thoroughly
python scripts/apply_move_plan.py --dry-run
cat artifacts/move_execution_log.txt

# Phase 5: Backup
git checkout -b backup/before-major-reorg-20251009
git push origin backup/before-major-reorg-20251009
git checkout feature/reorg-audit-20251009

# Phase 6: Execute
python scripts/apply_move_plan.py --apply --backup

# Phase 7: Verify and commit
git status
git diff --stat
# Manual verification of key files
git commit -m "refactor: comprehensive repository reorganization"
git push
```

---

## Troubleshooting

### Issue: "Module not found" error

**Problem**: Missing Python dependencies

**Solution**:
```bash
# For basic scripts (shouldn't happen - they use stdlib only)
python --version  # Verify Python 3.7+

# For semantic deduplication
pip install sentence-transformers numpy scipy

# Verify installation
python -c "import sentence_transformers; print('OK')"
```

---

### Issue: "Permission denied" on script execution

**Problem**: Script not executable

**Solution**:
```bash
# Make script executable
chmod +x scripts/*.py

# Or run with python explicitly
python scripts/audit_inventory.py
```

---

### Issue: Empty or missing artifacts directory

**Problem**: Scripts didn't run or failed silently

**Solution**:
```bash
# Create directory manually
mkdir -p artifacts

# Run scripts with verbose output
python scripts/audit_inventory.py --output-dir artifacts

# Check for errors
echo $?  # Should be 0 for success
```

---

### Issue: Git mv fails during apply_move_plan

**Problem**: Source file doesn't exist or target already exists

**Solution**:
```bash
# Run with dry-run to see which operations would fail
python scripts/apply_move_plan.py --dry-run

# Review validation errors in output

# Fix move plan:
# - Verify current_path is correct
# - Ensure proposed_path doesn't exist
# - Check for typos

# Test again
python scripts/apply_move_plan.py --dry-run
```

---

### Issue: Encoding errors when reading files

**Problem**: Non-UTF-8 files in repository

**Solution**:
```bash
# Find files with non-UTF-8 encoding
file * | grep -v UTF-8

# Convert to UTF-8 if needed
iconv -f ISO-8859-1 -t UTF-8 file.txt > file_utf8.txt

# Or skip problematic files in script
python scripts/audit_inventory.py --exclude "binary_files"
```

---

### Issue: Semantic deduplication is very slow

**Problem**: Large repository with many documents

**Solution**:
```bash
# Install FAISS for faster similarity search
pip install faiss-cpu

# Use FAISS mode
python scripts/deduplicate_semantic.py --use-faiss

# Or process subset
python scripts/deduplicate_semantic.py --input specific_directory/
```

---

### Issue: Move plan applied but links broken

**Problem**: Relative links not updated after moves

**Solution**:
```bash
# Find broken internal links
grep -r "](.*\.md)" --include="*.md" .

# Manually update links in affected files
# Or use sed for bulk replacement:
find . -name "*.md" -exec sed -i 's|old/path|new/path|g' {} +

# Verify links work
# (manually test key navigation paths)

# Commit link updates
git add .
git commit -m "fix: update links after reorganization"
```

---

## FAQ

### Q: Will these scripts modify my repository?

**A**: The audit scripts (`audit_inventory.py`, `normalize_conversations.py`, `deduplicate_semantic.py`) only READ files and generate reports. They never modify your repository.

Only `apply_move_plan.py` modifies files, and ONLY when run with `--apply` flag. The default `--dry-run` mode is safe.

---

### Q: Can I undo changes after applying a move plan?

**A**: Yes, through Git:

1. **Revert commit**: `git revert <commit-sha>`
2. **Reset to before**: `git reset --hard <commit-before>`
3. **Restore from backup**: See [Rollback Procedures](#rollback-procedures)

Always create a backup before applying changes.

---

### Q: How often should I run audits?

**A**: Recommended schedule:

- **Monthly**: Basic inventory audit
- **Quarterly**: Full audit including semantic duplicates
- **Before major changes**: Always audit first
- **After major additions**: Audit to catch duplicates early

The GitHub Actions workflow runs automatically on PRs.

---

### Q: What if I find duplicates but they're intentionally duplicated?

**A**: Not all duplicates should be removed. Valid reasons for duplication:

- Templates or boilerplate
- Examples in documentation
- Different contexts requiring same content

In `proposed_move_plan.csv`, use `action=propose` to document duplication without removing:

```csv
current_path,proposed_path,confidence,reason,action
template.md,example.md,high,Intentional template copy for examples,propose
```

---

### Q: Can I run these scripts on other repositories?

**A**: Yes! The scripts are designed to be repository-agnostic:

```bash
python scripts/audit_inventory.py --repo-root /path/to/other/repo
python scripts/normalize_conversations.py --input-dir /other/repo/conversations/
```

---

### Q: What's the difference between exact and semantic duplicates?

**A**:

- **Exact duplicates**: Byte-for-byte identical files (same SHA-1 hash)
  - Found by: `audit_inventory.py`
  - Action: Usually safe to delete one copy
  
- **Semantic duplicates**: Similar meaning/content but different wording
  - Found by: `deduplicate_semantic.py`
  - Action: Review carefully, may merge or keep separate

---

### Q: How do I contribute improvements to these scripts?

**A**: 

1. Fork the repository
2. Create feature branch: `git checkout -b feature/improve-audit-script`
3. Make changes and test thoroughly
4. Update documentation
5. Submit PR with clear description
6. Follow repository protocols in `docs/protocols.md`

---

### Q: Can these scripts handle binary files?

**A**: 

- `audit_inventory.py`: Yes, computes hashes for all files
- `normalize_conversations.py`: No, only processes text/markdown
- `deduplicate_semantic.py`: No, only analyzes text content
- `apply_move_plan.py`: Yes, can move any file type

---

### Q: What about privacy and sensitive data?

**A**:

⚠️ **Important**: Review files before committing, especially:

- Conversations (may contain private discussions)
- Configuration files (may have tokens/keys)
- Documents (may have personal information)

The scripts don't automatically redact sensitive data. Manual review required.

---

### Q: Why are there two folder numbering systems (00 vs 99)?

**A**: Naming convention:

- `00-`: Foundation/origins (appears first alphabetically)
- `01-09`: Primary content
- `10-89`: Secondary content
- `99-`: Deprecated/archived (appears last)

This PR proposes renaming `99-REGISTROS-HISTORICOS/` to `00-foundation-origins/` to reflect its foundational role.

---

## Additional Resources

### Repository Documentation

- [Protocols Guide](docs/protocols.md): Naming conventions, PR policy, backup procedures
- [Audit Changelog](docs/CHANGELOG-AUDIT.md): History of audit operations
- [Foundation Origins Overview](00-foundation-origins/00-overview.md): Purpose of origins directory

### Script Documentation

- [audit_inventory.py](scripts/audit_inventory.py): Inline documentation and docstrings
- [normalize_conversations.py](scripts/normalize_conversations.py): Inline documentation and docstrings
- [deduplicate_semantic.py](scripts/deduplicate_semantic.py): Inline documentation and docstrings
- [apply_move_plan.py](scripts/apply_move_plan.py): Inline documentation and docstrings

### External Resources

- [Sentence-Transformers Documentation](https://www.sbert.net/)
- [Git Documentation](https://git-scm.com/doc)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)
- [JSONL Format Specification](https://jsonlines.org/)

---

## Support

### Getting Help

1. **Check this README**: Most common questions answered above
2. **Review script help**: `python scripts/script_name.py --help`
3. **Check generated logs**: Review `artifacts/` for details
4. **Search issues**: [GitHub Issues](https://github.com/Genovese-Felipe/beneficios-estudantis-completo-2025/issues)
5. **Open new issue**: Provide details, error messages, and artifacts

### Reporting Bugs

When reporting issues, include:

- **Script name and command**: What you ran
- **Error message**: Full error output
- **Environment**: Python version, OS
- **Expected vs actual**: What should happen vs. what happened
- **Artifacts**: Attach relevant CSV files if possible

---

## License

This toolkit is part of the beneficios-estudantis-completo-2025 repository and follows the same license.

---

**Version**: 1.0.0  
**Created**: 2025-10-09  
**Last Updated**: 2025-10-09  
**Maintained By**: Repository owner and contributors  
**Questions**: Open a GitHub issue
