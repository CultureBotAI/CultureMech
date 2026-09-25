# YAML Record Review: METHYLOSARCINA QUISQUILLARUM AND M. FIBRATA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml
- Started UTC: 2026-09-24T05:52:13Z
- Finished UTC: 2026-09-24T05:54:03Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:006827
- **Name**: methylosarcina_quisquillarum_and_m_fibrata_medium
- **Original name**: METHYLOSARCINA QUISQUILLARUM AND M. FIBRATA MEDIUM
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owners**:
  `data/normalized_yaml/bacterial/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml`,
  `data/normalized_yaml/bacterial/KOMODO_921_METHYLOSARCINA_QUISQUILLARUM_AND_M._FIBRATA_MEDIUM.yaml`,
  and `data/normalized_yaml/bacterial/medium_921_modified_for_dsm_23269.yaml`
- **Merge inputs**: `KOMODO_921_METHYLOSARCINA_QUISQUILLARUM_AND_M._FIBRATA_MEDIUM`,
  `medium_921_modified_for_dsm_23269`,
  `methylosarcina_quisquillarum_and_m_fibrata_medium`
- **Merge fingerprint**: `8841902ee930d9032625aff4f342e52b845e8c3fee323c55069e55d2b1a876b5`
- **Canonical media term**: `komodo.medium:921`
- **Linked DSMZ/MediaDive source**: medium `921`
- **Category**: bacterial
- **Composition and physical state**: `UNDEFINED`, `SOLID_AGAR`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml --out /private/tmp/methylosarcina_quisquillarum_and_m_fibrata_medium.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The canonical generated record uses the KOMODO 921 identity and merges in a
direct DSMZ/MediaDive 921 record. The current DSMZ PDF and MediaDive REST
payload both identify DSMZ medium 921 as `METHYLOSARCINA QUISQUILLARUM AND
M. FIBRATA MEDIUM`, agreeing with the KOMODO 921 label.

The `medium_921_modified_for_dsm_23269` input is not resolved by the inspected
DSMZ 921 PDF: it has the same copied ingredient signature as KOMODO 921, but
the DSMZ 921 source text inspected here does not mention DSM 23269 or a
strain-specific modification.

An ignored-file-inclusive exact name search under `data/normalized_yaml` found
the direct DSMZ and KOMODO 921 inputs; the generated `merged_from` list also
names `medium_921_modified_for_dsm_23269`. Ignored-file-inclusive exact
searches for `921`, `921_23269`, `METHYLOSARCINA`, and
`methylosarcina_quisquillarum` under `data/raw/komodo`, `data/raw/mediadive`,
and `data/raw/mediadive_api` found no checked-in raw capture for the source.

## Evidence

DSMZ/MediaDive medium 921 is assembled from several stock solutions:

| Source scope | Final-medium addition |
|---|---|
| Solution 1, 10x NMS salts | 100 ml/L |
| Solution 2, Fe EDTA | 0.1 ml/L |
| Solution 3, Sodium molybdate | 1 ml/L |
| Trace elements | 1 ml/L |
| Phosphate buffer | 10 ml/L, after autoclaving and cooling |
| Agar | optional, 1.5% for solid medium |

The YAML omits all solution additions and flattens every stock at its own
concentration: NMS salts are 10-fold too high, Fe EDTA is 10000-fold too high,
Sodium molybdate and Trace elements are 1000-fold too high, and Phosphate
buffer is 100-fold too high. The record therefore stores values such as
`71.6 G_PER_L` `Na2HPO4 x 12 H2O` and `26 G_PER_L` `KH2PO4` even though only
10 ml/L Phosphate buffer is added to the final medium.

The direct DSMZ normalized input preserved parsed `preparation_steps`, but the
generated merge dropped them. DSMZ instructs the curator to dilute Solution 1,
add Solution 3, Trace elements, and Solution 2, optionally add agar, dispense,
use 50% methane in the gas phase for sealed vessels, autoclave at 115 C for
15 minutes, separately autoclave Phosphate buffer, add it only after cooling,
and grow liquid cultures with shaking. None of those steps appears in the
generated canonical record.

The DSMZ PDF does not contain two final-medium 121 C autoclave steps. Those are
solution-level steps from MediaDive's parsed Phosphate buffer and Solution 1
stocks and need to stay attached to their stocks, not to the final medium.

## Completeness

The record is complete enough for the broad KOMODO/DSMZ 921 identity and the
optional agar amount, but it is not complete enough to execute. It lacks the
five source solution additions, it lists stock-strength ingredient
concentrations as final concentrations, and it dropped the DSMZ final-medium
preparation workflow.

Empty `target_organisms`, `growth_metrics`, and `references` are not defects
for this generated import. The inspected DSMZ 921 PDF does not cite a primary
growth study.

The maintained normalized files already share the flattened stock ingredient
signature. The direct DSMZ normalized input keeps preparation text that this
merge file lacks, so ingredient fixes belong upstream while preparation loss
needs merge-level repair.

## Findings

### Blocker

None found.

### Major

1. **All DSMZ 921 stock recipes were flattened into final ingredients.** The
   final medium uses five solution additions by volume, but the YAML stores all
   NMS salts, Fe EDTA, Sodium molybdate, Trace elements, and Phosphate buffer
   stock components as final `ingredients`. Future fixes belong in all three
   normalized source records or in the DSMZ/KOMODO import/regeneration path
   that writes them; do not patch the generated merge directly.

2. **The generated merge dropped DSMZ preparation steps.** The direct DSMZ
   normalized input preserves main-medium, NMS, Trace elements, and Phosphate
   buffer preparation text, but the canonical merged record has no
   `preparation_steps`. The owner is the merge rule that combines the DSMZ
   source record with the KOMODO source-duplicate records.

3. **A strain-specific KOMODO variant was folded into the source duplicate.**
   `medium_921_modified_for_dsm_23269` is labeled as modified for DSM 23269,
   but the inspected DSMZ 921 source does not establish that it is equivalent to
   the general Methylosarcina quisquillarum/M. fibrata medium. Future curation
   should either preserve it as a distinct variant with evidence or record the
   source that proves the modification is an exact duplicate.

### Minor

None found.

## Recommended Edits

1. Replace flattened stock components in the normalized DSMZ and KOMODO 921
   records with volume-scoped additions for MediaDive solutions `5669`, `5670`,
   `5671`, `1893`, and `1894`.

2. Preserve Solution 1, Solution 2, Solution 3, Trace elements, and Phosphate
   buffer as stock recipes, with their own water and autoclave/storage
   preparation steps scoped to the relevant stock.

3. Update merge logic so the DSMZ final-medium preparation workflow survives
   source-duplicate merging.

4. Re-check the KOMODO `921_23269` source and keep it separate unless inspected
   evidence proves the DSM 23269 modification is a true source duplicate.

5. Regenerate
   `data/merge_yaml/merged/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml`
   and verify that the fingerprint changes only because of the reviewed
   solution-boundary, preparation, and duplicate-classification corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on all
  three normalized source records and on the regenerated merged record.
- Manually compare the regenerated record against DSMZ Medium 921 and MediaDive
  REST `921` to ensure all five stock additions remain volume-scoped.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`, then confirm the canonical record retains the DSMZ
  final-medium preparation workflow.

## Additional Notes

The KOMODO source note says `Aerobic: No`, while DSMZ 921 says sealed vessels
may use 50% methane in the gas phase. The current YAML has no structured
atmosphere, so this review did not treat the KOMODO note as a final-medium
condition.

The schema validators prove the generated YAML is structurally valid; they do
not detect source stock flattening, loss of preparation text, or an unsupported
source-duplicate relationship.
