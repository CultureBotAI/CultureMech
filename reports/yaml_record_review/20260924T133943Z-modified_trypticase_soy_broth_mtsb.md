# YAML Record Review: modified_trypticase_soy_broth_mtsb
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_trypticase_soy_broth_mtsb.yaml
- Started UTC: 2026-09-24T13:39:04Z
- Finished UTC: 2026-09-24T13:39:43Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_trypticase_soy_broth_mtsb`, CultureMech ID `CultureMech:009452`.

- Reviewed generated record: `data/merge_yaml/merged/modified_trypticase_soy_broth_mtsb.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_trypticase_soy_broth_mtsb.yaml`
- Media term: `TOGO:M2917`, `Modified trypticase soy broth (mTSB)`
- Source: `https://togomedium.org/medium/M2917`
- Merge fingerprint: `229fec7957b2e5e0765366e5a188ba678db29bc8890159b1c103ffdd10d02c56`
- `merged_from`: `modified_trypticase_soy_broth_mtsb`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The `TOGO:M2917` identity is correct for Modified trypticase soy broth.

The generated record expands the commercial 3% trypticase soy broth component into standard TSB constituents. The non-agar expansion is internally coherent: 17 g/L casein digest, 3 g/L soybean-meal digest, 2.5 g/L glucose, 5 g/L NaCl, and 2.5 g/L dipotassium phosphate sum to 30 g/L commercial TSB powder.

Two rows are outside the liquid mTSB chemistry:

- `Agar`, 15 g/L, comes from trypticase soy agar and is not present in TOGO `M2917`.
- `CO2` is an incubation atmosphere at 5%, not a dissolved medium ingredient.

## Evidence
Live TOGO `M2917` reports a concise article-derived recipe: 3% Trypticase soy broth, 0.6% yeast extract, and 5% CO2. Its source comment says the organism was grown on mTSB, defined as 3% trypticase soy broth with 0.6% yeast extract, and incubated at 37C with 5% CO2.

The TOGO payload does not list agar. It describes liquid mTSB transfer into 5 ml mTSB and 1 to 2 ml fresh mTSB cultures after colony transfer.

## Completeness
The commercial TSB base has been expanded to plausible constituent amounts, and 0.6% yeast extract is retained. However, the recipe is over-complete because it includes TSA-only agar in a `LIQUID` record.

The record is also missing structured handling for growth atmosphere: the source's 5% CO2 is represented as a variable ingredient instead of an incubation condition.

## Findings
1. Needs curation - `Agar` at 15 g/L is unsupported. TOGO `M2917` defines a broth, and the source prose describes liquid mTSB; agar came from a generic Tryptic Soy Agar composition and should not be in this liquid recipe.

2. Needs curation - `CO2` is modeled as a variable medium ingredient, but the source uses 5% CO2 as an incubation atmosphere.

3. Minor - `Yeast extract` is left as `0.6 PERCENT_W_V`. That is faithful to the source notation, but converting to 6 g/L would align it with the expanded 30 g/L TSB base.

4. Minor - the normalized notes cite Wikipedia as the TSB/TSA composition source. Product labels from BD, Sigma, or Neogen would be better evidence for the commercial TSB constituent expansion.

## Recommended Edits
- Remove the `Agar` ingredient from `data/normalized_yaml/bacterial/modified_trypticase_soy_broth_mtsb.yaml`.
- Move 5% CO2 out of `ingredients` and into an incubation or atmosphere field/note.
- Keep the expanded TSB base only if a product-specification citation is added; otherwise model `Trypticase soy broth` as the 3% complex component from TOGO.
- Optionally convert `0.6%` yeast extract to 6 g/L while preserving the source percent notation in notes.

## Follow-up Checks
- Re-fetch TOGO `M2917` and confirm the repaired YAML contains only 3% TSB plus 0.6% yeast extract as medium inputs.
- Confirm the regenerated `LIQUID` record has no agar row.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
The exact TOGO lookup for `M2917` was used for source comparison. A later broad exact-string search for local `Tryptic Soy Broth` references produced many unrelated corpus matches and was not used to establish absence or uniqueness.
