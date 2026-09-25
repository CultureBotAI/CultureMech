# YAML Record Review: modified_sporomusa_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml
- Started UTC: 2026-09-24T13:17:32Z
- Finished UTC: 2026-09-24T13:19:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:002830 |
| Name | modified_sporomusa_medium |
| Original name | MODIFIED SPOROMUSA MEDIUM |
| Category | bacterial |
| Source identity | mediadive.medium:J480, JCM Medium 480 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/modified_sporomusa_medium.yaml` or in the JCM/MediaDive stock-solution importer. |

An ignored-file-inclusive exact search for `CultureMech:002830`, `mediadive.medium:J480`, `modified_sporomusa_medium`, `GRMD=480`, and `JCM Medium J480` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained JCM owner, a TOGO M481 branch from the same JCM source page, index/report rows, and aggregate QA rows. The reviewed generated record is a singleton merge from `modified_sporomusa_medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml --out /private/tmp/modified_sporomusa_medium__4939c205.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record points to the intended JCM source: JCM Medium 480 is `MODIFIED SPOROMUSA MEDIUM`, a complex liquid medium prepared anaerobically under an N2-CO2 atmosphere.

Most ChEBI groundings are chemically plausible for their labels. The main identity problem is not the ChEBI mapping but the level at which rows are asserted: many YAML ingredients are stock contents from Medium 197, Medium 317, or internal phosphate, bicarbonate, mannitol, and dithiothreitol stocks rather than final-medium ingredients.

## Evidence

The inspected JCM 480 page lists NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, resazurin, yeast extract, and Casitone in 900 ml water as the main autoclaved portion. It then adds these stocks by volume: 10 ml trace vitamins from Medium 197, 1 ml trace element solution based on Medium 243 without sodium selenite pentahydrate, 1 ml Se/W solution from Medium 317, 30 ml phosphate solution, 20 ml 1 M mannitol, 50 ml 8% NaHCO3, and 10 ml 0.1 M dithiothreitol.

The YAML has no `solutions` array and turns those stocks into top-level `ingredients`: the one-liter vitamin-stock rows from Medium 197 are final-medium vitamin rows, the Se/W stock rows from Medium 317 are final-medium sodium selenite/tungstate rows, the 8% bicarbonate stock is a `333.333 G_PER_L` NaHCO3 row, the 0.1 M dithiothreitol stock is a `25 G_PER_L` row, and the 1 M mannitol stock is a `300 G_PER_L` row. The source supports those as measured stock additions, not as final concentrations.

The main basal salt rows are also unsupported numerically. JCM 480 lists 0.5 g/l NH4Cl, 0.5 g/l MgSO4 x 7 H2O, 0.25 g/l CaCl2 x 2 H2O, 2.25 g/l NaCl, 1 mg/l resazurin, 0.5 g/l yeast extract, and 0.5 g/l Casitone; the YAML reports 41.6667, 41.6667, 20.8333, 187.5, 0.0833333, 41.6667, and 41.6667 `G_PER_L`, respectively.

## Completeness

The record is missing every final-medium stock addition as a stock boundary. The JCM 480 page also requires an internal trace-element solution derived from Medium 243, but the YAML only preserves a free-text preparation note and never represents the 1 ml/l trace-element solution addition itself.

Empty `target_organisms`, `growth_evidence`, and `discussion` slots are acceptable for this JCM recipe import; the JCM 480 page is not a strain-level growth study.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Final-medium basal rows have unsupported concentrations. | JCM 480 gives sub-gram-to-gram amounts in 900 ml water; the YAML multiplies NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, resazurin, yeast extract, and Casitone into unrelated values such as `41.6667 G_PER_L` and `187.5 G_PER_L`. | `data/normalized_yaml/bacterial/modified_sporomusa_medium.yaml`; JCM/MediaDive unit normalization. |
| major | Post-autoclave stock additions are flattened as final-medium concentrations. | JCM adds 30 ml phosphate solution, 20 ml 1 M mannitol, 50 ml 8% NaHCO3, and 10 ml 0.1 M dithiothreitol. The YAML has no stock additions and stores K2HPO4, KH2PO4, mannitol, NaHCO3, and dithiothreitol directly as final ingredients at stock-like strengths. | `data/normalized_yaml/bacterial/modified_sporomusa_medium.yaml`; JCM stock-solution extraction. |
| major | Imported external stocks are flattened or dropped. | JCM adds 10 ml trace vitamins from Medium 197, 1 ml trace element solution based on Medium 243, and 1 ml Se/W solution from Medium 317. The YAML flattens vitamin and Se/W stock constituents into top-level final ingredients and has only a free-text note for the Medium 243 trace-element solution. | `data/normalized_yaml/bacterial/modified_sporomusa_medium.yaml`; cross-medium solution reference modeling. |
| minor | The MediaDive/JCM branch has a same-page TOGO duplicate to reconcile. | Exact ignored-file-inclusive search found `data/normalized_yaml/bacterial/TOGO_M481_Modified_Sporomusa_Medium.yaml`, which cites the same JCM `GRMD=480` page but is generated separately as `data/merge_yaml/merged/MODIFIED_SPOROMUSA_MEDIUM.yaml`. | Merge/source-duplicate curation for JCM GRMD 480. |

No blocker findings.

## Recommended Edits

1. Restore the main JCM 480 basal rows to their source quantities and keep them separate from every post-autoclave stock.
2. Represent phosphate solution, 1 M mannitol, 8% NaHCO3, and 0.1 M dithiothreitol as measured solution additions with their stock composition, concentration, and sterilization context.
3. Represent trace vitamins, trace element solution, and Se/W solution as stock or cross-medium solution references rather than flattening their one-liter stock recipes into the final ingredient list.
4. Add the Medium 243 trace-element solution addition at 1 ml/l instead of only mentioning it in prose.
5. Compare the corrected MediaDive/JCM 480 branch with TOGO M481 and reconcile them as source duplicates if their corrected formulations match.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sporomusa_medium__4939c205.yaml`.
- Re-inspect the regenerated record against JCM 480, Medium 197, Medium 243, and Medium 317 to confirm all stock additions retain their own basis and dose.
- Confirm the regenerated record has no final-medium `NaHCO3`, mannitol, dithiothreitol, vitamin, or Se/W rows at stock strength.
- Re-run merge freshness and confirm the JCM/MediaDive and TOGO M481 records from `GRMD=480` are not left as independent generated outputs when their source support is equivalent.

## Additional Notes

JCM 480 deliberately uses Medium 243 trace element solution without Na2SeO3 x 5 H2O. The imported row for `Na2SeO3` comes from the Medium 317 Se/W solution, not from that Medium 243 trace-element solution.
