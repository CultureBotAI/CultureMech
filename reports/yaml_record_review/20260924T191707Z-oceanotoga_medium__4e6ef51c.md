# YAML Record Review: oceanotoga_medium__4e6ef51c

- Repository: CultureMech
- Record: data/merge_yaml/merged/oceanotoga_medium__4e6ef51c.yaml
- Started UTC: 2026-09-24T19:17:07Z
- Finished UTC: 2026-09-24T19:18:13Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oceanotoga_medium__4e6ef51c.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:000604` and source term `mediadive.medium:1163a`.

The generated record merges three normalized owners:

- `data/normalized_yaml/bacterial/oceanotoga_medium.yaml`
- `data/normalized_yaml/bacterial/for_dsm_15011_and_dsm_24906.yaml`
- `data/normalized_yaml/bacterial/for_dsm_24739.yaml`

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oceanotoga_medium__4e6ef51c.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The canonical DSMZ identity is correct: the target is DSMZ Medium 1163a, Oceanotoga medium.

The generated duplicate graph is stale. It emits KOMODO Medium 1163.1 and 1163.2 as `SOURCE_DUPLICATE` children, but the normalized records already have a 2026-09-13 `RESOLVED_KOMODO_1163_OCEANOTOGA_TOPOLOGY` repair that models DSMZ Medium 1163a as the parent and the two KOMODO wrappers as `STRAIN_SPECIFIC_VARIANT` children.

## Evidence

Checked the generated record, the three normalized source owners, the KOMODO 1163 Oceanotoga repair script, an ignored-inclusive exact repository search for DSMZ 1163a and KOMODO 1163 ids plus the `oceanotoga_medium` slug, the DSMZ MediaDive REST payload for medium 1163a, and text extracted from the official DSMZ Medium 1163a PDF.

DSMZ Medium 1163a has three recipe scopes:

- Main medium: salts, HEPES, yeast extract, Modified Wolin's mineral solution at 10 ML_PER_L, sodium resazurin, L-Cysteine HCl x H2O, D-Glucose, Wolin's vitamin solution at 1 ML_PER_L, and 1000 ml distilled water.
- Modified Wolin's mineral solution: salts in a 1000 ml stock, with Na2SeO3 x 5 H2O and Na2WO4 x 2 H2O as milligram additions.
- Wolin's vitamin solution (10x): milligram vitamin quantities made up to 1000 ml.

## Completeness

The generated YAML is complete enough to expose the DSMZ recipe text, but it does not preserve solution boundaries:

- Modified Wolin's mineral solution and Wolin's vitamin solution are absent as solutions.
- Mineral-stock rows are flattened as final-medium ingredients even though only 10 ml stock is added per final liter.
- Vitamin-stock rows are flattened as final-medium ingredients even though only 1 ml of the 10x stock is added per final liter.
- NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are summed across the main medium and Modified Wolin mineral stock.
- The 1000 ml final distilled-water row from DSMZ is omitted.
- Stock preparation for Modified Wolin's mineral solution is mixed into the main medium's `preparation_steps`.

## Findings

- BLOCKER: Mineral and vitamin stock recipes are flattened into final-medium ingredients, causing stock concentrations to be interpreted as final concentrations.
- BLOCKER: NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are summed across the main medium and the mineral stock; the generated values 30.6736, 4.38477, and 0.238477 G_PER_L are not source rows.
- MAJOR: The generated record is stale relative to the September KOMODO 1163 topology repair and still treats `for_dsm_15011_and_dsm_24906` and `for_dsm_24739` as source duplicates rather than strain-specific variants.
- MAJOR: The record has no final distilled-water ingredient despite DSMZ Medium 1163a listing 1000 ml.
- MAJOR: Modified Wolin's mineral solution and Wolin's vitamin solution (10x) need to be nested solution additions at 10 ML_PER_L and 1 ML_PER_L, respectively.
- MAJOR: The mineral-stock pH-adjustment step is attached to the main medium instead of the mineral stock.

## Recommended Edits

- Split the DSMZ 1163a normalized representation into a main final medium plus nested `Modified Wolin's mineral solution` and `Wolin's vitamin solution (10x)` stocks.
- Add the main 1000 ML_PER_L distilled-water row and keep the two stock waters inside their solution records.
- Keep 29.6736 G_PER_L NaCl, 1.38477 G_PER_L MgSO4 x 7 H2O, and 0.138477 G_PER_L CaCl2 x 2 H2O in the final medium; keep 1 G_PER_L NaCl, 3 G_PER_L MgSO4 x 7 H2O, and 0.1 G_PER_L CaCl2 x 2 H2O only in the mineral stock.
- Regenerate from the current normalized topology so KOMODO 1163.1 and 1163.2 remain `STRAIN_SPECIFIC_VARIANT` children of the DSMZ 1163a parent rather than source duplicates.
- Keep the main anaerobic DSMZ preparation steps on the parent and the nitrilotriacetic-acid/KOH stock step on `Modified Wolin's mineral solution`.

## Follow-up Checks

- Run an ignored-inclusive exact search for `mediadive.medium:1163a`, `DSMZ_Medium1163a`, `komodo.medium:1163.1`, and `komodo.medium:1163.2` after repair to confirm the DSMZ parent and KOMODO children regenerate with variant topology.
- Rebuild merged YAML and confirm DSMZ 1163a stays distinct from TOGO M2122 if that source is a separate provider import.
- Re-run open-schema, strict, reference, and term validation after normalized YAML is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
