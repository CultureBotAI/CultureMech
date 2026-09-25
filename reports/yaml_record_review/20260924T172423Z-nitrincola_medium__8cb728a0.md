# YAML Record Review: NITRINCOLA MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrincola_medium__8cb728a0.yaml
- Started UTC: 2026-09-24T17:23:10Z
- Finished UTC: 2026-09-24T17:24:23Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:000616`, `nitrincola_medium`, generated from `data/normalized_yaml/bacterial/nitrincola_medium.yaml`.

The record represents MediaDive/DSMZ medium 1174, "NITRINCOLA MEDIUM".

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to the correct upstream DSMZ medium. MediaDive REST medium 1174 and the DSMZ 1174 PDF both identify the source as `NITRINCOLA MEDIUM` with pH 9.0.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` found this direct MediaDive owner plus an active KOMODO-derived normalized owner, `data/normalized_yaml/bacterial/KOMODO_1174_NITRINCOLA_medium.yaml`, and an active generated duplicate, `data/merge_yaml/merged/NITRINCOLA_MEDIUM.yaml`. The KOMODO record explicitly says it copied ingredients from DSMZ Medium 1174 and cites `mediadive.medium:1174`.

## Evidence
MediaDive and the DSMZ PDF list the same six solutes per liter: 0.25 g K2HPO4, 0.5 g NH4Cl, 0.1 g yeast extract, 10 g Na acetate, 17.5 g NaCl, and 4 g Na2B4O7, made up with 1000 ml distilled water. The generated direct MediaDive record captures all six non-water solutes at the correct gram-per-liter concentrations.

The provider pH and preparation instruction are also represented on the direct record: pH 9.0 and adjustment to pH 9.0 with 1M NaOH before autoclaving.

The merge layer leaves a duplicate recipe active at `data/merge_yaml/merged/NITRINCOLA_MEDIUM.yaml`. That KOMODO-derived duplicate has the same six DSMZ solutes and same pH but also models NaOH as a variable ingredient with "pH adjustment" notes. The direct MediaDive record properly keeps NaOH out of the ingredient list and represents the source statement as a pH-adjustment preparation step.

## Completeness
The direct MediaDive formula is chemically complete except for distilled water, which the MediaDive importer commonly omits from final media. The actionable defect is duplicate handling: DSMZ 1174 should not be represented by two active generated media that differ only because the KOMODO enrichment path materialized pH-adjustment NaOH as a variable ingredient.

## Findings
- `data/merge_yaml/merged/nitrincola_medium__8cb728a0.yaml` duplicates `data/merge_yaml/merged/NITRINCOLA_MEDIUM.yaml`; both resolve to DSMZ/MediaDive medium 1174.
- The KOMODO-derived duplicate adds variable NaOH as an ingredient even though DSMZ uses NaOH only to adjust pH before autoclaving.

## Recommended Edits
- Consolidate `data/normalized_yaml/bacterial/nitrincola_medium.yaml` with `data/normalized_yaml/bacterial/KOMODO_1174_NITRINCOLA_medium.yaml` so DSMZ/MediaDive 1174 and KOMODO 1174 merge into one generated recipe.
- Keep the direct MediaDive six-solute formula and pH 9.0 preparation semantics as the canonical form.
- Drop variable NaOH from the KOMODO-derived ingredient list or migrate it into a pH-adjustment preparation step before fingerprinting.

## Follow-up Checks
- Regenerate both affected generated YAML files and confirm only one active Nitrincola DSMZ 1174 record remains.
- Re-run open, strict, reference, and term validation on the surviving regenerated artifact.
- Re-check the surviving recipe against MediaDive REST medium 1174 and the DSMZ 1174 PDF.

## Additional Notes
None.
