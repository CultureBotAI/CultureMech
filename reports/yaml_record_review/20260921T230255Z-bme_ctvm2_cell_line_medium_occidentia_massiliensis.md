# YAML Record Review: bme_ctvm2_cell_line_medium_occidentia_massiliensis

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`
- Started UTC: 2026-09-21T23:02:55Z
- Finished UTC: 2026-09-21T23:05:26Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:001155` |
| Generated label | `bme_ctvm2_cell_line_medium_occidentia_massiliensis` |
| Original name | `BME/CTVM2 cell line medium (Occidentia massiliensis)` |
| Source term | `mediadive.medium:1670` / DSMZ Medium 1670 |
| Maintained owner | `data/normalized_yaml/bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml` |
| Related maintained solution | `data/normalized_yaml/bacterial/mediadive_3465_Main_sol_1670.yaml` |
| Generated status | Derived from one active normalized MediaDive input by `merge_recipes.py`; future fixes belong in normalized YAML or the MediaDive/DSMZ repair path, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:001155`,
`mediadive.medium:1670`, `mediadive.solution:3465`, `Medium 1670`, and
`bme_ctvm2_cell_line_medium_occidentia_massiliensis` under `data`, `src`, and
`scripts` found one active normalized MediaRecipe owner, one active normalized
`Main sol. 1670` SolutionRecipe sibling, generated index and merge copies,
one unrelated specialized `ZMB_ALS_noGlutamine` reference to
`mediadive.medium:1670`, and the checked-in
`scripts/repair_dsmz_1670_bme_score15.py` mutator that repaired this record on
September 11.

`find reports/yaml_record_review -name
'*bme_ctvm2_cell_line_medium_occidentia_massiliensis.md'` returned no path
before this report was created.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml --out /private/tmp/bme_ctvm2_cell_line_medium_occidentia_massiliensis.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema` entrypoint was checked during this review
batch and failed before target-specific validation while the project `uv`
environment tried to build `llvmlite==0.46.0` under Python 3.13. The
no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- DSMZ Medium 1670 and the MediaDive 1670 page both identify
  `BME/CTVM2 cell line medium (Occidentia massiliensis)`.
- DSMZ and MediaDive both give the medium batch as 70 ml L-15 medium,
  10 ml tryptose phosphate broth, 20 ml foetal/fetal bovine serum, and
  1 ml 200 mM L-glutamine.
- The active normalized owner already represents that formulation as
  `ML_PER_L` additions normalized from a 101 ml batch and keeps L-glutamine as
  a 9.90099 ml/L addition of a 200 mM stock.
- The generated merge is stale relative to the active normalized owner: it
  still publishes pre-repair direct `G_PER_L` rows for L-15 medium,
  tryptose-phosphate, fetal bovine serum, and L-glutamine.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/DSMZ_Medium1670.pdf.png` | Rendered DSMZ Medium 1670 PDF: medium identity, four recipe volumes, BME/CTVM2 culture procedure, infection procedure, and 28 C incubation |
| `/private/tmp/mediadive-1670.html` | MediaDive 1670 identity, source DSMZ link, rendered ingredient rows, and machine-readable procedure and reagent entries |
| `data/normalized_yaml/bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml` | Maintained MediaRecipe owner after the September 11 DSMZ 1670 repair |
| `data/normalized_yaml/bacterial/mediadive_3465_Main_sol_1670.yaml` | Maintained `Main sol. 1670` SolutionRecipe sibling after the September 11 DSMZ 1670 repair |
| `scripts/repair_dsmz_1670_bme_score15.py` | Maintained repair script that applies the September 11 correction |

Supported upstream:

- DSMZ Medium 1670 supports the medium identity, the four liquid components,
  ordinary-air incubation in sealed flasks or flat-sided tubes, weekly medium
  changes, the no-trypsin/no-EDTA subculture warning, and the infection step
  using 3 ml fresh medium plus 1 ml thawed `Occidentia` strain in a flask
  reduced to 5 ml.
- DSMZ supports the 28 C closed-lid incubation without CO2 and 7-10 day
  inspection after infection; the active normalized owner keeps `28 C` as
  `temperature_value: 28.0`.

Unsupported or stale in the generated merge:

- L-15 medium, tryptose-phosphate, and fetal bovine serum are still represented
  as 70, 10, and 20 `G_PER_L`; the source and repaired normalized owner use
  70, 10, and 20 ml in a 101 ml batch.
- L-glutamine is still represented as a direct `0.029228 G_PER_L` addition;
  the source and repaired normalized owner use 1 ml of a 200 mM L-glutamine
  stock in a 101 ml batch.
- The generated `HEAT` action on the infection step is unsupported. DSMZ says
  to infect the cells and incubate at 28 C, not to heat-sterilize or heat the
  medium.
- The generated merge lacks the repaired references, `ingredients_curated` and
  `has_ontology_mappings` flags, `temperature_value`, source-scoped ingredient
  notes, and 200 mM stock representation now present in the active normalized
  owner.

## Completeness

- Complete enough upstream: the maintained MediaRecipe and `Main sol. 1670`
  SolutionRecipe now preserve the source volume units, final 101 ml arithmetic,
  opaque cell-culture input identities, L-glutamine stock strength, 28 C
  infection temperature, and DSMZ/MediaDive references.
- Consequentially incomplete in the generated layer: it predates the
  September 11 repair and still publishes the pre-repair direct mass
  interpretation.
- Empty pH, salinity, agar, and storage fields are not defects here: the
  inspected DSMZ and MediaDive source pages do not provide those fields for the
  BME/CTVM2 medium recipe.
- Bounded search: ignored files were included in the exact search described
  under `Target`, and no second active normalized owner for
  `CultureMech:001155` was found under `data`, `src`, or `scripts`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated merge is stale and still publishes the pre-Sept direct `G_PER_L` interpretation of the 70 ml, 10 ml, 20 ml, and 1 ml DSMZ batch rows. | DSMZ Medium 1670 PDF render; MediaDive 1670 page; September 11 state of `data/normalized_yaml/bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml` and `data/normalized_yaml/bacterial/mediadive_3465_Main_sol_1670.yaml`. | No normalized edit is needed for this defect; regenerate `data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml` from the repaired normalized owner. |
| major | The generated preparation model is stale: its infection step is typed as `HEAT`, retains raw HTML, and lacks the repaired 28 C temperature slot. | DSMZ Medium 1670 PDF render; repaired normalized owner. | Regenerate the derived merge after normalized repair. |
| minor | The generated merge is missing the DSMZ/MediaDive references and curated-data flags added by the September 11 repair. | Repaired normalized owner and `scripts/repair_dsmz_1670_bme_score15.py`. | Regenerate the derived merge after normalized repair. |

## Recommended Edits

1. Rerun merge generation so
   `data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`
   inherits the source-faithful 101 ml recipe, `ML_PER_L` additions, nested
   200 mM L-glutamine stock, cleaned BME/CTVM2 preparation steps,
   `temperature_value: 28.0`, references, and data-quality flags from
   `data/normalized_yaml/bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`.
2. Ensure the regenerated merge still does not expand L-15 medium, tryptose
   phosphate broth, or foetal calf serum into unsupported chemical formulas;
   DSMZ and MediaDive list them as opaque cell-culture inputs.
3. Do not patch
   `data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`
   directly; it is a derived record.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`
  and `data/normalized_yaml/bacterial/mediadive_3465_Main_sol_1670.yaml`.
- Run the same validators on
  `data/merge_yaml/merged/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml`
  after merge regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch DSMZ Medium 1670 and MediaDive Medium 1670, then manually verify
  that the regenerated merge preserves the repaired volume arithmetic, the
  200 mM L-glutamine stock, the 28 C infection temperature, and the absence of
  unsupported mass conversions.

## Additional Notes

- `pypdf` could not extract DSMZ Medium 1670 without `cryptography`, and
  `cryptography` was not available in the offline `uv` cache; the PDF was
  rendered with Quick Look and inspected visually instead.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
