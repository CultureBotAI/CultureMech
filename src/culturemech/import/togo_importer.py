"""
TOGO Medium importer for CultureMech.

Converts TOGO Medium JSON data to CultureMech LinkML YAML format.
"""

import argparse
import json
import re
from datetime import datetime, timezone
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import yaml


class TogoImporter:
    """Import TOGO Medium data to CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """
        Initialize importer.

        Args:
            raw_data_dir: Directory containing togo_media.json
            output_dir: Root output directory for category-organized YAMLs (e.g. data/normalized_yaml/)
        """
        self.raw_data_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)

        # Create category directories
        self.categories = {
            "bacterial": self.output_dir / "bacterial",
            "fungal": self.output_dir / "fungal",
            "archaea": self.output_dir / "archaea",
            "specialized": self.output_dir / "specialized",
            "algae": self.output_dir / "algae",
        }

        for cat_dir in self.categories.values():
            cat_dir.mkdir(parents=True, exist_ok=True)

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "by_category": dict.fromkeys(self.categories.keys(), 0),
            "by_source": {},
        }

    def load_media_data(self) -> list[dict]:
        """Load TOGO media JSON."""
        media_file = self.raw_data_dir / "togo_media.json"
        if not media_file.exists():
            print(f"✗ Media file not found: {media_file}")
            print("  Run: just fetch-togo-raw")
            return []

        with open(media_file) as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "data" in data:
            return data["data"]
        return []

    def _sanitize_filename(self, name: str) -> str:
        r"""
        Sanitize filename for filesystem compatibility.

        Replaces ALL non-alphanumeric characters (except dash and dot) with underscore.
        This ensures filenames are safe for:
        - All operating systems (Windows, macOS, Linux)
        - Shell commands (no metacharacters)
        - CSV exports (no commas)
        - URLs (URL-safe characters only)

        Problematic characters replaced with '_':
        - Shell metacharacters: / \ : * ? " < > | ' ` ; & $ ! # % @ ^ ~ [ ] { } ( )
        - Separators: , (causes CSV issues)
        - Special symbols: + = (can cause issues in some contexts)
        - Non-ASCII: ° ´ and other accented/special characters
        - Whitespace: space, tab, newline

        Allowed characters: a-z A-Z 0-9 _ - .
        """
        clean_name = ""
        for char in name:
            if char.isalnum() or char in ["-", "."]:
                clean_name += char
            else:
                clean_name += "_"

        # Collapse multiple consecutive underscores
        while "__" in clean_name:
            clean_name = clean_name.replace("__", "_")

        # Remove leading/trailing underscores
        clean_name = clean_name.strip("_")

        return clean_name

    def _infer_category(self, medium: dict) -> str:
        """
        Infer category from medium name or metadata.

        Args:
            medium: TOGO medium object

        Returns:
            Category name (bacterial/fungal/archaea/specialized/algae)
        """
        name = medium.get("name", "").lower()

        # Fungal keywords
        if any(
            kw in name
            for kw in [
                "yeast",
                "malt",
                "potato dextrose",
                "sabouraud",
                "czapek",
                "fungal",
                "fungi",
            ]
        ):
            return "fungal"

        # Archaea keywords
        if any(
            kw in name for kw in ["halophil", "methanogen", "archae", "thermophil", "sulfolobus"]
        ):
            return "archaea"

        # Algae keywords
        if any(kw in name for kw in ["algae", "algal", "phyto", "chlorella", "spirulina"]):
            return "algae"

        # Specialized keywords
        if any(
            kw in name
            for kw in [
                "anaerobic",
                "marine",
                "extreme",
                "thermophil",
                "acidophil",
                "alkalophil",
            ]
        ):
            return "specialized"

        # Default to bacterial
        return "bacterial"

    def _extract_source_info(self, medium: dict) -> dict[str, str]:
        """
        Extract source information from medium.

        Args:
            medium: TOGO medium object

        Returns:
            Dict with source, original_id, url, gm_id
        """
        meta = medium.get("meta", {})

        # Extract gm_id from URL like "http://togomedium.org/medium/M3006"
        gm_url = meta.get("gm", "")
        gm_id = gm_url.split("/")[-1] if gm_url else ""

        original_id = meta.get("original_media_id", "")
        src_url = meta.get("src_url", "")

        # Extract source from original_media_id (e.g., "JCM_M1331" -> "JCM")
        source = ""
        if original_id and "_" in original_id:
            source = original_id.split("_")[0]

        # Build URL to TOGO page
        url = f"https://togomedium.org/medium/{gm_id}"

        return {
            "source": source or "TOGO",
            "original_id": original_id or gm_id,
            "url": url,
            "gm_id": gm_id,
            "src_url": src_url,
        }

    @staticmethod
    def _solution_name(value: object) -> str:
        """Normalize TOGO's local section labels for exact matching."""
        return str(value or "").strip().removesuffix(":").strip()

    @staticmethod
    def _decimal(value: object) -> Decimal | None:
        if value in (None, ""):
            return None
        try:
            return Decimal(str(value))
        except (InvalidOperation, ValueError):
            return None

    @staticmethod
    def _format_decimal(value: Decimal, places: int | None = None) -> str:
        if places is not None:
            quantum = Decimal(1).scaleb(-places)
            return format(value.quantize(quantum, rounding=ROUND_HALF_UP), f".{places}f")
        normalized = value.normalize()
        return format(normalized, "f")

    @staticmethod
    def _item_notes(item: dict) -> str | None:
        notes_parts = []
        role_labels = [role.get("label") for role in item.get("roles", []) if role.get("label")]
        if role_labels:
            notes_parts.append(f"Role: {', '.join(role_labels)}")
        property_labels = [
            prop.get("label") for prop in item.get("properties", []) if prop.get("label")
        ]
        if property_labels:
            notes_parts.append(f"Properties: {', '.join(property_labels)}")
        return "; ".join(notes_parts) if notes_parts else None

    @staticmethod
    def _is_gas_item(item: dict) -> bool:
        """Return whether TOGO explicitly classifies an item as a gas."""
        return any(
            str(prop.get("id") or "") == "GMO_000077"
            or str(prop.get("label") or "").casefold() in {"gas", "ガス"}
            for prop in item.get("properties", [])
            if isinstance(prop, dict)
        )

    def _ingredient_from_item(
        self,
        item: dict,
        *,
        batch_volume_ml: Decimal | None = None,
        allow_unquantified: bool = False,
        allow_final_concentration: bool = False,
    ) -> dict | None:
        """Convert one quantified TOGO item, optionally normalizing a stock batch."""
        amount = self._decimal(item.get("volume"))
        if amount is None:
            if not allow_unquantified:
                return None
            final_concentration = self._decimal(item.get("conc_value"))
            if final_concentration is not None and allow_final_concentration:
                ingredient = {
                    "preferred_term": item.get("component_name", "Unknown"),
                    "concentration": {
                        "value": self._format_decimal(final_concentration),
                        "unit": self._parse_unit(str(item.get("conc_unit") or "")),
                    },
                }
                notes = self._item_notes(item)
                if notes:
                    ingredient["notes"] = notes
                return ingredient
            if not item.get("gmo_id") or not self._is_gas_item(item):
                return None
            ingredient = {
                "preferred_term": item.get("component_name", "Unknown"),
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
            notes = self._item_notes(item)
            if notes:
                ingredient["notes"] = notes
            return ingredient

        unit = str(item.get("unit") or "")
        concentration_unit = self._parse_unit(unit)
        normalized_from_batch = False
        if batch_volume_ml is not None and unit.casefold().replace(" ", "") in {
            "g",
            "mg",
            "ml",
            "l",
        }:
            if batch_volume_ml <= 0:
                return None
            amount = amount * Decimal(1000) / batch_volume_ml
            normalized_from_batch = True

        if normalized_from_batch:
            amount_text = self._format_decimal(amount, places=9).rstrip("0").rstrip(".")
        else:
            amount_text = self._format_decimal(amount)

        ingredient = {
            "preferred_term": item.get("component_name", "Unknown"),
            "concentration": {
                "value": amount_text,
                "unit": concentration_unit,
            },
        }
        notes = self._item_notes(item)
        if notes:
            ingredient["notes"] = notes
        return ingredient

    def _assembled_solution_sections(self, medium: dict) -> list[tuple[dict, dict, Decimal]]:
        """Recognize a medium assembled from complete, locally defined solution batches.

        TOGO normally uses a local reference for a stock addition, where the referenced
        amount is not the stock's preparation volume. We only accept the narrower case
        where every primary component is local and each referenced millilitre amount
        exactly equals the sum of millilitre components in its matching section. That
        evidence makes both the stock-batch basis and final mixed-batch volume explicit.
        """
        components = [
            section for section in medium.get("components", []) if isinstance(section, dict)
        ]
        primary_sections = [
            section
            for section in components
            if not self._solution_name(section.get("subcomponent_name"))
        ]
        nested_sections = [
            section
            for section in components
            if self._solution_name(section.get("subcomponent_name"))
        ]
        if not primary_sections or not nested_sections:
            return []

        own_id = str((medium.get("meta", {}).get("gm") or "").split("/")[-1])
        primary_items = [
            item
            for section in primary_sections
            for item in section.get("items", [])
            if isinstance(item, dict)
        ]
        if not primary_items:
            return []

        section_by_name: dict[str, dict] = {}
        for section in nested_sections:
            name = self._solution_name(section.get("subcomponent_name"))
            if name in section_by_name:
                return []
            section_by_name[name] = section

        matches: list[tuple[dict, dict, Decimal]] = []
        for item in primary_items:
            amount = self._decimal(item.get("volume"))
            if (
                str(item.get("reference_media_id") or "") != own_id
                or str(item.get("unit") or "").lower().replace(" ", "") != "ml"
                or amount is None
                or amount <= 0
            ):
                return []
            name = self._solution_name(item.get("component_name"))
            section = section_by_name.get(name)
            if section is None:
                return []
            liquid_total = sum(
                (
                    self._decimal(component.get("volume")) or Decimal(0)
                    for component in section.get("items", [])
                    if str(component.get("unit") or "").lower().replace(" ", "") == "ml"
                ),
                Decimal(0),
            )
            if liquid_total != amount:
                return []
            matches.append((item, section, amount))

        if len(matches) != len(nested_sections):
            return []
        return matches

    def _extract_assembled_solutions(self, medium: dict) -> list[dict]:
        matches = self._assembled_solution_sections(medium)
        if not matches:
            return []

        total_batch_ml = sum((amount for _, _, amount in matches), Decimal(0))
        comments = [
            row
            for row in medium.get("comments", [])
            if isinstance(row, dict) and str(row.get("comment") or "").strip()
        ]
        section_indices = sorted(
            int(section.get("paragraph_index") or 0) for _, section, _ in matches
        )
        solutions = []
        for reference, section, batch_volume_ml in matches:
            composition = []
            for item in section.get("items", []):
                ingredient = self._ingredient_from_item(item, batch_volume_ml=batch_volume_ml)
                if ingredient is not None:
                    composition.append(ingredient)

            paragraph_index = int(section.get("paragraph_index") or 0)
            later_indices = [index for index in section_indices if index > paragraph_index]
            next_index = min(later_indices) if later_indices else None
            section_comments = [
                str(row["comment"]).strip()
                for row in comments
                if int(row.get("paragraph_index") or 0) > paragraph_index
                and (next_index is None or int(row.get("paragraph_index") or 0) < next_index)
            ]
            source_amount = self._decimal(reference.get("volume")) or Decimal(0)
            normalized_amount = source_amount * Decimal(1000) / total_batch_ml
            solution = {
                "preferred_term": self._solution_name(reference.get("component_name")),
                "composition": composition,
                "concentration": {
                    "value": self._format_decimal(normalized_amount, places=3),
                    "unit": "ML_PER_L",
                },
                "notes": (
                    f"Source batch uses {self._format_decimal(source_amount)} ml in "
                    f"{self._format_decimal(total_batch_ml)} ml total; normalized to ml/L."
                ),
            }
            if section_comments:
                solution["preparation_notes"] = " ".join(section_comments)
            solutions.append(solution)
        return solutions

    @classmethod
    def _is_primary_section(cls, section: dict) -> bool:
        name = cls._solution_name(section.get("subcomponent_name"))
        return not name or bool(re.fullmatch(r"main solution(?:\s+\d+)?", name, re.I))

    @staticmethod
    def _looks_like_solution_item(item: dict) -> bool:
        if item.get("reference_media_id"):
            return True
        name = str(item.get("component_name") or "")
        properties = {
            str(row.get("label") or "").casefold()
            for row in item.get("properties", [])
            if isinstance(row, dict)
        }
        return "solution" in properties or bool(re.search(r"\bsolution\b", name, re.I))

    def _local_batch_volume_ml(self, item: dict, section: dict) -> Decimal | None:
        """Infer a local stock basis only when TOGO's volumes corroborate it."""
        reference_amount = self._decimal(item.get("volume"))
        reference_unit = str(item.get("unit") or "").casefold().replace(" ", "")
        if reference_amount is None or reference_amount <= 0:
            return None
        if reference_unit == "l":
            reference_amount *= Decimal(1000)
        elif reference_unit != "ml":
            return None

        liquid_total = Decimal(0)
        water_amounts = []
        for component in section.get("items", []):
            if not isinstance(component, dict):
                continue
            amount = self._decimal(component.get("volume"))
            unit = str(component.get("unit") or "").casefold().replace(" ", "")
            if amount is None or unit not in {"ml", "l"}:
                continue
            amount_ml = amount * Decimal(1000) if unit == "l" else amount
            liquid_total += amount_ml
            if str(component.get("gmo_id") or "") == "GMO_001001":
                water_amounts.append(amount_ml)

        if reference_amount == liquid_total or reference_amount in water_amounts:
            return reference_amount
        return None

    def _local_solution_composition(
        self, item: dict, section: dict
    ) -> tuple[list[dict], list[str]]:
        batch_volume_ml = self._local_batch_volume_ml(item, section)
        if batch_volume_ml is None:
            return [], []

        composition = []
        nested_references = []
        for component in section.get("items", []):
            if not isinstance(component, dict):
                continue
            if component.get("reference_media_id"):
                nested_references.append(self._solution_name(component.get("component_name")))
                continue
            ingredient = self._ingredient_from_item(
                component,
                batch_volume_ml=batch_volume_ml,
                allow_unquantified=True,
            )
            if ingredient is not None:
                composition.append(ingredient)
        return composition, nested_references

    def _solution_from_item(self, item: dict, local_sections: dict[str, dict]) -> dict | None:
        """Convert a primary-recipe stock addition without flattening its contents."""
        # A concentration-only reagent such as 5 M NaOH is normally an adjustment
        # reagent named in preparation prose, not a quantified stock addition.
        amount = self._decimal(item.get("volume"))
        if amount is None and item.get("conc_value") is not None:
            return None

        name = self._solution_name(item.get("component_name"))
        if not name:
            return None
        local_section = local_sections.get(name)
        if local_section is None:
            composition: list[dict] = []
            nested_references: list[str] = []
        else:
            composition, nested_references = self._local_solution_composition(item, local_section)
        solution: dict[str, Any] = {
            "preferred_term": name,
            "composition": composition,
        }
        if amount is not None:
            solution["concentration"] = {
                "value": self._format_decimal(amount),
                "unit": self._parse_unit(str(item.get("unit") or "")),
            }

        notes = []
        item_notes = self._item_notes(item)
        if item_notes:
            notes.append(item_notes)
        reference = str(item.get("reference_media_id") or "")
        if reference:
            notes.append(f"Defined in TOGO medium {reference}.")
        if local_section is not None:
            if composition:
                notes.append(
                    "Local TOGO stock formulation is represented as an inline "
                    "composition; it is not flattened into final-medium ingredients."
                )
            else:
                notes.append(
                    "Local stock formulation is retained in the TOGO source payload; "
                    "its batch basis was not explicit enough to normalize safely."
                )
        if nested_references:
            solution["preparation_notes"] = (
                "The source stock also adds these referenced stocks, retained without "
                f"flattening: {', '.join(nested_references)}."
            )
        if notes:
            solution["notes"] = " ".join(notes)
        return solution

    def _extract_primary_components(self, medium: dict) -> tuple[list[dict], list[dict]] | None:
        """Extract final ingredients and stock additions from TOGO's primary layers.

        TOGO calls each final-recipe paragraph ``main solution N``. Other named
        sections describe locally defined stocks. Reading every section as final
        ingredients was the flattening defect; this method keeps those layers apart.
        """
        components = [
            section for section in medium.get("components", []) if isinstance(section, dict)
        ]
        primary_sections = [section for section in components if self._is_primary_section(section)]
        if not primary_sections:
            return None
        local_sections = {
            self._solution_name(section.get("subcomponent_name")): section
            for section in components
            if not self._is_primary_section(section)
        }

        ingredients: list[dict] = []
        solutions: list[dict] = []
        gas_keys: set[str] = set()
        for section in primary_sections:
            for item in section.get("items", []):
                if not isinstance(item, dict):
                    continue
                if self._looks_like_solution_item(item):
                    amount = self._decimal(item.get("volume"))
                    name = self._solution_name(item.get("component_name"))
                    explicit_solution_name = bool(re.search(r"\bsolution\b", name, re.I))
                    if amount is not None or item.get("reference_media_id"):
                        solution = self._solution_from_item(item, local_sections)
                        if solution is not None:
                            solutions.append(solution)
                        continue
                    if explicit_solution_name:
                        # With no working amount this is normally an adjustment
                        # stock described in the paragraph's preparation prose.
                        continue
                ingredient = self._ingredient_from_item(
                    item,
                    allow_unquantified=True,
                    allow_final_concentration=True,
                )
                if ingredient is not None:
                    if self._is_gas_item(item):
                        gas_key = (
                            str(item.get("gmo_id") or "").strip()
                            or str(ingredient.get("preferred_term") or "").casefold()
                        )
                        if gas_key in gas_keys:
                            continue
                        gas_keys.add(gas_key)
                    ingredients.append(ingredient)
        return ingredients, solutions

    @staticmethod
    def _extract_preparation_steps(medium: dict) -> list[dict]:
        steps = []
        for row in medium.get("comments", []):
            comment = str(row.get("comment") or "").strip() if isinstance(row, dict) else ""
            if not comment:
                continue
            lowered = comment.lower()
            if "autoclave" in lowered:
                action = "AUTOCLAVE"
            elif "filter" in lowered:
                action = "FILTER_STERILIZE"
            elif "adjust ph" in lowered:
                action = "ADJUST_PH"
            elif "dissolve" in lowered:
                action = "DISSOLVE"
            else:
                action = "MIX"
            steps.append(
                {
                    "step_number": len(steps) + 1,
                    "action": action,
                    "description": comment,
                }
            )
        return steps

    def _extract_ingredients(self, medium: dict) -> list[dict]:
        """
        Extract ingredients from medium.

        Args:
            medium: TOGO medium object

        Returns:
            List of ingredient descriptors
        """
        ingredients = []
        components = medium.get("components", [])

        if not components:
            # Placeholder ingredient if no composition
            return [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {"value": "variable", "unit": "G_PER_L"},
                    "notes": "Full composition available at source database",
                }
            ]

        # TOGO has nested structure: components -> items
        for comp_section in components:
            items = comp_section.get("items", [])
            for item in items:
                ingredient = self._ingredient_from_item(item)
                if ingredient is not None:
                    ingredients.append(ingredient)

        return (
            ingredients
            if ingredients
            else [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {"value": "variable", "unit": "G_PER_L"},
                    "notes": "Full composition available at source database",
                }
            ]
        )

    def _parse_unit(self, unit_str: str) -> str:
        """
        Parse unit string to CultureMech enum value.

        Args:
            unit_str: Unit string from TOGO (e.g., "g/L", "mg/L")

        Returns:
            CultureMech ConcentrationUnitEnum value
        """
        unit_lower = unit_str.lower().replace(" ", "")

        unit_map = {
            "g": "G_PER_L",
            "g/l": "G_PER_L",
            "g/liter": "G_PER_L",
            "mg": "MG_PER_L",
            "mg/l": "MG_PER_L",
            "mg/liter": "MG_PER_L",
            "ml": "ML_PER_L",
            "ml/l": "ML_PER_L",
            "l": "L",
            "μg/l": "MICROG_PER_L",
            "ug/l": "MICROG_PER_L",
            "m": "MOLAR",
            "mm": "MILLIMOLAR",
            "μm": "MICROMOLAR",
            "um": "MICROMOLAR",
            "%w/v": "PERCENT_W_V",
            "%v/v": "PERCENT_V_V",
            "%": "PERCENT_W_V",
        }

        return unit_map.get(unit_lower, "G_PER_L")

    def _extract_ph(self, medium: dict) -> dict:
        """
        Extract pH information.

        Args:
            medium: TOGO medium object

        Returns:
            Dict with ph_value or ph_range
        """
        ph_info = {}

        # TOGO may have pH as single value or range
        ph = medium.get("ph")
        if ph is not None:
            if isinstance(ph, (int, float)):
                ph_info["ph_value"] = float(ph)
            elif isinstance(ph, str):
                # Try to parse range like "7.0-7.5"
                if "-" in ph:
                    ph_info["ph_range"] = ph
                else:
                    try:
                        ph_info["ph_value"] = float(ph)
                    except ValueError:
                        pass

        return ph_info

    def _convert_to_culturemech(self, medium: dict) -> dict | None:
        """
        Convert TOGO medium to CultureMech schema.

        Args:
            medium: TOGO medium object

        Returns:
            CultureMech recipe dict or None if invalid
        """
        meta = medium.get("meta", {})
        name = meta.get("name")

        if not name:
            return None

        # Extract source info (includes gm_id)
        source_info = self._extract_source_info(medium)
        gm_id = source_info["gm_id"]

        # Base recipe
        recipe = {
            "name": name,
            "original_name": name,  # Store original name with all special characters
            "category": "imported",
            "medium_type": "COMPLEX",  # Default, could be refined
            "physical_state": "LIQUID",  # Default
        }

        # Description (if available)
        description = medium.get("description")
        if description:
            recipe["description"] = description

        # pH (if available)
        ph_info = self._extract_ph(medium)
        recipe.update(ph_info)

        # Preserve complete local batches as solutions when TOGO exposes enough
        # volume evidence to distinguish stock composition from final ingredients.
        solutions = self._extract_assembled_solutions(medium)
        if solutions:
            recipe["ingredients"] = []
            recipe["solutions"] = solutions
            preparation_steps = self._extract_preparation_steps(medium)
            if preparation_steps:
                recipe["preparation_steps"] = preparation_steps
        else:
            primary_components = self._extract_primary_components(medium)
            if primary_components is None:
                ingredients = self._extract_ingredients(medium)
                referenced_solutions = []
            else:
                ingredients, referenced_solutions = primary_components
            if ingredients:
                recipe["ingredients"] = ingredients
            if referenced_solutions:
                recipe["solutions"] = referenced_solutions
            if primary_components is not None:
                preparation_steps = self._extract_preparation_steps(medium)
                if preparation_steps:
                    recipe["preparation_steps"] = preparation_steps

        # Media term (TOGO database reference)
        recipe["media_term"] = {
            "preferred_term": f"TOGO Medium {gm_id}",
            "term": {"id": f"TOGO:{gm_id}", "label": name},
        }

        # Notes with source info
        notes_parts = [f"Source: {source_info['url']}"]
        if source_info["source"] and source_info["source"] != "TOGO":
            notes_parts.append(
                f"Original source: {source_info['source']} - {source_info['original_id']}"
            )
        if source_info.get("src_url"):
            notes_parts.append(f"Original URL: {source_info['src_url']}")
        recipe["notes"] = "\n".join(notes_parts)

        # Applications
        recipe["applications"] = ["Microbial cultivation"]

        # Curation history
        recipe["curation_history"] = [
            {
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "curator": "togo-import",
                "action": "Imported from TOGO Medium",
                "notes": f"Source: {source_info['source']}, ID: {gm_id}",
            }
        ]

        return recipe

    def import_all(self, limit: int | None = None) -> dict:
        """
        Import all TOGO media.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            Statistics dict
        """
        print("=" * 60)
        print("TOGO Medium Importer")
        print("=" * 60)

        # Load data
        media_data = self.load_media_data()
        if not media_data:
            print("✗ No media data found")
            return self.stats

        self.stats["total"] = len(media_data)
        print(f"Found {len(media_data)} media in TOGO data")

        if limit:
            media_data = media_data[:limit]
            print(f"Limiting to first {limit} media")

        # Import each medium
        for i, medium in enumerate(media_data, 1):
            meta = medium.get("meta", {})
            name = meta.get("name", "Unknown")

            # Extract gm_id from URL
            gm_url = meta.get("gm", "")
            gm_id = gm_url.split("/")[-1] if gm_url else "unknown"

            print(f"[{i}/{len(media_data)}] Importing {gm_id}: {name[:50]}...", end="")

            try:
                recipe = self._convert_to_culturemech(medium)
                if not recipe:
                    print(" ✗ (invalid)")
                    self.stats["failed"] += 1
                    continue

                # Determine category
                category = self._infer_category(medium)
                output_dir = self.categories[category]

                # Generate unique filename with source and ID
                source_info = self._extract_source_info(medium)
                source = source_info["source"]
                gm_id = source_info["gm_id"]

                # Sanitize name for filename
                clean_name = self._sanitize_filename(name)

                # Include source and ID for uniqueness (like MediaDive format)
                filename = f"TOGO_{gm_id}_{clean_name}.yaml"
                output_path = output_dir / filename

                # Write YAML
                with open(output_path, "w") as f:
                    yaml.dump(
                        recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False
                    )

                self.stats["success"] += 1
                self.stats["by_category"][category] += 1

                # Track by source
                source = self._extract_source_info(medium)["source"]
                self.stats["by_source"][source] = self.stats["by_source"].get(source, 0) + 1

                print(f" ✓ ({category})")

            except Exception as e:
                print(f" ✗ Error: {e}")
                self.stats["failed"] += 1

        # Print summary
        print("\n" + "=" * 60)
        print("Import Summary")
        print("=" * 60)
        print(f"Total: {self.stats['total']}")
        print(f"Success: {self.stats['success']}")
        print(f"Failed: {self.stats['failed']}")
        print(f"Success rate: {self.stats['success']/self.stats['total']*100:.1f}%")
        print("\nBy category:")
        for cat, count in self.stats["by_category"].items():
            if count > 0:
                print(f"  {cat:12s}: {count:4d}")
        print("\nBy source:")
        for source, count in sorted(
            self.stats["by_source"].items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {source:12s}: {count:4d}")
        print("=" * 60)

        return self.stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Import TOGO Medium data to CultureMech")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default="data/raw/togo",
        help="Input directory with TOGO raw JSON files (Layer 1: data/raw/togo/)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: data/normalized_yaml/)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of media to import (for testing)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics only (dry run)",
    )

    args = parser.parse_args()

    importer = TogoImporter(raw_data_dir=args.input, output_dir=args.output)

    if args.stats:
        media_data = importer.load_media_data()
        print(f"Total media: {len(media_data)}")
        print(f"Raw data: {args.input}")
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
