# YAML Record Review: Histidine salt; schaechter et al
- Repository: CultureMech
- Record: data/merge_yaml/merged/histidine_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-23T12:12:59Z
- Finished UTC: 2026-09-23T12:13:38Z
- Verdict: needs curation

## Target

Reviewed the generated MediaDB branch for MediaDB Medium 234, `Histidine salt; schaechter et al`, at `data/merge_yaml/merged/histidine_salt_schaechter_et_al.yaml`. The maintained source is `data/normalized_yaml/bacterial/histidine_salt_schaechter_et_al.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/histidine_salt_schaechter_et_al.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The `MEDIADB:234` grounding and label match the MediaDB 234 page for `Histidine salt; schaechter et al`. MediaDB connects this formulation to Salmonella enterica Typhimurium LT2 and to Schaechter et al. 1958, with PubMed link 13611202.

## Evidence

MediaDB 234 lists exactly six compound rows and reports the same millimolar amounts imported into the record: L-Histidine 2.57815 mM, Citrate 5.20497 mM, Dibasic sodium phosphate 28.0899 mM, Potassium chloride 9.92605 mM, Magnesium sulfate 0.405729 mM, and Sodium ammonium phosphate 8.32187 mM.

The CHEBI groundings are either supported by the MediaDB tab-delimited page or reasonable local improvements where MediaDB is more specific than the displayed component name. MediaDB does not assign a CHEBI ID to Sodium ammonium phosphate, and the record correctly leaves that ingredient ungrounded instead of inventing a near match.

## Completeness

The ingredient table is complete relative to MediaDB 234. The source exposes the associated organism and primary source, but this record type has no narrow slot for them. MediaDB 234 does not state pH, solvent, sterilization, or preparation details.

## Findings

- The `FILTER_STERILIZE` preparation step claims 0.22 um filtration and heat-sensitive-component handling that is not stated on the MediaDB 234 page.
- The `ADJUST_PH` step is a generic placeholder that says to adjust pH if specified, but MediaDB 234 has no pH value.
- The `DISSOLVE` step uses generic distilled-water wording that is not present in the MediaDB source.
- The curation-history import note cites Mazumdar et al. 2014, while MediaDB 234 cites Schaechter et al. 1958 as the actual formulation source.

## Recommended Edits

- Remove the synthetic preparation workflow from `data/normalized_yaml/bacterial/histidine_salt_schaechter_et_al.yaml`, or replace it with source-backed MediaDB preparation text if a maintained importer later captures one.
- Keep Sodium ammonium phosphate ungrounded unless a curator verifies an exact ontology term from a primary chemistry source.
- Clarify the MediaDB import provenance so the record distinguishes the MediaDB database citation from the Schaechter et al. 1958 source attached to Medium 234.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open MediaDB Medium 234 and its tab-delimited view to confirm the six millimolar amounts are unchanged.
- Re-open MediaDB Source 84 to confirm Schaechter et al. remains the source linked to Medium 234.

## Additional Notes

None.
