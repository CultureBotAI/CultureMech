"""
MediaDive to CultureMech Importer

Converts MediaDive MongoDB data (3,327 recipes) to CultureMech YAML format.

Data Sources:
- mediadive_media.json - Media records from DSMZ MediaDive
- mediadive_ingredients.json - Ingredient data with ChEBI mappings
- mediadive_solutions.json - Solution compositions

Architecture:
1. Load MediaDive JSON exports
2. Map to CultureMech LinkML schema
3. Enrich with ontology terms (CHEBI, NCBITaxon)
4. Generate validated YAML files

Integration with cmm-ai-automation:
- Uses pre-exported JSON files from MongoDB
- Leverages existing ChEBI mappings
- Extends with CultureMech-specific fields
"""

import json
import yaml
from pathlib import Path
from typing import Any, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaDiveImporter:
    """Import MediaDive data into CultureMech format."""

    def __init__(
        self,
        mediadive_data_dir: Path,
        output_dir: Path,
        curator: str = "mediadive-import",
        composition_dir: Optional[Path] = None
    ):
        """
        Initialize importer.

        Args:
            mediadive_data_dir: Directory containing MediaDive JSON files
            output_dir: Output directory for CultureMech YAML files
            curator: Curator name for curation history
            composition_dir: Optional directory containing composition JSON files
        """
        self.mediadive_dir = Path(mediadive_data_dir)
        self.output_dir = Path(output_dir)
        self.curator = curator
        self.composition_dir = Path(composition_dir) if composition_dir else None

        # Track filenames to detect duplicates
        self.generated_filenames = {}  # {filename: [medium_id1, medium_id2, ...]}
        self.duplicate_count = 0

        # Load data
        self.media = self._load_json("mediadive_media.json")
        self.ingredients = self._load_json("mediadive_ingredients.json")

        # Solutions file is optional
        try:
            self.solutions = self._load_json("mediadive_solutions.json")
            self.solutions_by_id = {sol["id"]: sol for sol in self.solutions["data"]}
        except FileNotFoundError:
            logger.info("Solutions file not found (optional)")
            self.solutions = {"count": 0, "data": []}
            self.solutions_by_id = {}

        # Index for quick lookups
        self.ingredients_by_id = {ing["id"]: ing for ing in self.ingredients["data"]}

        # Index ingredients by name (lowercase) for composition matching
        self.ingredients_by_name = {}
        for ing in self.ingredients["data"]:
            name_lower = ing["name"].lower()
            self.ingredients_by_name[name_lower] = ing

        # Load compositions if directory provided
        self.compositions = {}
        if self.composition_dir and self.composition_dir.exists():
            self._load_compositions()
            logger.info(f"Loaded {len(self.compositions)} compositions")

        logger.info(f"Loaded {self.media['count']} media recipes")
        logger.info(f"Loaded {self.ingredients['count']} ingredients")
        logger.info(f"Loaded {self.solutions['count']} solutions")

    def _load_json(self, filename: str) -> dict:
        """Load MediaDive JSON file."""
        path = self.mediadive_dir / filename
        with open(path) as f:
            return json.load(f)

    def _load_compositions(self):
        """Load all composition JSON files from composition directory."""
        if not self.composition_dir:
            return

        for comp_file in self.composition_dir.glob("*.json"):
            try:
                with open(comp_file) as f:
                    comp_data = json.load(f)
                    medium_id = comp_data.get("medium_id")
                    if medium_id:
                        self.compositions[medium_id] = comp_data
            except Exception as e:
                logger.warning(f"Could not load composition file {comp_file}: {e}")

    def import_all(self, limit: Optional[int] = None) -> list[Path]:
        """
        Import all MediaDive recipes to CultureMech format.

        Args:
            limit: Optionally limit number of recipes to import (for testing)

        Returns:
            List of generated YAML file paths
        """
        generated = []
        media_list = self.media["data"][:limit] if limit else self.media["data"]

        for medium in media_list:
            try:
                yaml_path = self.import_medium(medium)
                if yaml_path:
                    generated.append(yaml_path)
                    logger.info(f"✓ Imported {yaml_path.name}")
            except Exception as e:
                logger.error(f"✗ Error importing {medium.get('name', 'Unknown')}: {e}")

        logger.info(f"\n✓ Imported {len(generated)}/{len(media_list)} recipes")

        # Report duplicate statistics
        self._report_duplicates()

        return generated

    def _report_duplicates(self):
        """
        Report duplicate filename statistics.

        Checks if any filenames were generated multiple times, which would
        cause files to be overwritten.
        """
        if self.duplicate_count == 0:
            logger.info("✓ No duplicate filenames detected - all files are unique")
            return

        # Find all duplicates
        duplicates = {
            fname: ids
            for fname, ids in self.generated_filenames.items()
            if len(ids) > 1
        }

        logger.warning(f"\n⚠️  DUPLICATE FILENAME SUMMARY")
        logger.warning(f"═══════════════════════════════════════════════════════")
        logger.warning(f"Total duplicate events: {self.duplicate_count}")
        logger.warning(f"Unique filenames with duplicates: {len(duplicates)}")
        logger.warning(f"")
        logger.warning(f"Files that were OVERWRITTEN:")
        logger.warning(f"───────────────────────────────────────────────────────")

        for filename, medium_ids in sorted(duplicates.items()):
            logger.warning(f"")
            logger.warning(f"Filename: {filename}")
            logger.warning(f"  Conflicts: {len(medium_ids)} media mapped to same file")
            for idx, mid in enumerate(medium_ids, 1):
                logger.warning(f"    {idx}. {mid}")
            logger.warning(f"  → Only the LAST one ({medium_ids[-1]}) was saved!")

        logger.warning(f"")
        logger.warning(f"═══════════════════════════════════════════════════════")
        logger.warning(f"⚠️  {len(duplicates)} file(s) were overwritten!")
        logger.warning(f"⚠️  Data loss: {self.duplicate_count} media lost")
        logger.warning(f"═══════════════════════════════════════════════════════")

    def import_medium(self, medium: dict) -> Optional[Path]:
        """
        Convert a single MediaDive medium to CultureMech YAML.

        Generates a sanitized filename while preserving the original name
        in the YAML content. See docs/FILENAME_SANITIZATION.md for details.

        Filename format: {SOURCE}_{ID}_{SANITIZED_NAME}.yaml
        Example: DSMZ_9a_VY_2_REDUCED_MEDIUM.yaml

        Original name "VY/2, REDUCED MEDIUM" is preserved in the 'original_name'
        field within the YAML file.
        """
        recipe = self._convert_to_culturemech(medium)

        if not recipe:
            return None

        # Generate unique filename with source and ID
        name = recipe["name"]
        medium_id = medium.get('id', 'unknown')
        source = medium.get('source', 'unknown')

        # Sanitize filename: Replace ALL problematic characters with underscore
        # See _sanitize_filename() docstring for complete list
        clean_name = self._sanitize_filename(name)

        # Include source and ID for uniqueness
        filename = f"{source}_{medium_id}_{clean_name}.yaml"

        # Determine category
        category = self._infer_category(medium)
        output_path = self.output_dir / category / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Check for duplicate filenames
        full_filename = f"{category}/{filename}"
        medium_identifier = f"{source}:{medium_id}"

        if full_filename in self.generated_filenames:
            # Duplicate detected!
            self.duplicate_count += 1
            existing_ids = self.generated_filenames[full_filename]
            logger.warning(
                f"⚠️  DUPLICATE FILENAME: {filename}\n"
                f"   Category: {category}\n"
                f"   Current medium: {medium_identifier} ('{name}')\n"
                f"   Previous medium(s): {', '.join(existing_ids)}\n"
                f"   File will be OVERWRITTEN!"
            )
            # Add to list of media with this filename
            self.generated_filenames[full_filename].append(medium_identifier)
        else:
            # First time seeing this filename
            self.generated_filenames[full_filename] = [medium_identifier]

        # Check if file already exists on disk (not from this run)
        if output_path.exists():
            logger.debug(f"Overwriting existing file: {filename}")

        # Write YAML
        with open(output_path, 'w') as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return output_path

    def _convert_to_culturemech(self, medium: dict) -> Optional[dict]:
        """
        Convert MediaDive medium to CultureMech schema.

        MediaDive structure:
        {
            "id": 1,
            "name": "NUTRIENT AGAR",
            "complex_medium": 1,
            "source": "DSMZ",
            "link": "https://www.dsmz.de/...",
            "min_pH": 7,
            "max_pH": 7,
            "reference": null,
            "description": null
        }
        """
        if not medium.get("name"):
            return None

        original_name = medium["name"]

        recipe = {
            "name": medium["name"],
            "original_name": original_name,  # Store original name with all special characters
            "category": "imported",  # Will be updated by _infer_category

            # Media type
            "medium_type": "COMPLEX" if medium.get("complex_medium") else "DEFINED",

            # Default to liquid (MediaDive doesn't specify)
            "physical_state": "LIQUID",

            # pH
        }

        # Add pH if available
        if medium.get("min_pH") is not None:
            if medium["min_pH"] == medium.get("max_pH"):
                recipe["ph_value"] = float(medium["min_pH"])
            else:
                recipe["ph_range"] = f"{medium['min_pH']}-{medium.get('max_pH', medium['min_pH'])}"

        # Media term (database reference)
        # Use mediadive.medium:ID format for kg-microbe compatibility
        if medium.get("id"):
            source = medium.get("source", "MediaDive")
            medium_id = medium["id"]
            recipe["media_term"] = {
                "preferred_term": f"{source} Medium {medium_id}",
                "term": {
                    "id": f"mediadive.medium:{medium_id}",
                    "label": medium["name"]
                }
            }

        # Description and link
        notes_parts = []
        if medium.get("source"):
            notes_parts.append(f"Source: {medium['source']}")
        if medium.get("link"):
            notes_parts.append(f"Link: {medium['link']}")
        if notes_parts:
            recipe["notes"] = " | ".join(notes_parts)

        # Ingredients - try to load from composition data
        medium_id = f"medium_{medium.get('id')}"
        composition_ingredients = self._parse_composition_ingredients(medium_id)

        if composition_ingredients:
            # Use actual composition data
            recipe["ingredients"] = composition_ingredients
            logger.debug(f"Loaded {len(composition_ingredients)} ingredients for {medium_id}")
        else:
            # Fallback to placeholder
            recipe["ingredients"] = [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {
                        "value": "variable",
                        "unit": "G_PER_L"
                    },
                    "notes": "Full composition available at source database"
                }
            ]

        # Preparation steps - try to load from API data
        prep_steps = self._parse_preparation_steps(str(medium.get('id')))
        if prep_steps:
            recipe["preparation_steps"] = prep_steps
            logger.debug(f"Loaded {len(prep_steps)} preparation steps for medium {medium.get('id')}")

        # Applications (generic for now)
        recipe["applications"] = [
            "Microbial cultivation"
        ]

        # References
        if medium.get("reference"):
            recipe["references"] = [
                {
                    "reference": medium["reference"]
                }
            ]

        # Curation history
        recipe["curation_history"] = [
            {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "curator": self.curator,
                "action": "Imported from MediaDive",
                "notes": f"Source: {medium.get('source', 'MediaDive')}, ID: {medium.get('id')}"
            }
        ]

        return recipe

    def _parse_composition_ingredients(self, medium_id: str) -> Optional[list]:
        """
        Parse composition data into CultureMech ingredient format.

        Priority:
        1. API-fetched data (from mediadive_api/)
        2. PDF-parsed data (from compositions/)

        Args:
            medium_id: Medium ID to look up composition (e.g., "medium_1", "dsmz_1")

        Returns:
            List of IngredientDescriptor dicts, or None if no composition found
        """
        # Extract numeric ID from medium_id (e.g., "medium_1" -> "1")
        numeric_id = medium_id.replace('medium_', '')

        # Try API data first (higher priority - more complete)
        api_ingredients = self._parse_api_composition(numeric_id)
        if api_ingredients:
            return api_ingredients

        # Fallback to PDF-parsed compositions
        # Try multiple ID patterns (medium_1, dsmz_1, etc.)
        composition = None
        for pattern in [medium_id, f"dsmz_{numeric_id}"]:
            composition = self.compositions.get(pattern)
            if composition:
                break

        if not composition or not composition.get("composition"):
            return None

        ingredients = []
        for comp_item in composition["composition"]:
            ingredient_name = comp_item.get("name", "").strip()
            if not ingredient_name:
                continue

            # Skip conditional ingredients like "if necessary"
            if "if necessary" in ingredient_name.lower():
                ingredient_name = ingredient_name.replace(", if necessary", "").replace(" if necessary", "").strip()

            # Build ingredient descriptor
            ing_desc = {
                "preferred_term": ingredient_name
            }

            # Look up ChEBI ID from ingredients database
            ing_data = self.ingredients_by_name.get(ingredient_name.lower())
            if ing_data and ing_data.get("ChEBI"):
                ing_desc["term"] = {
                    "id": f"CHEBI:{ing_data['ChEBI']}",
                    "label": ing_data["name"]
                }

            # Add concentration if available
            if comp_item.get("concentration") and comp_item.get("unit"):
                # Handle both string and numeric concentrations
                conc_value = comp_item["concentration"]
                if isinstance(conc_value, (int, float)):
                    conc_value = str(conc_value)

                unit = comp_item["unit"]

                # Map unit to CultureMech enums
                unit_map = {
                    "g/L": "G_PER_L",
                    "mg/L": "MG_PER_L",
                    "ml/L": "ML_PER_L",
                    "µg/L": "UG_PER_L",
                    "μg/L": "UG_PER_L",  # Alternative unicode
                    "mM": "MM",
                    "µM": "UM",
                    "μM": "UM",
                    "%": "PERCENT",
                    "g": "G_PER_L",  # Assume per liter
                    "mg": "MG_PER_L",
                    "ml": "ML_PER_L",
                    "µg": "UG_PER_L",
                    "μg": "UG_PER_L",
                }
                standard_unit = unit_map.get(unit, "G_PER_L")

                ing_desc["concentration"] = {
                    "value": conc_value,
                    "unit": standard_unit
                }

            # Add role as notes if available (from medium_* files)
            if comp_item.get("role"):
                ing_desc["notes"] = f"Role: {comp_item['role']}"

            ingredients.append(ing_desc)

        return ingredients if ingredients else None

    def _parse_api_composition(self, medium_id: str) -> Optional[list]:
        """
        Parse composition from API-fetched data.

        API structure:
        {
          "medium": {...},
          "solutions": [
            {
              "id": 1,
              "name": "Main sol. 1",
              "recipe": [
                {
                  "compound": "Peptone",
                  "compound_id": 1,
                  "amount": 5.0,
                  "unit": "g",
                  "g_l": 5.0,
                  "optional": 0
                }
              ]
            }
          ]
        }

        Args:
            medium_id: Medium ID (e.g., "1", "2a")

        Returns:
            List of ingredient dictionaries in CultureMech format
        """
        # Check if API data file exists (sibling directory to mediadive_dir)
        api_data_file = self.mediadive_dir.parent / "mediadive_api" / "mediadive_api_media.json"
        if not api_data_file.exists():
            return None

        # Load API data (cache it for performance)
        if not hasattr(self, '_api_data_cache'):
            try:
                with open(api_data_file) as f:
                    self._api_data_cache = json.load(f)
            except Exception as e:
                logger.warning(f"Could not load API data file: {e}")
                self._api_data_cache = None
                return None

        if not self._api_data_cache:
            return None

        # Find medium by ID
        medium_data = None
        for medium in self._api_data_cache.get("data", []):
            # API data has medium.id directly
            if str(medium.get("medium", {}).get("id")) == str(medium_id):
                medium_data = medium
                break

        if not medium_data:
            return None

        # Parse ingredients from solutions
        ingredients = []
        for solution in medium_data.get("solutions", []):
            for item in solution.get("recipe", []):
                # Skip if compound_id is None
                if not item.get("compound_id"):
                    continue

                compound_name = item.get("compound", "")

                # Skip solvents (water, distilled water) - these are implicit in concentrations
                if compound_name.lower() in ["water", "distilled water", "deionized water", "h2o"]:
                    continue

                # Build ingredient descriptor
                ingredient = {
                    "preferred_term": compound_name
                }

                # Look up ChEBI ID via ingredients database
                ing_data = self.ingredients_by_name.get(compound_name.lower())
                if ing_data and ing_data.get("ChEBI"):
                    ingredient["term"] = {
                        "id": f"CHEBI:{ing_data['ChEBI']}",
                        "label": ing_data.get("name", compound_name)
                    }

                # Add concentration
                if item.get("g_l") is not None:
                    # Use normalized g/L value from API
                    ingredient["concentration"] = {
                        "value": str(item["g_l"]),
                        "unit": "G_PER_L"
                    }
                elif item.get("amount") is not None:
                    # Fallback to raw amount and unit
                    unit = item.get("unit", "g")
                    normalized_unit = self._normalize_unit(unit)
                    ingredient["concentration"] = {
                        "value": str(item["amount"]),
                        "unit": normalized_unit
                    }

                # Add optional flag as note
                if item.get("optional", 0) == 1:
                    ingredient["notes"] = "Optional ingredient"

                # Add condition if present
                if item.get("condition"):
                    condition_note = f" ({item['condition']})"
                    ingredient["notes"] = ingredient.get("notes", "") + condition_note

                ingredients.append(ingredient)

        return ingredients if ingredients else None

    def _normalize_unit(self, unit: str) -> str:
        """
        Normalize concentration unit to CultureMech enum.

        Args:
            unit: Raw unit string from API (e.g., "g", "mg", "ml")

        Returns:
            Normalized unit enum value
        """
        unit_map = {
            "g": "G_PER_L",
            "g/L": "G_PER_L",
            "mg": "MG_PER_L",
            "mg/L": "MG_PER_L",
            "µg": "MICROG_PER_L",
            "µg/L": "MICROG_PER_L",
            "μg": "MICROG_PER_L",
            "μg/L": "MICROG_PER_L",
            "mM": "MILLIMOLAR",
            "µM": "MICROMOLAR",
            "μM": "MICROMOLAR",
            "%": "PERCENT_W_V",
            "% (w/v)": "PERCENT_W_V",
            "% (v/v)": "PERCENT_V_V",
        }
        return unit_map.get(unit, "G_PER_L")

    def _parse_preparation_steps(self, medium_id: str) -> Optional[list]:
        """
        Parse preparation steps from API-fetched data.

        API structure:
        {
          "solutions": [
            {
              "steps": [
                {"step": "Adjust pH to 7.0."},
                {"step": "Autoclave at 121°C for 15 minutes."}
              ]
            }
          ]
        }

        Args:
            medium_id: Medium ID (e.g., "1", "2a")

        Returns:
            List of PreparationStep dictionaries
        """
        # Check if API data file exists
        api_data_file = self.mediadive_dir.parent / "mediadive_api" / "mediadive_api_media.json"
        if not api_data_file.exists():
            return None

        # Load API data (use cache if available)
        if not hasattr(self, '_api_data_cache'):
            try:
                with open(api_data_file) as f:
                    self._api_data_cache = json.load(f)
            except Exception as e:
                logger.warning(f"Could not load API data file: {e}")
                self._api_data_cache = None
                return None

        if not self._api_data_cache:
            return None

        # Find medium by ID
        medium_data = None
        for medium in self._api_data_cache.get("data", []):
            if str(medium.get("medium", {}).get("id")) == str(medium_id):
                medium_data = medium
                break

        if not medium_data:
            return None

        # Extract steps from all solutions
        all_steps = []
        for solution in medium_data.get("solutions", []):
            for step_data in solution.get("steps", []):
                step_text = step_data.get("step", "").strip()
                if step_text:
                    all_steps.append(step_text)

        if not all_steps:
            return None

        # Convert to PreparationStep format
        prep_steps = []
        for i, step_text in enumerate(all_steps, 1):
            action = self._classify_preparation_action(step_text)
            prep_step = {
                "step_number": i,
                "action": action,
                "description": step_text
            }
            prep_steps.append(prep_step)

        return prep_steps

    def _classify_preparation_action(self, step_text: str) -> str:
        """
        Classify preparation step text into action enum.

        Uses keyword matching to map free-text to PreparationActionEnum.

        Args:
            step_text: Step description text

        Returns:
            Action enum value (e.g., "ADJUST_PH", "AUTOCLAVE")
        """
        step_lower = step_text.lower()

        # Action classification rules (order matters - more specific first)
        if any(kw in step_lower for kw in ["autoclave", "steam steril"]):
            return "AUTOCLAVE"
        elif any(kw in step_lower for kw in ["filter", "0.22", "0.45", "membrane"]):
            return "FILTER_STERILIZE"
        elif any(kw in step_lower for kw in ["adjust ph", "ph to", "raise ph", "lower ph"]):
            return "ADJUST_PH"
        elif any(kw in step_lower for kw in ["pour plate", "petri dish", "dispense"]):
            return "POUR_PLATES"
        elif any(kw in step_lower for kw in ["add agar", "agar for solid"]):
            return "ADD_AGAR"
        elif any(kw in step_lower for kw in ["dissolve", "suspend"]):
            return "DISSOLVE"
        elif any(kw in step_lower for kw in ["heat", "warm", "boil", "°c", "degrees"]):
            return "HEAT"
        elif any(kw in step_lower for kw in ["cool", "chill", "ice"]):
            return "COOL"
        elif any(kw in step_lower for kw in ["store", "storage", "refrigerat", "freeze"]):
            return "STORE"
        elif any(kw in step_lower for kw in ["aliquot", "divide", "portion"]):
            return "ALIQUOT"
        elif any(kw in step_lower for kw in ["mix", "stir", "shake", "agitat"]):
            return "MIX"
        else:
            # Default to MIX for unclassified steps
            return "MIX"

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize media name for use as a filename.

        REPLACES ALL PROBLEMATIC CHARACTERS WITH UNDERSCORE (_)

        Problematic characters replaced (ALL become '_'):
        ================================================
        1. Shell metacharacters:
           / (slash) - path separator
           \\ (backslash) - path separator on Windows
           : (colon) - drive separator on Windows
           * (asterisk) - wildcard
           ? (question mark) - wildcard
           " (double quote) - string delimiter
           < (less than) - redirect
           > (greater than) - redirect
           | (pipe) - pipe operator
           ' (single quote) - string delimiter
           ` (backtick) - command substitution
           ; (semicolon) - command separator
           & (ampersand) - background operator
           $ (dollar sign) - variable expansion
           ! (exclamation) - history expansion
           # (hash) - comment
           % (percent) - job control
           @ (at sign) - array operator
           ^ (caret) - history substitution
           ~ (tilde) - home directory
           [ ] (brackets) - wildcards
           { } (braces) - expansion
           ( ) (parentheses) - subshell

        2. CSV/data problematic:
           , (comma) - CSV field separator

        3. Special symbols:
           + (plus) - can cause issues in URLs
           = (equals) - can cause issues in parameters
           (space) - causes quoting issues
           (tab) - whitespace issues
           (newline) - line break issues

        4. Non-ASCII:
           ° (degree) - encoding issues
           ´ (acute accent) - encoding issues
           All other non-ASCII - potential encoding issues

        KEEPS ONLY:
        ===========
        - Letters: a-z, A-Z
        - Numbers: 0-9
        - Hyphen: - (safe separator)
        - Period: . (file extension separator)

        Examples:
        ---------
        "BACILLUS "RACEMILACTICUS" MEDIUM" → "BACILLUS_RACEMILACTICUS_MEDIUM"
        "VY/2, REDUCED MEDIUM" → "VY_2_REDUCED_MEDIUM"
        "PFENNIG'S MEDIUM I" → "PFENNIG_S_MEDIUM_I"
        "MRS MEDIUM (pre-reduced)" → "MRS_MEDIUM_pre-reduced"
        "MEDIUM (N2/CO2)" → "MEDIUM_N2_CO2"

        Args:
            name: Original media name (with any characters)

        Returns:
            Sanitized filename-safe string (no extension)
        """
        # Replace ALL non-alphanumeric except dash and dot with underscore
        clean_name = ''
        for char in name:
            if char.isalnum() or char in ['-', '.']:
                clean_name += char
            else:
                clean_name += '_'

        # Collapse multiple consecutive underscores
        while '__' in clean_name:
            clean_name = clean_name.replace('__', '_')

        # Remove leading/trailing underscores
        clean_name = clean_name.strip('_')

        return clean_name

    def _infer_category(self, medium: dict) -> str:
        """
        Infer recipe category from medium properties.

        Categories: bacterial, fungal, archaea, specialized
        """
        name = medium.get("name", "").lower()

        # Fungal media keywords
        if any(kw in name for kw in ["yeast", "malt", "potato dextrose", "sabouraud", "czapek"]):
            return "fungal"

        # Archaeal media keywords
        if any(kw in name for kw in ["halophil", "methanogen", "thermophil"]):
            return "archaea"

        # Specialized media keywords
        if any(kw in name for kw in ["anaerobic", "marine", "extreme", "photo"]):
            return "specialized"

        # Default to bacterial
        return "bacterial"

    def get_statistics(self) -> dict:
        """Get statistics about MediaDive data."""
        stats = {
            "total_media": self.media["count"],
            "total_ingredients": self.ingredients["count"],
            "total_solutions": self.solutions["count"],
            "media_by_type": {
                "defined": sum(1 for m in self.media["data"] if not m.get("complex_medium")),
                "complex": sum(1 for m in self.media["data"] if m.get("complex_medium"))
            },
            "media_by_source": {}
        }

        # Count by source
        for medium in self.media["data"]:
            source = medium.get("source", "Unknown")
            stats["media_by_source"][source] = stats["media_by_source"].get(source, 0) + 1

        return stats


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Import MediaDive recipes into CultureMech"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        help="MediaDive raw data directory (Layer 1: raw/mediadive/)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: normalized_yaml/)"
    )
    parser.add_argument(
        "-c", "--compositions",
        type=Path,
        help="Optional directory containing composition JSON files"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of recipes to import (for testing)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics and exit"
    )

    args = parser.parse_args()

    importer = MediaDiveImporter(
        mediadive_data_dir=args.input,
        output_dir=args.output,
        composition_dir=args.compositions
    )

    if args.stats:
        stats = importer.get_statistics()
        print("\nMediaDive Statistics:")
        print(json.dumps(stats, indent=2))
        return

    # Import recipes
    generated = importer.import_all(limit=args.limit)

    print(f"\n✓ Successfully imported {len(generated)} recipes")
    print(f"  Output directory: {args.output}")


if __name__ == "__main__":
    main()
