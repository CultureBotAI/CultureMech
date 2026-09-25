# YAML Record Review: thermoproteus_neutrophilus_medium__dcefca4b

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_neutrophilus_medium__dcefca4b.yaml`
- Started UTC: 2026-09-25T10:39:00Z
- Finished UTC: 2026-09-25T10:42:24Z
- Verdict: needs curation

## Target

- Reviewed generated direct JCM 195 record `CultureMech:002557`.
- Media term: `mediadive.medium:J195`, `THERMOPROTEUS NEUTROPHILUS MEDIUM`.
- Source claims in the record point to JCM Medium 195 through MediaDive.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoproteus_neutrophilus_medium__dcefca4b.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; exited 0 with no diagnostics.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- JCM Medium 195 and MediaDive medium J195 identify Thermoproteus Neutrophilus Medium.
- The JCM source adds 1 L Modified Brock salt base solution and a small set of top-level reductant, carbonate, yeast, sulfur, and indicator additions.
- An exact ignored-inclusive search found the same JCM 195 source represented by this direct import and by TOGO M188.

## Evidence

- `/private/tmp/jcm_195.html` lists Modified Brock salt base solution as a 1 L input to JCM 195.
- `/private/tmp/mediadive_J195.json` keeps Modified Brock salt base solution as MediaDive solution 3819 and records it as a nested component of the main JCM 195 solution.
- `/private/tmp/togo_M188.json` confirms that TOGO M188 is another JCM 195 import, though the TOGO record leaves the Brock base as a reference to M156.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact JCM 195 identifiers, so ignored generated indexes were included.

## Completeness

- The generated record preserves pH 6.5, the top-level JCM additions, and the JCM preparation text.
- Modified Brock salt base has been expanded into top-level basal ingredients, and the record no longer identifies those rows as a nested salt-base solution.
- The source water basis from the Modified Brock salt base is absent.
- Sulfur powder is grounded to sulfur atom rather than elemental sulfur.

## Findings

- The Modified Brock salt base solution hierarchy was lost during the direct MediaDive import.
- Distilled water from the salt base is absent.
- JCM 195 is split across direct JCM and TOGO M188 generated outputs.
- Sulfur powder uses an overly generic sulfur atom grounding.

## Recommended Edits

- Preserve Modified Brock salt base solution as a nested source component, or keep explicit provenance for its expansion into JCM 195.
- Preserve the 1000 ml distilled-water row from the Modified Brock base.
- Reground sulfur powder to elemental sulfur.
- Merge the repaired direct JCM source with repaired TOGO M188 once their normalized representation agrees.

## Follow-up Checks

- Rebuild the merged YAML and confirm Modified Brock salt base has not silently become unqualified top-level salts.
- Re-run schema, strict, reference, and term validation on the regenerated JCM 195 target.
- Re-run exact ignored-inclusive searches for `mediadive.medium:J195` and `TOGO_M188_Thermoproteus_Neutrophilus_Medium`.

## Additional Notes

- An initial local source search for this batch included a speculative `mediadive.medium:88` pattern and matched unrelated Sulfolobus records; I discarded that output and reran the search with exact DSMZ 185 and JCM/NBRC Thermoproteus Neutrophilus IDs.
