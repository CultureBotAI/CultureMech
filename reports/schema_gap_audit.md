# Schema gap audit — `src/culturemech/schema/culturemech.yaml`

Probes: `scripts/audit_schema.py` (re-runnable). Cross-referenced against the full-corpus validation TSV at `reports/instance_validation_failures.tsv`.

Schema dimensions at the time of the original audit: 40 classes, 25 enums, 0 top-level slots (everything is class-attached attributes), 2,135 lines. After the schema changes in PR #15, the schema is ~2,400 lines with 44 classes (added: `SolutionRecipe`, `ChebiTerm`, `IngredientSynonym`, `IngredientCurationMetadata`, `SourceReference`). The findings below describe the **pre-PR** schema; items marked ✓ are addressed by this PR. Re-run `scripts/audit_schema.py` after merge for a refreshed snapshot.

## 1. Closed-schema validation isn't wired into the validator

The schema's authors clearly intend a closed model — most classes have explicit `attributes:` blocks with no `additional_properties: true`. But `just validate-all` runs `linkml-validate` without `--config` or any plugin tuning, which means closed-schema enforcement is off and unknown fields silently pass. Closed mode flagged **19,403 unexpected_field rows** (and another ~10,000 in the multi-key "other" bucket) on the full corpus that the existing validator didn't see. Fixing this is `just validate-strict` (Step 1 of this analysis); making it the default validator is the highest-leverage schema-level change.

## 2. 30 of 40 classes lack an `identifier:` slot

Only `MediaRecipe.id`, `Term.id`, `MediaDatabaseTermId.id`, and a handful of derived term classes have `identifier: true`. Every descriptor (`IngredientDescriptor`, `OrganismDescriptor`, `SolutionDescriptor`, `CofactorDescriptor`, `MediaVariant`, `EvidenceItem`, `CurationEvent`, …) has none. Consequence: descriptors that are merged or referenced cross-recipe have no stable handle; deduplication has to rely on `preferred_term` string equality.

Most-impactful additions (in priority order — these are the ones that get referenced often):
- `IngredientDescriptor` (line 546, 15 attrs) — natural identifier: `term.id` (CHEBI). Add `identifier: true` on `term` *or* lift `preferred_term` as identifier.
- `OrganismDescriptor` (line 692, 14 attrs) — natural identifier: `term.id` (NCBITaxon).
- `SolutionDescriptor` (line 638, 9 attrs) — natural identifier: `preferred_term`.
- `MediaVariant` (line 1202, 6 attrs) — has `name`; lift it as identifier.
- `EvidenceItem` (line 1313) — has `reference` (PMID/DOI); lift it as identifier.

(See `audit_schema.py` output for the full 30-class list.)

## 3. 16 slots use `range: string` where an enum or typed term clearly fits

| Class.slot | Description | Suggested range |
|---|---|---|
| `MediaRecipe.fingerprint_version` | "Version of fingerprinting algorithm" | new `FingerprintVersionEnum` |
| `MediaRecipe.ph_range` | "Acceptable pH range (e.g. 6.8-7.2)" | structured `PhRange` class with `min`, `max` floats |
| `MediaRecipe.light_cycle` | "Photoperiod light:dark cycle" | new `LightCycleEnum` + free-text fallback, or a `LightCycle` class |
| `MediaRecipe.temperature_range` | "Optimal temperature range" | structured `TemperatureRange` class (mirrors existing `TemperatureValue`) |
| `MediaRecipe.salinity` | "Salt concentration for marine/brackish media" | structured `Salinity` class with `value` float + `SalinityUnitEnum` |
| `MergeMetadata.merge_version` | "Version of merge pipeline used" | new `MergePipelineVersionEnum` |
| `MergeMetadata.merge_mode` | "conservative/aggressive/variant-aware" | new `MergeModeEnum` (3 values are explicitly listed) |
| `MergeMetadata.fingerprint_mode` | "chemical/variant/original" | new `FingerprintModeEnum` (3 values explicit) |
| `OrganismDescriptor.growth_phase` | `'exponential', 'stationary'` | new `GrowthPhaseEnum` |
| `PerturbationContext.level_unit` | `'mg/L', 'mM', '%', '°C', 'µmol·m⁻²·s⁻¹'` | reuse / extend `ConcentrationUnitEnum` + add temperature/light units |
| `Dataset.dataset_type` | "genomics, transcriptomics, metabolomics, etc." | new `DatasetTypeEnum` |
| `StorageConditions.container_type` | "glass bottle, polypropylene tube" | new `ContainerTypeEnum` |
| `ImportMetadata.import_version` | regex `vMAJOR.MINOR.PATCH_YYYY-MM-DD` mentioned in description | add `pattern:` regex even if range stays `string` |
| `UpdateEvent.import_version` | same as above | same |
| `OrganismDescriptor.community_function` | "specific functional contribution" | leave as string (genuinely free-text) — flag for review |
| `SourceData.community_ids` | "List of CommunityMech IDs" | typed reference (CommunityMech ID curie) instead of free string |

## 4. Term/ontology slot naming is divergent

Three different conventions coexist (`audit_schema.py` § "Term/ontology slot naming divergence"):

- `term` — generic ontology link (CHEBI/NCBITaxon/etc). Used on 6 descriptors.
- `<provenance>_term` — `gtdb_term`, `culturemech_term`, `mediaingredientmech_term`, `media_term`. Mix of "where the term is from" and "what kind of term it is".
- `<provenance>_id` — `genome_assembly_id`, `mediaingredientmech_id`, `ontology_id`, `dataset_id`, `source_id`. Bare-string IDs, no embedded label.
- `ontology_term` — used on `PerturbationContext`, `StrainModification` only.

Consequence: a downstream consumer can't write a single function "give me all the ontology IDs on this record"; they must enumerate every spelling. Suggested cleanup:
- Standardize on `<provenance>_term` for typed term objects (kept via the `Term` hierarchy).
- Standardize on `<provenance>_id` only for bare-string identifiers where a typed term doesn't exist upstream.
- Rename `ontology_term` → `descriptor_term` or fold into the `term` convention.

## 5. `required:` is inconsistent for analogous attributes

| Slot name | Required in | Optional in |
|---|---|---|
| `concentration` | `IngredientDescriptor` | `SolutionDescriptor` |
| `description` | `PreparationStep` | `Dataset`, `MediaRecipe`, `MediaVariant`, `StrainModification` |
| `evidence` | `GrowthMetrics` | 9 other classes |
| `id` | `Term` | `MediaRecipe`, `MediaRecipeReference` |
| `import_date` | `ImportMetadata` | `SourceData` |
| `name` | `MediaRecipe`, `MediaVariant`, `RecipeSynonym`, `TransporterAnnotation` | `MediaRecipeReference` |
| `role` | `NutrientOverride` | `IngredientDescriptor` |
| `source_id` | `ImportMetadata` | `RecipeSynonym` |
| `temperature` | `StorageConditions` | `PreparationStep`, `SterilizationDescriptor` |

Some of these are intentional (e.g. `id` *required* on `Term` but optional on `MediaRecipeReference` because references can be by name). Others are likely accidental drift — `concentration` being required on `IngredientDescriptor` but not on `SolutionDescriptor` is exactly what produces the **1,228** `solutions[*].composition`-missing errors in the corpus.

## 6. `data_quality_flags` is the wrong shape

Schema (`culturemech.yaml:410-413`):
```yaml
data_quality_flags:
  description: Data quality indicators for transparency
  range: string
  multivalued: true
```
But **273 records** carry a dict, e.g. `{incomplete_composition: false, has_ontology_mappings: true, ingredients_curated: true, curation_method: 'automated_expert_mapping'}`. The dict carries genuinely useful structure that the array-of-strings shape can't express.

Suggested fix: introduce a `DataQualityFlags` class with the fields visible in the data (`incomplete_composition: bool`, `has_ontology_mappings: bool`, `ingredients_curated: bool`, `curation_method: enum`, `commercial_product: bool`, `source_information_unavailable: bool`, `manual_extraction: bool`, `trivial_medium: bool`), then change the slot range. Migrate the existing flat-string flags to the structured form.

## 7. CHEBI grounding pattern is too narrow for real ingredients

`IngredientDescriptor.term.id` is constrained to `^CHEBI:\d+$` (via the `Term.id` pattern). The corpus carries **1,872 ingredient term IDs** that are `FOODON:*` (food ontology — wheat extract, peptone, yeast extract) or `UBERON:*` (anatomical — brain, heart for BHI media). These are not mistakes; they are the right ontologies for those entities.

Two options:
1. Accept polymorphic identifiers: change the pattern to `^(CHEBI|FOODON|UBERON|ENVO):\d+$`, or remove the pattern entirely on `Term.id` and enforce per-subclass.
2. Introduce sibling term classes (`FoodOntologyTerm`, `AnatomicalTerm`) and let `IngredientDescriptor.term` be a polymorphic union.

Option 1 is the smaller change; option 2 preserves stronger typing.

## 8. Three overlapping mechanisms model "variant"

- `MediaRecipe.variants[]: MediaVariant` — inline variants, free-text `modifications: string[]`.
- `MediaRecipe.parent_media: MediaRecipeReference` and `MediaRecipe.variant_children[]: MediaRecipeReference` — cross-recipe links with a typed `relationship: MediaVariantRelationshipEnum` (16 values).
- `MediaVariant.modifications: string[]` — *free text*, doesn't use the relationship enum.

A curator wanting to express "this variant is the same recipe at higher salinity" can either fill `MediaVariant.modifications: ["3% NaCl instead of 1%"]` (free text, not queryable) or attach a `MediaRecipeReference` with `relationship: SALINITY_VARIANT` (typed). The two are visible to different consumers and never reconcile. Recommend folding inline `MediaVariant.modifications` into the typed `MediaVariantRelationshipEnum` taxonomy, or splitting into "modifications" (free-text human description) + "relationship" (typed enum) so both layers are explicit.

## 9. Enum casing audit

All declared enums use consistent casing (UPPER_SNAKE for all). The corpus, however, contains **610 records** that emit lowercase `algae`/`bacterial`/`fungal`/`archaea`/`specialized` for `category` AND **675 records** that emit UPPER `ALGAE`/`BACTERIAL`/`FUNGAL`/`ARCHAEA`/`SPECIALIZED`. The schema's `CategoryEnum` accepts the lowercase form; the uppercase records are wrong by ~610 (covered under instance validation, but the schema could disambiguate by accepting both with one canonicalized form).

## 10. Enums declared but never used: none

Probe finds zero orphan enums. Every declared enum is referenced as a `range:` somewhere.

## 11. Range references resolve cleanly

Probe finds zero attributes whose `range:` points at an undeclared class/enum/built-in. The schema is internally consistent there.

---

## How findings traceback to validation errors

| Schema issue | Validation rows it explains |
|---|---:|
| Closed-mode disabled in default validator | All 19,403 `unexpected_field` + ~10k `other` rows would have been caught earlier |
| `data_quality_flags` shape too narrow | 273 `type_mismatch` rows |
| CHEBI pattern too narrow | 1,872 `pattern_mismatch` rows |
| `physical_state` / `name` / `medium_type` required at root + records being non-MediaRecipe shape | 14,352 `missing_required` rows (4,784 × 3) |
| `solutions[*]` schema doesn't admit `name`/`notes` | ~4,000 `unexpected_field` + 4,171 multi-key "other" rows |
| Old field names (`date`, `instruction`, `reference_id`) not migrated | 21,050 paired errors |

These six items account for ~46,000 of the 59,401 ERROR rows.

## Re-run

```bash
uv run python scripts/audit_schema.py
```
