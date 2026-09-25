# YAML Record Review: MOORELLA AN10 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moorella_an10_medium__7be013ef.yaml
- Started UTC: 2026-09-24T14:00:50Z
- Finished UTC: 2026-09-24T14:01:38Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002989 |
| Name | moorella_an10_medium |
| Original name | MOORELLA AN10 MEDIUM |
| Source owner | data/normalized_yaml/bacterial/moorella_an10_medium.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 7be013ef1a945beebe25330f00acfdcaaa602e100a5dc6056ca047dd05bf765c |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moorella_an10_medium__7be013ef.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/moorella_an10_medium__7be013ef.yaml --out /private/tmp/moorella_an10_medium__7be013ef.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/moorella_an10_medium__7be013ef.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/moorella_an10_medium__7be013ef.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The record identifies JCM GRMD 642, `MOORELLA AN10 MEDIUM`, imported through the legacy JCM/MediaDive path. The live JCM GRMD 642 page now returns `Nothing found.`, but TOGO M656 still resolves the same JCM_M642 recipe as `Moorella AN10 Medium`.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for exact GRMD 642, JCM J642 / M642, TOGO M656, and Moorella AN10 labels found this direct-JCM normalized owner and a separate TOGO owner at `data/normalized_yaml/bacterial/TOGO_M656_Moorella_AN10_Medium.yaml`. The generated corpus likewise contains this file and `data/merge_yaml/merged/MOORELLA_AN10_MEDIUM.yaml`, so one JCM medium has two CultureMech IDs.

The `media_term` is weakly grounded because `mediadive.medium:J642` is a JCM provider identifier stored under the MediaDive medium namespace. Most simple ingredients have reasonable CHEBI terms, but `FeSO4 x 6 H2O` is grounded to CHEBI:75832 `iron(2+) sulfate (anhydrous)`, which conflicts with the named hexahydrate.

## Evidence

TOGO M656 exposes this medium as a structured three-solution recipe: 862 ml Solution A, 100 ml Solution B, and 20 ml Solution C are mixed under N2-CO2 4:1, then the medium is reduced with 0.3 g/L L-Cysteine-HCl-H2O and 0.3 g/L Na2S x 9 H2O from sterile stocks held under N2.

The generated record is a flat projection of the component stocks, not the final medium:

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| Solution A is an 862 ml component containing 1 g yeast extract, 1 g Casitone, 0.348 g K2HPO4, 0.227 g KH2PO4, 0.5 g NH4Cl, 0.5 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 2.25 g NaCl, 0.1 g FeSO4 x 6 H2O, 0.5 g L-Cysteine-HCl-H2O, 0.5 g Na2S x 9 H2O, 1 mg resazurin, 10 ml M190 trace vitamins, 1 ml M481 trace elements, and 1 ml M312 Se/W | Solution A ingredients are top-level final rows, rescaled to one liter of stock; trace elements from M481 are absent | The Solution A stock was neither preserved as a stock nor converted to final-medium contributions. |
| Solution B is 100 ml water plus 5 g fructose | Top-level `Fructose` at 50 g/L | The value is the stock concentration, not the final concentration after adding 100 ml. |
| Solution C is 20 ml 8% NaHCO3 | Top-level `NaHCO3` at 20 g/L | The source gives a 20 ml stock volume. |
| M190 trace vitamins and M312 Se/W are stock references | M190 vitamin and M312 selenite/tungstate components are top-level ingredients at stock concentration | The record loses the stock hierarchy and overstates the final amounts. |
| Main recipe contains 0.3 g/L L-Cysteine-HCl-H2O and 0.3 g/L Na2S x 9 H2O as final reducing agents | L-Cysteine-HCl-H2O and Na2S x 9 H2O are both 0.580046 g/L | The direct import rescaled the 0.5 g Solution A stock rows and does not preserve the separate final 0.3 g/L additions. |

The preparation text is mostly present, including N2-CO2 4:1 and N2 atmospheres, but the last step about using trace element solution of Medium No. 243 without Na2SeO3 x 5H2O is an orphaned instruction because the corresponding M481 trace-element composition is missing from the ingredient list.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema defect for this provider recipe.

The record is materially incomplete for stock composition and assembly. It has no Solution A, B, or C rows, no structured M481 trace-element solution, no structured M190 trace-vitamin solution, and no structured M312 Se/W solution, even though those boundaries are needed to interpret the 862 ml / 100 ml / 20 ml mixing instructions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | This record duplicates TOGO M656 and gives JCM GRMD 642 a second CultureMech ID. | The ignored-inclusive search found both `moorella_an10_medium__7be013ef.yaml` and `MOORELLA_AN10_MEDIUM.yaml` for the same GRMD 642 source. | `data/normalized_yaml/bacterial/moorella_an10_medium.yaml` and source de-duplication before `merge_recipes.py`. |
| Major | The three-solution source recipe was flattened into final ingredients at stock concentrations. | Solution A, Solution B, and Solution C are separate TOGO M656 subcomponents, but this YAML stores rows such as `Fructose` 50 g/L and `NaHCO3` 20 g/L as top-level final ingredients. | The legacy JCM/MediaDive importer that produced `data/normalized_yaml/bacterial/moorella_an10_medium.yaml`. |
| Major | Referenced M190 and M312 stock components were inlined at stock strength, while the M481 trace-element stock was dropped. | TOGO M656 references 10 ml M190, 1 ml M481, and 1 ml M312; this file has the M190 vitamin and M312 Se/W ingredients as top-level rows but no M481 trace-element composition. | The legacy JCM/MediaDive stock flattener. |
| Major | The final reducing-agent amounts are wrong. | TOGO M656 adds 0.3 g/L L-Cysteine-HCl-H2O and 0.3 g/L Na2S x 9 H2O to the mixed medium; this record has 0.580046 g/L for both after rescaling the Solution A stock components. | `data/normalized_yaml/bacterial/moorella_an10_medium.yaml`. |
| Major | FeSO4 x 6 H2O has the wrong CHEBI grounding. | The preferred term names the hexahydrate, while CHEBI:75832 is labeled `iron(2+) sulfate (anhydrous)`. | CHEBI enrichment over the legacy normalized owner. |
| Minor | The source CURIE is not a resolvable JCM term. | The record stores `mediadive.medium:J642` for a JCM GRMD 642 page. | `data/normalized_yaml/bacterial/moorella_an10_medium.yaml`. |

## Recommended Edits

1. Reconcile `data/normalized_yaml/bacterial/moorella_an10_medium.yaml` with `data/normalized_yaml/bacterial/TOGO_M656_Moorella_AN10_Medium.yaml` so GRMD 642 produces one generated record and one CultureMech ID.
2. Prefer TOGO M656 as the maintained owner unless the legacy direct-JCM importer contains source evidence missing from TOGO.
3. Repair the surviving M656 owner so Solutions A, B, and C remain structured 862 ml, 100 ml, and 20 ml additions rather than flattened final ingredients.
4. Resolve M190, M481, and M312 as named stock references or copy only their referenced stock subcomponents.
5. Encode the final 0.3 g/L L-Cysteine-HCl-H2O and 0.3 g/L Na2S x 9 H2O reducing-agent additions separately from the 0.5 g Solution A stock ingredients.
6. Replace `mediadive.medium:J642` with a resolvable JCM or TOGO source term if this owner is retained.
7. Correct the FeSO4 x 6 H2O CHEBI grounding after the stock hierarchy has been fixed.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated Moorella AN10 record.
- Manually compare the regenerated YAML against TOGO M656, including the 862 ml / 100 ml / 20 ml stock assembly, M190 / M481 / M312 references, and final 0.3 g/L reducing-agent additions.
- Run an ignored-inclusive search for `GRMD=642`, `JCM_M642`, `mediadive.medium:J642`, and `TOGO:M656` across `data/normalized_yaml` and `data/merge_yaml` to confirm the stale direct-JCM duplicate was reconciled.

## Additional Notes

The live JCM GRMD 642 page returned `Nothing found.`, so TOGO M656 was the inspected source for the original formula.
