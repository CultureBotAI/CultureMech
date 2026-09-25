# YAML Record Review: Methionine salt; schaechter et al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-24T05:30:55Z
- Finished UTC: 2026-09-24T05:32:00Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml`, a generated `MediaRecipe` for `CultureMech:007129` with `name: methionine_salt_schaechter_et_al`, `original_name: Methionine salt; schaechter et al`, and source grounding `MEDIADB:233`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml --out /private/tmp/methionine_salt_schaechter_et_al.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDB identity is correct. MediaDB medium 233 is `Methionine salt; schaechter et al`, a non-minimal defined medium with six millimolar components.

The cross-resource grounding is wrong. The record's `kg_microbe_match` is `mediadive.medium:J526`, but MediaDive/JCM J526 is `NORRIS FERROPLASMA MEDIUM`, a pH 1.2 JCM recipe containing MgSO4 x 7 H2O, ammonium sulfate, KCl, KH2PO4, FeSO4 x 7 H2O, yeast extract, and water. It does not identify the MediaDB 233 methionine/citrate medium.

## Evidence

Supported source claims:

- MediaDB medium 233 supports the record's six ingredients and their millimolar amounts: citrate 5.20497, D-methionine 4.02118, dibasic sodium phosphate 28.0899, potassium chloride 9.92605, magnesium sulfate 0.405729, and sodium ammonium phosphate 8.32187.
- MediaDB medium 233 links the recipe to `Schaechter et al, 1958` and to growth-data record 457 for Salmonella enterica Typhimurium LT2.
- MediaDB source 84 gives the Schaechter 1958 paper title and PMID 13611202; the journal archive route confirms the same article title and DOI `10.1099/00221287-19-3-592`.
- MediaDB growth-data record 457 reports Salmonella enterica Typhimurium LT2 on this medium with growth rate 0.561 1/h, pH 7.0, no temperature, and note `doublings/hr`.

Unsupported or over-scoped generated claims:

- The three preparation steps are generic importer placeholders. MediaDB 233 does not say to dissolve in distilled water, adjust pH if specified, or filter-sterilize at 0.22 um.
- The `mediadive.medium:J526` match is for a different medium.
- The broad applications `Cultivation of genome-sequenced organisms`, `Metabolic modeling`, and `Systems biology research` are inherited from the database context; MediaDB 233 itself only names Salmonella enterica Typhimurium LT2 as the organism on this exact recipe.

## Completeness

Empty optional discussions and recipe variant arrays were not treated as defects.

Consequential gaps:

- There is no structured citation for Schaechter et al. 1958 or PMID 13611202.
- MediaDB growth-data record 457 is not represented in `target_organisms` or `growth_metrics`.
- `Sodium ammonium phosphate` remains unresolved to CHEBI because MediaDB provides no CHEBI ID for that row; that is acceptable if retained as an explicit unresolved ingredient.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `kg_microbe_match` points to the wrong medium. | JCM/MediaDive J526 is NORRIS FERROPLASMA MEDIUM at pH 1.2, not MediaDB 233 `Methionine salt; schaechter et al`. | `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`; KG-Microbe matching. |
| Major | Unsupported generic preparation steps were imported. | MediaDB 233 gives ingredients and growth/source links but no distilled-water dissolution, pH-adjustment, or 0.22 um filter-sterilization instructions. | `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`; MediaDB import. |
| Major | The nearest recipe source is not represented. | MediaDB 233 points to Schaechter et al. 1958, MediaDB source 84 gives PMID 13611202, and the record only carries a generic MediaDB homepage plus a curation-history note to Mazumdar et al. 2014. | `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`; MediaDB import. |
| Major | MediaDB's growth assertion is dropped. | MediaDB growth-data record 457 ties this recipe to Salmonella enterica Typhimurium LT2, growth rate 0.561 1/h, pH 7.0, and note `doublings/hr`; the YAML has no target organism or growth metric. | `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`; MediaDB import. |

## Recommended Edits

1. Remove or correct `kg_microbe_match: mediadive.medium:J526`.
2. Delete unsupported generic preparation steps unless an inspected source supports concrete preparation conditions.
3. Add structured source metadata for MediaDB source 84, PMID 13611202, and DOI `10.1099/00221287-19-3-592`.
4. Represent MediaDB growth-data record 457 as a Salmonella enterica Typhimurium LT2 growth claim with pH 7.0 and the reported growth rate, or record why MediaDB growth rows are intentionally out of scope.
5. Keep `Sodium ammonium phosphate` unresolved until a chemically exact identifier is verified.
6. Regenerate `data/merge_yaml/merged/methionine_salt_schaechter_et_al.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against MediaDB medium 233 and confirm all six ingredient amounts remain 5.20497, 4.02118, 28.0899, 9.92605, 0.405729, and 8.32187 mM.
- Re-run KG-Microbe matching and verify no JCM 526/NORRIS FERROPLASMA MEDIUM identifier remains on this MediaDB recipe.
- Fetch MediaDB source 84 and growth-data record 457 to verify the Schaechter citation and Salmonella growth claim.

## Additional Notes

- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:007129` and `data/normalized_yaml/bacterial/methionine_salt_schaechter_et_al.yaml`.
