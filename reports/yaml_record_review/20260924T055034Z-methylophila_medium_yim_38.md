# YAML Record Review: METHYLOPHILA MEDIUM (YIM 38)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylophila_medium_yim_38.yaml
- Started UTC: 2026-09-24T05:48:48Z
- Finished UTC: 2026-09-24T05:50:34Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:001089
- **Name**: methylophila_medium_yim_38
- **Original name**: METHYLOPHILA MEDIUM (YIM 38)
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml`
- **Merge input**: `methylophila_medium_yim_38`
- **Merge fingerprint**: `9a12dccc085bbf0dd30b0c77a7e22d783067cd8f0aa77188bd9b6b490c8a8d91`
- **Source identity**: DSMZ / MediaDive medium `1608`
- **Media term**: `mediadive.medium:1608` / DSMZ Medium 1608
- **Category**: bacterial
- **Composition and physical state**: `UNDEFINED`, `SOLID_AGAR`
- **pH**: 7.5

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylophila_medium_yim_38.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylophila_medium_yim_38.yaml --out /private/tmp/methylophila_medium_yim_38.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylophila_medium_yim_38.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylophila_medium_yim_38.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The record identity is correct. The local `media_term` identifier
`mediadive.medium:1608`, label `METHYLOPHILA MEDIUM (YIM 38)`, source note URL,
and live MediaDive REST payload all identify DSMZ medium 1608.

The DSMZ Medium 1608 PDF URL currently returns a TYPO3 `Page Not Found` HTML
document rather than a PDF. The MediaDive 1608 REST payload is still available
and contains the source main solution, Vitamin solution, pH, preparation, and
storage rows reflected in the YAML.

An ignored-file-inclusive exact filename search under `data/` found only
`data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml` and this
generated merge file. Ignored-file-inclusive exact searches for `1608`,
`methylophila_medium_yim_38`, and `METHYLOPHILA MEDIUM (YIM 38)` under
`data/raw/mediadive` and `data/raw/mediadive_api` found no checked-in raw
MediaDive JSON for the source.

## Evidence

The main direct ingredient rows match MediaDive 1608. Yeast extract is 4 g/L,
malt extract is 5 g/L, Bacto agar is 15 g/L, and the pH is 7.5. The glucose
amount, `4 G_PER_L`, is also dimensionally consistent with MediaDive's 16 ml of
a 25% sterile-filtered glucose stock.

The Vitamin solution is not represented correctly. MediaDive adds 5 ml of
`mediadive.solution:3350` per liter of main medium; that stock contains 0.2 mg/L
each of thiamine hydrochloride dihydrate, pyridoxine hydrochloride, riboflavin,
nicotinic acid, L-phenylalanine, and biotin. The YAML has no `solutions` block
and instead stores all six stock members as final `0.0002 G_PER_L` ingredients.
Because only 5 ml stock is added to 1 L medium, each vitamin-like component is
200-fold too high in the flattened record.

The source also scopes the stock storage step to Vitamin solution. MediaDive's
Vitamin solution record says to store it dark and cold at 5 C, but the YAML
attaches that storage text as final-medium step 3.

The source distinguishes Bacto yeast extract and Bacto agar and labels glucose
as a 25% sterile-filtered addition. The final ingredient amounts are usable, but
those attributes were not preserved near the ingredient rows, and the generic
post-cooling preparation step does not show that glucose is the sterile-filtered
stock added after autoclaving.

## Completeness

The record is complete enough for DSMZ/MediaDive identity, pH, the direct
complex ingredients, agar, and glucose's final equivalent. It is incomplete for
the Vitamin solution because the stock solution itself, its 5 ml/L addition, and
its storage boundary are absent.

Empty `target_organisms`, `growth_metrics`, and `references` are not defects
for this generated import. The inspected MediaDive payload does not include a
primary growth study.

The maintained normalized YAML has the same flattened Vitamin solution rows and
final-level storage step as this merge record, so these issues are present
before merge generation.

## Findings

### Blocker

None found.

### Major

1. **Vitamin solution 3350 was flattened into final-medium ingredients.**
   MediaDive 1608 adds 5 ml/L Vitamin solution, but the YAML promotes the
   stock's six 0.2 mg/L component rows into final `0.0002 G_PER_L` ingredients.
   This drops the `mediadive.solution:3350` stock addition and records every
   vitamin-like stock member 200-fold too high. Future fixes belong in
   `data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml` or the
   MediaDive import/regeneration path that writes that normalized file; do not
   patch `data/merge_yaml/merged/methylophila_medium_yim_38.yaml` directly.

2. **Vitamin solution storage was attached to the final medium.** The
   `Store in the dark and cold (5 C)` step belongs to the Vitamin solution
   stock, not the final agar medium. The maintained owner is
   `data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml`.

### Minor

1. **Ingredient attributes are not preserved.** MediaDive marks yeast extract
   and agar as `Bacto` and glucose as `25%, sterile-filtered`. Those qualifiers
   are absent from the YAML ingredient rows even though the amounts are
   otherwise dimensionally consistent.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml`, replace
   the flattened vitamin ingredients with a 5 ml/L Vitamin solution addition
   grounded to `mediadive.solution:3350`.

2. Preserve the Vitamin solution 3350 stock recipe as a stock-solution record or
   structured solution member, with its dark/cold storage instruction scoped to
   that stock.

3. Preserve MediaDive source attributes for Bacto yeast extract, Bacto agar, and
   25% sterile-filtered glucose, either as source-scoped ingredient notes or
   structured preparation notes.

4. Regenerate `data/merge_yaml/merged/methylophila_medium_yim_38.yaml` from the
   normalized source and verify that the merge fingerprint changes only because
   of the reviewed Vitamin solution and attribute corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylophila_medium_yim_38.yaml` and the
  regenerated `data/merge_yaml/merged/methylophila_medium_yim_38.yaml`.
- Manually compare the regenerated record against the MediaDive REST `1608`
  payload to ensure Vitamin solution remains a 5 ml/L final-medium addition and
  its components remain stock-scoped.
- Retry the DSMZ Medium 1608 PDF URL; if it remains unavailable, preserve the
  MediaDive REST payload provenance as the inspected source for any edit.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

The DSMZ PDF check could not run because the configured PDF URL returned an HTML
404 page. The MediaDive REST payload was sufficient to verify the current
record's identity, formula, pH, and stock-boundary defect.
