# YAML Record Review: caulobacter_pye_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml
- Started UTC: 2026-09-22T06:21:30Z
- Finished UTC: 2026-09-22T06:24:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| class | MediaRecipe |
| id | CultureMech:000928 |
| name | caulobacter_pye_medium |
| category | bacterial |
| generated path | data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml |
| generated status | Derived singleton from `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml` |
| media term | `mediadive.medium:1462`, DSMZ Medium 1462 / CAULOBACTER PYE MEDIUM |
| merge fingerprint | `d09c2c93c2e777054bfb8f6d3e68ab99986b50dd95b4baa5ca2c79c223847603` |

This generated record is a one-record merge: `merged_from` contains only `caulobacter_pye_medium`, and its maintained owner is `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml`.

`find data -iname '*pye*' -print` found the Caulobacter PYE target among many similarly named PYE and PYES records under `data/merge_yaml/merged`, `data/normalized_yaml/bacterial`, and `data/normalized_yaml/specialized`. The search covered ignored files because `find` does not honor `.gitignore`; no other local record shared `CultureMech:000928` or `mediadive.medium:1462`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml --out /private/tmp/CAULOBACTER_PYE_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| Reference integrity | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 checks, all validations passed. |
| Term labels | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only an `eutils` / `pkg_resources` deprecation warning was emitted. |
| Embedded history | Not checked | `just validate-history` validates standalone `history/*.yaml` files, not embedded `MediaRecipe.curation_history` blocks. |

## Identity and Grounding

The primary source identity is correct: DSMZ Medium 1462 and MediaDive medium 1462 are CAULOBACTER PYE MEDIUM. The generated `media_term` points to `mediadive.medium:1462`, and the source URL in the maintained normalized owner resolves to the DSMZ Medium 1462 PDF.

One cross-reference is wrong: the generated record carries `kg_microbe_match: mediadive.medium:49`. MediaDive medium 49 is C/10 MEDIUM with Casitone, CaCl2 x 2 H2O, Agar, and Distilled water at pH 7.2. It is not Caulobacter PYE Medium 1462.

Ingredient groundings for calcium chloride dihydrate (`CHEBI:86158`) and agar (`CHEBI:2509`) match the inspected source rows. Peptone and Yeast extract are intentionally ungrounded undefined complex ingredients.

## Evidence

| Claim | Status |
|---|---|
| DSMZ / MediaDive Medium 1462 identity | Supported by the inspected DSMZ PDF and MediaDive JSON. |
| Peptone 2 g/L | Supported by DSMZ and MediaDive. |
| Yeast extract 1 g/L | Supported by DSMZ and MediaDive, but the MediaDive `attribute: Difco` qualifier is not retained. |
| CaCl2 x 2 H2O 0.07 g/L | Supported for the liquid formulation. The DSMZ preparation text says calcium chloride is added from a sterilized stock after autoclaving and also says not to add supplemental calcium for agar media. |
| Agar 12 g/L for solid medium | Supported as optional solid-medium agar. |
| pH 7.0 | Supported by DSMZ step 2 and by MediaDive `min_pH: 7`, `max_pH: 7`. |
| `kg_microbe_match: mediadive.medium:49` | Unsupported; MediaDive 49 is C/10 MEDIUM, not CAULOBACTER PYE MEDIUM. |

## Completeness

The formulation is nearly source-complete but loses two source details:

- The maintained and generated records omit `Distilled water 1000 ml`. MediaDive does not expose a `g_l` value for water, so this must remain a volume / final-volume preparation row rather than being recast as `1000 G_PER_L`.
- The source says `Yeast extract (Difco)`; the record keeps only `Yeast extract`.

The record correctly leaves target organisms, incubation temperature, salinity, atmosphere, and storage empty because the inspected DSMZ and MediaDive recipe for medium 1462 do not provide those values.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | The record denotes a solid-agar medium while keeping the liquid-only calcium chloride addition. | `physical_state: SOLID_AGAR` and `Agar` 12 g/L make the record the agar form, but the ingredient list also includes CaCl2 x 2 H2O 0.07 g/L. DSMZ Medium 1462 says calcium chloride is post-autoclave stock for the base formulation and that agar media should not receive supplemental calcium. | Split or variant-model `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml` so the liquid PYE parent has calcium chloride and the solid-agar variant has agar without supplemental calcium; then regenerate `data/merge_yaml/merged/`. |
| major | `kg_microbe_match` points to the wrong MediaDive medium. | The generated record's `media_term.term.id` is `mediadive.medium:1462`, while `kg_microbe_match` is `mediadive.medium:49`. MediaDive 49 resolves to C/10 MEDIUM, and local indexes map `mediadive.medium:49` to `data/normalized_yaml/bacterial/c_10_medium.yaml`. | Remove the stale `kg_microbe_match` from `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml` or replace it only with a checked exact CultureMech/KG-Microbe match. Audit `scripts/enrich_with_kg_microbe_matches.py` output or the historical match table if this was not manually introduced. |
| minor | The solvent / final volume is missing. | DSMZ Medium 1462 lists Distilled water 1000.00 ml, and MediaDive stores `amount: 1000`, `unit: ml`, `g_l: null`; the YAML does not represent this source row. | Add a supported water/final-volume representation to the maintained MediaDive owner without inventing a mass concentration. |
| minor | The Yeast extract supplier qualifier is missing. | DSMZ writes `Yeast extract (Difco)`, and MediaDive stores `attribute: Difco`; the YAML keeps only `preferred_term: Yeast extract`. | Preserve `Difco` as a note or source attribute when MediaDive ingredient attributes are retained. |

## Recommended Edits

1. Remodel `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml` so liquid and solid-agar PYE are not flattened into one formula containing both supplemental CaCl2 x 2 H2O and agar.
2. Delete or correct `kg_microbe_match: mediadive.medium:49`; this record should not claim identity with C/10 MEDIUM.
3. Restore the DSMZ / MediaDive `Distilled water 1000 ml` and `Difco` yeast-extract qualifier in the maintained owner if the project intends to preserve source solvent and supplier rows.
4. Regenerate `data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml` from the maintained owner.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation against `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml` and the regenerated `data/merge_yaml/merged/CAULOBACTER_PYE_MEDIUM.yaml`.
- Re-read DSMZ Medium 1462 and confirm the regenerated solid-agar variant has Agar 12 g/L and no supplemental calcium.
- Search with `rg --no-ignore --hidden -n "mediadive.medium:49|kg_microbe_match: mediadive.medium:49" data src scripts reports` and confirm no remaining non-C/10 record points at MediaDive 49.

## Additional Notes

- `rg --no-ignore --hidden -n "CAULOBACTER_PYE_MEDIUM|Caulobacter PYE|CAULOBACTER PYE|caulobacter_pye|Medium 1462|mediadive.medium:1462|CultureMech:000928" data src scripts reports` covered ignored files while resolving the generated target, maintained singleton owner, indexes, and old validation archives.
- `data/curation/organism_candidates.json` contains a stale organism-candidate row derived from the words CAULOBACTER PYE. I did not treat that as a target-organism defect because no target-organism claim from that candidate was applied to the maintained YAML.
