# YAML Record Review: BDELLOVIBRIO (YP) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bdellovibrio_yp_medium.yaml
- Started UTC: 2026-09-21T19:30:50Z
- Finished UTC: 2026-09-21T19:33:53Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/bdellovibrio_yp_medium.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:001356`.
- Name: `bdellovibrio_yp_medium`.
- Original name: `BDELLOVIBRIO (YP) MEDIUM`.
- Source identity: `mediadive.medium:257`, label `BDELLOVIBRIO (YP) MEDIUM`, source DSMZ Medium 257.
- Generated status: derived merge output under `data/merge_yaml/merged/`; future curation belongs in the normalized duplicate owners plus merge regeneration.
- Maintained owners:
  - `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml`, `CultureMech:001356`, `mediadive.medium:257`.
  - `data/normalized_yaml/bacterial/tris_yp_medium.yaml`, `CultureMech:004661`, `komodo.medium:257`, with notes that it was enriched from DSMZ Medium 257.
- Merge metadata: the generated record merges `bdellovibrio_yp_medium` and `tris_yp_medium` on fingerprint `555ab9dce651f07cc6b35372794878b0c3236c715d735522b93c9ce044d531c3` and preserves `tris_yp_medium` as a `SOURCE_DUPLICATE` synonym.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bdellovibrio_yp_medium.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/bdellovibrio_yp_medium.yaml --out /private/tmp/bdellovibrio_yp_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/bdellovibrio_yp_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/bdellovibrio_yp_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- The generated CultureMech ID resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml`; the merged duplicate ID `CultureMech:004661` resolves to `data/normalized_yaml/bacterial/tris_yp_medium.yaml`.
- MediaDive JSON, the rendered MediaDive page, and the linked DSMZ PDF all identify source medium 257 as `BDELLOVIBRIO (YP) MEDIUM`, with DSMZ as the source and pH 7.5.
- The source recipe is 1000 ml of 0.05 M Tris-HCl buffer at pH 7.5 with BD Bacto yeast extract and BD Bacto peptone. The current `Tris-HCl buffer` row instead records `value: '1000'`, `unit: G_PER_L`, and `CHEBI:9754` / `tris`, so the amount unit and exact chemical or solution grounding do not agree with the source.
- The `SOURCE_DUPLICATE` merge between MediaDive 257 and KOMODO 257 is plausible: the KOMODO owner says it is DSMZ Medium 257 and carries the same three ingredient signatures.

## Evidence

- The 3 g/L yeast extract and 0.6 g/L peptone rows are supported by MediaDive 257 and by the DSMZ PDF.
- The source supports `Tris-HCl buffer (0.05 M, pH 7.5) 1000.00 ml`; it does not support `1000` `G_PER_L` of Tris-HCl buffer.
- The source supports the high-level pH value 7.5 for the medium, and specifically scopes the Tris-HCl buffer itself to pH 7.5.
- The MediaDive JSON, MediaDive HTML, and DSMZ PDF all contain the same two double-layer agar preparation steps. The current record preserves those instructions, but leaves source HTML tags in a single `AUTOCLAVE` step that also describes cooling, sterile YP addition, plate pouring, drying, prey growth, top-layer preparation, mixing, and pouring.
- A gitignore-independent search over `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` for the two CultureMech IDs, the MediaDive and KOMODO source IDs, `DSMZ Medium 257`, and both duplicate slugs found the normalized owners, generated indexes, the generated merge, exact-term repair scripts, and import-priority reports. It did not find a repository-owned raw MediaDive or KOMODO payload for this record.

## Completeness

- Consequentially incomplete: the machine-readable composition cannot represent the MediaDive amount for Tris-HCl buffer until that row is changed from a 1000 g/L ingredient to the source's 1000 ml of 0.05 M, pH 7.5 buffer.
- Consequentially incomplete: the full double-layer agar plate procedure mentions 12.0 g Bacto agar in 900 ml distilled water for the bottom layer, a 0.6% Bacto agar top layer, 0.5 ml sterile YP medium, and 0.5 ml prey cell suspension, but those layer components are only embedded in the free-text preparation step.
- Empty target-organism or growth-evidence slots are not a defect here. DSMZ Medium 257 gives generic prey/host setup language and no named strain or measured growth outcome in the inspected source.
- No external DOI or PMID reference is required for the source-table rows that come directly from MediaDive/DSMZ.
- The generated merge is stale relative to both normalized owners for the September 2026 exact-term curation events on yeast extract and peptone; regenerating the merge after source corrections should carry those maintained groundings forward.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Tris-HCl buffer` is modeled with the wrong amount unit. DSMZ/MediaDive says 1000 ml of buffer in a 1000 ml main solution; both normalized owners say `1000` `G_PER_L`. | `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml` and `data/normalized_yaml/bacterial/tris_yp_medium.yaml` |
| Major | `Tris-HCl buffer` is grounded to `CHEBI:9754` / `tris`, which drops the HCl/buffer identity and contradicts the preferred term. The row should stay unresolved or be converted to an exact buffer or solution representation instead of forcing it to free Tris. | `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml` and `data/normalized_yaml/bacterial/tris_yp_medium.yaml` |
| Major | The generated record has no structured representation of the bottom-layer and top-layer agar materials from the source procedure, so agar, distilled water, sterile YP additions, and cell-suspension volumes are absent from machine-readable ingredients or solutions. | Start with `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml`; mirror the duplicate owner or merge only after the authoritative MediaDive representation is fixed |
| Minor | The first preparation step still contains `<p>` and `<b>` source markup and conflates the whole plate-making protocol under action `AUTOCLAVE`. | `data/normalized_yaml/bacterial/bdellovibrio_yp_medium.yaml` |

## Recommended Edits

1. In both normalized duplicate owners, change the `Tris-HCl buffer` row so it represents 1000 ml/L of 0.05 M buffer at pH 7.5, or replace it with a proper solution reference if the repository has or adds a Tris-HCl buffer solution record.
2. Remove the unsupported `CHEBI:9754` / `tris` grounding from the `Tris-HCl buffer` row unless an exact Tris-HCl buffer or solution grounding is verified.
3. Split the double-layer agar protocol into source-faithful machine-readable layer ingredients or nested solution/component rows where the schema can express them: bottom-layer Bacto agar plus water, addition of sterile YP medium after cooling to 60 C, top-layer 0.6% Bacto agar aliquots, and the 0.5 ml additions before pouring.
4. Split the raw preparation paragraph into ordered operations without HTML tags, while preserving the 121 C for 15 min YP sterilization, 60 C and 45 C cooling points, two to three day drying window, 24 h slant culture, and same-day inoculation instruction.
5. Regenerate `data/merge_yaml/merged/bdellovibrio_yp_medium.yaml` after the normalized owners are corrected so the merged record reflects the fixed Tris-HCl row and the existing September 2026 yeast extract/peptone term curation.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on the corrected normalized owners and the regenerated merged record.
- Rerun the repository merge verifier documented for merge-input changes to prove `data/merge_yaml/merged/bdellovibrio_yp_medium.yaml` is derived from the updated normalized YAML.
- Manually compare the regenerated ingredient and preparation rows against the DSMZ Medium 257 PDF or MediaDive 257 JSON to verify that `Tris-HCl buffer` remains 1000 ml, not 1000 g, and that no agar-layer quantity is promoted into the wrong 1000 ml main solution.

## Additional Notes

- The MediaDive page, the MediaDive JSON export, and the DSMZ PDF all agreed for every inspected row and preparation step, so there was no source conflict to preserve.
- The source-table recipe numbers are `1`, `2`, and `4`; the missing `3` is an upstream numbering detail only and did not affect the ingredient comparison.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.
