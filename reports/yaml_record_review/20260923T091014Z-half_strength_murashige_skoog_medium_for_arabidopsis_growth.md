# YAML Record Review: half_strength_murashige_skoog_medium_for_arabidopsis_growth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml
- Started UTC: 2026-09-23T09:07:33Z
- Finished UTC: 2026-09-23T09:10:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015433 |
| Name | half_strength_murashige_skoog_medium_for_arabidopsis_growth |
| Original name | Half-strength Murashige-Skoog medium for Arabidopsis growth |
| Category | specialized |
| Generated path | data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml |
| Maintained parent | data/normalized_yaml/specialized/Half_strength_Murashige_Skoog_medium_for_Arabidopsis_growth.yaml |
| Merge fingerprint | f4f564dc3bbc6b904751a943d64e5e8afdcbb7ab975d97f31697faa7e3aa345e |

This is a generated August 2026 merge product imported from CommunityMech
`CommunityMech:000003` and `CommunityMech:000022`. Future edits belong in the
CommunityMech source import, the maintained normalized parent, or the generated
external-match overlay; `data/merge_yaml/merged/` should then be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml --out /private/tmp/half_strength_murashige_skoog_medium_for_arabidopsis_growth.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Failed with 1 error: no cached content was available for `doi:10.1038/nature16192` at `source_data.evidence[0].snippet` |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The record identifies a half-strength Murashige-Skoog medium for Arabidopsis
  growth imported from CommunityMech, not a MediaDive or culture-collection
  medium.
- The DOI `10.1038/nature16192` resolves to the 2015 Nature article
  `Functional overlap of the Arabidopsis leaf and root microbiota`.
- The DOI page contains the imported snippet's broad gnotobiotic Arabidopsis
  statement in the abstract, so the citation is plausible for a gnotobiotic
  Arabidopsis growth system.
- The record claims `physical_state: LIQUID`, but the imported recipe contains
  `Agar` at 0.8% w/v and notes square Petri plates in vertical orientation.
  Those fields describe a solid or semisolid agar plate, not a liquid culture.
- `kg_microbe_match: mediadive.medium:263` is a false cross-source match.
  MediaDive numeric medium `263` is DSMZ `TIBI MEDIUM`, not an Arabidopsis
  half-strength Murashige-Skoog plant-growth medium.

## Evidence

Supported by inspected sources:

- The DOI page supports the article title, DOI identity, and high-level
  gnotobiotic Arabidopsis plant-system evidence snippet.
- The snippet attached in `source_data.evidence[0]` is a near-exact extract from
  the Nature abstract.
- CHEBI `CHEBI:17992` is the correct grounding for sucrose.
- CHEBI `CHEBI:2509` is the correct grounding for agar.
- ENVO `ENVO:00005801` labels the source environment as rhizosphere.

Unsupported, stale, or over-scoped in this generated record:

- The single DOI evidence object does not support 0.5 times Murashige-Skoog
  basal salts, 1.0% w/v sucrose, 0.8% w/v agar, pH 5.7, 22 C, square Petri
  plates, vertical plate orientation, 16 h light/8 h dark, or light intensity
  120.
- The extracted 16-page supplementary PDF for the DOI did not contain the
  searched recipe terms `Murashige`, `MS medium`, `sucrose`, `agar`, `5.7`,
  `120`, `square`, or `vertical`.
- `Murashige-Skoog basal salts` uses `unit: VARIABLE`, leaving the meaning of
  `value: '0.5'` implicit. If the intended unit is half-strength relative to a
  manufacturer formulation, that needs a concentration factor or source note.
- `physical_state: LIQUID` contradicts the agar-containing Petri plate recipe.
- `kg_microbe_match: mediadive.medium:263` is unsupported because MediaDive 263
  is DSMZ TIBI Medium.
- The generated record is stale relative to the maintained parent because it is
  missing `id_lineage_token` and the structured `sources` promoted by the
  September `repair_communitymech_sources_score10_batch10.py` pass.

## Completeness

- The source provenance is incomplete at publication granularity. The record
  names only a DOI and CommunityMech IDs; it does not name a method section,
  table, supplementary data file, or CommunityMech field that supports each
  recipe and incubation field.
- The maintained normalized parent already contains the CommunityMech IDs in
  `sources[]`; regeneration is needed for that September provenance repair to
  reach `data/merge_yaml/merged`.
- An exact `rg --no-ignore --hidden` search for
  `CommunityMech:000003\b|CommunityMech:000022\b|10\.1038/nature16192\b|mediadive\.medium:263\b`
  across `data/merge_yaml` and `data/normalized_yaml` found the target and its
  normalized parent for the CommunityMech IDs and DOI; the same search also
  found unrelated records carrying the same false `kg_microbe_match` to
  `mediadive.medium:263`.
- Empty explicit strain-growth slots are acceptable for the generated record as
  long as the imported CommunityMech community IDs remain available through
  structured `sources[]`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact formulation and growth-condition fields are not backed by the attached DOI evidence. | The DOI abstract supports a gnotobiotic Arabidopsis system, but inspected article HTML and extracted supplementary text did not support the 0.5 times MS salts, sucrose, agar, pH, temperature, vessel, light, or orientation values. | Add claim-specific evidence from CommunityMech or the primary method source to `data/normalized_yaml/specialized/Half_strength_Murashige_Skoog_medium_for_Arabidopsis_growth.yaml`, or repair the CommunityMech importer to preserve those evidence links. |
| Major | `physical_state` contradicts the agar plate formulation. | The record contains 0.8% w/v agar and square Petri plate notes but says `physical_state: LIQUID`. | Correct `physical_state` in the maintained normalized parent to the repository's agar/semisolid value and regenerate. |
| Major | `kg_microbe_match` points to a different medium. | The record says `kg_microbe_match: mediadive.medium:263`; MediaDive numeric medium 263 is DSMZ `TIBI MEDIUM`. | Refresh or repair the external match generation that writes `kg_microbe_match`, then regenerate `data/merge_yaml/merged/`. |
| Major | The generated record is stale relative to its maintained parent. | The maintained parent contains `id_lineage_token` and `sources[]` added on 2026-09-13, but this generated August record lacks both fields. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/specialized/Half_strength_Murashige_Skoog_medium_for_Arabidopsis_growth.yaml`. |
| Minor | The source evidence explanation is an auto-filled placeholder. | `source_data.evidence[0].explanation` says `Auto-filled placeholder: explanation not supplied by upstream import.` | Replace the placeholder in the maintained parent or import mapping after claim-specific evidence is attached. |

## Recommended Edits

1. Replace the broad DOI-level evidence with claim-specific CommunityMech or
   primary-source evidence for the MS salt factor, sucrose, agar, pH,
   temperature, vessel, light regime, light intensity, and vertical orientation
   values.
2. Correct `physical_state` from `LIQUID` to the repository's solid-agar or
   agar-plate value.
3. Replace `unit: VARIABLE` on `Murashige-Skoog basal salts` with an explicit
   half-strength concentration representation or add a source note explaining
   the factor.
4. Remove or recompute the stale `kg_microbe_match: mediadive.medium:263` value
   in the match-generation input or overlay that owns generated
   `kg_microbe_match` values.
5. Regenerate `data/merge_yaml/merged/` so the September `sources[]` repair in
   the maintained normalized parent is present in the generated record.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `half_strength_murashige_skoog_medium_for_arabidopsis_growth` output.
- Re-run the reference validator after adding claim-specific primary evidence;
  it should no longer report unavailable content for the sole DOI-backed
  snippet.
- Inspect the regenerated YAML and confirm it contains `sources[]`, no
  `kg_microbe_match` to `mediadive.medium:263`, a non-liquid `physical_state`,
  and evidence scoped directly to the recipe and environmental-condition
  values.
- Re-fetch DOI `10.1038/nature16192` or any replacement primary source and
  confirm the cited snippets support the exact formula and growth conditions.

## Additional Notes

- Nature's accessible article HTML provided title and abstract metadata; recipe
  verification required checking supplementary material as well.
- The supplementary PDF linked from the Nature page was reachable and extracted
  with `mutool`, but it covered supplementary figures rather than the recipe
  details needed here.
