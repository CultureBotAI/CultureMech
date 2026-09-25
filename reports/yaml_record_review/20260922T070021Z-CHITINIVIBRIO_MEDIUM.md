# YAML Record Review: CHITINIVIBRIO MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml
- Started UTC: 2026-09-22T06:56:49Z
- Finished UTC: 2026-09-22T07:00:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:000930` |
| Name | `chitinivibrio_medium` |
| Original name | `CHITINIVIBRIO MEDIUM` |
| Media term | `mediadive.medium:1464` / `CHITINIVIBRIO MEDIUM` |
| Source | DSMZ Medium 1464 PDF via MediaDive |
| Generated status | Derived merge in `data/merge_yaml/merged/`, generated from `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml` and `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml` |

The maintained owners are the two normalized inputs named in `merged_from`.
Future value or relationship fixes should land in those owner files or in the
merge generator; `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml` should be
regenerated rather than hand-edited.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml --out /private/tmp/CHITINIVIBRIO_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The stable identity fields point to one DSMZ source recipe: `CultureMech:000930`,
  `chitinivibrio_medium`, original name `CHITINIVIBRIO MEDIUM`, and
  `mediadive.medium:1464`.
- The DSMZ Medium 1464 PDF and MediaDive 1464 JSON agree that CHITINIVIBRIO
  MEDIUM uses `15 g/l` NaHCO3 and `95 g/l` Na2CO3 in its mineral base.
- The generated canonical record now lists `8 g/L` NaHCO3 and `22 g/L` Na2CO3.
  Those are the sibling CHITINISPIRILLUM MEDIUM / DSMZ 1465 concentrations from
  `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml`, not the
  Chitinivibrio concentrations in DSMZ 1464 or
  `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml`.
- The two normalized parents explicitly record the relationship as
  `CONCENTRATION_VARIANT`; the child note says the carbonate/bicarbonate axis is
  the distinction between Chitinivibrio and Chitinispirillum.
- An ignored-independent search with `rg --no-ignore --hidden` for
  `chitinivibrio`, `chitinispirillum`, `mediadive.medium:1464`,
  `mediadive.medium:1465`, `CultureMech:000930`, and `CultureMech:000931`
  across `data/normalized_yaml` and `data/merge_yaml/merged` found only this
  generated target and its two normalized owners for the identifiers reviewed
  here.

## Evidence

I inspected the direct DSMZ Medium 1464 PDF, MediaDive's medium 1464 JSON, and
MediaDive's composition 1464 JSON. Those sources support these final-medium
claims in the generated record: pH 10.0, NaCl at `6 g/L`, K2HPO4 at `1 g/L`,
Chitin at `1.5 g/L` as an imported midpoint for the stated 1-2 g/L range,
MgSO4 at `1 mM` / `0.12037 g/L`, yeast extract at `20 mg/L` / `0.02 g/L`,
NH4Cl at `4 mM` / `0.21396 g/L`, and Na2S at `1 mM` / `0.07906 g/L`.

The same inspected sources do not support three consequential parts of the
generated record:

- **Carbonate/bicarbonate concentrations are from the wrong medium.** DSMZ 1464
  and MediaDive 1464 list `15 g/l` NaHCO3 and `95 g/l` Na2CO3. The generated
  record lists `8 g/L` and `22 g/L`, matching DSMZ 1465.
- **The Pfennig and Lippert stock solutions were flattened as direct medium
  ingredients at their stock concentrations.** DSMZ 1464 adds Acidic trace
  metals at `1 ml/l` and Vitamine mixture at `1 ml/l`; the record has no
  `solutions` block and instead stores stock concentrations such as EDTA
  `5 g/L`, FeSO4 x 7 H2O `2 g/L`, and B12 `0.005 g/L` as if they were final
  medium values. MediaDive composition reports the corresponding final
  concentrations as EDTA `0.005 g/L`, FeSO4 x 7 H2O `0.002 g/L`, and B12
  `0.0000016667 g/L`.
- **The preparation steps are detached from their solution scope.** "Sterilize
  by filtration and keep at 4 C. Before addition to the medium mix 1:1:1" is
  a Vitamine mixture instruction, while "adjust pH to 3-4 with HCl; autoclave
  in closed bottles, 120 C, 20 min." is an Acidic trace metals instruction. In
  the generated record both are unscoped top-level preparation steps, and the
  top-level post-autoclave addition line survives as an empty `MIX` step.

## Completeness

- Consequential stock-solution structure is missing. DSMZ 1464 and MediaDive
  encode a main solution, Acidic trace metals, Vitamine mixture, three vitamin
  subsolutions, their water amounts, stock volumes, and the `1:1:1` mixture
  boundary; none of those are representable in this generated record.
- An ignored-independent `rg --no-ignore --hidden` search for `^solutions:`
  across `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml`,
  `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml`, and
  `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml` found no
  solution blocks, so the omission is inherited from maintained normalized
  inputs rather than introduced only by the merge file.
- The generated record is stale relative to both maintained parents: it still
  ends at the 2026-08-06 merge events and lacks the 2026-08-20
  `apply_mim_groundings.py` event that added the explicit `CHEBI:17029`
  grounding for Chitin in the normalized records.
- No `target_organisms`, `growth_metrics`, or dedicated growth-evidence entries
  are present. That is not a defect for this source recipe; the inspected DSMZ
  and MediaDive formulation records establish the recipe, not strain-specific
  growth.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated canonical record denotes DSMZ 1464 / CHITINIVIBRIO MEDIUM but carries the Chitinispirillum carbonate and bicarbonate concentrations. | The reviewed file has `mediadive.medium:1464` and `CHITINIVIBRIO MEDIUM` but lists NaHCO3 `8 g/L` and Na2CO3 `22 g/L`. DSMZ Medium 1464 and MediaDive 1464 list NaHCO3 `15 g/L` and Na2CO3 `95 g/L`; `8` and `22` are the DSMZ 1465 Chitinispirillum values. | The source values in `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml` and `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml` are already distinct, so the durable fix belongs in `src/culturemech/merge/merger.py` or adjacent merge emission logic before regenerating `data/merge_yaml/merged`. |
| major | Pfennig and Lippert stocks are flattened at stock concentrations and diluted final-medium concentrations are therefore wrong by orders of magnitude. | DSMZ 1464 adds `1 ml/l` Acidic trace metals and `1 ml/l` Vitamine mixture to the main solution. The record lists EDTA `5 g/L` instead of final `0.005 g/L` and B12 `0.005 g/L` instead of final `0.0000016667 g/L`, and has no `solutions` block to preserve the stock boundary. | Add the DSMZ 1464 and 1465 stock/subsolution hierarchy to `data/normalized_yaml/bacterial/chitinivibrio_medium.yaml` and `data/normalized_yaml/bacterial/chitinispirillum_medium.yaml`, or fix the MediaDive importer if these stock rows are intended to be source-owned. |
| major | The generated record is stale and dropped post-merge ingredient grounding from both normalized owners. | Both normalized owners have the 2026-08-20 `apply_mim_groundings.py` curation event and an explicit `CHEBI:17029` term for Chitin. `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml` lacks both because it was last generated on 2026-08-06. | Rerun `just merge-recipes` after the merge bug is fixed so `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml` reflects the current normalized inputs. |

## Recommended Edits

1. Change the merge writer so a concentration-variant group cannot publish the
   sibling's ingredient amounts under a different stable DSMZ identity. The
   narrowest fix is in `src/culturemech/merge/merger.py`: when a multi-record
   group keeps an identity-specific canonical ID/source, its ingredient list
   should remain from that same canonical record unless the merger can preserve
   per-source concentration variants explicitly.
2. Model the DSMZ 1464/1465 solution hierarchy in the two normalized owner
   records or in the MediaDive import path that owns their flattened starting
   data. The future records should represent Acidic trace metals and Vitamine
   mixture as solutions added at `1 ml/l`, preserve the three vitamin
   subsolutions, include the water rows, and attach each preparation instruction
   to the correct solution scope.
3. Regenerate `data/merge_yaml/merged/` from the corrected normalized records
   and merge logic so Chitin keeps its `CHEBI:17029` grounding and the generated
   `curation_history` includes the current source events.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/chitinivibrio_medium.yaml`
  and `just validate-strict data/normalized_yaml/bacterial/chitinispirillum_medium.yaml`
  after normalized edits.
- Run `just validate-media-variant-links` to prove the Chitinivibrio and
  Chitinispirillum parent/child relationship is still reciprocal and internally
  consistent.
- Run `just merge-recipes` and then `just verify-merges` to prove the derived
  canonical record is a fresh output of the repaired merge rule.
- Re-open the regenerated `data/merge_yaml/merged/CHITINIVIBRIO_MEDIUM.yaml`
  and compare the carbonate/bicarbonate values, Chitin grounding, solution
  hierarchy, stock dilution arithmetic, and scoped preparation steps against
  DSMZ Medium 1464 before closing this review finding.

## Additional Notes

- DSMZ spells the vitamin stock "Vitamine mixture"; the imported name preserves
  that spelling.
- The generated merge on Chitinivibrio/Chitinispirillum is explainable: the
  merge layer intentionally fingerprints ingredient identity and ignores
  concentrations. The defect is the derived record's unsupported
  identity-specific concentration set, not the existence of a concentration
  variant relationship between these two recipes.
