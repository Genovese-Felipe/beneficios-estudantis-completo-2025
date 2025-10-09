# [Technique Name]

**Version**: 1.0.0  
**Last Updated**: YYYY-MM-DD  
**Author**: [Your Name or Team]  
**Status**: [Draft | Review | Approved | Deprecated]

## Overview

Brief 2-3 sentence summary of what this technique accomplishes and why it matters.

## Context

### When to Use
- Specific scenario or use case 1
- Specific scenario or use case 2
- Specific scenario or use case 3

### When NOT to Use
- Situation where this technique is inappropriate
- Alternative approaches that might be better
- Known limitations that would make this unsuitable

### Prerequisites
- Required knowledge: e.g., "Understanding of REST APIs"
- Required tools: e.g., "Node.js 18+, npm"
- Required access: e.g., "GitHub Student Developer Pack"
- Required setup: e.g., "GitHub Copilot extension installed"

## Implementation

### Step 1: [Initial Setup]

Brief description of what this step accomplishes.

```bash
# Example command or code
command --option value
```

**Expected outcome**: What you should see after this step.

### Step 2: [Main Configuration]

Description of the main configuration or setup process.

```python
# Example code with comments
def example_function():
    """
    Clear docstring explaining the function.
    """
    # Implementation details
    pass
```

**Expected outcome**: What success looks like.

### Step 3: [Verification]

How to verify the technique is working correctly.

```bash
# Verification commands
test-command --verify
```

**Expected outcome**: Confirmation that everything is working.

## Complete Example

Full working example that demonstrates the technique end-to-end.

```language
# Complete, runnable code example
# This should be copy-pasteable and functional

# Setup
initial_setup()

# Main implementation
result = main_technique()

# Verification
assert result == expected_value
print("Success!")
```

**Sample Output**:
```
Expected output from running the example
```

## Configuration Options

### Required Settings

| Option | Type | Description | Example |
|--------|------|-------------|---------|
| `option1` | string | What this option does | `"value"` |
| `option2` | number | Numeric configuration | `42` |

### Optional Settings

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `optional1` | boolean | `false` | Enable feature X |
| `optional2` | string | `"auto"` | Configuration mode |

## Trade-offs

### Advantages
- ✅ Benefit 1: Clear description
- ✅ Benefit 2: Clear description
- ✅ Benefit 3: Clear description

### Disadvantages
- ❌ Limitation 1: Clear description
- ❌ Limitation 2: Clear description
- ⚠️ Consideration: Important caveat

### Performance Considerations
- Impact on speed, memory, or resources
- Scalability characteristics
- Known bottlenecks

## Alternatives

### Alternative Approach 1: [Name]

**When to use**: Brief description of when this alternative is better.

**Pros**: Key advantages

**Cons**: Key disadvantages

**See**: [Link to documentation or guide]

### Alternative Approach 2: [Name]

**When to use**: Brief description of when this alternative is better.

**Pros**: Key advantages

**Cons**: Key disadvantages

**See**: [Link to documentation or guide]

## Troubleshooting

### Issue: [Common Problem 1]

**Symptoms**: How this problem manifests

**Cause**: Why this happens

**Solution**:
```bash
# Commands or steps to fix
fix-command --option
```

### Issue: [Common Problem 2]

**Symptoms**: How this problem manifests

**Cause**: Why this happens

**Solution**:
```bash
# Commands or steps to fix
another-fix-command
```

### Getting Help

If you encounter issues not covered here:
1. Check official documentation: [Link]
2. Search existing issues: [Link to issue tracker]
3. Ask in community: [Link to discussion forum]
4. Review operations logs: `21-github-and-copilot-tech/02-operations-logs/`

## References

### Official Documentation
- [Link to official docs](https://example.com/docs)
- [API Reference](https://example.com/api)

### Related Techniques
- [Related technique 1](./related-technique-1.md)
- [Related technique 2](./related-technique-2.md)

### External Resources
- [Tutorial or blog post](https://example.com/tutorial)
- [Video guide](https://example.com/video)
- [Community examples](https://example.com/examples)

## Version History

### 1.0.0 - YYYY-MM-DD
- Initial version
- Documented basic implementation
- Added examples and troubleshooting

---

## Notes for Template Users

**When creating a new technique document:**

1. **Copy this template** to a new file in `01-techniques/`
2. **Name the file** using kebab-case: `technique-name.md`
3. **Fill in all sections** - remove the italicized instructions
4. **Test all code examples** to ensure they work
5. **Include real examples** from actual usage when possible
6. **Review for clarity** - can someone unfamiliar implement this?
7. **Update the index** if one exists for the techniques catalog

**Section guidance:**

- **Overview**: Elevator pitch for the technique
- **Context**: Help readers decide if this is right for their situation
- **Implementation**: Step-by-step, actionable instructions
- **Examples**: Working code that can be copied and run
- **Trade-offs**: Honest assessment of pros and cons
- **Alternatives**: Help readers choose the best approach
- **Troubleshooting**: Address common pitfalls proactively
- **References**: Enable deeper learning

**Quality checklist:**

- [ ] All code examples tested and working
- [ ] Prerequisites clearly stated
- [ ] Success criteria defined for each step
- [ ] Trade-offs honestly assessed
- [ ] Alternatives provided
- [ ] Common issues addressed
- [ ] Links verified and working
- [ ] Reviewed by peer

---

**This template itself should not be modified without updating the governance protocols.**
