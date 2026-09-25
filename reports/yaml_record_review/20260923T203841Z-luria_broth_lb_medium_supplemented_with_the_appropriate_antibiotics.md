# YAML Record Review: Luria Broth (LB) Medium Supplemented With The Appropriate Antibiotics

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics.yaml`
- Started UTC: `2026-09-23T20:37:41Z`
- Finished UTC: `2026-09-23T20:38:41Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:009441`
- `name`: `luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics`
- `original_name`: `Luria Broth (LB) medium supplemented with the appropriate antibiotics`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M2903`
- `merge_fingerprint`: `22a6ac6b6d72ed8add2b45f64cf9624d23514a63abbbf48a17688330021d4dfc`
- `merged_from`: `luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:009441`, `TOGO:M2903`, `M2903`, `luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics`, and the merge fingerprint found the maintained TOGO M2903 owner and this generated record.
- TOGO M2903 identifies the source as `Luria Broth (LB) medium supplemented with the appropriate antibiotics`.
- TOGO M2903 lists 30 ug/ml chloramphenicol, 1 L Luria Broth (LB) medium, and a comment that strains were cultured with either 30 ug/ml chloramphenicol or 20 ug/ml gentamicin.
- The `kg_microbe_match: mediadive.medium:74` field resolves to DSMZ Medium 74, `THERMUS THERMOPHILUS MEDIUM`, not an LB antibiotic medium.

## Evidence

- The generated record keeps the TOGO chloramphenicol numeric value but stores it as 30 `G_PER_L`.
- A 30 ug/ml chloramphenicol addition should be represented as 0.03 g/L if the record is normalized to grams per liter.
- TOGO comments also mention 20 ug/ml gentamicin, but the generated record has no gentamicin row or variant note.
- The generated record expands the 1 L prepared LB source row into 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride via an external Laboratory Notes URL.
- The maintained owner has an August MIM grounding for chloramphenicol, but this generated record predates that update and keeps the row ungrounded.

## Completeness

- The chloramphenicol row is present but has the wrong unit.
- The gentamicin option from the TOGO comment is absent.
- The prepared LB base is expanded to a plausible Miller-style base, but the expansion is not source-native.
- The generated record has no structured references for TOGO M2903 or for the LB base expansion source.
- The generated record carries an unrelated `kg_microbe_match`.

## Findings

1. Chloramphenicol is one million-fold too concentrated.
   - Evidence: TOGO lists chloramphenicol at 30 ug/ml, while the generated record stores 30 `G_PER_L`.
   - Impact: the generated selective medium is chemically unusable and no longer represents the source concentration.

2. The gentamicin alternative is missing.
   - Evidence: the TOGO comment says `Cm 30 ug/ml or gentamicin 20 ug/ml`, but the generated record contains chloramphenicol only.
   - Impact: the record loses one of the two explicitly enumerated antibiotic conditions behind the title's `appropriate antibiotics` wording.

3. The generated artifact predates known chloramphenicol grounding.
   - Evidence: the maintained owner has an August MIM ChEBI mapping for chloramphenicol, while the generated chloramphenicol row has no `term`.
   - Impact: current generated output remains under-grounded even though the normalized source has been repaired.

4. The KG-Microbe match points to an unrelated DSMZ recipe.
   - Evidence: `mediadive.medium:74` resolves to Thermus Thermophilus medium.
   - Impact: downstream reconciliation can connect the LB antibiotic record to a different DSMZ formula.

## Recommended Edits

1. Convert chloramphenicol from 30 ug/ml to the correct final mass concentration or add a microgram-per-milliliter unit if supported.
2. Add gentamicin 20 ug/ml as a separate optional antibiotic condition or split M2903 into chloramphenicol and gentamicin variants.
3. Regenerate after the August MIM grounding so chloramphenicol retains its ChEBI term.
4. Remove or recompute `kg_microbe_match: mediadive.medium:74`.
5. Replace the Laboratory Notes LB expansion with a curated LB parent link or a stable LB specification, and add structured references.

## Follow-up Checks

- Re-fetch TOGO M2903 and confirm regenerated output preserves both 30 ug/ml chloramphenicol and 20 ug/ml gentamicin.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `TOGO:M2903` and `luria_broth_lb_medium_supplemented_with_the_appropriate_antibiotics` to confirm no duplicate TOGO M2903 owner was introduced.

## Additional Notes

- Exact duplicate and KG-Microbe match checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
