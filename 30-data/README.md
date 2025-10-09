# 30-data

## Overview

This directory serves as the central repository for structured data, datasets, data dictionaries, and data-related resources that support analyses, documentation, and decision-making across the project.

## Purpose

- **Centralized Data Storage**: Single source of truth for all structured data
- **Data Documentation**: Maintain comprehensive data dictionaries and schemas
- **Reproducibility**: Enable verification and replication of analyses
- **Data Governance**: Ensure data quality, consistency, and proper documentation

## Directory Structure

### datasets/
Raw and processed datasets used throughout the project, organized by topic and purpose.

**Expected Contents:**
- Benefit program catalogs (CSV, JSON)
- Economic impact data (cost savings, usage statistics)
- Program eligibility matrices
- Time-series data (program changes over time)
- Comparative data (across programs, institutions, regions)

### dictionaries/
Data dictionaries, schemas, and metadata documentation for all datasets.

**Expected Contents:**
- Field definitions and descriptions
- Data type specifications
- Value constraints and validation rules
- Relationship documentation
- Change logs for schema updates

## Data Standards

### File Formats
- **Tabular Data**: CSV (UTF-8, comma-delimited, quoted strings)
- **Hierarchical Data**: JSON (formatted, 2-space indent)
- **Documentation**: Markdown for human-readable descriptions
- **Schemas**: JSON Schema or similar formal specifications

### Naming Conventions
- **Datasets**: `[topic]-[type]-[date].csv` (e.g., `benefits-catalog-2025-01-09.csv`)
- **Dictionaries**: `[dataset-name]-dictionary.md`
- Use lowercase with hyphens (kebab-case)
- Include version or date when data changes over time

### Documentation Requirements
Every dataset must have:
1. **Data dictionary** describing all fields
2. **README or header** explaining purpose and context
3. **Source attribution** with links to original data
4. **Update timestamp** indicating data currency
5. **License information** if applicable

## Data Quality Principles

### Accuracy
- Verify data against original sources
- Document any transformations or calculations
- Flag estimated or uncertain values
- Include margin of error where applicable

### Completeness
- Document missing data and reasons
- Use consistent null/NA representations
- Indicate data gaps in dictionaries
- Note sampling or coverage limitations

### Consistency
- Use standard formats across datasets
- Maintain consistent field naming
- Apply uniform units and scales
- Ensure referential integrity

### Currency
- Include data collection or update dates
- Archive outdated datasets rather than deleting
- Document update frequency and schedule
- Note when data becomes stale

## Usage Guidelines

### For Analysts
1. **Before using data**: Review the data dictionary
2. **During analysis**: Document data sources and versions used
3. **After analysis**: Share cleaned/processed data back if valuable
4. **Always**: Check currency - ensure data is still relevant

### For Contributors
1. **Adding new data**: Create corresponding data dictionary
2. **Updating data**: Document changes and increment version
3. **Derived data**: Cite source datasets and transformations
4. **Large files**: Consider compression or external hosting

### For AI Assistants
- Consult `ai_assistant_guide.yaml` for area-specific guidance
- Validate data before using in analyses or calculations
- Always cite specific datasets when making data-driven claims
- Note data limitations in any derived conclusions

## Data Privacy and Sensitivity

### Public Data Only
- This repository contains only publicly available information
- No personal, confidential, or proprietary data
- No API keys, credentials, or sensitive identifiers

### Source Attribution
- All data sources must be properly cited
- Include links to original sources when available
- Respect licenses and terms of use
- Acknowledge data providers

## Common Datasets

(To be populated as data is added)

### Benefit Programs Catalog
- **File**: `datasets/benefits-catalog-YYYY-MM-DD.csv`
- **Purpose**: Comprehensive list of all benefit programs
- **Fields**: Program name, provider, category, eligibility, value, URL
- **Update Frequency**: Monthly

### Economic Impact Data
- **File**: `datasets/economic-impact-YYYY-MM-DD.csv`
- **Purpose**: Calculated savings and economic value
- **Fields**: Program, cost_without, cost_with, savings, basis
- **Update Frequency**: Quarterly

### Program Comparison Matrix
- **File**: `datasets/program-comparisons-YYYY-MM-DD.csv`
- **Purpose**: Side-by-side feature and value comparisons
- **Update Frequency**: As needed

## Relationship to Other Areas

### 10-product-guide
- Product guide references data for claims and calculations
- Data supports economic analyses in ECONOMIA-CALCULADA.md

### 20-github-education-analyses
- Analyses use datasets for evidence-based findings
- Research generates new derived datasets

### 21-github-and-copilot-tech
- Technical guides may reference tool/service datasets
- DATA-ML-TOOLS.md describes data science platforms

### 40-scripts
- Scripts may generate or process datasets
- Document data provenance when scripts create data

## Future Enhancements

Planned improvements:
- Automated data validation scripts
- Version control for datasets (DVC or similar)
- Data visualization gallery
- API endpoints for data access
- Regular automated updates from source APIs

## Contributing Data

To contribute a new dataset:
1. Ensure data is publicly sourced and properly licensed
2. Clean and validate the data
3. Create data dictionary using template
4. Follow naming conventions
5. Document sources and methodology
6. Add entry to this README

---

**Last Updated**: 2025-01-09  
**Status**: Initial Setup - Awaiting Dataset Population  
**Maintained By**: Data Management Team
