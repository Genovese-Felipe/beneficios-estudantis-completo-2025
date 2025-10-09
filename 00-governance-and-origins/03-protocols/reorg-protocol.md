# Repository Reorganization Protocol

**Version**: 1.0.0  
**Effective Date**: 2025-01-09  
**Last Updated**: 2025-01-09  
**Status**: Active  
**Maintained By**: Repository Governance Team

## Purpose

This protocol defines the standard operating procedure for reorganizing the repository structure, including directory creation, file relocation, deduplication, and documentation updates.

## Scope

This protocol applies to:
- Major structural reorganizations
- Directory renaming or consolidation
- Bulk file relocations
- Deduplication operations
- Archival of legacy content

This protocol does NOT apply to:
- Minor file edits or content updates
- Addition of single new files
- Regular maintenance operations
- Routine content updates

## Principles

### Core Principles

1. **Transparency**: All operations must be logged and documented
2. **Safety**: Use dry-run mode by default; require explicit approval for changes
3. **Reversibility**: Maintain ability to rollback through comprehensive logging
4. **Preservation**: Archive rather than delete; maintain audit trails
5. **Consistency**: Follow established naming conventions and standards

### Directory Naming Standards

- **Top-level directories**: `NN-kebab-case` where NN is 00-99
- **Subdirectories**: `NN-kebab-case` or `kebab-case` as appropriate
- **Special directories**: `.git`, `.github` excepted from numbering
- **Reserved ranges**:
  - 00-09: Governance and foundational
  - 10-29: Product and documentation
  - 30-49: Data and tools
  - 50-89: Reserved for future use
  - 90-99: Archive and deprecated

### File Naming Standards

- **Documentation**: `UPPER-CASE-KEBAB.md` or `kebab-case.md`
- **Code**: Follow language conventions
- **Configuration**: `kebab-case.yaml`, `kebab-case.json`, etc.
- **Assets**: `lowercase-kebab.png`, `lowercase-kebab.svg`, etc.

## Roles and Responsibilities

### Repository Maintainer
- Approve reorganization plans
- Review and approve dry-run results
- Authorize execution of changes
- Final sign-off on operations

### Operations Team
- Plan and execute reorganizations
- Create specifications and scripts
- Monitor operations
- Document results

### Reviewers
- Review reorganization plans
- Validate dry-run results
- Verify quality standards
- Approve operation reports

## Standard Operating Procedure

### Phase 1: Planning

**Objective**: Define scope and create detailed plan

**Duration**: Variable (typically 1-5 days)

**Steps**:

1. **Identify Need**
   - Document reason for reorganization
   - Define objectives and success criteria
   - Assess scope and impact
   - Identify stakeholders

2. **Analyze Current State**
   - Document existing structure
   - Identify issues or inefficiencies
   - Catalog content by type
   - Detect potential duplicates

3. **Design Target State**
   - Define ideal structure
   - Map content to new locations
   - Identify gaps or missing areas
   - Document naming conventions

4. **Create Migration Plan**
   - List all operations (create, move, archive)
   - Define order of operations
   - Identify dependencies
   - Estimate duration and resources

5. **Risk Assessment**
   - Identify potential issues
   - Plan mitigations
   - Define rollback strategy
   - Set success criteria

6. **Stakeholder Review**
   - Share plan with team
   - Gather feedback
   - Incorporate suggestions
   - Obtain preliminary approval

**Deliverable**: Reorganization plan document

### Phase 2: Preparation

**Objective**: Create tools and specifications for execution

**Duration**: Variable (typically 1-3 days)

**Steps**:

1. **Create Backup**
   ```bash
   git status
   git add .
   git commit -m "Pre-reorganization checkpoint"
   git push
   ```

2. **Create Specification File**
   - Use `reorg-spec.yaml` format
   - Define all directories to create
   - Define all file moves
   - Configure deduplication
   - **Set dry_run: true**

3. **Develop/Update Scripts**
   - Update `40-scripts/reorg.py` as needed
   - Test script logic
   - Verify error handling
   - Add logging

4. **Prepare Documentation**
   - Draft README.md for each new area
   - Draft ai_assistant_guide.yaml files
   - Prepare protocol documents
   - Draft templates

5. **Create Test Environment**
   - Test on copy or branch if possible
   - Validate script behavior
   - Check for edge cases

**Deliverable**: 
- `reorg-spec.yaml` with dry_run: true
- Updated scripts
- Draft documentation

### Phase 3: Dry Run

**Objective**: Preview changes without applying them

**Duration**: Variable (typically 1-4 hours)

**Steps**:

1. **Execute Dry Run**
   ```bash
   python 40-scripts/reorg.py --dry-run
   ```

2. **Review Output**
   - Check list of operations
   - Verify directories to be created
   - Verify files to be moved
   - Check duplicate detection results
   - Review any warnings or errors

3. **Validate Against Plan**
   - Confirm operations match specification
   - Verify no unexpected operations
   - Check for missing operations
   - Validate naming conventions

4. **Generate Report**
   - Document dry-run results
   - List all planned operations
   - Note any issues found
   - Recommend adjustments

5. **Stakeholder Review**
   - Share dry-run results
   - Discuss any concerns
   - Make adjustments if needed
   - Obtain approval to proceed

**Deliverable**: Dry-run report with approval to proceed

### Phase 4: Execution

**Objective**: Apply changes to repository

**Duration**: Variable (typically minutes to hours)

**Steps**:

1. **Final Checkpoint**
   ```bash
   git status
   git add .
   git commit -m "Pre-execution checkpoint"
   git push
   ```

2. **Update Specification**
   - Change `dry_run: false` in reorg-spec.yaml
   - Commit this change for audit trail

3. **Execute Reorganization**
   ```bash
   python 40-scripts/reorg.py --apply
   ```

4. **Monitor Execution**
   - Watch for errors
   - Check logs in real-time
   - Be ready to intervene if needed

5. **Handle Issues**
   - If errors occur, stop execution
   - Document the issue
   - Determine if rollback needed
   - Fix issue and resume or rollback

**Deliverable**: Executed reorganization with logs

### Phase 5: Verification

**Objective**: Confirm changes are correct and complete

**Duration**: Variable (typically 1-4 hours)

**Steps**:

1. **Automated Verification**
   ```bash
   # Run CI checks
   # Run validation scripts
   # Check for broken links
   ```

2. **Manual Verification**
   - Spot-check moved files
   - Verify directory structure
   - Check documentation completeness
   - Test workflows

3. **Reference Validation**
   - Check for broken internal links
   - Update cross-references
   - Verify imports/includes
   - Test navigation

4. **Quality Checks**
   - All required files present
   - Naming conventions followed
   - Documentation complete
   - No files in wrong locations

5. **Stakeholder Validation**
   - Demonstrate changes to team
   - Gather feedback
   - Address any issues
   - Obtain sign-off

**Deliverable**: Validation report

### Phase 6: Documentation

**Objective**: Complete all required documentation

**Duration**: Variable (typically 2-8 hours)

**Steps**:

1. **Create Operations Report**
   - Use reorg-report-template.md
   - Document all operations
   - Include metrics and results
   - Note issues and resolutions
   - Capture lessons learned

2. **Update Repository Documentation**
   - Update root README.md
   - Update CHANGELOG.md
   - Update CONTRIBUTING.md if affected
   - Add notes to relevant docs

3. **Complete Area Documentation**
   - Ensure all README.md files complete
   - Ensure all ai_assistant_guide.yaml files complete
   - Add any needed how-to guides
   - Update cross-references

4. **Archive Old Structure Documentation**
   - Move old docs to 90-archive/legacy/
   - Include README explaining changes
   - Maintain for reference

**Deliverable**: Complete documentation package

### Phase 7: Communication

**Objective**: Inform stakeholders of changes

**Duration**: 1 day

**Steps**:

1. **Prepare Announcement**
   - Summarize changes
   - Explain rationale
   - Provide migration guide if needed
   - Note any action items

2. **Notify Stakeholders**
   - Post to relevant channels
   - Update project wiki/docs
   - Send notifications
   - Respond to questions

3. **Update External References**
   - Update links in external docs
   - Notify external projects if affected
   - Update citations

**Deliverable**: Communication complete

### Phase 8: Monitoring

**Objective**: Ensure changes are stable

**Duration**: 1-2 weeks

**Steps**:

1. **Monitor for Issues**
   - Watch for bug reports
   - Check CI/CD status
   - Monitor error logs
   - Track user feedback

2. **Address Issues Promptly**
   - Fix broken references
   - Correct mislabeled content
   - Address confusion
   - Update documentation

3. **Collect Feedback**
   - Survey users/contributors
   - Gather improvement suggestions
   - Document pain points

4. **Final Review**
   - Assess if objectives met
   - Measure against success criteria
   - Document for future improvements

**Deliverable**: Monitoring summary

## Tools and Resources

### Required Tools
- `40-scripts/reorg.py`: Main reorganization script
- `reorg-spec.yaml`: Configuration specification
- Git version control system

### Templates
- `21-github-and-copilot-tech/02-operations-logs/reorg-report-template.md`
- `00-governance-and-origins/04-templates/`: Additional templates

### Documentation
- This protocol document
- Area README.md files
- Area ai_assistant_guide.yaml files

## Safety Mechanisms

### Dry-Run Mode
- **Always** run dry-run first
- Review output thoroughly
- Obtain approval before applying
- Use dry-run to catch issues early

### Logging
- Log all operations to files
- Include timestamps and context
- Log both successes and failures
- Make logs searchable

### Backups
- Commit before major operations
- Push to remote before applying changes
- Consider creating tags for major reorgs
- Document backup locations

### Rollback Procedures
If issues occur:
1. Stop execution immediately
2. Assess the damage/scope
3. Review logs to understand what happened
4. Decide: fix forward or rollback
5. If rollback: `git reset --hard <checkpoint>`
6. Document incident

## Quality Standards

### Directory Structure
- Top-level follows NN-kebab-case
- Required directories present
- No unexpected directories
- Proper nesting and organization

### Documentation
- Every directory has README.md
- Every directory has ai_assistant_guide.yaml
- Cross-references are valid
- Templates provided where needed

### File Organization
- Files in correct locations
- Naming conventions followed
- No orphaned files
- Proper categorization

### Deduplication
- All duplicates identified
- Archive decisions documented
- Index maintained
- No data loss

## Compliance

### Audit Requirements
- Operations log for every reorganization
- Approvals documented
- Changes tracked in version control
- Ability to reproduce decisions

### Retention
- Keep all operations logs permanently
- Maintain archived content
- Preserve decision rationale
- Track protocol versions

## Version History

### 1.0.0 - 2025-01-09
- Initial version
- Established 8-phase procedure
- Defined standards and principles
- Created safety mechanisms

---

## Appendix A: Checklist

Quick reference checklist for reorganization operations:

### Planning
- [ ] Reorganization need identified and documented
- [ ] Current state analyzed
- [ ] Target state designed
- [ ] Migration plan created
- [ ] Risks assessed and mitigated
- [ ] Plan reviewed and approved

### Preparation
- [ ] Backup created (commit + push)
- [ ] Specification file created
- [ ] Scripts updated and tested
- [ ] Documentation drafted
- [ ] Test environment validated

### Dry Run
- [ ] Dry run executed successfully
- [ ] Output reviewed thoroughly
- [ ] Operations validated against plan
- [ ] Dry-run report created
- [ ] Approval obtained to proceed

### Execution
- [ ] Final checkpoint created
- [ ] Specification updated (dry_run: false)
- [ ] Reorganization executed
- [ ] Execution monitored
- [ ] Issues handled appropriately

### Verification
- [ ] Automated checks passed
- [ ] Manual verification completed
- [ ] References validated
- [ ] Quality standards met
- [ ] Stakeholder sign-off obtained

### Documentation
- [ ] Operations report completed
- [ ] Repository docs updated
- [ ] Area documentation complete
- [ ] Old docs archived

### Communication
- [ ] Announcement prepared
- [ ] Stakeholders notified
- [ ] External references updated
- [ ] Questions addressed

### Monitoring
- [ ] Issues monitored for 1-2 weeks
- [ ] Problems addressed promptly
- [ ] Feedback collected
- [ ] Final review completed

---

**This protocol is a living document and should be updated based on lessons learned from each reorganization operation.**
