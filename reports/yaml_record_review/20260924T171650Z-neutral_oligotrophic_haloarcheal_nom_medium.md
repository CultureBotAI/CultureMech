# YAML Record Review: neutral_oligotrophic_haloarcheal_nom_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml
- Started UTC: 2026-09-24T17:15:56Z
- Finished UTC: 2026-09-24T17:16:50Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml` as a generated `MediaRecipe` for TOGO M2156, `CultureMech:008750`, label `neutral_oligotrophic_haloarcheal_nom_medium`, category `bacterial`, and original name `Neutral Oligotrophic Haloarcheal (NOM) Medium`.

The generated record was merged from `data/normalized_yaml/bacterial/neutral_oligotrophic_haloarcheal_nom_medium.yaml`. It is derived; the normalized TOGO M2156 owner should be repaired and regenerated.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml --out /private/tmp/neutral_oligotrophic_haloarcheal_nom_medium.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarcheal_nom_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The record denotes TOGO M2156, imported from NBRC medium 1513.
- The inspected live NBRC 1513 page and TOGO M2156 API payload agree on the title `Neutral Oligotrophic Haloarcheal (NOM) Medium`; the `haloarcheal` spelling is source text, not only a filename error.
- A gitignore-independent hidden-file search for `TOGO:M2156`, `NBRC_M1513`, `NO=1513`, `Neutral Oligotrophic Haloarcheal`, and `neutral_oligotrophic_haloarcheal_nom_medium` across `data/normalized_yaml` and `data/merge_yaml` found only this normalized owner and its generated merge in the curated YAML corpus.

## Evidence

NBRC 1513 lists yeast extract, Hipolypepton, sodium pyruvate, KH2PO4, KCl, CaCl2.2H2O, NH4Cl, MgSO4.7H2O, MgCl2.6H2O, NaCl, optional agar, and 1 L distilled water, followed by pH 7.5. It also marks the Hipolypepton row with a supplier footnote for FUJIFILM Wako Pure Chemical Corporation.

The generated record carries the mineral and carbon-source quantities from the source, but three representational details are wrong: `Distilled water` is `1 G_PER_L` instead of a 1 L final-volume solvent, `Agar (if needed)` is a required 15 g/L ingredient with `physical_state: SOLID_AGAR`, and `Hipolypeptone*` is moved out of the main ingredient table into an empty `Unknown solution` row.

## Completeness

- Consequential gap: pH 7.5 is present in TOGO metadata and NBRC page text but absent from the generated record.
- Consequential error: optional agar is modeled as a required solid-agar formulation.
- Consequential error: Hipolypepton is missing from the main ingredients and represented as an empty solution.
- Consequential error: the final 1 L water volume is represented as `1 G_PER_L`.
- Empty optional fields are not defects. The inspected NBRC page does not provide incubation temperature or a target organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Hipolypepton was incorrectly migrated to an empty solution wrapper. | NBRC 1513 lists `Hipolypepton*` as a 0.25 g ingredient with a supplier footnote; the generated record has `Hipolypeptone*` as an empty `Unknown solution` at 0.25 `G_PER_L`. | Move Hipolypepton back into `ingredients` in `data/normalized_yaml/bacterial/neutral_oligotrophic_haloarcheal_nom_medium.yaml` and preserve the supplier note. |
| major | Conditional agar is treated as required. | NBRC and TOGO call the row `Agar (if needed)` at 15 g; the generated record sets `physical_state: SOLID_AGAR` and stores the agar row without optionality. | Model the base as liquid with an explicit optional agar variant, or mark the agar addition as conditional if the schema supports it. |
| major | pH and final volume are wrong or absent. | TOGO M2156 has `ph: 7.5`, NBRC displays `pH 7.5`, and NBRC lists distilled water as 1 L. The generated record has no `ph_value` and lists distilled water as `1 G_PER_L`. | Add `ph_value: 7.5` and represent distilled water as a 1 L final-volume solvent rather than a mass concentration. |

## Recommended Edits

1. Recurate the normalized M2156 owner from NBRC 1513 so Hipolypepton is a normal 0.25 g/L ingredient with the FUJIFILM Wako supplier footnote.
2. Preserve pH 7.5 and the 1 L water volume.
3. Separate the base liquid NOM medium from the optional 15 g/L agar addition or explicitly mark agar as conditional.
4. Regenerate the merged YAML.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired normalized owner and regenerated merge.
- Re-run a gitignore-independent hidden-file search for `TOGO:M2156`, `NBRC_M1513`, and `NO=1513` across `data/normalized_yaml` and `data/merge_yaml` to confirm the singleton source identity remains bounded.
- Manually compare the regenerated record against NBRC 1513 and TOGO M2156.

## Additional Notes

The NBRC live page was available at review time. The TOGO M2156 API payload agreed with the NBRC ingredient quantities and pH.
