# YAML Record Review: amphibacillus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml`
- Started UTC: 2026-09-21T11:33:00Z
- Finished UTC: 2026-09-21T11:33:56Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:000875` |
| Name | `amphibacillus_medium` |
| Original name | `AMPHIBACILLUS MEDIUM` |
| Source identity | DSMZ Medium 1413, `mediadive.medium:1413` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/amphibacillus_medium.yaml` |

The generated record is a one-source merge and mirrors the normalized DSMZ Medium 1413 owner. The similarly named DSMZ Medium 529 / KOMODO 529 Amphibacillus records are separate maintained records with different stable IDs and a different generated merge.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml` | Passed. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml --out /private/tmp/amphibacillus_medium__114d6189.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The top-level identity is DSMZ Medium 1413:

- `id: CultureMech:000875`
- `name: amphibacillus_medium`
- `media_term.preferred_term: DSMZ Medium 1413`
- `media_term.term.id: mediadive.medium:1413`
- source URL in `notes`: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1413.pdf`

The record correctly keeps DSMZ Medium 1413 separate from the older DSMZ Medium 529 Amphibacillus medium, even though both normalize to `name: amphibacillus_medium`.

Most primary ingredient groundings are exact. The one exact-form mismatch is `NiCl2 x 6 H2O`, which is grounded to anhydrous `CHEBI:34887` / nickel dichloride instead of a nickel chloride hexahydrate term.

## Evidence

Inspected source document:

- DSMZ Medium 1413 PDF from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1413.pdf`

Supported by DSMZ Medium 1413:

- AMPHIBACILLUS MEDIUM identity, pH 10.0 after sterilization, liquid state, and complex undefined classification.
- The mineral base contains 15 g NaHCO3, 95 g Na2CO3, 16 g NaCl, 1 g K2HPO4, and 1000 ml distilled water.
- Before inoculation, DSMZ instructs adding MgSO4 to 1 mM, yeast extract to 0.5 g/L, glucose to 2.0 g/L from a 20% stock, and Trace Metals (Pfennig & Lippert) to 1 ml/L from sterile stock solutions.
- `MgSO4: 0.12037 G_PER_L` is the correct mass equivalent for 1 mM anhydrous magnesium sulfate.

Unsupported or mismatched claims:

- Trace Metals (Pfennig & Lippert) is flattened into root EDTA, FeSO4, ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows at apparent stock concentration. DSMZ 1413 only adds 1 ml of this stock per liter.
- The source says to add MgSO4, yeast extract, glucose, and trace metals before inoculation from sterile stocks. The record stores them as ordinary root ingredients, and the only preparation text for these additions is the dangling phrase `Before inoculation add from sterile stock solutions:`.
- `preparation_steps[1].description: pH 3.0-4.0` is detached from its Trace Metals stock context.
- The DSMZ 1413 PDF does not itself provide the Pfennig & Lippert trace-metal formula; the record gives no source citation that supports those internal stock rows.

## Completeness

Consequential gaps:

- The record lacks a named Trace Metals (Pfennig & Lippert) solution reference with a 1 ml/L addition amount and a source for the stock formula.
- The post-sterilization stock-addition list is incomplete in `preparation_steps`.
- No target-organism or growth-evidence claim is present; that is an empty optional field, not a defect by itself.
- `Yeast extract` remains ungrounded; no exact small-molecule term should be forced for this undefined component.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*amphibacillus_medium__114d6189.md'` found no prior report for this generated target.
- `rg --no-ignore --hidden` over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the target label, DSMZ 1413 identity, and merge fingerprint found the one-source generated target, its normalized owner, older DSMZ/KOMODO 529 Amphibacillus siblings, and no existing `amphibacillus_medium__114d6189` review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Trace Metals (Pfennig & Lippert) is flattened into root ingredients at apparent stock strength. | DSMZ 1413 adds Trace Metals at 1 ml/L; the record has EDTA at 5 g/L and FeSO4 x 7 H2O at 2.2 g/L as if the stock recipe were the final medium. | `data/normalized_yaml/bacterial/amphibacillus_medium.yaml` and the MediaDive stock-expansion path |
| Major | The post-sterilization additions are procedurally incomplete. | DSMZ says MgSO4, yeast extract, glucose, and Trace Metals are added from sterile stock solutions before inoculation; `preparation_steps[0]` ends after the colon and the stock rows are indistinguishable from mineral-base rows. | `data/normalized_yaml/bacterial/amphibacillus_medium.yaml` |
| Major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | The preferred term and trace-stock ingredient are hexahydrate; the target uses `CHEBI:34887`, while local ChEBI contains exact `CHEBI:53542` for nickel chloride hexahydrate. | MediaIngredientMech label index or post-import ingredient grounding |
| Minor | A trace-stock pH instruction is stranded as a top-level medium step. | The standalone `pH 3.0-4.0` step has no action context and is not present in the DSMZ 1413 one-page source; it likely belongs to the hidden Trace Metals stock preparation. | `data/normalized_yaml/bacterial/amphibacillus_medium.yaml` |

## Recommended Edits

1. Replace the flattened trace-metal rows with a Trace Metals (Pfennig & Lippert) stock reference added at 1 ml/L, or rescale each trace metal to its final amount and cite the maintained stock formula source.
2. Rewrite the preparation steps so the mineral base, sterilization, and four before-inoculation sterile additions are explicit and in source order.
3. Move the `pH 3.0-4.0` detail under the Trace Metals stock solution after its stock source is represented, or drop it from the top-level medium if no inspected stock source supports it.
4. Ground `NiCl2 x 6 H2O` to exact nickel chloride hexahydrate or leave the hydrate ungrounded if the packaged MIM label index still rejects the exact ChEBI term.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/amphibacillus_medium.yaml` and the no-project single-record schema/strict/term/reference checks after the normalized record is corrected.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/amphibacillus_medium__114d6189.yaml`.
- Manually compare the regenerated record with DSMZ Medium 1413 and the inspected Pfennig & Lippert trace-metal source to confirm the mineral-base ingredients and sterile additions remain in separate formulation contexts.

## Additional Notes

- `data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml` and `data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml` are distinct Medium 529 Amphibacillus records. Their shared label is not evidence for the Medium 1413 Trace Metals formula.
- `data/import_tracking/reports/concentration_plausibility.tsv` already flags `FeSO4 x 7 H2O 2.2 G_PER_L` in this record as stock-solution magnitude.
