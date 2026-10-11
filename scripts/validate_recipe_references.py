#!/usr/bin/env python3
"""Validate recipe references through LinkML with literal official-source handling."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict
from pathlib import Path

from linkml.validator import Validator
from linkml_reference_validator.cli.shared import load_validation_config
from linkml_reference_validator.plugins.reference_validation_plugin import ReferenceValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError

from culturemech.validation.recipe_references import RecipeTextValidator
from culturemech.validation.write_validated import DEFAULT_SCHEMA_PATH, infer_target_class


def validate_data(data, schema, text_validator, target_class=None):
    instances = data if isinstance(data, list) else [data]
    if not instances or any(not isinstance(i, dict) for i in instances):
        raise ValueError("Expected a recipe mapping or nonempty list of mappings")
    plugin = ReferenceValidationPlugin(config=text_validator.config)
    plugin.validator = text_validator
    schema_view = SchemaView(str(schema))
    validator = Validator(schema=schema_view.schema, validation_plugins=[plugin])
    results = []
    for instance in instances:
        cls = target_class or infer_target_class(instance)
        if not schema_view.get_class(cls):
            raise ValueError(f"Unknown target class: {cls}")
        results.extend(validator.validate(instance, target_class=cls).results)
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH)
    parser.add_argument("--target-class")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument(
        "--refresh", action="store_true", help="Refresh official recipe raw captures"
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit individual checks, including passes"
    )
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.WARNING)
    try:
        config = load_validation_config(args.config)
        if args.cache_dir:
            config.cache_dir = args.cache_dir
        text_validator = RecipeTextValidator(config, refresh=args.refresh)
        data = YAML(typ="safe").load(args.file.read_text())
        issues = validate_data(data, args.schema, text_validator, args.target_class)
        if args.json:
            print(
                json.dumps(
                    {
                        "file": str(args.file),
                        "checks": [asdict(r) for r in text_validator.results],
                        "issues": [str(r.message) for r in issues],
                        "valid": not issues and all(r.is_valid for r in text_validator.results),
                    },
                    indent=2,
                )
            )
        else:
            for issue in issues:
                print(f"  [{issue.severity.value}] {issue.message}")
                if issue.instantiates:
                    print(f"    Location: {issue.instantiates}")
            print(f"Reference checks: {len(text_validator.results)}; issues: {len(issues)}")
        return int(bool(issues) or any(not r.is_valid for r in text_validator.results))
    except (OSError, ValueError, TypeError, YAMLError) as error:
        print(f"[ERROR] reference_validation: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
