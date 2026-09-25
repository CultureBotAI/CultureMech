# YAML Record Review: modified_sap2_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_sap2_medium__8615ab3d.yaml
- Started UTC: 2026-09-24T13:01:24Z
- Finished UTC: 2026-09-24T13:02:11Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:010379`, `modified_sap2_medium`, generated from `data/normalized_yaml/bacterial/TOGO_M955_Modified_SAP2_Medium.yaml`.
- The record represents TOGO `M955`, sourced from JCM `JCM_M910-2`, named `Modified SAP2 Medium`.
- The generated TOGO record was compared with TOGO `M955`, JCM `GRMD=910`, and the maintained normalized YAML that already resolves the source cross-reference.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M955` points to JCM `JCM_M910-2`, which uses JCM Medium 651 with 1.0 x artificial seawater and omits agar for liquid medium.
- A gitignore-independent exact search for `TOGO:M955`, `JCM_M910-2`, and `GRMD=910` found this branch plus related SAP2 branches for the same JCM page, including a TOGO `M954` branch and a MediaDive branch.
- The maintained M955 YAML grounds Tryptone to MICRO:0000182 and Yeast extract to FOODON:03315426, but the generated record drops both terms.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM `GRMD=910` says to use Medium 651 with 1.0 x artificial seawater instead of 0.5 x artificial seawater and to omit agar for liquid medium.
- TOGO `M955` preserves the 1.0 x Artificial seawater cross-reference to `M954`.
- The maintained normalized record resolves M955 by preserving 1.0 x Artificial seawater as a 1 L solution, grounding the two BD nutrient rows, setting pH 7.0, adding preparation steps for the SAP2 cross-reference, and recording references to TOGO `M955`, JCM `GRMD=910`, and JCM `GRMD=651`.

## Completeness

- The Yeast extract and Tryptone rows are present.
- The 1.0 x Artificial seawater cross-reference is present only as an empty `solutions` stub with a `G_PER_L` concentration.
- The curated 1 L solution volume, pH 7.0, preparation steps, references, top-level explanatory notes, and data quality flags are absent.

## Findings

- Blocker: the 1.0 x Artificial seawater source cross-reference is emitted as an empty solution with `1` `G_PER_L` instead of the maintained 1 L solution addition.
- Major: merge generation drops already-curated cross-reference resolution fields, including `ph_value: 7.0`, `preparation_steps`, `references`, `data_quality_flags`, and source-resolving top-level `notes`.
- Major: generated Yeast extract and Tryptone rows lose their maintained FOODON and MICRO grounding.

## Recommended Edits

- Preserve maintained `solutions` entries with literal `L` units during merge generation.
- Preserve maintained pH, preparation steps, references, top-level notes, and data quality flags from cross-reference repairs.
- Preserve curated ontology grounding for Yeast extract and Tryptone.
- Keep the link from 1.0 x Artificial seawater to the curated artificial-seawater stock instead of emitting an empty generic solution.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after fixing cross-reference field preservation.
- Recompare the regenerated record against `data/normalized_yaml/bacterial/TOGO_M955_Modified_SAP2_Medium.yaml`, TOGO `M955`, JCM `GRMD=910`, and JCM `GRMD=651`.
- Confirm with a gitignore-independent exact identifier search that TOGO `M955` remains distinct from related SAP2 JCM 910 branches.

## Additional Notes

None found.
