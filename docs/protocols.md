# Repository Protocols and Guidelines

**Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09**  
*Note: Copilot is powered by AI; mistakes are possible. Review carefully.*

---

## Table of Contents

1. [Naming Conventions](#naming-conventions)
2. [Directory Organization](#directory-organization)
3. [File Management](#file-management)
4. [Pull Request Policy](#pull-request-policy)
5. [Backup Procedures](#backup-procedures)
6. [Link Management](#link-management)
7. [Documentation Standards](#documentation-standards)
8. [Review Process](#review-process)

---

## Naming Conventions

### Directory Names

**Pattern**: `##-category-name`

**Rules**:
- Use two-digit numerical prefix (00, 01, 02, ..., 99)
- Lowercase letters only
- Hyphens for word separation
- No spaces, underscores, or special characters

**Examples**:
```
✅ Good:
00-foundation-origins/
01-github-education/
02-technical-capabilities/

❌ Bad:
Foundation Origins/
1_github_education/
GITHUB-EDUCATION/
```

**Prefix Meanings**:
- `00-` Foundation and origins (appears first)
- `01-09` Primary content categories
- `10-89` Secondary content categories
- `90-98` Auxiliary content
- `99-` Deprecated/archived content (appears last)

### File Names

#### Markdown Documentation Files

**Pattern**: `UPPER-CASE-KEBAB.md` (main docs) or `lowercase-with-hyphens.md` (supporting docs)

**Examples**:
```
Main documents:
✅ README.md
✅ GUIA-COMPLETO.md
✅ TOP-50-PRIORIDADES.md
✅ ECONOMIA-CALCULADA.md

Supporting documents:
✅ overview.md
✅ protocols.md
✅ getting-started.md
```

#### Script Files

**Pattern**: `snake_case.py`

**Examples**:
```
✅ audit_inventory.py
✅ normalize_conversations.py
✅ deduplicate_semantic.py
```

#### Configuration Files

**Pattern**: `lowercase.json` or `lowercase.yml`

**Examples**:
```
✅ assistant_instructions.json
✅ repo-audit.yml
✅ package.json
```

---

## Directory Organization

### Principles

1. **Minimize Depth**: Prefer 2-3 levels of nesting maximum
2. **Logical Grouping**: Related content in same directory
3. **Numbered Ordering**: Use prefixes to control display order
4. **Clear Purpose**: Each directory should have obvious role

### Standard Structure

```
repository-root/
├── README.md                      # Main entry point
├── GUIA-COMPLETO.md              # Comprehensive guide
├── .gitignore                     # Git exclusions
├── 00-foundation-origins/         # Project origins and history
│   ├── 00-overview.md
│   ├── assistant_instructions.json
│   ├── conversations/
│   └── analysis/
├── 01-primary-content/            # Main content directories
├── 02-secondary-content/          # Supporting content
├── docs/                          # Repository documentation
│   ├── protocols.md
│   └── CHANGELOG-AUDIT.md
├── scripts/                       # Automation and tools
│   ├── audit_inventory.py
│   └── [other scripts]
└── [other root-level files]
```

### Directory README Requirements

Every directory MUST contain a `README.md` that explains:
- Purpose of the directory
- Contents overview
- How to use/navigate
- Related directories
- Last updated date

---

## File Management

### Creating New Files

1. **Check for Duplicates**: Search repository first to avoid duplication
2. **Choose Location**: Follow directory organization principles
3. **Follow Naming**: Use appropriate naming convention
4. **Add Header**: Include AI authorship attribution if applicable
5. **Update Parent README**: Link to new file in directory README

### Moving/Renaming Files

⚠️ **Important**: Moving files breaks links and must be done carefully.

**Process**:
1. **Create Move Plan**: Document in `proposed_move_plan.csv`
2. **Review Plan**: Get maintainer approval
3. **Use Git Commands**: Always use `git mv`, never manual rename
4. **Update Links**: Run link update script or manual update
5. **Test**: Verify all internal links still work
6. **Commit**: Single commit with clear message

**Example**:
```bash
# Wrong (breaks git history)
mv old-file.md new-file.md
git add new-file.md

# Correct (preserves git history)
git mv old-file.md new-file.md
git commit -m "refactor: rename old-file.md to new-file.md"
```

### Deleting Files

**Before Deleting**:
1. ✅ Verify file is truly unused
2. ✅ Check for inbound links from other files
3. ✅ Search codebase for references
4. ✅ Consider archiving instead of deleting

**Process**:
```bash
# Remove from git
git rm file-to-delete.md

# Commit with explanation
git commit -m "chore: remove outdated file-to-delete.md

Reason: Content superseded by new-file.md
Verified no inbound links remain"
```

---

## Pull Request Policy

### Before Creating PR

1. **Run Scripts**: Execute audit scripts to check for issues
2. **Update Documentation**: Ensure README and docs are current
3. **Test Links**: Verify all internal links work
4. **Review Changes**: Check git diff for unintended changes
5. **Update Changelog**: Add entry to appropriate changelog file

### PR Title Format

**Pattern**: `type: brief description`

**Types**:
- `feat`: New feature or content
- `fix`: Bug fix or correction
- `docs`: Documentation only changes
- `refactor`: Restructuring without changing functionality
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
✅ feat: add semantic duplicate detection script
✅ docs: update README with audit toolkit usage
✅ refactor: reorganize 99-REGISTROS-HISTORICOS to 00-foundation-origins
✅ fix: correct broken links in GUIA-COMPLETO.md
```

### PR Description Requirements

**Must Include**:

1. **English Overview**: Summary of changes
2. **Portuguese Overview**: Resumo das mudanças
3. **Checklist**: List of all changes with checkboxes
4. **Rationale**: Why these changes are needed
5. **Testing**: How changes were validated
6. **Impact**: What's affected by changes
7. **Links**: Related issues or discussions

**Template**:
```markdown
## Overview / Visão Geral

**English**: [Brief description]

**Português**: [Descrição breve]

## Changes / Mudanças

- [ ] Change 1
- [ ] Change 2
- [ ] Change 3

## Rationale / Justificativa

[Why these changes are needed]

## Testing / Testes

[How changes were validated]

## Impact / Impacto

[What's affected]

## Related / Relacionado

- Issue #123
- Discussion #456
```

### Review Checklist

Before merging, verify:

- [ ] All CI checks pass
- [ ] No merge conflicts
- [ ] Documentation updated
- [ ] Links tested and working
- [ ] No sensitive information committed
- [ ] Follows naming conventions
- [ ] PR description complete
- [ ] At least one approval (if required)

---

## Backup Procedures

### Before Major Changes

**Always create backup when**:
- Reorganizing multiple files
- Deleting content
- Making automated bulk changes
- Applying move plans

**Methods**:

1. **Git Branch**: Create feature branch (safest)
```bash
git checkout -b backup/before-reorganization-20251009
git push -u origin backup/before-reorganization-20251009
```

2. **Local Copy**: Copy directory structure
```bash
cp -r repository-root/ ../backup-20251009/
```

3. **Script Backup**: Use built-in backup feature
```bash
python scripts/apply_move_plan.py --backup
```

### Backup Retention

- **Git branches**: Keep for 3 months after merge
- **Local copies**: Delete after successful verification
- **Script backups**: Keep in separate directory, exclude from git

---

## Link Management

### Internal Links

**Use Relative Paths**:
```markdown
✅ Good:
[See protocols](docs/protocols.md)
[Overview](../README.md)

❌ Bad:
[See protocols](https://github.com/user/repo/blob/main/docs/protocols.md)
```

**Benefits**:
- Works in local clone
- Works with different branches
- Survives repository moves

### External Links

**Format**:
```markdown
✅ Good:
[GitHub Education](https://education.github.com/)

✅ Also Good (for repeated links):
See [GitHub Education][gh-edu] for more info.

[gh-edu]: https://education.github.com/
```

### After Moving Files

**Must Update**:
1. All links TO moved file
2. All links FROM moved file (if relative paths change)
3. README files mentioning the file
4. Table of contents entries

**Tools**:
```bash
# Find all markdown files linking to old path
grep -r "old-path/file.md" --include="*.md"

# Use sed for bulk updates (review changes carefully)
find . -name "*.md" -exec sed -i 's|old-path|new-path|g' {} +
```

---

## Documentation Standards

### Markdown Files

**Required Elements**:

1. **Title**: H1 header at top
2. **Attribution**: If AI-generated
3. **Purpose Section**: What this document covers
4. **Table of Contents**: For files >200 lines
5. **Metadata**: At bottom (last updated, maintainer)

**Example Structure**:
```markdown
# Document Title

**Generated with assistance from GitHub Copilot on YYYY-MM-DD**  
*Note: Copilot is powered by AI; mistakes are possible. Review carefully.*

## Purpose

[What this document is for]

## Table of Contents

1. [Section 1](#section-1)
2. [Section 2](#section-2)

## Section 1

[Content]

## Section 2

[Content]

---

**Last Updated**: YYYY-MM-DD  
**Maintained By**: [Name/Role]
```

### Code Files

**Required Elements**:

1. **Shebang**: For executable scripts
2. **Docstring**: Module/file-level documentation
3. **Attribution**: If AI-assisted
4. **Function Docstrings**: For all public functions
5. **Usage Examples**: In help text or docstring

**Example**:
```python
#!/usr/bin/env python3
"""
Script Title and Brief Description

Generated with assistance from GitHub Copilot on YYYY-MM-DD
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

Longer description of what the script does.

Usage:
    python script.py [options]

Examples:
    python script.py --input data.csv
"""

def function_name(param: str) -> str:
    """
    Brief function description.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
    """
    pass
```

---

## Review Process

### Self-Review Checklist

Before submitting for review:

- [ ] Code/content is complete and tested
- [ ] Documentation is updated
- [ ] Links are verified
- [ ] Naming conventions followed
- [ ] No sensitive information included
- [ ] Git history is clean (no debug commits)
- [ ] PR description is complete

### Peer Review Checklist

When reviewing others' PRs:

- [ ] Changes match PR description
- [ ] Code quality is acceptable
- [ ] Documentation is clear and complete
- [ ] No obvious bugs or issues
- [ ] Security concerns addressed
- [ ] Performance considerations noted
- [ ] Maintainability is good

### Approval Criteria

PR can be merged when:

1. ✅ All CI checks pass
2. ✅ At least one approval from maintainer
3. ✅ No unresolved review comments
4. ✅ Documentation updated
5. ✅ Breaking changes documented
6. ✅ Tests pass (if applicable)

---

## Maintenance Schedule

### Regular Tasks

**Weekly**:
- Check for broken external links
- Review new issues and PRs
- Update pinned issues if needed

**Monthly**:
- Review audit reports
- Check for duplicate content
- Update outdated information
- Clean up stale branches

**Quarterly**:
- Run full repository audit
- Review and update protocols
- Check platform benefits currency
- Update economic calculations

**Annually**:
- Major content review
- Reorganization if needed
- Update learning paths
- Refresh all examples

---

## Questions and Exceptions

### When to Deviate from Protocols

Protocols can be adapted when:
- Technical limitations require it
- Clear benefit outweighs consistency
- Emergency fixes needed
- Backward compatibility required

**Process**:
1. Document reason for deviation
2. Get maintainer approval
3. Note exception in commit message
4. Consider updating protocols if pattern emerges

### Getting Help

- **Issues**: Open GitHub issue for questions
- **Discussions**: Use GitHub Discussions for broad topics
- **Direct**: Contact maintainer for sensitive matters

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-09  
**Maintained By**: Repository owner and contributors  
**Review Schedule**: Quarterly
