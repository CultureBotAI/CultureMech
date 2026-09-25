# YAML Record Review: Medium for tick cells (Rickettsia)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml
- Started UTC: 2026-09-24T02:08:24Z
- Finished UTC: 2026-09-24T02:09:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001032 |
| Record name | medium_for_tick_cells_rickettsia |
| Original name | Medium for tick cells (Rickettsia) |
| Generated path | data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_tick_cells_rickettsia.yaml |
| Upstream source | DSMZ/MediaDive medium 1555 |
| Upstream URL | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1555.pdf |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_tick_cells_rickettsia.yaml`.
Future formula and classification fixes belong in that normalized owner.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml --out /private/tmp/medium_for_tick_cells_rickettsia.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The source identity is correct: MediaDive medium 1555 and the DSMZ Medium 1555
  PDF are both titled `Medium for tick cells (Rickettsia)`.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for `mediadive.medium:1555`, `DSMZ Medium 1555`,
  `DSMZ_Medium1555`, the source label, and the slug found only this maintained
  owner and its generated copy.
- The bacterial category and `Microbial cultivation` application are
  over-scoped. The DSMZ page describes L15C medium used to culture IRE11 tick
  host cells, then infect those eukaryotic host cells with Rickettsia. The
  source does not say this formulation is a direct bacterial growth medium.
- The liquid physical state, complex medium type, and undefined composition
  type are consistent with the serum-containing source formulation.

## Evidence

- DSMZ and MediaDive support the modified L15C rows for L-aspartic acid,
  L-glutamine, L-proline, L-glutamic acid, alpha-ketoglutaric acid, D-glucose,
  5 mM NaOH, 25 mM HEPES, 0.25% NaHCO3, and final pH 7.5.
- The imported percentages for Fetal bovine serum, Tryptose-phosphate broth,
  and lipoprotein concentrate are unsupported as `G_PER_L`. The source lists
  them as 10%, 5%, and 0.1% supplements, without stating that those liquid or
  broth supplements are weight/volume percentages or can be converted to
  100 g/L, 50 g/L, and 1 g/L.
- The pH-adjustment instruction is preserved in text: DSMZ says pH is adjusted
  to 7.5 using 1 M NaOH, and the YAML carries that in a preparation step.
- Several preparation steps are source text fragments rather than actionable
  medium-preparation steps. `Supplemented L15C medium is used with` and
  `Alterations were made to the following reagents:` are headings whose
  following lists were converted to ingredients, not useful standalone actions.

## Completeness

- The formulation should preserve percentage semantics for serum, tryptose
  phosphate broth, and lipoprotein concentrate instead of coercing them to
  gram-per-liter values.
- The source's L15C dilution and supplemented-medium wording are only partially
  structured; the relationship between base L15C, 33% added water by volume,
  and the supplements needs explicit modeling.
- Empty target-organism growth assertions and solution lists are acceptable for
  this DSMZ page; the source describes tick-cell infection workflow, not a
  quantified Rickettsia growth claim.
- The exact gitignore-independent search over normalized and merged YAML found
  no same-source duplicate beyond this owner and generated record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The recipe is classified as a bacterial microbial-cultivation medium even though the source describes a tick host-cell culture medium used for infection. | DSMZ 1555 describes L15C for IRE11 tick host cells and a downstream Rickettsia infection protocol; the formulation is not asserted as a direct bacterial growth medium. | `data/normalized_yaml/bacterial/medium_for_tick_cells_rickettsia.yaml` |
| Major | Liquid percentage supplements were converted to unsupported `G_PER_L` values. | Fetal bovine serum, Tryptose-phosphate broth, and lipoprotein concentrate are listed as 10%, 5%, and 0.1%; the YAML stores 100, 50, and 1 `G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_tick_cells_rickettsia.yaml` |
| Minor | Several preparation entries are headings or context paragraphs, not ordered medium-preparation actions. | The DSMZ prose headings around the L15C supplement list and Rickettsia infection protocol were imported as `MIX` steps. | `data/normalized_yaml/bacterial/medium_for_tick_cells_rickettsia.yaml` |

## Recommended Edits

1. Reclassify the record or add an explicit scope note that DSMZ 1555 is L15C
   tick-cell culture medium used for Rickettsia infection, not a direct
   bacterial medium.
2. Preserve Fetal bovine serum, Tryptose-phosphate broth, and lipoprotein
   concentrate as percent supplements unless the source or an inspected
   reference states weight/volume amounts.
3. Restructure the preparation text so L15C dilution, supplemented-medium
   composition, pH 7.5 adjustment with 1 M NaOH, and Rickettsia infection
   conditions are separated instead of stored as generic `MIX` steps.
4. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_tick_cells_rickettsia.yaml`.
- Re-inspect DSMZ Medium 1555 and confirm that percent supplements remain
  percentages or volumes rather than inferred grams.
- Confirm that the regenerated preparation section no longer contains
  standalone heading fragments as generic steps.
- Repeat an exact gitignore-independent search for `mediadive.medium:1555`,
  `DSMZ_Medium1555`, and `medium_for_tick_cells_rickettsia` across normalized
  and merged YAML if source ownership changes.

## Additional Notes

- Source checks used the MediaDive REST endpoint for medium 1555 and the DSMZ
  Medium 1555 PDF.
- No record YAML was edited during this review.
