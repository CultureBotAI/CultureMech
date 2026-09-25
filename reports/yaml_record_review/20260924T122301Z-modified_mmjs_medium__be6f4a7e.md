# YAML Record Review: modified_mmjs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_mmjs_medium__be6f4a7e.yaml
- Started UTC: 2026-09-24T12:23:01Z
- Finished UTC: 2026-09-24T12:23:01Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002858`, `modified_mmjs_medium`, generated from `data/normalized_yaml/bacterial/modified_mmjs_medium.yaml`.
- The record represents JCM Medium J508 / MediaDive `mediadive.medium:J508`, named `MODIFIED MMJS MEDIUM`.
- The generated record was compared with the maintained MediaDive normalized record, JCM `GRMD=508`, MediaDive `J508`, and the parallel TOGO `M509` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J508`, JCM `GRMD=508`, and TOGO `M509` all identify the same JCM recipe for Modified MMJS Medium.
- A gitignore-independent duplicate check for the exact normalized name and JCM/MediaDive identifiers found a second maintained record, `data/normalized_yaml/bacterial/TOGO_M509_Modified_MMJS_Medium.yaml`, and a second generated record, `data/merge_yaml/merged/MODIFIED_MMJS_MEDIUM.yaml`.
- `data/normalized_yaml/bacterial/modified_mmjs_medium_b.yaml` is a different record for JCM `J592` and was not treated as a duplicate of the reviewed JCM `J508` record.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists NaCl, K2HPO4, KH2PO4, CaCl2 x 2 H2O, NH4Cl, NaNO3, MgSO4 x 7 H2O, MgCl2 x 6 H2O, KCl, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Fe2(SO4)3 x n H2O, H2WO4, Na2S2O3 x 5 H2O, 3 g sulfur powder, 10 ml Trace mineral solution, 1 ml Trace vitamins, 2 g NaHCO3, and 1 L distilled water.
- The JCM table names the Trace mineral solution as a local cross-reference that should use Medium No. 413 with 0.01 g/L final Na2MoO4 x 2 H2O.
- MediaDive `J508` preserves the same main recipe and carries the 10 ml Trace mineral solution as solution `4286` with the same Medium No. 413 instruction in a solution step.
- MediaDive `J508` also carries the 1 ml Trace vitamins addition as solution `3861`, a 1000 ml vitamin stock recipe.
- The generated YAML lacks a structured 10 ml Trace mineral solution addition and flattens the 1 ml Trace vitamins stock into top-level ingredient rows at stock concentrations.

## Completeness

- Main salts, sulfur, sodium thiosulfate pentahydrate, and sodium bicarbonate are present.
- The 10 ml Trace mineral solution cross-reference is present only in a preparation step and is missing as a structured addition.
- The 1 ml Trace vitamins addition is missing as a structured addition; its stock components are flattened into the main ingredient list.
- The 1 L main-water row and the 1000 ml Trace vitamins water row are absent.
- The generated sulfur row keeps the source mass but grounds `Sulfur (powder)` to `CHEBI:26833`, `sulfur atom`, rather than elemental sulfur.

## Findings

- Blocker: the structured 10 ml Trace mineral solution addition was dropped from `ingredients`. Because that solution is defined only by a JCM cross-reference plus a Medium No. 413 molybdate adjustment, dropping the solution row loses the amount and makes the recipe impossible to reconstruct from structured data.
- Blocker: the 1 ml Trace vitamins stock is flattened into top-level ingredients at 1 L stock strength. The generated 0.002 g/L biotin, 0.002 g/L folic acid, and companion vitamin rows are stock concentrations, not direct main-medium additions.
- Major: source water rows are omitted for the main recipe and the Trace vitamins stock, obscuring the recipe scopes that distinguish the 1 L base from the nested 1 L stock.
- Major: `Sulfur (powder)` is grounded to `CHEBI:26833` with the label `sulfur atom`; the source ingredient is elemental sulfur powder.
- Major: the same JCM 508 medium is maintained under two CultureMech IDs, `CultureMech:002858` for MediaDive and `CultureMech:009899` for TOGO, and it generates two separate merged YAML records.

## Recommended Edits

- Preserve the 10 ml Trace mineral solution row as a structured solution addition, including the note to use JCM Medium No. 413 with 0.01 g/L final Na2MoO4 x 2 H2O.
- Preserve the 1 ml Trace vitamins row as a structured solution addition or nested stock recipe rather than flattening vitamin stock components into the top-level ingredients.
- Keep the 1 L base water and 1000 ml Trace vitamins water rows if water rows are in scope for structured recipes.
- Re-ground the sulfur powder row to elemental sulfur, for example `CHEBI:33403`, after confirming the preferred local grounding for source `Sulfur (powder)`.
- Merge or explicitly cross-link the MediaDive `J508` and TOGO `M509` maintained records before regeneration so JCM `GRMD=508` has a single CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting the MediaDive import or normalized YAML.
- Recompare regenerated structured solution rows against JCM `GRMD=508`, including the Medium No. 413 trace-mineral cross-reference and the 1 ml Trace vitamins addition.
- Confirm that generated YAML no longer contains both `modified_mmjs_medium__be6f4a7e.yaml` and `MODIFIED_MMJS_MEDIUM.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
