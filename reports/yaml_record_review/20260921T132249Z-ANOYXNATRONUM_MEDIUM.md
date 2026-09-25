# YAML Record Review: anoyxnatronum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml
- Started UTC: 2026-09-21T13:21:38Z
- Finished UTC: 2026-09-21T13:22:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003907 |
| Label | anoyxnatronum_medium |
| Original label | ANOYXNATRONUM medium |
| Source term | komodo.medium:1187 |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml; data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml |
| Generated record | data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml |

This is a generated merge of the KOMODO Medium 1187 import and the MediaDive
DSMZ Medium 1187 import. Future fixes should land in the two normalized source
records, source-specific importers, or merge rule that owns the lost duplicate
content, then `data/merge_yaml/merged/` should be regenerated.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The generated record denotes the intended misspelled DSMZ/KOMODO recipe:
DSMZ Medium 1187 is titled `ANOYXNATRONUM MEDIUM`, and both normalized owners
point at Medium 1187.

The source duplicate relation between the KOMODO and MediaDive owners is
plausible because their physical state, pH, and flattened ingredient signatures
match exactly. That merge is still incomplete scientifically: the DSMZ source
recipe contains nested `Trace elements SL-10` and `Vitamin solution` additions,
so matching flattened signatures only proves both imports share the same stock
flattening defect.

Most hydrate-sensitive salts are grounded exactly. The exception visible in
this review is `NiCl2 x 6 H2O`, which is grounded to anhydrous
`CHEBI:34887` / nickel dichloride.

## Evidence

The inspected DSMZ Medium 1187 PDF supports the top-level pH 9.0 and these
top-level ingredients: 25 g Na2CO3, 25 g NaHCO3, 0.2 g KCl, 0.1 g MgCl2 x 6
H2O, 0.5 g NH4Cl, 0.2 g K2HPO4, 0.2 g Yeast extract, 1 ml Trace elements
SL-10 from DSMZ Medium 320, 1 ml Vitamin solution from DSMZ Medium 141, 0.7 g
Na2S x 9 H2O, 5 g Glucose, and 1000 ml Distilled water.

The inspected DSMZ Medium 320 PDF supports `Trace element solution SL-10` as a
1 L stock containing HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x
6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and distilled water.
The inspected DSMZ Medium 141 PDF supports `Wolin's vitamin solution` as a 1 L
stock containing Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl,
Riboflavin, Nicotinic acid, Calcium D-(+)-pantothenate, Vitamin B12,
p-Aminobenzoic acid, (DL)-alpha-Lipoic acid, and distilled water.

The generated record does not preserve those source boundaries. It exposes all
SL-10 and vitamin-stock ingredients directly at the same g/L stock
concentrations and omits the two 1 ml stock-addition rows from DSMZ 1187.

DSMZ Medium 1187 also supports an anaerobic protocol: prepare the medium
without the vitamins, Na2S, yeast extract, NaHCO3, and Na2CO3; boil; cool under
N2; add bicarbonate/carbonate; dispense under N2; autoclave; then add vitamin
solution, yeast extract, Na2S, and glucose from sterile N2-prepared stocks.
The generated merge drops those preparation steps entirely, although the
MediaDive owner still has them.

## Completeness

The generated record is missing three source-level ingredients from DSMZ 1187:
distilled water, the 1 ml SL-10 stock addition, and the 1 ml vitamin-solution
stock addition. It is also missing all source preparation instructions and any
solution boundary for DSMZ Medium 320 SL-10 or DSMZ Medium 141 Wolin's vitamin
solution.

An ignored-inclusive exact search for
`CultureMech:003907|CultureMech:000629|komodo.medium:1187|mediadive.medium:1187|KOMODO_1187_ANOYXNATRONUM_medium|anoyxnatronum_medium|ANOYXNATRONUM`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the two normalized source owners, the generated merge, registries,
indexes, the archived source-duplicate review, and validation/import-tracking
reports, but no third maintained owner for Medium 1187.

The absence of `target_organisms` is not automatically a defect because the
source recipe establishes a medium formulation and does not assert a specific
growth result.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| major | Two referenced DSMZ stock additions were flattened into final-medium ingredients. | DSMZ 1187 adds 1 ml SL-10 and 1 ml vitamin solution; the generated record omits those stock additions and publishes all SL-10 and Wolin vitamin components directly as final `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml`, `data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml`, and the DSMZ/KOMODO stock import mapping |
| major | The generated duplicate merge drops the DSMZ preparation protocol. | The MediaDive owner contains pH, anaerobic N2 preparation, autoclaving, cooled sterile-stock additions, and SL-10 preparation steps; the generated merge has no `preparation_steps` after choosing the KOMODO child as canonical. | `merge_recipes.py` duplicate field reconciliation |
| major | The KOMODO source note contradicts the DSMZ oxygen requirement. | The canonical generated record says `Aerobic: Yes`; DSMZ 1187 instructs anaerobic preparation, cooling under N2, dispensing under N2, and adding sterile stocks prepared under N2. | KOMODO importer or source-normalization rule |
| major | `NiCl2 x 6 H2O` is grounded to the anhydrous nickel salt. | DSMZ 320 lists nickel chloride hexahydrate in SL-10, but the merged row uses `CHEBI:34887` / nickel dichloride. | normalized owners or MediaIngredientMech enrichment |
| minor | The KOMODO import's first curation timestamp is malformed and survives into the generated record. | The embedded history starts with `2026-01-27T01:15:01.fZ`, which is not an ISO 8601 instant. | `data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml` |

## Recommended Edits

1. Restore DSMZ 1187 with explicit 1 ml `Trace elements SL-10` and 1 ml
   `Vitamin solution` additions instead of publishing DSMZ 320 and DSMZ 141
   stock members as final-medium solutes.
2. Represent DSMZ 320 SL-10 and DSMZ 141 Wolin's vitamin solution as nested
   stock solutions or resolvable solution references, including the stock-local
   distilled-water rows.
3. Preserve the DSMZ 1187 distilled-water final-volume row.
4. Change KOMODO-derived `Aerobic: Yes` provenance to an anaerobic/aerobic
   state that agrees with the DSMZ source, or drop the unsupported flag if
   KOMODO's boolean cannot represent the N2-handled recipe.
5. Reconcile source duplicates without dropping the MediaDive/DSMZ preparation
   steps when the generated canonical record keeps the KOMODO identity.
6. Replace the anhydrous nickel dichloride grounding only with a verified
   nickel chloride hexahydrate term, or leave that ingredient unresolved.
7. Normalize the malformed KOMODO import timestamp without rewriting unrelated
   curation history events.

## Follow-up Checks

- Re-run `just validate` and `just validate-strict` on both normalized source
  owners after the stock hierarchy, preparation, and timestamp fixes land.
- Re-run `just validate-terms` after changing the nickel chloride grounding.
- Re-run `just verify-merges` and verify the regenerated
  `data/merge_yaml/merged/ANOYXNATRONUM_MEDIUM.yaml` still merges the two source
  owners while preserving the DSMZ preparation text.
- Manually compare the regenerated merge against DSMZ Medium 1187, DSMZ Medium
  320, and DSMZ Medium 141 to ensure stock-local SL-10 and vitamin rows are not
  exposed as final-medium grams per liter.

## Additional Notes

`data/import_tracking/reports/concentration_plausibility.tsv` already flags the
1.5 g/L `FeCl2 x 4 H2O` row as stock-solution magnitude in both normalized
owners. That flag is the local audit signal for the broader SL-10 flattening
defect.
