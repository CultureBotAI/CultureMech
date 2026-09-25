# YAML Record Review: METHYLONATRUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml
- Started UTC: 2026-09-24T05:44:42Z
- Finished UTC: 2026-09-24T05:46:14Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:000570
- **Name**: methylonatrum_medium
- **Original name**: METHYLONATRUM MEDIUM
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylonatrum_medium.yaml`
- **Merge input**: `methylonatrum_medium`
- **Merge fingerprint**: `cf0bc26dd1e315f4ffa5bd0a9bcfe5596d306bf208745dfa8b55be03ca6e461f`
- **Source identity**: DSMZ / MediaDive medium `1134`
- **Media term**: `mediadive.medium:1134` / DSMZ Medium 1134
- **Category**: bacterial
- **Composition and physical state**: `DEFINED`, `LIQUID`
- **pH**: 10.0

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml --out /private/tmp/methylonatrum_medium__cf0bc26d.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The record identity is correct for DSMZ/MediaDive medium 1134. The YAML source
note, `media_term` CURIE, and `Imported from MediaDive` history entry all point
to source ID 1134, and both the live MediaDive REST payload and current DSMZ
PDF identify medium 1134 as `METHYLONATRUM MEDIUM`.

An ignored-file-inclusive exact name search under `data/normalized_yaml` found
two other normalized records with `name: methylonatrum_medium`, but this merge
record was generated only from `data/normalized_yaml/bacterial/methylonatrum_medium.yaml`.
The other same-name records belong to DSMZ/KOMODO medium 1170 and are not
evidence for the reviewed DSMZ 1134 formula.

An ignored-file-inclusive exact filename search under `data/` found only the
maintained normalized YAML and this generated merge YAML for the source file.
Ignored-file-inclusive exact searches for `1134` and `methylonatrum_medium`
under `data/raw/mediadive` and `data/raw/mediadive_api` found no checked-in raw
MediaDive JSON; only source README files are present in those raw directories.

## Evidence

The direct main-medium mass rows match DSMZ 1134 and the MediaDive 1134 REST
payload: 1 g/L `K2HPO4`, 1 g/L `KNO3`, 11 g/L `Na2CO3`, 18 g/L `NaCl`, 18 g/L
`NaS2O3 x 5 H2O`, 100 ug/L Vitamin B12, and 2 ml/L methanol represented as
1.584 g/L using the MediaDive equivalent.

The pH and main preparation paragraph are also preserved. DSMZ says the pH is
10.0, the medium is prepared in closed vessels with a medium-to-headspace ratio
of 1:5 to 1:10, methanol plus `MgSO4 x 7 H2O` plus `NaS2O3 x 5 H2O` are added
from autoclaved stock solutions after medium sterilization, Vitamin B12 is
filter-sterilized into the sterile medium, and incubation uses 150 rpm shaking.

Two source rows are unsupported in their current structured form:

| Source row | YAML row | Problem |
|---|---|---|
| 1 ml/L `Trace elements (SL6, medium 27)` | Seven SL-6 salts at stock strength, including `0.1 G_PER_L` `ZnSO4 x 7 H2O` and `0.3 G_PER_L` `H3BO3` | MediaDive solution 25 is the SL-6 stock; the YAML drops that solution reference and promotes its undiluted composition into final-medium `ingredients`. |
| 2.0 ml `MgSO4 x 7 H2O` | `2 G_PER_L` `MgSO4 x 7 H2O` | DSMZ and MediaDive record a volume addition, and DSMZ says to add it from an autoclaved stock. The inspected source does not state a stock concentration that would justify `2 G_PER_L`. |

## Completeness

The record is complete enough for the DSMZ/MediaDive medium identity, pH,
direct mass rows, Vitamin B12 amount, and main post-sterilization instructions.
It is incomplete as a structured recipe because the SL-6 trace stock is absent
as a solution addition and `MgSO4 x 7 H2O` is not preserved as a volume-scoped
stock addition with an unresolved stock strength.

The empty `target_organisms`, `growth_metrics`, and `references` fields are not
defects for this generated import. The inspected DSMZ formula does not cite a
primary growth paper or name a tested strain.

The maintained normalized YAML has the same flattened trace ingredients and
`2 G_PER_L` MgSO4 value as this merge record, so these issues are present
before merge generation.

## Findings

### Blocker

None found.

### Major

1. **Trace element solution SL-6 was flattened into final-medium ingredients.**
   DSMZ 1134 adds 1 ml/L `Trace elements (SL6, medium 27)`, and MediaDive
   represents that stock as `mediadive.solution:25`. The YAML has no `solutions`
   block and instead stores all seven SL-6 stock salts as final ingredients at
   the stock's g/L values, causing a 1000-fold concentration error. Future
   fixes belong in
   `data/normalized_yaml/bacterial/methylonatrum_medium.yaml` or the MediaDive
   import/regeneration path that writes that normalized file; do not patch
   `data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml` directly.

2. **A 2 ml MgSO4 stock addition was converted to an unsupported 2 g/L final
   ingredient.** The DSMZ and MediaDive 1134 rows are volume additions of
   `MgSO4 x 7 H2O`; the preparation text further confirms that MgSO4 is added
   from an autoclaved stock after sterilization. The YAML's `2 G_PER_L`
   concentration assumes an unstated stock strength. The maintained owner is
   `data/normalized_yaml/bacterial/methylonatrum_medium.yaml`.

### Minor

None found.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/methylonatrum_medium.yaml`, replace the
   flattened SL-6 trace salts with a 1 ml/L `Trace element solution SL-6`
   addition grounded to `mediadive.solution:25`.

2. Preserve the MediaDive solution-25 SL-6 composition as a stock-solution
   record or structured solution member, including its water row inside the
   stock rather than in final-medium `ingredients`.

3. Replace the `2 G_PER_L` `MgSO4 x 7 H2O` row with a 2 ml/L stock addition or
   an explicit unresolved volume-scoped entry that does not invent a stock mass
   concentration.

4. Regenerate `data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml` from
   the normalized source and verify that the merge fingerprint changes only
   because of the reviewed SL-6 and MgSO4 corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylonatrum_medium.yaml` and the
  regenerated `data/merge_yaml/merged/methylonatrum_medium__cf0bc26d.yaml`.
- Manually compare the regenerated record against DSMZ Medium 1134 and the
  MediaDive REST `1134` payload to ensure SL-6 remains a 1 ml/L final-medium
  addition and the MgSO4 row remains a volume addition.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

MediaDive's live 1134 REST payload exposes `Trace element solution SL-6` as
stable solution ID 25, so there is enough structured upstream data to avoid
flattening the trace stock when DSMZ 1134 is reimported.

The schema validators prove that the current record is structurally valid; they
do not check the dimensional error caused by turning a 2 ml stock addition into
a 2 g/L ingredient or the concentration error caused by flattening SL-6.
