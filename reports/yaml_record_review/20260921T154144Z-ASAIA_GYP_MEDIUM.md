# YAML Record Review: ASAIA GYP medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml
- Started UTC: 2026-09-21T15:38:45Z
- Finished UTC: 2026-09-21T15:41:45Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:004094` |
| Label | `ASAIA GYP medium` |
| Normalized owners | `data/normalized_yaml/bacterial/KOMODO_1330_ASAIA_GYP_medium.yaml`; `data/normalized_yaml/bacterial/asaia_gyp_medium.yaml` |
| Source | KOMODO `komodo.medium:1330`; DSMZ/MediaDive `mediadive.medium:1330` |
| Generated status | Generated two-input merge of `KOMODO_1330_ASAIA_GYP_medium.yaml` and `asaia_gyp_medium.yaml`; future fixes belong in normalized source records or the merge rule, then in regenerated merges/pages. |

The generated record merges two exact source duplicates under fingerprint
`f298883b822f7018c3f40a68e4f264aa9890065f353cc841b093592dc3a97c3c`.
The KOMODO child record points to the DSMZ/MediaDive parent
`CultureMech:000787`, and that parent points back with a `SOURCE_DUPLICATE`
`variant_children` entry.

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml` reported `No issues found`. |
| Strict validation | Passed: the no-project Python 3.11 invocation of `scripts/validate_strict.py data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml --out /private/tmp/ASAIA_GYP_MEDIUM.strict.tsv --workers 1 --quiet` scanned 1 file and wrote 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 snippet checks, and reported all validations passed. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported validation passed after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone records under `history/`, not a focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

The documented `just` entry points remain blocked by the project-level Python
3.13 `llvmlite==0.46.0` build failure, so the focused no-project Python 3.11
validator invocations above were used for this one record.

## Identity and Grounding

The duplicate identity is coherent. `CultureMech:004094` is registered to the
KOMODO `ASAIA GYP medium` normalized record, `CultureMech:000787` is registered
to the DSMZ/MediaDive `ASAIA GYP MEDIUM` parent, and both normalized records
carry the same six non-water ingredients, pH 6.8, solid-agar state, and
`SOURCE_DUPLICATE` relationship. The generated record keeps the canonical
KOMODO source term and records the DSMZ parent as `parent_media`.

MediaDive medium 1330 reports `ASAIA GYP MEDIUM`, DSMZ as its source, the same
pH 6.8, and a PDF link to `DSMZ_Medium1330.pdf`; the DSMZ PDF is also titled
`1330. ASAIA GYP MEDIUM`.

CHEBI groundings for glucose, glycerol, calcium carbonate, and agar match the
ingredient labels. Peptone and yeast extract are unresolved mixtures in this
record, which is acceptable; no exact single CHEBI grounding was forced.

## Evidence

The generated record has no structured `references` or snippet-level
`evidence`. The source trail is still checkable through the MediaDive parent
and the DSMZ PDF.

| Claim | Source check |
|---|---|
| Glucose, glycerol, peptone, yeast extract, and calcium carbonate concentrations are 10, 10, 10, 5, and 7 g/L. | Supported by the DSMZ PDF and MediaDive medium 1330 JSON. |
| Agar is 15 g/L for solid medium. | Supported by MediaDive medium 1330 JSON and by the DSMZ note that the medium may be solidified with 15 g/L agar. |
| pH is 6.8. | Supported by the DSMZ PDF and MediaDive medium 1330 JSON. |
| `KOMODO_1330_ASAIA_GYP_medium` and `asaia_gyp_medium` are source duplicates. | Supported locally: the KOMODO record states that DSMZ Medium 1330 supplied its ingredients, and the two normalized records have matching physical state, pH, ingredient set, and concentrations. |

Unsupported or incomplete claims:

- The formulation omits the 1000 ml distilled-water row present in both the
  DSMZ PDF and MediaDive main solution 1330 JSON.
- The generated merge omits the DSMZ/MediaDive preparation note carried by the
  `asaia_gyp_medium.yaml` parent: the note explains calcium carbonate
  buffering, opaque agar-plate settling, colony clearing as acid dissolves
  calcium carbonate, and pH 6.8.

## Completeness

- Empty `target_organisms` and growth-evidence slots are not automatic
  defects. MediaDive currently exposes associated Asaia strains for medium
  1330, so a later growth-evidence pass could add them if CultureMech wants
  MediaDive strain associations represented.
- A gitignore-independent exact search for
  `CultureMech:004094|CultureMech:000787|komodo.medium:1330|mediadive.medium:1330|KOMODO_1330_ASAIA_GYP_medium`
  under `data`, `scripts`, `history`, `src`, `reports`, and
  `references_cache` found the two normalized records, generated indexes,
  generated reports, and this generated merge as expected.
- `find reports/yaml_record_review -maxdepth 1 -name '*ASAIA_GYP_MEDIUM.md'`
  found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The merged `MediaRecipe` omits the explicit 1000 ml distilled-water row. | DSMZ Medium 1330 lists `Distilled water 1000.0 ml`; MediaDive solution `2665` for medium 1330 also has `Distilled water`, amount `1000`, unit `ml`. Both `data/normalized_yaml/bacterial/KOMODO_1330_ASAIA_GYP_medium.yaml` and `data/normalized_yaml/bacterial/asaia_gyp_medium.yaml` omit that row, so the generated merge omits it too. | Both normalized source records, or the MediaDive/KOMODO import mapping that drops final-volume water rows. |
| Minor | The generated merge preserves the KOMODO child but drops source-supported preparation context from the DSMZ/MediaDive parent. | `data/normalized_yaml/bacterial/asaia_gyp_medium.yaml` carries a preparation step with the DSMZ calcium-carbonate/solid-agar explanation and pH. The generated merge has no `preparation_steps`. | Merge rule for source duplicates, after deciding whether parent-only preparation notes should be lifted into the generated canonical record. |
| Minor | The KOMODO import timestamp is malformed. | The first `curation_history` timestamp is `2026-01-27T01:15:02.fZ`, which is not a valid ISO timestamp, but it still passes the current `^20[0-9]{2}-` schema pattern. | `data/normalized_yaml/bacterial/KOMODO_1330_ASAIA_GYP_medium.yaml` and a broader guarded curation-history timestamp cleanup. |

## Recommended Edits

1. Restore `Distilled water`, 1000 ml per 1 L medium, to
   `data/normalized_yaml/bacterial/asaia_gyp_medium.yaml` and
   `data/normalized_yaml/bacterial/KOMODO_1330_ASAIA_GYP_medium.yaml`, or fix
   the relevant import rule if the omission is reproducible from MediaDive
   solution JSON.
2. Decide whether `SOURCE_DUPLICATE` merges should carry preparation steps that
   appear on one exact source duplicate. If so, preserve the DSMZ/MediaDive
   calcium-carbonate and pH note when regenerating `ASAIA_GYP_MEDIUM.yaml`.
3. Normalize `2026-01-27T01:15:02.fZ` through a guarded curation-history
   cleanup rather than relying on the generated merge to hide it.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on both
  normalized ASAIA GYP source records.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating `data/merge_yaml/merged/ASAIA_GYP_MEDIUM.yaml`.
- Re-fetch MediaDive `download/medium/1330/json` or the DSMZ PDF and confirm
  the generated record contains all seven MediaDive recipe rows, including
  the water final volume and the agar condition.
- Add or run a focused curation-history timestamp check if one becomes
  available for embedded `MediaRecipe.curation_history` arrays.

## Additional Notes

- Local `data/normalized_yaml/bacterial/mediadive_2665_Main_sol_1330.yaml`
  already has the water row and the DSMZ/MediaDive preparation note, which
  makes the omission specific to the normalized `MediaRecipe` records and the
  generated duplicate merge reviewed here.
- Local `data/normalized_yaml/bacterial/mediadive_1330_Main_sol_621.yaml` is a
  different MediaDive solution and is not evidence for this record despite the
  confusing `mediadive_1330` filename stem.
