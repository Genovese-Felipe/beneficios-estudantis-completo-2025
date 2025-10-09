# Repository Reorganization Report

**Operation ID**: REORG-YYYY-MM-DD-NNN  
**Date**: YYYY-MM-DD  
**Time**: HH:MM:SS UTC  
**Performed By**: [Person/Tool Name]  
**Status**: [Planned | In Progress | Completed | Failed | Rolled Back]

## Executive Summary

Brief 2-3 sentence overview of what was accomplished, why it was done, and the overall outcome.

**Key Metrics**:
- Files moved: N
- Duplicates archived: N
- Directories created: N
- Storage saved: N MB/GB
- Duration: N minutes/hours

## Objective

### Primary Goal
Clear statement of the main objective for this reorganization.

### Secondary Goals
- Secondary objective 1
- Secondary objective 2
- Secondary objective 3

### Success Criteria
- [ ] Criterion 1: Specific, measurable outcome
- [ ] Criterion 2: Specific, measurable outcome
- [ ] Criterion 3: Specific, measurable outcome

## Scope

### In Scope
- What files/directories were included
- What operations were performed
- What areas were affected

### Out of Scope
- What was explicitly excluded
- What was deferred for future operations
- What existing content was left unchanged

## Method

### Planning Phase

**Duration**: N hours/days

**Activities**:
1. Analyzed current structure
2. Defined target structure
3. Created migration plan
4. Identified risks and mitigations

**Decisions Made**:
- Key decision 1 and rationale
- Key decision 2 and rationale

### Preparation Phase

**Duration**: N hours/days

**Activities**:
1. Backed up repository: [backup location/method]
2. Created dry-run specification
3. Tested migration script
4. Reviewed with stakeholders

**Tools Used**:
- Tool 1: Purpose and version
- Tool 2: Purpose and version

### Execution Phase

**Duration**: N hours

**Dry Run**:
- Date/time: YYYY-MM-DD HH:MM
- Issues found: N
- Adjustments made: Brief description

**Actual Execution**:
- Date/time: YYYY-MM-DD HH:MM
- Mode: [Automated | Manual | Hybrid]
- Monitoring: [Real-time | Post-execution]

## Results

### Files and Directories

#### Created
- `00-governance-and-origins/` - New governance area
- `10-product-guide/` - Consolidated product docs
- [Additional directories...]

**Total directories created**: N

#### Moved
| Original Path | New Path | Reason |
|---------------|----------|--------|
| `path/to/file1.md` | `new/path/file1.md` | Centralization |
| `path/to/file2.md` | `new/path/file2.md` | Category alignment |

**Total files moved**: N

#### Archived
| File | Original Location | Archive Location | Reason | Hash |
|------|-------------------|------------------|--------|------|
| `file1.md` | `old/path/` | `90-archive/duplicates/` | Duplicate | `abc123...` |
| `file2.md` | `old/path/` | `90-archive/legacy/` | Superseded | N/A |

**Total files archived**: N  
**Storage saved**: N MB

#### Deleted
| File | Reason | Approved By | Date |
|------|--------|-------------|------|
| (List any files deleted, if applicable) | | | |

**Note**: Prefer archiving over deletion for audit purposes.

### Structure Changes

#### Before
```
repository/
├── old-structure/
│   ├── file1.md
│   └── file2.md
├── another-old/
└── README.md
```

#### After
```
repository/
├── 00-governance-and-origins/
│   ├── 01-conversations/
│   └── 02-source-extractions/
├── 10-product-guide/
├── README.md
└── [Additional structure...]
```

### Compliance

#### Standards Adherence
- [x] Top-level folders use NN-kebab-case naming
- [x] Repository root contains only metadata files
- [x] All archived content indexed in duplicates-index.csv
- [x] Operations logged in this report

#### Quality Checks
- [x] All files moved successfully
- [x] No broken references
- [x] Documentation updated
- [x] CI/CD pipeline passes

## Issues and Resolutions

### Issue 1: [Brief Description]

**Severity**: [Low | Medium | High | Critical]  
**Discovered**: During [planning | dry-run | execution | validation]

**Description**: Detailed description of what went wrong.

**Impact**: Who/what was affected and how.

**Resolution**: How the issue was resolved.

**Prevention**: How to prevent this in future operations.

### Issue 2: [Brief Description]

[Same format as above]

## Quality Verification

### Automated Checks
- [x] Directory structure matches specification
- [x] All required README.md files present
- [x] All required ai_assistant_guide.yaml files present
- [x] No files left in disallowed locations
- [x] Duplicate index complete and valid
- [x] CI workflow passes

### Manual Verification
- [x] Spot-checked moved files for integrity
- [x] Verified reference updates
- [x] Reviewed logs for errors
- [x] Tested key workflows
- [x] Confirmed no data loss

### Stakeholder Review
- [ ] Reviewed by: [Name] on [Date]
- [ ] Approved by: [Name] on [Date]
- [ ] Feedback incorporated: [Date]

## Performance

### Execution Time
- Planning: N hours
- Preparation: N hours
- Dry run: N minutes
- Actual execution: N minutes
- Verification: N minutes
- **Total**: N hours

### Resource Usage
- CPU: Average N%, Peak N%
- Memory: Average N MB, Peak N MB
- Disk I/O: N MB read, N MB written

### Efficiency Metrics
- Files per minute: N
- Duplicates detected per second: N
- [Additional metrics as relevant]

## Lessons Learned

### What Went Well
1. Positive outcome 1 and why it succeeded
2. Positive outcome 2 and why it succeeded
3. Positive outcome 3 and why it succeeded

### What Could Be Improved
1. Area for improvement 1 and how to improve
2. Area for improvement 2 and how to improve
3. Area for improvement 3 and how to improve

### Unexpected Findings
- Surprising discovery 1
- Surprising discovery 2
- How these affect future operations

## Recommendations

### Immediate Next Steps
1. Action 1 with owner and timeline
2. Action 2 with owner and timeline
3. Action 3 with owner and timeline

### Future Improvements
1. Enhancement 1 for next reorganization
2. Enhancement 2 for tooling/process
3. Enhancement 3 for documentation

### Governance Updates
- [ ] Update reorg-protocol.md with new learnings
- [ ] Revise reorg-spec.yaml based on experience
- [ ] Enhance automation scripts
- [ ] Update templates

## References

### Related Documentation
- [Reorganization Protocol](../../00-governance-and-origins/03-protocols/reorg-protocol.md)
- [Specification Used](../../reorg-spec.yaml)
- [Previous Reorganizations](./previous-reorg-YYYY-MM-DD.md)

### External Resources
- [Link to relevant tools]
- [Link to best practices]
- [Link to community discussions]

## Appendices

### Appendix A: Full File Movement Log

Complete list of all file operations (can be external file if very large).

```
YYYY-MM-DD HH:MM:SS - MOVE: path/to/file1.md -> new/path/file1.md
YYYY-MM-DD HH:MM:SS - MOVE: path/to/file2.md -> new/path/file2.md
[...]
```

### Appendix B: Duplicate Detection Details

Full output from duplicate detection, including hashes and file sizes.

### Appendix C: Configuration Files

#### reorg-spec.yaml (version used)
```yaml
[Include relevant portions or link to version]
```

### Appendix D: Script Logs

Full logs from automation scripts (can be external file if very large).

---

## Sign-off

**Operation Completed By**: [Name]  
**Date**: YYYY-MM-DD  
**Signature/Approval**: [Digital signature or approval record]

**Quality Review By**: [Name]  
**Date**: YYYY-MM-DD  
**Status**: [Approved | Approved with Conditions | Rejected]

**Comments**: [Any additional notes or requirements]

---

## Notes for Template Users

**When creating a reorganization report:**

1. **Create report file** before starting operations
2. **Update in real-time** or immediately after each phase
3. **Be comprehensive** - future you will thank you
4. **Include evidence** - screenshots, logs, metrics
5. **Be honest** about issues and failures
6. **Document decisions** and their rationale
7. **Think like an auditor** - what would they want to know?

**Quality checklist:**

- [ ] All sections completed (mark N/A if not applicable)
- [ ] Metrics accurate and verified
- [ ] Issues documented with resolutions
- [ ] Lessons learned captured
- [ ] Recommendations specific and actionable
- [ ] References provided
- [ ] Reviewed for clarity and completeness

**This template itself should not be modified without updating the governance protocols.**
