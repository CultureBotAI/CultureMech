# YAML Record Review: modified_sw_25_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sw_25_medium.yaml
- Started UTC: 2026-09-24T13:21:56Z
- Finished UTC: 2026-09-24T13:24:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:007717 |
| Name | modified_sw_25_medium |
| Original name | Modified SW-25 Medium |
| Category | bacterial |
| Source identity | TOGO:M1191, imported from JCM_M1114 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/TOGO_M1191_Modified_SW-25_Medium.yaml` or the TOGO/JCM solution importer. |

An ignored-file-inclusive exact search for `CultureMech:007717`, `TOGO:M1191`, `TOGO_M1191_Modified_SW-25_Medium`, `M1191`, and `GRMD=1114` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained TOGO owner, related `modified_sw_25_medium` records for the same JCM GRMD=1114 page, index/report rows, and aggregate QA rows. The reviewed generated record is a singleton merge from `TOGO_M1191_Modified_SW-25_Medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sw_25_medium.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sw_25_medium.yaml --out /private/tmp/modified_sw_25_medium.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sw_25_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sw_25_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The TOGO identity is correct: live TOGO M1191 resolves to `Modified SW-25 Medium`, reports `original_media_id: JCM_M1114`, names pH 7.5, and carries the same ingredient labels and amounts as the YAML. The exact JCM URL embedded by TOGO, `GRMD=1114`, currently returns a JCM `Nothing found` page, so direct JCM corroboration was unavailable from the cited URL.

The ChEBI groundings that are present are exact for the salts and water. The central grounding error is structural: the salts belong to the nested SW-25 solution, not to the top-level medium alongside yeast extract and Casamino acids.

## Evidence

The live TOGO payload has a main solution containing 1 g yeast extract, 1 g Casamino acids, and 1 L of `SW--25 solution`. A separate `SW--25 solution` subcomponent is made in 1 L water with MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, MgCl2 x 6H2O, KCl, NaHCO3, and NaBr.

The YAML loses that boundary. The `solutions` entry for `SW--25 solution` has an empty `composition` and a false `1 G_PER_L` concentration, while all SW-25 stock salts and the stock's 1 L water row were promoted to top-level final-medium ingredients.

The TOGO payload also preserves preparation comments for pH 7.5, autoclaving, optional agar for solid medium, and making the SW-25 stock to 1 L. None of those source-supported comments is represented in `ph_value` or `preparation_steps`.

## Completeness

The record is missing all preparation detail and the full composition of its required SW-25 solution. `target_organisms`, `growth_evidence`, and `discussion` are empty; those empty optional fields are acceptable for a recipe-only TOGO import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The nested SW-25 solution is empty and its salts were flattened into final-medium ingredients. | TOGO M1191 adds 1 L of `SW--25 solution` to yeast extract and Casamino acids, then separately defines the SW-25 salts in that solution. The YAML has an empty `solutions[0].composition` and top-level rows for all SW-25 solution salts. | `data/normalized_yaml/bacterial/TOGO_M1191_Modified_SW-25_Medium.yaml`; TOGO subcomponent-to-solution import logic. |
| major | The SW-25 stock volume and water basis are represented as grams-per-liter concentrations. | TOGO M1191 says the final medium uses 1 L of `SW--25 solution`, and the stock itself is brought to 1 L distilled water. The YAML stores both as `1 G_PER_L`: once in `solutions[0].concentration` and once in the top-level `Distilled water` ingredient. | `data/normalized_yaml/bacterial/TOGO_M1191_Modified_SW-25_Medium.yaml`; TOGO unit normalization. |
| major | Source pH and autoclaving instructions were dropped. | TOGO comments say to adjust pH to 7.5 and autoclave, and to add 20 g/l agar for solid medium. The YAML has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1191_Modified_SW-25_Medium.yaml`; TOGO comment import. |
| minor | The original JCM URL no longer resolves to a source page. | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1114` returned a JCM page saying `Nothing found`; the TOGO API still cites that URL as `src_url`. | Source-provenance curation for JCM_M1114 / TOGO M1191. |
| minor | The SW-25 JCM/TOGO branches need duplicate or variant reconciliation. | The exact ignored-file-inclusive search found `TOGO_M1192_Modified_SW-25_Medium.yaml` and `modified_sw_25_medium.yaml`, both citing `GRMD=1114` or TOGO M1191, plus separate generated outputs with different fingerprints. | Merge/source-duplicate curation for the JCM_M1114 source family. |

No blocker findings.

## Recommended Edits

1. Populate `SW--25 solution` with distilled water and the MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, MgCl2 x 6H2O, KCl, NaHCO3, and NaBr rows from TOGO paragraph 3.
2. Remove those SW-25 stock rows from top-level `ingredients`; keep only yeast extract, Casamino acids, and a 1 L solution addition in the final-medium scope.
3. Replace both false `1 G_PER_L` volume rows with volume or solution-addition semantics.
4. Restore pH 7.5 and the autoclave instruction from the TOGO comments, and preserve the optional 20 g/l agar note as a solid-medium variant or preparation note.
5. Investigate the retired JCM `GRMD=1114` URL and update provenance to a currently resolvable source if JCM moved the page.
6. Compare M1191, M1192, and the direct MediaDive/JCM branch to decide which are source duplicates and which are true SW-25 variants.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sw_25_medium.yaml`.
- Inspect the regenerated YAML against live TOGO M1191 to confirm SW-25 is a populated nested solution and the top-level medium has only yeast extract, Casamino acids, and the solution addition.
- Search for `GRMD=1114` with ignored files included after provenance correction to ensure every same-source SW-25 branch has been reconciled.

## Additional Notes

The JCM miss was checked by fetching the exact URL from TOGO and the YAML on 2026-09-24; I did not find an alternate JCM URL for Medium 1114 during this bounded record review.
