# YAML Record Review: Sulfolobus Medium-D

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_d.yaml` (`CultureMech:002486`)
- Started UTC: `2026-09-25T08:11:31Z`
- Finished UTC: `2026-09-25T08:11:54Z`
- Verdict: pass with minor issues

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_d.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfolobus_medium_d.yaml` |
| CultureMech ID | `CultureMech:002486` |
| Media term | `mediadive.medium:J1322` |
| Original source | JCM Medium J1322, Sulfolobus Medium-D |
| Merge fingerprint | `bb48476cb45cbf41d58468e7d08b8ab58219e02d86949172ff58f6abdeefc1dd` |
| Merged from | `sulfolobus_medium_d` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:002486` identifier, `mediadive.medium:J1322` source term, JCM Medium J1322 identity, and pH 4.5 value. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:002486`, `mediadive.medium:J1322`, the merge fingerprint, and `sulfolobus_medium_d.yaml` found this normalized source and generated merge as the only direct recipe records.

The ingredient groundings are plausible for the MediaDive payload: yeast extract, tryptone, ammonium sulfate, KH2PO4, hydrate-specific MgSO4, CaCl2, FeCl3, MnCl2, Na2B4O7, ZnSO4, CuCl2, Na2MoO4, VOSO4 hydrate, and CoSO4 x 7 H2O are all represented with matching final concentrations.

The exact JCM `GRMD=1322` URL stored in the source note currently returns a JCM page with `Nothing found`, so the live JCM page could not be used to verify J1322 directly. The MediaDive REST payload still resolves `J1322` as a JCM-sourced Sulfolobus Medium-D record.

## Evidence

MediaDive J1322 models the main solution as 1000 ml of Modified Brock's salt base solution, 1 g yeast extract, 1 g tryptone, and a pH adjustment to 4.5 with H2SO4. The referenced Modified Brock's salt base contains 1.3 g ammonium sulfate, 0.28 g KH2PO4, 0.25 g MgSO4 x 7 H2O, 0.07 g CaCl2 x 2 H2O, 2 mg FeCl3 x 6 H2O, 1.8 mg MnCl2 x 4 H2O, 4.5 mg Na2B4O7 x 10 H2O, 0.22 mg ZnSO4 x 7 H2O, 0.05 mg CuCl2 x 2 H2O, 0.03 mg Na2MoO4 x 2 H2O, 0.03 mg VOSO4 x n H2O, 0.01 mg CoSO4 x 7 H2O, and 1 L distilled water.

The generated YAML preserves the non-water ingredients at the MediaDive `g_l` concentrations and records the pH 4.5 H2SO4 adjustment. It flattens the Modified Brock's salt base into the top-level list and omits the source water row.

## Completeness

The generated record is mostly complete for a flat representation of MediaDive J1322. The only recipe detail lost is the explicit `Modified Brock's salt base solution` wrapper and its 1 L water row.

`target_organisms` is absent. The MediaDive and JCM recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- The direct JCM `GRMD=1322` URL in `notes` currently resolves to a `Nothing found` page.
- The 1000 ml Modified Brock's salt base solution is flattened into top-level ingredients, and the 1 L distilled-water row is omitted.

## Recommended Edits

- Re-check JCM Medium J1322 and update the source link if JCM has moved or removed the `GRMD=1322` page.
- If source hierarchy is preserved for JCM referenced media in a future generator pass, keep J1322 as 1000 ml of Modified Brock's salt base plus 1 g/L yeast extract, 1 g/L tryptone, and final pH 4.5.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation if the normalized source or generated YAML changes.
- Re-run exact gitignore-independent searches for `CultureMech:002486`, `mediadive.medium:J1322`, `bb48476cb45cbf41d58468e7d08b8ab58219e02d86949172ff58f6abdeefc1dd`, and `sulfolobus_medium_d.yaml`.
- Confirm a replacement JCM 1322 URL, if any, still matches the MediaDive J1322 ingredient list.

## Additional Notes

Empty optional fields that are unrelated to source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized MediaDive source and any future source-link refresh.
