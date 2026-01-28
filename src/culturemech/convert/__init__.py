"""Raw to raw_yaml converters for CultureMech.

This package contains converters that transform raw source files
(JSON, TSV, SQL, etc.) into raw YAML format without any normalization
or validation.

Layer conversion:
    raw/ (Layer 1) → raw_yaml/ (Layer 2)

These converters perform mechanical format conversion only:
- Preserve original field names exactly
- Preserve original value formats
- No LinkML schema validation
- No ontology term resolution
- No data normalization

For normalized, validated recipes, see culturemech.import package.
"""
