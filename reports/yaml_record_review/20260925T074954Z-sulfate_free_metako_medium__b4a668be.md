# YAML Record Review: SULFATE-FREE METAKO MEDIUM

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_free_metako_medium__b4a668be.yaml` (`CultureMech:002299`)
- Started UTC: `2026-09-25T07:49:54Z`
- Finished UTC: `2026-09-25T07:50:21Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_free_metako_medium__b4a668be.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfate_free_metako_medium.yaml` |
| CultureMech ID | `CultureMech:002299` |
| Media term | `mediadive.medium:J1126` |
| Original source | JCM `J1126`, SULFATE-FREE METAKO MEDIUM |
| Merge fingerprint | `b4a668be09972cc6c537660a4ea723882c4cb2a09aac900ee828923a18980899` |
| Merged from | `sulfate_free_metako_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, MediaDive J1126 term, JCM source URL, and single-source merge fingerprint for the MediaDive import of JCM medium 1126.

Exact gitignore-independent searches with `--no-ignore --hidden` for `mediadive.medium:J1126`, `CultureMech:002299`, `SULFATE-FREE METAKO MEDIUM`, and `sulfate_free_metako_medium` found this MediaDive owner, the TOGO M1205 and M1206 records for the same recipe family, and no conflicting use of `CultureMech:002299`.

Most ChEBI groundings are plausible and the MediaDive import preserves exact hydrate terms for `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, and `FeCl3 x 6 H2O`. `NiCl2 x 6 H2O` is still grounded to an anhydrous nickel dichloride label, and the `KI` row still carries a legacy `mediaingredientmech_term` entry even though its primary ChEBI term is potassium iodide.

## Evidence

The MediaDive REST record for J1126 keeps a 1018 ml `Main sol. J1126` solution that contains basal salts, 1 ml `Trace element solution`, 0.4 ml `Selenite-tungstate solution`, 2 ml `Trace vitamins solution`, 10 ml of a 1 M trimethylamine stock, and two 2.5 ml additions of 5% reducing-agent stocks. Its basal `g_l` values, such as `20.3831 G_PER_L` for NaCl and `0.0834971 G_PER_L` for KBr, match the generated YAML and show that the basal rows were diluted into MediaDive's final 1018 ml volume.

The same REST payload has separate 1 L stock recipes for the trace-element, selenite-tungstate, and trace-vitamin solutions. Those stock recipe rows are also present in the generated YAML, but only as top-level ingredients at stock strength. An exact gitignore-independent search for `solutions:`, `Trace element solution`, `Selenite`, and `Trace vitamins` in the generated YAML produced no matches, confirming that the nested solution hierarchy was not carried into the merged record.

The JCM 1126 page corroborates MediaDive's source structure: a main table, an anaerobic post-autoclave trimethylamine addition, two pre-inoculation reducing-agent additions, a separate trace-element solution table, and a strain-specific comment for JCM 32479.

## Completeness

The generated record has final-volume basal concentrations but incomplete stock modeling. Without solution records or stock-addition metadata, consumers cannot tell which top-level rows are final medium compounds and which rows belong only to 1 ml/L, 0.4 ml/L, or 2 ml/L stocks.

`target_organisms` is absent. The JCM medium page and MediaDive medium record identify a medium recipe but do not assert growth observations, so no organism should be inferred.

## Findings

- The three MediaDive child stocks were flattened into the top-level ingredient list. Trace-element values such as `0.61 G_PER_L` `MnCl2 x 4 H2O` and `0.15 G_PER_L` nitrilotriacetic acid are stock concentrations from a 1 ml/L addition, not final medium concentrations.
- The selenite-tungstate and vitamin stock ingredients have the same hierarchy loss; for example `0.4 G_PER_L` NaOH is the 1 L selenite-tungstate stock strength, and `0.0049 G_PER_L` biotin is the 1 L vitamin stock strength.
- The 10 ml 1 M trimethylamine addition and the two 2.5 ml 5% reducing-agent additions are represented as `10 G_PER_L`, `2.5 G_PER_L`, and `2.5 G_PER_L` top-level ingredient rows, losing both stock concentration and addition volume.
- `SrCl2 x 6 H2O` is the sum of the final-volume basal strontium chloride row and the undiluted trace-stock row, as shown by `[Merged 2 duplicates: 0.0117878, 0.01]`; those two terms came from different solution scopes and should not be summed at this stage.
- Preparation steps are present but underspecified: step 1 combines autoclaving and the later trimethylamine addition, step 2 is labeled `AUTOCLAVE` even though it describes aseptic pre-inoculation addition, and step 3 stores the JCM 32479 replacement comment as a generic `MIX` step.
- `NiCl2 x 6 H2O` needs an exact hydrate grounding check; its current primary ChEBI label drops the waters of crystallization.

## Recommended Edits

- Repair the MediaDive import or normalized source so `data/normalized_yaml/bacterial/sulfate_free_metako_medium.yaml` preserves the MediaDive `solutions` hierarchy, then regenerate `data/merge_yaml/merged/sulfate_free_metako_medium__b4a668be.yaml`.
- Keep the 1018 ml main solution's final-volume basal ingredient values, but model the trace-element, selenite-tungstate, and trace-vitamin recipes as child solutions instead of promoting their stock rows to final ingredients.
- Represent trimethylamine, Na2S*9H2O, and L-Cysteine*HCl*H2O as stock additions with 10 ml/L or 2.5 ml/L addition volumes and their 1 M or 5% stock strengths.
- Prevent duplicate-merging across different solution scopes so basal `SrCl2 x 6 H2O` and trace-stock `SrCl2 x 6 H2O` remain separate until a final-medium expansion is explicitly requested.
- Split the preparation text into actions that preserve anaerobic dispensing under N2/CO2, sealed autoclaving, overnight standing, sterile anaerobic trimethylamine addition, and aseptic pre-inoculation reducing-solution addition.
- Move the JCM 32479 replacement comment to a note or link it to the dedicated replacement variant represented by TOGO M1206/JCM_M1126-2; it is not an operational `MIX` step for this base recipe.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Compare the regenerated MediaDive J1126 record against TOGO M1205 and TOGO M1206 so the same JCM source and the JCM 32479 replacement variant have intentional merge boundaries.
- Re-run exact gitignore-independent searches for `CultureMech:002299`, `mediadive.medium:J1126`, and `sulfate_free_metako_medium` to verify no extra duplicate was introduced.

## Additional Notes

Empty optional fields that are unrelated to stock hierarchy and target-organism evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the MediaDive import, the maintained normalized source, and the stock-aware generation path.
