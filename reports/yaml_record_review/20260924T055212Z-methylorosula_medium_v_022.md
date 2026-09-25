# YAML Record Review: METHYLOROSULA MEDIUM V-022

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylorosula_medium_v_022.yaml
- Started UTC: 2026-09-24T05:50:35Z
- Finished UTC: 2026-09-24T05:52:12Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:004119
- **Name**: methylorosula_medium_v_022
- **Original name**: METHYLOROSULA MEDIUM V-022
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owners**:
  `data/normalized_yaml/bacterial/KOMODO_1403_METHYLOROSULA_MEDIUM_V-022.yaml`
  and `data/normalized_yaml/bacterial/methylorosula_medium_v_022.yaml`
- **Merge inputs**: `KOMODO_1403_METHYLOROSULA_MEDIUM_V-022`,
  `methylorosula_medium_v_022`
- **Merge fingerprint**: `d7d8ef0249fa2eba3d94aae6cb20bd8a7105da62b91629a3202f137bc47d2f6f`
- **Source identities**: KOMODO medium `1403`, DSMZ/MediaDive medium `1403`
- **Canonical media term**: `komodo.medium:1403`
- **Category**: bacterial
- **Composition and physical state**: `DEFINED`, `LIQUID`
- **pH**: 6.0

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylorosula_medium_v_022.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylorosula_medium_v_022.yaml --out /private/tmp/methylorosula_medium_v_022.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylorosula_medium_v_022.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylorosula_medium_v_022.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The generated record is the canonical merge of a KOMODO row and an unlinked
DSMZ/MediaDive source duplicate. KOMODO ID 1403 explicitly cites DSMZ Medium
1403, and the current DSMZ PDF plus MediaDive REST payload both identify DSMZ
1403 as `METHYLOROSULA MEDIUM V-022`.

The pH 6.0 and liquid physical state are source-supported. DSMZ Medium 1403 is
a liquid medium adjusted to pH 6.0 and dispensed in tubes or flasks with screw
caps.

An ignored-file-inclusive exact name search under `data/normalized_yaml` found
the two source records merged here. Ignored-file-inclusive exact searches for
`1403`, `METHYLOROSULA`, and `methylorosula_medium_v_022` under
`data/raw/komodo`, `data/raw/mediadive`, and `data/raw/mediadive_api` found no
checked-in raw capture for the KOMODO or MediaDive source.

## Evidence

The top-level DSMZ main salts are correct before the trace-stock merge: the
main medium contains 0.05 g/L ammonium sulfate, 0.04 g/L `MgCl2 x 6 H2O`, and
0.07 g/L `KH2PO4`, plus 1 ml/L Trace Element Solution and distilled water.

The trace stock boundary is not preserved in either normalized input or in this
merge record. DSMZ and MediaDive add 1 ml/L Trace Element Solution
`mediadive.solution:2847`, but the YAML flattens every stock component into
final `ingredients` at the stock concentrations. It also merges the stock's
0.003 g/L `MgCl2 x 6 H2O` with the main medium's 0.04 g/L `MgCl2 x 6 H2O`,
producing an unsupported final `0.043000000000000003 G_PER_L` value.

Methanol is also dimensionally wrong. DSMZ and MediaDive specify
filter-sterilized methanol to a final concentration of 0.5% v/v before
inoculation, but the YAML stores methanol as `0.5 G_PER_L`.

The unlinked DSMZ normalized record preserves the preparation text:
prepare the liquid medium, adjust to pH 6.0, dispense in screw-cap tubes or
flasks, autoclave, then add filter-sterilized methanol before inoculation. The
generated merge drops `preparation_steps` entirely, so the canonical output
loses a source-supported workflow that exists in one maintained input.

## Completeness

The generated record is complete enough for the duplicate-source identity, pH,
and direct main salts, but it is incomplete as an executable recipe because the
1 ml/L Trace Element Solution addition and the methanol post-autoclave step are
not represented.

Empty `target_organisms`, `growth_metrics`, and `references` are not defects
for this generated import. The inspected DSMZ/MediaDive source does not include
a primary growth study.

Because the two normalized inputs already share the flattened trace stock and
`0.5 G_PER_L` methanol value, those fixes must happen upstream of the merge.
Because the DSMZ normalized input has the preparation step but the merge output
does not, the preparation loss belongs to merge handling for source duplicates.

## Findings

### Blocker

None found.

### Major

1. **Trace Element Solution was flattened into final-medium ingredients.**
   DSMZ/MediaDive medium 1403 adds 1 ml/L Trace Element Solution, but both
   normalized inputs and the generated merge promote the trace stock salts into
   final `ingredients`. Future fixes belong in both normalized source records
   or in the DSMZ/KOMODO import/regeneration path that writes them; do not patch
   `data/merge_yaml/merged/methylorosula_medium_v_022.yaml` directly.

2. **Methanol uses the wrong unit.** The source specifies final methanol as
   0.5% v/v, added filter-sterilized before inoculation. The YAML records
   `0.5 G_PER_L`, which turns a volume/volume final concentration into a mass
   concentration without support. The maintained owners are the two normalized
   inputs.

3. **The merge dropped source-supported preparation steps.** The DSMZ
   normalized input has the pH/autoclave/filter-sterilized methanol workflow,
   but the merged canonical record has no `preparation_steps`. The owner is the
   merge rule that combines
   `data/normalized_yaml/bacterial/methylorosula_medium_v_022.yaml` with
   `data/normalized_yaml/bacterial/KOMODO_1403_METHYLOROSULA_MEDIUM_V-022.yaml`.

### Minor

None found.

## Recommended Edits

1. Replace flattened Trace Element Solution members in both normalized source
   records with a 1 ml/L addition of `mediadive.solution:2847`, and preserve the
   solution-2847 stock recipe in a stock scope.

2. Represent methanol as a 0.5% v/v final addition with a filter-sterilized,
   before-inoculation preparation scope instead of `0.5 G_PER_L`.

3. Change duplicate merge handling so source-supported `preparation_steps` from
   the DSMZ record survive when it is merged with the KOMODO source-duplicate
   record.

4. Regenerate `data/merge_yaml/merged/methylorosula_medium_v_022.yaml` from the
   normalized sources and verify that its merge fingerprint changes only
   because of the reviewed trace-stock, methanol, and preparation corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on both
  normalized source records and on the regenerated merged record.
- Manually compare the regenerated record against DSMZ Medium 1403 and
  MediaDive REST `1403` to ensure Trace Element Solution remains a 1 ml/L
  final-medium addition and methanol remains 0.5% v/v.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`, then confirm the generated record retains DSMZ's
  preparation workflow.

## Additional Notes

The KOMODO source note says `Aerobic: No`, but the inspected DSMZ 1403 formula
does not state an anaerobic atmosphere. No structured atmosphere is present in
the YAML, so this review did not treat the KOMODO note as a final-medium
condition.

The schema validators prove that the current merged YAML is structurally valid;
they do not detect the missing preparation steps or the stock/final
concentration conflation.
