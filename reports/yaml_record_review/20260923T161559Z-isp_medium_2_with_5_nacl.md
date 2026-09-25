# YAML Record Review: isp_medium_2_with_5_nacl

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml`
- Started UTC: 2026-09-23T16:14:20Z
- Finished UTC: 2026-09-23T16:16:01Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:006155` |
| Label | `isp_medium_2_with_5_nacl` |
| Source term | `komodo.medium:636`, `ISP medium 2 WITH 5% NaCl` |
| Source duplicate owner | `data/normalized_yaml/bacterial/KOMODO_636_ISP_medium_2_WITH_5_NaCl.yaml` |
| DSMZ owner | `data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml` |
| Strain-specific KOMODO owners | `medium_636_modified_for_dsm_14598.yaml`, `medium_636_modified_for_dsm_18447.yaml`, `medium_636_modified_for_dsm_45264.yaml` |
| Generated target | `data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml` |

This generated record merges KOMODO Medium 636, the direct DSMZ Medium 636
record, and three KOMODO strain-specific copies of the same DSMZ formula. The
merge is identity-preserving: all five maintained owners have the same
ingredient signature and point back to DSMZ Medium 636.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml` | Passed with `No issues found`. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml --out /private/tmp/isp_medium_2_with_5_nacl.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the configured reference pass performed 0 checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` validator | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not the embedded `MediaRecipe.curation_history` block in generated YAML. |

## Identity and Grounding

The generated record denotes DSMZ Medium 636 exactly, even though KOMODO
Medium 636 is the primary `media_term`. The primary KOMODO owner states `DSMZ
Medium: 636`, the direct MediaDive/DSMZ owner uses `mediadive.medium:636`, and
the three strain-specific KOMODO sources are all `SOURCE_DUPLICATE` children
with the same five ingredients.

DSMZ and MediaDive agree on the formula identity: `ISP MEDIUM 2 WITH 5% NaCl`,
pH 7.3 to 7.5, 4 g/L yeast extract, 10 g/L malt extract, 4 g/L dextrose,
20 g/L agar, and 50 g/L NaCl.

An ignored-file-inclusive exact `rg` for `komodo.medium:636`,
`komodo.medium:636_14598`, `komodo.medium:636_18447`,
`komodo.medium:636_45264`, and `mediadive.medium:636` under
`data/normalized_yaml`, `data/merge_yaml/merged`, and
`reports/yaml_record_review` found the five expected normalized owners, this
generated target, and generated JSON indexes; it did not find another
same-accession owner outside those paths.

## Evidence

The ingredients, amounts, units, physical state, and pH range are supported by
MediaDive's current Medium 636 REST response and the DSMZ Medium 636 PDF. NaCl
is correctly kept at `50 G_PER_L`, so this is a 5% NaCl agar rather than one of
the unrelated ISP-2 10% or 15% salt variants elsewhere in the corpus.

The KOMODO and strain-specific KOMODO owners all say they copied DSMZ Medium
636 and have the same five ingredient rows as the DSMZ owner. The generated
merge therefore collapses true source duplicates, not salinity variants.

Two low-risk source details are absent. DSMZ specifies 1000 ml distilled water,
but neither the DSMZ owner nor the generated target has a water row. DSMZ also
qualifies yeast extract, malt extract, and dextrose as Difco ingredients; those
supplier qualifiers are not preserved in the ingredient rows.

## Completeness

`target_organisms` and `growth_metrics` can remain empty. The inspected
MediaDive and DSMZ sources define the medium formula, not strain-specific
growth outcomes for DSM 14598, DSM 18447, DSM 45264, or any other isolate.

The generated `SOURCE_DUPLICATE` links are plausible and complete enough for
the five inspected owners. The direct DSMZ record is retained as `parent_media`
for the primary KOMODO record, and the three strain-specific KOMODO records
are retained as source-duplicate children/synonyms.

The exact `find reports/yaml_record_review -maxdepth 1 -name
'*isp_medium_2_with_5_nacl*.md'` search included ignored files and found no
pre-existing report for this generated stem before this report was created.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Minor | DSMZ's 1000 ml distilled-water row is absent. | MediaDive and the DSMZ PDF list `Distilled water` at 1000 ml for Medium 636; all maintained owners and the generated merge omit it. | `data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml` or the MediaDive importer; then the KOMODO copies can re-copy the repaired DSMZ ingredient set. |
| Minor | Supplier qualifiers for three complex ingredients were dropped. | The DSMZ PDF and MediaDive REST response qualify yeast extract, malt extract, and dextrose as Difco ingredients; generated rows store only the bare ingredient names. | `data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml` and KOMODO/DSMZ enrichment rules. |

## Recommended Edits

1. Add the supported 1000 ml distilled-water row to
   `data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml` and propagate
   the same DSMZ ingredient set to the four KOMODO-derived records.
2. Preserve the Difco qualifiers on yeast extract, malt extract, and dextrose,
   either in ingredient names or structured ingredient notes.
3. Regenerate `data/merge_yaml/merged/` and confirm the five Medium 636 source
   duplicates still merge into one `isp_medium_2_with_5_nacl` generated record.

## Follow-up Checks

- Run `just validate-schema` and `just validate-strict` on the repaired DSMZ
  owner and four KOMODO owners.
- Run `just validate-terms` after adding the water row and supplier qualifiers.
- Regenerate the generated YAML, then rerun schema, strict, term, and reference
  validation on `data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml`.
- Manually compare the regenerated record with DSMZ Medium 636 and MediaDive
  Medium 636 for the six rows, 1 L final volume, and pH 7.3 to 7.5.

## Additional Notes

- No blocker or major findings were found.
- The source fetches used MediaDive REST `/rest/medium/636` and the DSMZ Medium
  636 PDF linked from that REST payload.
- The generated record uses the KOMODO `CultureMech:006155` stable ID as the
  canonical duplicate. That is a provenance preference, not a source-identity
  defect, because the record keeps the direct DSMZ 636 owner as
  `parent_media`.
