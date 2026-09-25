# YAML Record Review: Sulfate-Free Metako Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_free_metako_medium__eb71619a.yaml` (`CultureMech:007733`)
- Started UTC: `2026-09-25T07:51:16Z`
- Finished UTC: `2026-09-25T07:51:42Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_free_metako_medium__eb71619a.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M1206_Sulfate-Free_Metako_Medium.yaml` |
| CultureMech ID | `CultureMech:007733` |
| Media term | `TOGO:M1206` |
| Original source | JCM `JCM_M1126-2`, strain-specific Sulfate-Free Metako Medium variant |
| Merge fingerprint | `eb71619a2659c06db9d7efe4bb41eababb11be97ad6076fc1c4ac43206b4c1ed` |
| Merged from | `TOGO_M1206_Sulfate-Free_Metako_Medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, TOGO M1206 media term, `JCM_M1126-2` source, and single-source merge fingerprint. TOGO M1206 is the JCM 32479 replacement variant of JCM 1126: it keeps the sulfate-free Metako base and replaces the trimethylamine stock with final 0.55 g/L sodium lactate plus 1.0 g/L yeast extract.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M1206`, `JCM_M1126-2`, `CultureMech:007733`, and `sulfate_free_metako_medium` found this TOGO M1206 owner, the paired TOGO M1205 base recipe, and the MediaDive J1126 representation. The searches found no conflicting use of `CultureMech:007733`.

Most retained ingredient groundings are plausible. `MgCl2*6H2O` and `Na2B4O7*10H2O` are exact hydrated compounds, while the simple added rows for sodium lactate and yeast extract match the M1206 source intent.

## Evidence

The TOGO M1206 JSON has a one-liter basal table with `1 mg` resazurin, `12 mg` `SrCl2*6H2O`, `3 mg` NaF, `85 mg` KBr, `1 mg` LiCl, and `34 mg` `Na2B4O7*10H2O`. It then adds 1 ml/L trace element solution from M1205, 0.4 ml/L selenite-tungstate solution, 2 ml/L trace vitamins, 1 g/L yeast extract, 0.55 g/L sodium lactate under N2, and 2.5 ml/L each of the 5% Na2S*9H2O and 5% L-Cysteine*HCl*H2O reducing solutions.

The generated YAML keeps only the final yeast extract and sodium lactate rows from the replacement section. The other stock additions are migrated into five empty `solutions` entries with `G_PER_L` units, and no `preparation_steps` section survives.

The original JCM 1126 page contains the corresponding replacement comment: for strain JCM 32479, trimethylamine is replaced with sodium lactate at 0.55 g/L and yeast extract at 1.0 g/L. That supports M1206 as a real variant, not an accidental duplicate of M1205.

## Completeness

The generated variant is incomplete because it loses stock addition volumes, anaerobic addition sequence, preparation text, and source cross-references needed to recreate the medium.

`target_organisms` is absent. The variant is labeled for strain JCM 32479, but neither the TOGO medium payload nor the JCM medium page provides a linked taxon or growth evidence suitable for a `target_organisms` assertion.

## Findings

- The same basal milligram salts as M1205 are 1000x too high in the generated top-level ingredient list: `Resazurin` is `1 G_PER_L`, `KBr` is `85 G_PER_L`, `Na2B4O7*10H2O` is `34 G_PER_L`, `SrCl2*6H2O` is `12 G_PER_L`, `NaF` is `3 G_PER_L`, and `LiCl` is `1 G_PER_L`.
- The trace-element, selenite-tungstate, trace-vitamin, Na2S*9H2O, and L-Cysteine*HCl*H2O solution records are all empty and use `G_PER_L` to store what were 1, 0.4, 2, 2.5, and 2.5 ml/L additions.
- Preparation steps are absent even though TOGO and JCM both provide anaerobic dispensing, sealed autoclaving, overnight standing, N2 storage, and pre-inoculation reducing-solution addition instructions.
- Nitrogen appears twice as gas rows, once as `Nitrogen gas` in the N2/CO2 basal atmosphere and once as `N2` in the lactate/yeast replacement section, without enough structure to say which stock or vessel each row belongs to.
- The M1206 cross-reference to M1205 is present only as literal solution text; the generated variant cannot resolve the trace-element stock or identify that its composition is inherited from the base medium.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1206_Sulfate-Free_Metako_Medium.yaml` or the TOGO import/solution migration path, then regenerate `data/merge_yaml/merged/sulfate_free_metako_medium__eb71619a.yaml`.
- Convert basal milligram rows to g/L magnitudes instead of carrying raw milligram numbers as `G_PER_L`.
- Keep sodium lactate at 0.55 g/L and yeast extract at 1.0 g/L as the M1206 replacement for the trimethylamine stock.
- Represent the M1205 trace-element cross-reference, M431 selenite-tungstate stock, M701 trace-vitamin stock, and 5% reducing-agent stocks as volume-per-liter additions or equivalent structured solution references.
- Add preparation steps for N2/CO2 dispensing, sealed autoclaving, overnight standing, N2-protected lactate/yeast handling, and aseptic pre-inoculation addition of Na2S*9H2O and L-Cysteine*HCl*H2O.
- Preserve the intentional distinction between TOGO M1205 and TOGO M1206 when comparing this variant to the base Sulfate-Free Metako Medium and the MediaDive J1126 import.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M1206`, `JCM_M1126-2`, `CultureMech:007733`, and `sulfate_free_metako_medium` to confirm the repaired variant still indexes separately from the base recipe.
- Compare the regenerated record against TOGO M1205 and MediaDive J1126 so only the trimethylamine-to-lactate/yeast replacement differentiates M1206 from the base where the primary sources agree.

## Additional Notes

Empty optional fields that are unrelated to source-backed organism targets were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the stock-aware generation path.
