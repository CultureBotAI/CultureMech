# YAML Record Review: SULFOBACILLUS medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfobacillus_medium__128cc833.yaml` (`CultureMech:006248`)
- Started UTC: `2026-09-25T08:00:57Z`
- Finished UTC: `2026-09-25T08:01:50Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfobacillus_medium__128cc833.yaml` |
| Normalized sources | `data/normalized_yaml/bacterial/KOMODO_665_SULFOBACILLUS_medium.yaml`; `data/normalized_yaml/bacterial/KOMODO_1023_MANNING_medium.yaml`; `data/normalized_yaml/bacterial/sulfobacillus_medium.yaml` |
| CultureMech ID | `CultureMech:006248` |
| Media term | `komodo.medium:665` |
| Source family | KOMODO 665, DSMZ/MediaDive 665, and KOMODO 1023 Manning medium |
| Merge fingerprint | `128cc83369b573b90cf1945180515c4989ab3406b3a6c8643493592858a15ace` |
| Merged from | `KOMODO_1023_MANNING_medium`; `KOMODO_665_SULFOBACILLUS_medium`; `sulfobacillus_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record identifies as KOMODO Medium 665 copied from DSMZ/MediaDive 665, but it also merged KOMODO 1023 Manning medium as though it were an exact duplicate. That conflicts with the maintained normalized records: `KOMODO_1023_MANNING_medium.yaml` and `sulfobacillus_medium.yaml` already describe the Manning/Sulfobacillus pair as a `CONCENTRATION_VARIANT`, not a `SOURCE_DUPLICATE`.

Exact gitignore-independent searches with `--no-ignore --hidden` for `komodo.medium:665`, `KOMODO_665`, `KOMODO_1023`, `MANNING_medium`, `sulfobacillus_medium`, and `CultureMech:006248` found the generated over-merge, the DSMZ 665/MediaDive parent, KOMODO 1023, and a separate DSMZ 969 Sulfobacillus Medium that shares the slug but has a different formula and must stay out of this cluster.

The ingredient groundings are plausible; the defect is variant identity and formula provenance, not ChEBI mapping.

## Evidence

The DSMZ/MediaDive 665 source uses three solutions: 700 ml Solution A with ammonium sulfate, KCl, K2HPO4, MgSO4*7H2O, and Ca(NO3)2; 301 ml Solution B with FeSO4*7H2O plus 10 N H2SO4; and 20 ml Solution C containing 1% yeast extract. It gives final medium pH 1.9-2.4, asks for Solution A pH 2.0-2.2 with sulfuric acid, and says Solution B should be filter sterilized or handled under N2 before autoclaving.

The maintained KOMODO 665 normalized record matches the DSMZ/MediaDive 665 final-concentration import, including `FeSO4 x 7 H2O` at `146.844 G_PER_L`. The generated YAML instead has `FeSO4 x 7 H2O` at `33.4 G_PER_L` and all other mineral rows at the KOMODO 1023 Manning concentrations.

KOMODO 1023 Manning medium is documented locally as a concentration variant of the Sulfobacillus medium family with a different pH range and a different mineral/FeSO4 concentration axis. The generated record nevertheless keeps `CultureMech:006248`, `komodo.medium:665`, and a `parent_media` claim of exact DSMZ 665 provenance while carrying Manning's formula rows.

## Completeness

The generated record is incomplete because the DSMZ 665 stock-combination steps were dropped, and internally inconsistent because the primary media term no longer matches the merged ingredient values.

`target_organisms` is absent. The fetched DSMZ/MediaDive 665 source provides a medium recipe but not a source-backed growth organism for this record.

## Findings

- KOMODO 1023 Manning medium was merged into the KOMODO 665/DSMZ 665 exact-duplicate cluster even though it is a concentration variant.
- The generated `CultureMech:006248` record now carries Manning concentrations (`6 G_PER_L` ammonium sulfate, `0.2 G_PER_L` KCl, `0.2 G_PER_L` K2HPO4, `1 G_PER_L` MgSO4*7H2O, `0.02 G_PER_L` Ca(NO3)2, and `33.4 G_PER_L` FeSO4*7H2O) under the KOMODO 665 media term.
- DSMZ 665/MediaDive 665 final concentrations from `sulfobacillus_medium.yaml`, including `146.844 G_PER_L` FeSO4*7H2O and `1 G_PER_L` 10 N H2SO4, are absent from the generated YAML.
- `H2SO4` is `VARIABLE` in the generated record despite the DSMZ/MediaDive parent carrying a concrete 1 ml 10 N sulfuric-acid addition in Solution B and a pH-adjustment role for Solution A.
- DSMZ preparation steps for Solution A pH adjustment, Solution B iron oxidation avoidance, autoclaving, and combining the three solutions are absent.
- The generated `parent_media` relationship says the KOMODO 665 row exactly matches the DSMZ 665 parent signature, but the ingredient list reflects KOMODO 1023 Manning instead.

## Recommended Edits

- Repair the merge inputs or merge logic so KOMODO 1023 remains a `CONCENTRATION_VARIANT` and is not merged into the exact-duplicate cluster for KOMODO 665/DSMZ 665.
- Regenerate `data/merge_yaml/merged/sulfobacillus_medium__128cc833.yaml` from only `KOMODO_665_SULFOBACILLUS_medium.yaml` and `sulfobacillus_medium.yaml`, unless another source has the exact DSMZ 665 fingerprint.
- Restore the DSMZ/MediaDive 665 final concentrations for `CultureMech:006248`, including `FeSO4 x 7 H2O` at `146.844 G_PER_L`.
- Preserve the DSMZ 665 three-solution preparation steps or model Solution A/B/C explicitly where the schema supports it.
- Preserve the fixed 10 N H2SO4 Solution B addition and sulfuric-acid pH-adjustment note instead of falling back to a variable H2SO4 row.
- Keep DSMZ 969 separate despite sharing the `sulfobacillus_medium` slug.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `komodo.medium:665`, `KOMODO_665`, `KOMODO_1023`, `MANNING_medium`, `sulfobacillus_medium`, and `CultureMech:006248` to confirm only exact DSMZ 665 duplicates merge.
- Compare regenerated KOMODO 665 against DSMZ/MediaDive 665 and compare KOMODO 1023 against its Manning source to ensure the documented concentration-variant relationship survives.

## Additional Notes

Empty optional fields that are unrelated to source-backed organism targets were not treated as defects.

The generated YAML should not be hand-edited. The review findings target duplicate resolution and regeneration from the maintained KOMODO and MediaDive normalized sources.
