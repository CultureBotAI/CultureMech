# YAML Record Review: Sucrose-Bennett's Agar
- Repository: CultureMech
- Record: data/merge_yaml/merged/sucrose_bennetts_agar__5098f2de.yaml
- Started UTC: 2026-09-25T07:42:46Z
- Finished UTC: 2026-09-25T07:42:46Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:010395` / `sucrose_bennetts_agar` from `data/merge_yaml/merged/sucrose_bennetts_agar__5098f2de.yaml`.

The generated record has one source, `TOGO:M96`, imported from JCM medium 104.

## Validation
- Schema validation: Passed with `No issues found`.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
TOGO M96 correctly identifies the underlying source as JCM medium 104, and its formula is the same 15 g/L agar Sucrose-Bennett's Agar formula as `mediadive.medium:J104`.

The exact local search found this TOGO M96 record and a separate generated canonical `sucrose_bennetts_agar.yaml` for the MediaDive J104 import. A first search for `JCM_M104` was too broad because it also matched longer JCM identifiers, and that output was discarded before rerunning with a digit boundary.

## Evidence
The TOGO M96 payload has source `JCM_M104`, pH 7.3, and six main-solution rows: 1 L distilled water, 10 g sucrose, 15 g agar, 1 g yeast extract from BD-Difco, 2 g N-Z amine type A from Sheffield, and 1 g beef extract from BD-Difco.

The JCM 104 page and the MediaDive J104 payload report the same recipe per liter: 1 g/L yeast extract, 1 g/L beef extract, 2 g/L N-Z amine type A, 10 g/L sucrose, 15 g/L agar, 1 L distilled water, and pH adjustment to 7.3.

## Completeness
The generated TOGO ingredient list has the correct non-water mass concentrations.

The generated water row is wrong because TOGO's 1 L water row was imported as 1 `G_PER_L`. The generated record also drops pH 7.3 even though it is present in TOGO metadata and the JCM page.

This record is an unmerged duplicate of the canonical MediaDive J104 generated record. The records did not merge because TOGO retained branded ingredient labels such as `Yeast extract (BD-Difco)` and `N--Z amine, type A (Sheffield)` and represented water differently.

## Findings
- The main Sucrose-Bennett ingredient masses match JCM 104.
- The 1 L distilled-water row is represented as 1 g/L.
- The pH 7.3 target is missing.
- The same JCM 104 recipe exists in the generated tree under `mediadive.medium:J104`, so this TOGO source should be deduplicated after label and water normalization.

## Recommended Edits
- Fix `data/normalized_yaml/bacterial/TOGO_M96_Sucrose-Bennett_s_Agar.yaml` or the TOGO import logic, then regenerate `data/merge_yaml/merged/sucrose_bennetts_agar__5098f2de.yaml`; do not hand-edit the generated merged YAML.
- Convert 1 L distilled water into volume metadata rather than a 1 g/L final ingredient.
- Restore `ph_value: 7.3` from TOGO or JCM.
- Normalize the branded yeast extract, beef extract, and N-Z amine labels enough for this source to merge with the MediaDive J104 Sucrose-Bennett canonical record.

## Follow-up Checks
- Confirm the regenerated TOGO M96 source no longer has a 1 g/L water row.
- Confirm pH 7.3 is present.
- Confirm TOGO M96 and MediaDive J104 share a duplicate fingerprint after water and label normalization.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The final exact local search for `TOGO:M96`, `JCM_M104`, `CultureMech:010395`, and `mediadive.medium:J104` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.
