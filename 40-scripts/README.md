# 40-scripts

## Overview

This directory contains automation scripts, utilities, and tools that support repository operations, data processing, validation, and maintenance tasks.

## Purpose

- **Automation**: Reduce manual effort through scripted workflows
- **Consistency**: Ensure operations follow standardized procedures
- **Validation**: Automate quality checks and compliance verification
- **Efficiency**: Speed up repetitive tasks and complex operations

## Directory Structure

Scripts are organized by purpose and functionality at the root level of this directory. As the collection grows, subdirectories may be created for better organization.

## Key Scripts

### reorg.py
Repository reorganization and deduplication script.

**Purpose**: 
- Create and validate directory structure
- Move files according to reorg-spec.yaml
- Identify and archive duplicate files
- Log all operations for transparency

**Usage**:
```bash
# Dry run (default - no changes made)
python reorg.py --dry-run

# Apply changes (after reviewing dry run)
python reorg.py --apply

# Custom spec file
python reorg.py --spec custom-spec.yaml
```

**Features**:
- Dry-run mode for safe preview
- SHA-256 based duplicate detection
- Comprehensive operation logging
- YAML-based configuration
- Rollback support (future)

See `reorg-spec.yaml` in repository root for configuration.

## Script Standards

### General Requirements
- **Python 3.8+** for Python scripts
- **Shebang line** at top of executable scripts
- **Documentation**: Docstrings and inline comments
- **Error handling**: Graceful failure with clear messages
- **Logging**: Use structured logging for operations
- **Testing**: Include unit tests where appropriate

### Command-Line Interface
- Use **argparse** for argument parsing
- Provide `--help` documentation
- Support `--verbose` and `--quiet` flags where relevant
- Use `--dry-run` for operations that modify files
- Return appropriate exit codes (0=success, non-zero=error)

### Safety Features
- **Dry-run by default** for destructive operations
- **Confirmation prompts** for risky operations
- **Backup creation** before modifications
- **Logging** all changes for audit trail
- **Rollback capability** where feasible

## Usage Guidelines

### For Operators
1. **Always test in dry-run mode first**
2. Review logs before applying changes
3. Keep backup of important data
4. Document custom configurations
5. Report issues and unexpected behaviors

### For Developers
- Follow PEP 8 style guide for Python
- Include docstrings for modules, classes, and functions
- Add type hints for better IDE support
- Write tests for critical functionality
- Document dependencies in requirements.txt

### For AI Assistants
- Consult `ai_assistant_guide.yaml` for area-specific guidance
- Review script documentation before use
- Log script executions in 21-github-and-copilot-tech/02-operations-logs/
- Report issues for investigation

## Dependencies

### Core Dependencies
```
PyYAML>=6.0  # YAML parsing
```

Additional dependencies should be documented in `requirements.txt` in repository root.

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Or using poetry, pipenv, etc.
poetry install
```

## Configuration

Scripts are configured through:
1. **YAML configuration files** (e.g., reorg-spec.yaml)
2. **Command-line arguments** for runtime options
3. **Environment variables** for sensitive data

### Configuration Best Practices
- Store configs in repository root or `.config/`
- Never commit secrets or credentials
- Use environment variables for sensitive data
- Provide example configs (.example suffix)
- Document all configuration options

## Script Development

### Adding a New Script

1. **Plan the script**
   - Define clear purpose and scope
   - Identify inputs, outputs, and side effects
   - Consider error cases and edge conditions

2. **Implement**
   - Follow coding standards
   - Include help documentation
   - Add error handling
   - Implement logging

3. **Test**
   - Test normal operation
   - Test error cases
   - Test with various inputs
   - Verify dry-run mode

4. **Document**
   - Update this README
   - Add inline documentation
   - Create usage examples
   - Document in 21-github-and-copilot-tech/03-how-to/ if complex

### Code Review Checklist
- [ ] Follows coding standards
- [ ] Includes documentation
- [ ] Has error handling
- [ ] Tested with various inputs
- [ ] Logs operations appropriately
- [ ] Uses dry-run for destructive ops
- [ ] Returns proper exit codes
- [ ] Updated README.md

## Operations Logging

All script executions should be logged to:
```
21-github-and-copilot-tech/02-operations-logs/
```

Include:
- Timestamp
- Script name and version
- Command-line arguments
- Summary of operations performed
- Any errors or warnings
- Execution duration

## Testing

### Manual Testing
1. Run with `--dry-run` first
2. Test with minimal data set
3. Verify expected outputs
4. Check logs for errors
5. Validate no unintended side effects

### Automated Testing
For scripts with unit tests:
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_reorg.py

# Run with coverage
python -m pytest --cov=. tests/
```

## Security Considerations

- **Never commit secrets**: Use environment variables or secure vaults
- **Validate inputs**: Sanitize and validate all user inputs
- **Limit permissions**: Run with minimal required permissions
- **Audit logging**: Log security-relevant operations
- **Code review**: Have scripts reviewed before use in production

## Troubleshooting

### Common Issues

**Script fails with import error**
- Ensure dependencies are installed: `pip install -r requirements.txt`

**Permission denied**
- Check file permissions: `chmod +x script.py`
- Verify write access to target directories

**Unexpected behavior**
- Run in verbose mode: `--verbose`
- Check logs in 02-operations-logs/
- Verify configuration files are correct

## Relationship to Other Areas

### 00-governance-and-origins
- Scripts implement governance protocols
- Configuration follows established standards

### 21-github-and-copilot-tech
- Script usage documented in 03-how-to/
- Execution logs stored in 02-operations-logs/

### 30-data
- Scripts may process or validate datasets
- Data provenance tracked when scripts generate data

### 90-archive
- Scripts may move files to archive
- Deduplication results logged in duplicates/

## Future Enhancements

Planned improvements:
- Automated testing in CI/CD
- Script performance monitoring
- Enhanced rollback capabilities
- Interactive mode for complex operations
- Web UI for common operations

---

**Last Updated**: 2025-01-09  
**Maintained By**: Automation and Tools Team
