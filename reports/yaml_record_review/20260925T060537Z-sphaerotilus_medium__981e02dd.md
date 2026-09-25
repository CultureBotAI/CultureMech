# YAML Record Review: sphaerotilus_medium__981e02dd

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerotilus_medium__981e02dd.yaml
- Started UTC: 2026-09-25T06:04:10Z
- Finished UTC: 2026-09-25T06:05:38Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO M618 / JCM Medium 610, Sphaerotilus Medium.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/sphaerotilus_medium__981e02dd.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The TOGO identity is correct: M618 imports JCM Medium 610, SPHAEROTILUS MEDIUM. The generated record predates the repaired `JCM_J610_SPHAEROTILUS_MEDIUM.yaml` source duplicate and is still a one-source TOGO merge.

Glycerol is correctly grounded to CHEBI:17754. The repaired normalized TOGO and JCM records also ground tryptone, yeast extract, agar, and water and preserve nutritional and solidifying roles.

## Evidence

TOGO M618 and the JCM Medium 610 page both list 0.5 g Tryptone (BD-Difco), 1.0 g glycerol, 0.1 g Yeast extract (BD-Difco), 10.0 g agar if needed, 1.0 L distilled water, and pH adjustment to 7.0. JCM also states that media should be autoclaved at 121 C for 15 minutes unless otherwise stated.

## Completeness

The generated record preserves all non-water source masses and the optional wording for agar. It omits pH 7.0, the JCM autoclave metadata, and the MediaDive/JCM J610 source duplicate, and it imports distilled water with the wrong unit.

## Findings

- Critical: `Distilled water` is modeled as `1` `G_PER_L`; TOGO and JCM specify 1.0 L distilled water.
- Major: pH 7.0 and the JCM default autoclaving instruction are missing from the generated record.
- Major: the generated file is stale relative to the repaired normalized records and does not merge the equivalent MediaDive/JCM J610 source duplicate.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/sphaerotilus_medium__981e02dd.yaml` from the repaired TOGO M618 and MediaDive/JCM J610 normalized records.
- Preserve the 1.0 L distilled-water row, pH 7.0, JCM autoclave metadata, and source references from the repaired normalized YAML.
- Confirm the regenerated output records the TOGO M618 to JCM J610 SOURCE_DUPLICATE relationship.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated merged record.
- Confirm `Distilled water` no longer appears as `1` `G_PER_L`.
- Confirm the regenerated merge contains both `TOGO_M618_Sphaerotilus_Medium` and `JCM_J610_SPHAEROTILUS_MEDIUM` provenance.

## Additional Notes

None found.
