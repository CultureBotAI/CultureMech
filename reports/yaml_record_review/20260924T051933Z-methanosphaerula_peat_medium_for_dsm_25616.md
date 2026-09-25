# YAML Record Review: Methanosphaerula (Peat) Medium (for DSM 25616)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml
- Started UTC: 2026-09-24T05:18:22Z
- Finished UTC: 2026-09-24T05:19:33Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml`, a generated `MediaRecipe` for `CultureMech:009216` with `name: methanosphaerula_peat_medium_for_dsm_25616`, `original_name: Methanosphaerula (Peat) Medium (for DSM 25616)`, and medium grounding `TOGO:M2661`.

The merged record was generated from `methanosphaerula_peat_medium_for_dsm_25616`; the maintained owner is `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml --out /private/tmp/methanosphaerula_peat_medium_for_dsm_25616.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The record identity is correct at the source-accession level: TOGO `M2661` is the DSMZ 1094 recipe variant labelled for DSM 25616, derived from `DSMZ_Medium1094.pdf`.

The grounded content is not a faithful DSM 25616 variant. TOGO and DSMZ specify the base Methanosphaerula peat medium plus a 0.02 g/L yeast extract supplement from an anoxic filtered stock, final pH 6.2, 5-10 vol% inoculum, and 100-200 rpm shaking. The record captures only the yeast extract amount, then repeats the same flattened base-medium import errors seen in TOGO `M2655`.

## Evidence

Supported source claims:

- TOGO `M2661` supports the record label, TOGO ID, DSMZ 1094 source URL, the 0.02 g/L yeast extract supplement, and pH 6.2 metadata.
- TOGO `M2661` supports the imported base-medium Solution A-G recipe with the same nested trace, Wolin vitamin, Solution C, Solution E, Solution F, and Solution G subrecipes seen in the base TOGO record.

Unsupported or over-scoped generated claims:

- The record serializes Solution A-G final additions, Solution A children, Solution B children, and the trace element stock as empty `solutions` rows or flat top-level ingredients with `G_PER_L` units.
- Trace-stock milligram quantities and Wolin vitamin milligram quantities are asserted as final `G_PER_L` concentrations. Examples include `Na2Mo4 x 2 H2O: 24 G_PER_L`, `CoCl2 x 6 H2O: 24 G_PER_L`, and `Biotin: 2 G_PER_L`.
- The `Distilled water` ingredient merges seven solvent rows from distinct stocks into a single `2940.0 G_PER_L` row.
- The imported TOGO quantities differ from the current DSMZ 1094 PDF and MediaDive 1094 record for several base-medium quantities. DSMZ/MediaDive use Solution A 943 ml, Solution B 13 ml, Solution D 1 ml, and 900 ml water in Solution A; TOGO and this YAML use 932.9 ml, 12.55 ml, 10 ml, and 890 ml.
- The yeast extract row is amount-only. It does not preserve that DSMZ adds it from a sterile anoxic stock solution sterilized by filtration.

## Completeness

The schema-optional evidence, discussions, growth, and target organism fields are empty; those empty slots are not defects by themselves.

Consequential gaps:

- The Solution A-G and nested stock hierarchy is absent, so the base medium cannot be reconstructed from the generated record.
- Final pH 6.2, 5-10 vol% inoculum, and 100-200 rpm shaking for DSM 25616 are absent.
- The yeast extract stock preparation is absent.
- The final pH 5.7 and base preparation details from DSMZ 1094 are not represented either, aside from gas pseudo-ingredients.
- MediaDive solution links point to unrelated solution IDs; the DSMZ 1094 solution IDs are 2201-2208 plus 5980, not 5342, 5343, 5312, 5313, 4959, 6293, 3625, or 6187.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ 1094 stock hierarchy was flattened and stock units were changed into top-level `G_PER_L` assertions. | TOGO M2661 and DSMZ 1094 structure this recipe as Solution A-G plus nested Trace element solution and Wolin's vitamin solution. The YAML stores stock children as top-level ingredients or empty solution stubs and gives milliliter and milligram source rows mass-concentration units. | `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`; likely the TOGO importer and solution migrator. |
| Major | Cross-scope solvent merging produced an impossible water concentration. | The `Distilled water` note says the row merged 890, 1000, 20, 1000, 10, 10, and 10 ml rows from separate Solution A, trace, Solution C, Wolin, and Solution E-G scopes. | `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`; duplicate ingredient cleanup and merge logic. |
| Major | The variant-specific DSM 25616 preparation context was dropped. | DSMZ and TOGO specify yeast extract from a sterile anoxic filtered stock, final pH 6.2, 5-10 vol% inoculum, and shaking at 100-200 rpm. The record stores only `Yeast extract: 0.02 G_PER_L`. | `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`; TOGO comment importer. |
| Major | MediaDive solution IDs are wrong. | The record links Solution A-G and Trace element solution to 5342, 5343, 5312, 5313, 4959, 6293, 3625, and 6187. DSMZ/MediaDive 1094 uses 2201-2208 and 5980 for its nested stocks. | `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`; MediaDive solution linker. |
| Major | The imported base-medium amounts conflict with the current authoritative DSMZ source. | DSMZ/MediaDive say the base medium uses 943 ml Solution A, 13 ml Solution B, 1 ml Solution D, and 900 ml water in Solution A; TOGO M2661 and this YAML encode 932.9 ml, 12.55 ml, 10 ml, and 890 ml. | TOGO M2661 import input and `data/normalized_yaml/archaea/methanosphaerula_peat_medium_for_dsm_25616.yaml`. |

## Recommended Edits

1. Recurate the normalized M2661 record so DSMZ 1094's Solution A-G, Trace element solution, Wolin's vitamin solution, and DSM 25616 supplement remain scoped instead of flattened.
2. Add the DSM 25616 pH 6.2, anoxic filtered yeast-extract stock, inoculum percentage, and shaking speed from the DSMZ note.
3. Fix or remove the incorrect `mediadive.solution:*` links for Solution A-G and Trace element solution.
4. Preserve the TOGO-vs-DSMZ source quantity differences as an explicit unresolved conflict if TOGO remains authoritative, or update the import to the current DSMZ/MediaDive quantities.
5. Regenerate `data/merge_yaml/merged/methanosphaerula_peat_medium_for_dsm_25616.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated DSM 25616 record against the DSMZ 1094 PDF and TOGO M2661 API output.
- Confirm that yeast extract remains the only added DSM 25616 ingredient, and that pH, inoculum, and shaking are condition or preparation annotations rather than extra ingredients.
- Confirm that every base-medium stock ingredient remains under its source solution.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- The exact owner search used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:009216`, `DSM 25616`, and `methanosphaerula_peat_medium_for_dsm_25616`.
