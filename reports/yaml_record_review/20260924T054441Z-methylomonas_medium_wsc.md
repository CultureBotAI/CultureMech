# YAML Record Review: METHYLOMONAS MEDIUM (WSC)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylomonas_medium_wsc.yaml
- Started UTC: 2026-09-24T05:43:08Z
- Finished UTC: 2026-09-24T05:44:41Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:001215
- **Name**: methylomonas_medium_wsc
- **Original name**: METHYLOMONAS MEDIUM (WSC)
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylomonas_medium_wsc.yaml`
- **Merge input**: `methylomonas_medium_wsc`
- **Merge fingerprint**: `6f65eec086acd804511df831848e0f44374223959f7a1a990442776965a92f2c`
- **Source identity**: DSMZ / MediaDive medium `1738`
- **Media term**: `mediadive.medium:1738` / DSMZ Medium 1738
- **Category**: bacterial
- **Composition and physical state**: `DEFINED`, `LIQUID`
- **pH**: 7.8-7.9
- **Rare-earth flag**: `high_ree: true`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylomonas_medium_wsc.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylomonas_medium_wsc.yaml --out /private/tmp/methylomonas_medium_wsc.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylomonas_medium_wsc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylomonas_medium_wsc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The record identity is correct. The YAML source note, `media_term` CURIE, and
label point to DSMZ/MediaDive medium 1738, and both the live MediaDive REST
payload and current DSMZ PDF identify medium 1738 as `METHYLOMONAS MEDIUM
(WSC)`.

The pH range 7.8-7.9 is source-supported. DSMZ and MediaDive both put that
range on the final medium and on Solution 5, the 40X buffer. The `high_ree`
flag is also source-supported because Solution 3 contains lanthanum nitrate
hexahydrate and cerium nitrate hexahydrate.

An ignored-file-inclusive exact filename search under `data/` found only the
maintained normalized YAML and this generated merge YAML for
`methylomonas_medium_wsc.yaml`. Ignored-file-inclusive exact searches for
`1738` and `methylomonas_medium_wsc` under `data/raw/mediadive` and
`data/raw/mediadive_api` found no checked-in raw MediaDive JSON; only source
README files are present in those raw directories.

## Evidence

DSMZ and MediaDive medium 1738 are organized as five stock solutions added by
volume to distilled water:

| Source solution | MediaDive ID | Source addition to 1 L final medium |
|---|---:|---|
| Solution 1, 20X Basal Salts Solution | 5817 | 50 ml |
| Solution 2, Wolfe's Vitamin Solution | 5818 | 10 ml |
| Solution 3, Acidic Trace Elements Solution | 5819 | 0.5 ml |
| Solution 4, Alkaline Trace Elements Solution | 5820 | 0.2 ml |
| Solution 5, 40X Buffer Solution | 5821 | 25 ml |
| Distilled water | n/a | 914.30 ml |

The YAML has no `solutions` block. Instead it records the undiluted ingredients
from every source stock as final `ingredients`: Solution 1 rows are 20-fold too
concentrated, Wolfe vitamin rows are 100-fold too concentrated, Acidic Trace
Elements rows are 2000-fold too concentrated, Alkaline Trace Elements rows are
5000-fold too concentrated, and 40X Buffer rows are 40-fold too concentrated.

Two merged duplicate rows demonstrate that independent stock scopes were
collapsed. The source has 0.08 g/L `H3BO3` inside Solution 1 and 0.01 g/L
`H3BO3` inside Solution 3, but the YAML has one `0.09 G_PER_L` row. It also has
0.40 g/L NaOH inside Solution 4 and 11.80 g/L NaOH inside Solution 5, but the
YAML has one `12.200000000000001 G_PER_L` row.

The preparation steps have the same stock/final boundary loss. DSMZ has
solution-level preparation for Solution 1, Solution 3, and Solution 5, plus
main-medium instructions for combining water with Solutions 1, 3, and 4,
adding N2, methane, and oxygen to serum bottles, autoclaving, then adding
Solutions 2 and 5 after cooling. The YAML preserves those words, but attaches
all nine parsed steps to the final recipe, so the Solution 1 dissolve step,
Solution 3 composition heading, and Solution 5 pH adjustment appear after the
final-medium pH statement.

The final-medium gas protocol itself is present in the YAML and remains
source-supported: DSMZ flushes serum bottles with N2 and injects methane and
oxygen to final headspace concentrations of 5-10% CH4 and 21% O2.

## Completeness

The record is complete enough for the DSMZ/MediaDive medium identity, the pH
range, the rare-earth flag, and the gas/autoclave/post-cooling procedure, but it
is not complete as a structured recipe because none of the five source stock
solutions is represented as a solution addition.

The empty `target_organisms`, `growth_metrics`, and `references` fields are not
defects for this generated import. The DSMZ formula itself does not cite a
primary growth paper or name a tested strain.

The maintained normalized YAML has the same stale flattened stock ingredients
and final-level preparation steps as this merge record, so this issue is
present before merge generation.

## Findings

### Blocker

None found.

### Major

1. **All five source stock additions were flattened into final ingredients.**
   DSMZ/MediaDive medium 1738 adds five solutions by volume, but the YAML omits
   `solutions` and promotes undiluted Solution 1-5 component concentrations to
   final `ingredients`. This creates 20-fold, 40-fold, 100-fold, 2000-fold, and
   5000-fold concentration errors and collapses `H3BO3` and `NaOH` stock rows
   from different source solutions into unsupported final concentrations.
   Future fixes belong in
   `data/normalized_yaml/bacterial/methylomonas_medium_wsc.yaml` or the
   MediaDive import/regeneration path that writes that normalized file; do not
   patch `data/merge_yaml/merged/methylomonas_medium_wsc.yaml` directly.

2. **Stock-specific preparation steps were attached to the final medium.** The
   final recipe has nine preparation steps, including Solution 1, Solution 3,
   and Solution 5 subrecipe steps that DSMZ scopes to stock preparation. Without
   structured stock solutions, downstream readers cannot tell which steps make
   a stock and which steps make the final serum bottles. The maintained owner
   is `data/normalized_yaml/bacterial/methylomonas_medium_wsc.yaml`.

### Minor

None found.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/methylomonas_medium_wsc.yaml`, replace
   the flattened stock components with solution additions for MediaDive
   solutions `5817`, `5818`, `5819`, `5820`, and `5821` at 50, 10, 0.5, 0.2,
   and 25 ml/L, respectively.

2. Preserve the contents of the five DSMZ stock recipes as stock-solution
   records or structured solution members, including stock water rows inside
   those stocks rather than in final-medium `ingredients`.

3. Scope the Solution 1 dissolve step, the Acidic Trace Elements composition
   note, and the Solution 5 pH adjustment to their own stock solutions; leave
   only the main water/stock combination, headspace injection, autoclave,
   post-cooling stock addition, and final-pH steps on the final medium.

4. Remove the duplicate-merge `H3BO3` and `NaOH` artifacts when those rows are
   returned to their distinct stock scopes.

5. Regenerate `data/merge_yaml/merged/methylomonas_medium_wsc.yaml` from the
   normalized source and verify that the merge fingerprint changes only because
   of the reviewed solution-boundary corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylomonas_medium_wsc.yaml` and the
  regenerated `data/merge_yaml/merged/methylomonas_medium_wsc.yaml`.
- Manually compare the regenerated record against DSMZ Medium 1738 and the
  MediaDive REST `1738` payload to ensure each Solution 1-5 ingredient remains
  scoped to its stock recipe and each stock addition remains volume-scoped to
  the final medium.
- Re-run the concentration-plausibility report or its narrow equivalent and
  confirm `bacterial/methylomonas_medium_wsc.yaml` no longer carries the
  `FeSO4 x 7 H2O` stock-strength anomaly row.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

WSC and SURF share the same MediaDive solution identifiers for Wolfe's Vitamin
Solution, Acidic Trace Elements Solution, Alkaline Trace Elements Solution, and
40X Buffer Solution, but WSC has its own 20X Basal Salts Solution. A future
repair should preserve that distinction instead of reusing the SURF basal-salts
stock.

The schema, term, and reference validators all passed because the current YAML
is structurally valid even though its ingredient concentrations are scoped to
the wrong source solutions.
