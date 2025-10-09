# Techniques Inventory

**Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09**  
*Note: Copilot is powered by AI; mistakes are possible. Review carefully.*

## Purpose

This document tracks proven techniques, patterns, and approaches that have been successful in developing and maintaining this repository. It serves as a knowledge base for both human maintainers and AI agents.

## How to Use

### For Maintainers
- Review this document when planning new features or refactoring
- Add new techniques as you discover them
- Update existing entries with lessons learned
- Reference specific techniques in code comments and documentation

### For AI Agents
- Read this document to understand established patterns
- Apply these techniques when implementing new features
- Add new techniques you discover during work
- Reference techniques in commit messages

---

## Repository Organization

### Technique: Numbered Directory Prefixes

**Status**: ✅ Established  
**First Used**: 2025-01-08  
**Source**: `99-REGISTROS-HISTORICOS/` conversations

**Description**:
Use two-digit numerical prefixes for directories to control sort order and indicate importance/sequence.

**Pattern**:
```
00-foundation-origins/     # Foundation, always first
01-primary-content/        # Main deliverables
02-secondary-content/      # Supporting content
...
99-deprecated/             # Archived content, always last
```

**Benefits**:
- Predictable alphabetical sorting
- Clear hierarchy and importance
- Easy to insert new categories without renaming
- Intuitive for both humans and tools

**Pitfalls to Avoid**:
- Don't use single digits (use `01` not `1`)
- Don't skip numbers arbitrarily (maintain logical sequence)
- Don't reuse prefixes for different purposes

---

### Technique: Bilingual Documentation (Portuguese + English)

**Status**: ✅ Established  
**First Used**: 2025-01-08  
**Source**: Repository README requirements

**Description**:
Provide key documentation in both Portuguese (primary) and English to maximize accessibility.

**Pattern**:
```markdown
# Title

## English Overview
[English content here]

## Visão Geral em Português
[Portuguese content here]
```

**Benefits**:
- Accessible to international contributors
- Better for AI agents (often trained primarily on English)
- Professional presentation
- Facilitates collaboration

**When to Apply**:
- Main README files
- Overview documents
- API documentation
- Public-facing content

**When to Skip**:
- Internal technical notes
- Code comments (English is standard)
- Quick notes/drafts

---

## Code Quality

### Technique: AI Authorship Attribution

**Status**: ✅ Established  
**First Used**: 2025-10-09  
**Source**: This PR requirements

**Description**:
Explicitly acknowledge when code/documentation was generated with AI assistance.

**Pattern**:
```python
"""
Script Name and Description

Generated with assistance from GitHub Copilot (AI assistant) on YYYY-MM-DD
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

[Rest of docstring]
"""
```

**Benefits**:
- Transparency about creation process
- Sets expectations for review rigor
- Helps track AI-generated content
- Professional disclosure

**Best Practices**:
- Include in file header, not individual functions
- Include date of generation
- Add disclaimer about AI limitations
- Keep concise (2-3 lines max)

---

### Technique: Dry-Run Mode for Destructive Operations

**Status**: ✅ Established  
**First Used**: 2025-10-09  
**Source**: `apply_move_plan.py` implementation

**Description**:
Always provide a safe simulation mode for operations that modify files.

**Pattern**:
```python
def main():
    parser.add_argument('--dry-run', action='store_true', default=True)
    parser.add_argument('--apply', action='store_true')
    
    args = parser.parse_args()
    dry_run = not args.apply
    
    if dry_run:
        print("[DRY-RUN] Would execute: ...")
    else:
        print("Executing: ...")
```

**Benefits**:
- Prevents accidental data loss
- Allows validation before commitment
- Builds user confidence
- Standard Unix tool pattern

**Best Practices**:
- Make dry-run the default
- Require explicit `--apply` flag for real changes
- Print clear indication of mode
- Show exactly what would happen

---

## Data Processing

### Technique: CSV for Structured Audit Data

**Status**: ✅ Established  
**First Used**: 2025-10-09  
**Source**: Audit toolkit requirements

**Description**:
Use CSV format for tabular audit data that humans and tools need to review/modify.

**Benefits**:
- Human-readable and editable
- Works with spreadsheet tools
- Easy to diff in git
- Simple to parse programmatically

**When to Use**:
- File inventories
- Duplicate reports
- Move plans
- Any tabular data for review

**When to Skip**:
- Hierarchical data (use JSON)
- Large binary data (use specialized formats)
- Real-time data (use databases)

---

### Technique: JSONL for Conversation Archives

**Status**: ✅ Established  
**First Used**: 2025-10-09  
**Source**: `normalize_conversations.py` implementation

**Description**:
Use JSON Lines (JSONL) format for storing sequences of structured records.

**Pattern**:
```json
{"id": 1, "data": "..."}
{"id": 2, "data": "..."}
```

**Benefits**:
- One record per line (easy to stream)
- Can append without parsing entire file
- Works with standard Unix tools (grep, wc, etc.)
- Efficiently handles large datasets

**When to Use**:
- Log files with structured data
- Conversation archives
- Event streams
- Large collections of records

---

## Documentation

### Technique: Comprehensive Script Help Text

**Status**: ✅ Established  
**First Used**: 2025-10-09  
**Source**: All audit toolkit scripts

**Description**:
Provide extensive help text with examples in script `--help` output.

**Pattern**:
```python
parser = argparse.ArgumentParser(
    description='Brief description',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Examples:
  # Basic usage
  python script.py
  
  # Advanced usage
  python script.py --option value

Notes:
  - Important note 1
  - Important note 2
    """
)
```

**Benefits**:
- Self-documenting scripts
- No need to reference external docs
- Easy to keep in sync with code
- Follows Unix conventions

**Include**:
- Basic usage examples
- Common use cases
- Important notes/warnings
- Dependency information

---

## To Be Documented

The following techniques are in use but need formal documentation:

- [ ] Error handling patterns for file operations
- [ ] Consistent logging approaches
- [ ] Test data generation for scripts
- [ ] Git commit message conventions
- [ ] PR description templates
- [ ] Link update strategies after moves

---

## Adding New Techniques

When you discover a new useful technique:

1. **Verify It Works**: Test in multiple scenarios
2. **Document the Pattern**: Provide code example
3. **Explain Benefits**: Why is this better than alternatives?
4. **Note Pitfalls**: What mistakes should be avoided?
5. **Provide Context**: When to use vs. when to skip
6. **Reference Source**: Link to conversation/commit where it originated

**Template**:
```markdown
### Technique: [Name]

**Status**: ✅ Established / 🚧 Experimental / ❌ Deprecated  
**First Used**: YYYY-MM-DD  
**Source**: [Reference]

**Description**:
[What it is]

**Pattern**:
[Code example]

**Benefits**:
- Benefit 1
- Benefit 2

**When to Use**:
- Scenario 1
- Scenario 2

**Pitfalls**:
- Thing to avoid 1
- Thing to avoid 2
```

---

## Deprecated Techniques

### Technique: Single-digit Directory Prefixes

**Status**: ❌ Deprecated  
**Replaced By**: Two-digit prefixes  
**Reason**: Sorting issues (10 comes before 2 in ASCII)

---

**Last Updated**: 2025-10-09  
**Maintained By**: Repository owner and AI agents
