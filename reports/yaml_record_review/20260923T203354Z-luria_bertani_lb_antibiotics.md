# YAML Record Review: Luria-Bertani (LB) + Antibiotics

- Repository: CultureMech
- Record: `data/merge_yaml/merged/luria_bertani_lb_antibiotics.yaml`
- Started UTC: `2026-09-23T20:32:49Z`
- Finished UTC: `2026-09-23T20:33:54Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:009658`
- `name`: `luria_bertani_lb_antibiotics`
- `original_name`: `Luria-Bertani (LB) + antibiotics`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M3217`
- `merge_fingerprint`: `e22626294893098fe5a9dfc7babf6fac81db845182d09857c737f24991a4e9f1`
- `merged_from`: `luria_bertani_lb_antibiotics`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/luria_bertani_lb_antibiotics.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:009658`, `TOGO:M3217`, `M3217`, `luria_bertani_lb_antibiotics`, and the merge fingerprint found the maintained TOGO M3217 owner and this generated record.
- TOGO M3217 identifies the medium as `Luria-Bertani (LB) + antibiotics`.
- TOGO M3217 has no original source URL, but its comments state that `Escherichia coli` strain DH5alpha, strain HN-2 derivatives, and Xcc strain XC1 derivatives were cultured in LB at 37 C, 30 C, and 28 C, respectively.
- TOGO M3217 describes the antibiotic additions as ampicillin 100 ug/ml, rifampicin 50 ug/ml, kanamycin 50 ug/ml, gentamicin 50 ug/ml, and tetracycline 15 ug/ml.
- The maintained owner has post-merge MIM ChEBI groundings for kanamycin, tetracycline, and gentamicin, but this generated record predates that August repair and still lacks those terms.

## Evidence

- The generated record keeps the TOGO numeric antibiotic values but stores all five under `G_PER_L`: 100 g/L ampicillin, 50 g/L kanamycin, 50 g/L rifampicin, 15 g/L tetracycline, and 50 g/L gentamicin.
- The source comments give the same numbers in ug/ml, so the final mass concentrations should be 0.1 g/L ampicillin, 0.05 g/L kanamycin, 0.05 g/L rifampicin, 0.015 g/L tetracycline, and 0.05 g/L gentamicin.
- TOGO represents the basal `Luria-Bertani (LB)` as 1 L of prepared LB medium.
- The generated record expands the LB base to a Miller-style formula of 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride using a Laboratory Notes URL rather than a product specification.

## Completeness

- All five TOGO antibiotic rows are present but have the wrong concentration unit.
- All three inferred LB Miller constituents are present, but the source TOGO record only asserted 1 L LB medium.
- The maintained owner has ChEBI mappings for all five antibiotics; the generated record carries mappings only for ampicillin and rifampicin.
- The source organism and temperature context in TOGO comments is not represented as target organism or growth-condition metadata.
- The generated record has no structured references for TOGO M3217 or for the LB base expansion source.

## Findings

1. All antibiotic concentrations are one million-fold too high.
   - Evidence: TOGO reports antibiotic values in ug/ml, while the generated record stores the same numeric values as `G_PER_L`.
   - Impact: the generated formulation would be chemically unusable and no longer represents selective LB at standard antibiotic concentrations.

2. The generated file predates known antibiotic grounding fixes.
   - Evidence: the maintained owner has August 2026 ChEBI mappings for kanamycin, tetracycline, and gentamicin, while the generated record still lacks `term` entries for those three ingredients.
   - Impact: regenerated outputs would improve ontology coverage, but the current generated page remains under-grounded.

3. The LB base expansion is not grounded to a product specification.
   - Evidence: TOGO supplies only a prepared `Luria-Bertani (LB)` component, while the generated record expands it to tryptone, yeast extract, and sodium chloride using a Laboratory Notes recipe page despite notes claiming product-specification provenance.
   - Impact: the expanded base may be useful, but its stated provenance is weaker than the source text implies.

4. TOGO organism and condition context is not represented.
   - Evidence: TOGO comments mention `Escherichia coli` DH5alpha, HN-2 derivatives, Xcc strain XC1 derivatives, and 37 C / 30 C / 28 C culture temperatures; the generated record has no target-organism or growth-condition fields.
   - Impact: users lose the strain and temperature context that accompanied the antibiotic LB recipe.

## Recommended Edits

1. Convert antibiotic concentrations from ug/ml to final g/L or add a microgram-per-milliliter unit if the schema supports it.
2. Regenerate the record after the August MIM grounding so kanamycin, tetracycline, and gentamicin retain ChEBI terms.
3. Replace the Laboratory Notes LB expansion reference with a stable product specification or curated LB parent record, and link the antibiotic medium as a variant of that parent.
4. Add structured references for TOGO M3217 and for the LB base expansion source used.
5. Preserve the organism and temperature statements from TOGO as structured target-organism or growth-condition metadata where the schema allows.

## Follow-up Checks

- Re-fetch TOGO M3217 and confirm all five antibiotics regenerate as ug/ml-equivalent final concentrations.
- Confirm kanamycin, tetracycline, and gentamicin keep their ChEBI mappings after regeneration.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `TOGO:M3217` and `luria_bertani_lb_antibiotics` to confirm no duplicate TOGO M3217 owner was introduced.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
