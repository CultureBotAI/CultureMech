"""Lossless consolidation keys, distinct from ingredient-set candidate matches.

No conversion, hydrate stripping, stock expansion or source-equivalence inference
is performed. All scientific fields (including notes and unknown extensions) must
match as encoded. List order stays significant because evidence can cite indices
and preparation order. A match preserves assertions; it does not certify them.
"""

import json
from copy import deepcopy
from datetime import date, datetime
from hashlib import sha256

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter

ROOT_LISTS = frozenset(
    {"evidence", "references", "curation_history", "sources", "synonyms", "categories"}
)
ROOT_IDENTITY = frozenset(
    {
        "id",
        "id_lineage_token",
        "name",
        "original_name",
        "category",
        "media_term",
        "merged_from",
        "merge_fingerprint",
        "_source_path",
    }
)


def _json_default(value):
    if isinstance(value, (date, datetime)):
        return {"yaml_date": value.isoformat()}
    raise ValueError(f"Unsupported formulation value: {type(value).__name__}")


def _encode(value):
    return json.dumps(
        value, sort_keys=True, ensure_ascii=True, allow_nan=False, default=_json_default
    )


def formulation_content(recipe):
    """Project only fields whose equality is required for lossless merging."""

    def project(value, ancestors, root=False):
        if isinstance(value, (dict, list)):
            if id(value) in ancestors:
                raise ValueError("Cyclic formulation data")
            ancestors = ancestors | {id(value)}
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                if key == "evidence" or (root and key in ROOT_LISTS):
                    if not isinstance(item, list):
                        raise ValueError(f"Formulation provenance {key} must be a list")
                    _encode(item)  # Reject cycles/non-finite values even in excluded annotations.
                elif not (root and key in ROOT_IDENTITY):
                    result[key] = project(item, ancestors)
            return result
        if isinstance(value, list):
            return [project(item, ancestors) for item in value]
        return value

    return project(recipe, set(), root=True)


class FormulationFingerprinter(RecipeFingerprinter):
    """Conservative exact-assertion grouping, not chemical-equivalence matching."""

    def fingerprint(self, recipe):
        # Retain existing record routing and malformed-stock validation.
        if super().fingerprint(recipe) is None:
            return None
        content = _encode(formulation_content(recipe))
        return sha256(("culturemech-formulation-v1\n" + content).encode("utf-8")).hexdigest()

    def fingerprint_file(self, recipe_path):
        """Parse exact source bytes without the legacy escape-repair heuristic."""
        with open(recipe_path, encoding="utf-8") as stream:
            recipe = yaml.safe_load(stream)
        if not isinstance(recipe, dict):
            raise ValueError(f"Recipe is not a dictionary: {recipe_path}")
        return self.fingerprint(recipe)


def merge_formulation_evidence(recipes):
    """Deep-copy the first compatible record, retaining all scoped evidence.

    Scalar provenance (e.g. source_data/import_metadata) is not discarded: unlike
    explicitly unionable lists, it remains part of the required-equality key.
    Root identity is canonical; merged_from continues to identify source records.
    """
    if not recipes:
        raise ValueError("Cannot merge an empty formulation list")
    keys = {_encode(formulation_content(recipe)) for recipe in recipes}
    if len(keys) != 1:
        raise ValueError("Incompatible formulations; ingredient-set similarity is insufficient")

    def merge(nodes, root=False):
        first = nodes[0]
        if isinstance(first, dict):
            result = deepcopy(first)
            union_fields = ROOT_LISTS if root else {"evidence"}
            for field in sorted(union_fields):
                if not any(field in node for node in nodes):
                    continue
                entries = deepcopy(first.get(field, []))
                for node in nodes[1:]:
                    for entry in node.get(field, []):
                        if entry not in entries:
                            entries.append(deepcopy(entry))
                result[field] = entries
            for field in first:
                if field in union_fields or (root and field in ROOT_IDENTITY):
                    continue
                result[field] = merge([node[field] for node in nodes])
            return result
        if isinstance(first, list):
            return [merge([node[i] for node in nodes]) for i in range(len(first))]
        return deepcopy(first)

    return merge(recipes, root=True)
