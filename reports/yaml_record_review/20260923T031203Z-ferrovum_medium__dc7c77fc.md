# YAML Record Review: ferrovum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferrovum_medium__dc7c77fc.yaml
- Started UTC: 2026-09-23T03:11:26Z
- Finished UTC: 2026-09-23T03:12:03Z
- Verdict: needs curation

## Target

CultureMech:010314 is the generated merged record for TOGO Medium M897, `Ferrovum  Medium`, a Togo split of JCM Medium 860 for pH 1.7 cultivation.

Togo M897 contains the basal JCM 860 water and MgSO4 x 7 H2O rows, then references 50 ml Modified UBS solution from M896, 20 ml 1.0 M FeSO4 solution at pH 2.0, and 10 ml Trace element solution.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator exited 0.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, `TOGO:M897` medium term, and original JCM 860 URL point to the intended Togo source.

The magnesium sulfate heptahydrate primary term is correct, but the generated row has no `mediaingredientmech_chebi_term` link after the 2026-06-10 primary-term fix.

The Togo metadata carries `ph: 1.7`, but the generated record does not expose that as `ph_value`.

## Evidence

The generated ingredients match the two concrete non-adjustment rows in Togo M897: 920 ml distilled water and 12.32 g MgSO4 x 7 H2O.

The rest of the medium remains unresolved. Modified UBS solution is a 50 ml addition by reference to M896, FeSO4 is a 20 ml 1.0 M post-autoclave solution, and Trace element solution is a 10 ml referenced stock. In the generated record, all three are empty `solutions` entries with their source volumes stored as `G_PER_L`.

The Togo M897 preparation comments are also absent. Those comments carry the pH 2.3 basal-medium adjustment, the filter-sterilized post-autoclave additions, and the JCM 30830 pH 1.7 note.

## Completeness

The generated record is incomplete for Togo M897 and for JCM 860 because the Modified UBS, FeSO4, and trace-element stock additions are not materialized and the preparation comments are missing.

The M897 pH 1.7 target is also missing as structured metadata.

## Findings

1. The 50 ml Modified UBS solution, 20 ml 1.0 M FeSO4 solution, and 10 ml Trace element solution are empty solution stubs instead of nested stock additions.
2. The pH 1.7 target from Togo metadata was not migrated into `ph_value`.
3. The pH 2.3 preparation adjustment and post-autoclave filter-sterilized-addition instruction are absent.
4. MgSO4 x 7 H2O is missing a MediaIngredientMech CHEBI link even though it has the correct primary CHEBI term.

## Recommended Edits

1. Resolve the M897 references to the Modified UBS, FeSO4, and trace-element stocks or merge this split back into the complete JCM 860 representation after stock-aware curation.
2. Preserve the M897 pH 1.7 target and the JCM 860 pH 2.3 preparation instruction distinctly.
3. Replace the empty solution stubs with nested stocks or correctly scaled final solute concentrations.
4. Add a MediaIngredientMech CHEBI link for magnesium sulfate heptahydrate if the corresponding ingredient record exists.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after resolving the stock references.
- Confirm the post-fix record still resolves to `TOGO:M897` if it remains separate.
- Confirm `Modified UBS solution`, `1.0 M FeSO4 solution`, and `Trace element solution` are no longer empty.

## Additional Notes

None found.
