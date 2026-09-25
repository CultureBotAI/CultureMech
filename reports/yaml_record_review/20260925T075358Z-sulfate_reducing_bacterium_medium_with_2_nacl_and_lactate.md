# YAML Record Review: Sulfate-Reducing Bacterium Medium With 2% NaCl And Lactate

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate.yaml` (`CultureMech:010039`)
- Started UTC: `2026-09-25T07:53:58Z`
- Finished UTC: `2026-09-25T07:54:56Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M639_Sulfate-Reducing_Bacterium_Medium_With_2_NaCl_And_Lactate.yaml` |
| CultureMech ID | `CultureMech:010039` |
| Media term | `TOGO:M639` |
| Original source | JCM `JCM_M627`, Sulfate-Reducing Bacterium Medium With 2% NaCl And Lactate |
| Merge fingerprint | `c5f0ae5c372576037f31c7d5786114283c3d9e0a058951ad803d8ea96467bd46` |
| Merged from | `TOGO_M639_Sulfate-Reducing_Bacterium_Medium_With_2_NaCl_And_Lactate` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, TOGO M639 term, JCM_M627 source, and single-source merge fingerprint.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M639`, `JCM_M627`, `CultureMech:010039`, and `sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate` found this M639 owner, the paired TOGO M640 agar variant from `JCM_M627-2`, an older MediaDive J627 normalized source, and later lactate/pyruvate records that incorporated the older source. No conflicting use of `CultureMech:010039` was found.

The inorganic salts have plausible groundings, including the corrected MgSO4*7H2O hydrate term. The `L--Sodium lactate` ingredient still has only a legacy `mediaingredientmech_term` and should be grounded directly to a ChEBI sodium L-lactate term during curation.

## Evidence

The original JCM 627 page defines this record as JCM Medium 552 supplemented with 2% final NaCl. JCM 552 is the lactate base: it contains KH2PO4, NH4Cl, Na2SO4, CaCl2*2H2O, MgSO4*7H2O, base NaCl, yeast extract, 1 ml vitamin solution, 1 ml FeCl2 solution, 1 ml trace element solution, L-sodium lactate, 1 mg resazurin, L-cysteine*H2O*HCl, and 1 L water.

TOGO M639 expands the M552 base and keeps the JCM 627 wrapper comment, but the generated YAML changes the defining `2% (final) NaCl` supplement into a `VARIABLE` NaCl row. It also moves the three 1 ml stock additions into empty solution records with `G_PER_L` units and drops the pH 7.5 preparation text.

JCM 552 and the TOGO M639 comment both say to mix everything except L-sodium lactate and L-cysteine*H2O*HCl, adjust to pH 7.5, autoclave under N2, separately autoclave the lactate and cysteine in 10 ml water under N2, add them to the medium, then readjust to pH 7.5 with sterile 1 N NaOH. None of those steps are represented.

## Completeness

The generated record is incomplete because the 2% NaCl supplement is not numeric, the stock-solution additions are empty, pH 7.5 is absent, and the anaerobic preparation sequence is absent.

`target_organisms` is absent. The fetched JCM 627 and JCM 552 medium pages do not assert a source-backed growth organism for this recipe, so no target was inferred.

## Findings

- `NaCl` is stored as `VARIABLE`, even though JCM 627 defines the recipe by a 2% final NaCl supplement on top of the JCM 552 base.
- The base recipe's 1 mg resazurin row is stored as `1 G_PER_L`, a 1000x unit slip.
- The 1 ml/L vitamin, FeCl2, and trace-element additions are empty `solutions` entries that use `G_PER_L` instead of representing volume-per-liter stock additions or resolvable cross-references.
- `NaOH` is a `VARIABLE` top-level ingredient, losing the source role as sterile 1 N NaOH for pH 7.5 readjustment.
- The generated file lacks all preparation steps: initial pH 7.5 adjustment, anaerobic autoclaving under N2, separate autoclaving of lactate and cysteine in 10 ml water, addition of those supplements, and final pH 7.5 readjustment.
- `L--Sodium lactate` lacks a primary ChEBI term even though the recipe depends on that defined carbon source.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M639_Sulfate-Reducing_Bacterium_Medium_With_2_NaCl_And_Lactate.yaml` or the TOGO expansion for JCM wrapper media, then regenerate `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate.yaml`.
- Resolve JCM 627 through JCM 552 and represent the 2% final NaCl instruction numerically instead of leaving NaCl as `VARIABLE`.
- Keep the vitamin solution, FeCl2 solution, and trace element solution as 1 ml/L stock additions or structured cross-references, not empty `G_PER_L` solution records.
- Convert resazurin from 1 mg/L to `0.001 G_PER_L`.
- Add pH 7.5 and preparation steps for the anaerobic autoclaving, separate lactate/cysteine autoclaving, supplement addition, and sterile NaOH readjustment.
- Ground `L--Sodium lactate` to a ChEBI term such as sodium L-lactate and keep TOGO M640 as the separate agar variant rather than merging agar into this liquid record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M639`, `JCM_M627`, `CultureMech:010039`, and `sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate` to confirm the liquid and agar variants remain distinct.
- Compare the repaired M639 source against M640, the older MediaDive J627 source, and the lactate/pyruvate records that copied from it so stale copy-forward formulae can be fixed in their own records.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock references and growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the JCM wrapper expansion path.
