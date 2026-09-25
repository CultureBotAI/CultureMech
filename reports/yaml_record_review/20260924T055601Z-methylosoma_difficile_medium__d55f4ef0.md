# YAML Record Review: METHYLOSOMA DIFFICILE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml
- Started UTC: 2026-09-24T05:54:04Z
- Finished UTC: 2026-09-24T05:56:01Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:002904
- **Name**: methylosoma_difficile_medium
- **Original name**: METHYLOSOMA DIFFICILE MEDIUM
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylosoma_difficile_medium.yaml`
- **Merge input**: `methylosoma_difficile_medium`
- **Merge fingerprint**: `d55f4ef0c26075fa7446ee76df2545fc43c8f30449048133ef58fc8e455e19a3`
- **Source identity**: JCM / MediaDive medium `J556`
- **Media term**: `mediadive.medium:J556` / JCM Medium J556
- **Category**: bacterial
- **Composition and physical state**: `DEFINED`, `LIQUID`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml --out /private/tmp/methylosoma_difficile_medium__d55f4ef0.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The record identity is correct for JCM/MediaDive J556. The local `media_term`
identifier `mediadive.medium:J556`, source URL, and live JCM page all identify
medium 556 as `METHYLOSOMA DIFFICILE MEDIUM`; the live MediaDive REST payload
matches that identity.

An ignored-file-inclusive exact name search under `data/normalized_yaml` found a
separate TOGO M560 normalized record with the same `name:` value, but the
reviewed merge record was generated only from
`data/normalized_yaml/bacterial/methylosoma_difficile_medium.yaml`. The TOGO
record was not used as evidence for this JCM J556 review.

Ignored-file-inclusive exact searches for `Methylosoma_Difficile`, `M560`,
`J556`, `GRMD=556`, and `methylosoma_difficile_medium` under `data/raw/togo`,
`data/raw/mediadive`, and `data/raw/mediadive_api` found no checked-in raw
capture for this source.

## Evidence

The base salt rows are supported by JCM J556 and the MediaDive J556 payload:
NaCl, `MgCl2 x 6 H2O`, KCl, `CaCl2 x 2 H2O`, and `Na2SO4` appear in the main
solution with the gram amounts that MediaDive normalizes over a 1002 ml final
volume.

The gas-phase workflow is also supported. JCM instructs the medium to be
distributed into tubes with more than 80% gas phase, sealed with butyl rubber
stoppers, and finally given a gas phase of 20% methane and 5% CO2 in air by
volume. The YAML preserves that instruction.

All post-autoclave stock additions are misrepresented as final ingredients:

| Source row | Source amount | YAML representation |
|---|---:|---|
| 2 M HEPES buffer, pH 7.0 | 5 ml | `HEPES buffer` at `5 G_PER_L` |
| 1 M Phosphate buffer, pH 7.2 | 0.15 ml | Phosphate prep text only; no solution addition |
| 0.09 M KNO3 solution | 0.544 ml | `KNO3` at `0.544 G_PER_L` |
| FeCl2 solution | 1 ml | FeCl2 stock HCl and FeCl2 components flattened |
| Trace element solution | 1 ml | Trace stock salts flattened |
| Vitamin solution, filter-sterilized | 1 ml | Vitamin stock members flattened |

The concentration-plausibility report independently flags this normalized file
for two vitamin stock-strength rows and the FeCl2 stock row, which aligns with
the manual source comparison.

## Completeness

The record is complete enough for the JCM/MediaDive identity, direct main salts,
and gas-phase preparation. It is incomplete as a structured recipe because none
of the six post-autoclave additions is volume-scoped to the final medium.

Empty `target_organisms`, `growth_metrics`, and `references` are not defects
for this generated import. The inspected JCM and MediaDive records do not cite
a primary growth paper.

The maintained normalized YAML has the same flattened solution rows as this
merge record, so the defect is already present before merge generation.

## Findings

### Blocker

None found.

### Major

1. **Post-autoclave stock additions were flattened into final ingredients.**
   JCM J556 adds HEPES buffer, 1 M phosphate buffer, KNO3 solution, FeCl2
   solution, Trace element solution, and Vitamin solution by volume after the
   base medium is autoclaved. The YAML turns those stock volumes or
   stock-strength recipes into final `G_PER_L` ingredient rows, losing every
   stock boundary and several molarity attributes. Future fixes belong in
   `data/normalized_yaml/bacterial/methylosoma_difficile_medium.yaml` or the
   MediaDive/JCM import path that writes that normalized file; do not patch the
   generated merge directly.

2. **The 1 M Phosphate buffer addition is missing from the structured
   composition.** The YAML keeps the note describing how to mix 28 ml 1 M
   `KH2PO4` with 78 ml 1 M `Na2HPO4`, but it omits the source row that adds
   0.15 ml of the 1 M Phosphate buffer to JCM 556.

### Minor

None found.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/methylosoma_difficile_medium.yaml`,
   replace the flattened HEPES, KNO3, FeCl2, Trace element, and Vitamin rows
   with volume-scoped post-autoclave additions matching JCM 556.

2. Add the 0.15 ml 1 M Phosphate buffer addition as a structured stock addition
   and keep the 28 ml/78 ml preparation note scoped to that buffer.

3. Preserve the FeCl2, Trace element, and Vitamin solution recipes as
   stock-solution records or structured solution members with their stock water
   rows inside the stock scopes.

4. Regenerate
   `data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml` from
   the normalized source and verify that the merge fingerprint changes only
   because of the reviewed stock-boundary corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylosoma_difficile_medium.yaml` and the
  regenerated `data/merge_yaml/merged/methylosoma_difficile_medium__d55f4ef0.yaml`.
- Manually compare the regenerated record against JCM Medium 556 and MediaDive
  REST `J556` to ensure every post-autoclave stock remains a volume addition.
- Re-run the concentration-plausibility report or its narrow equivalent and
  confirm this record no longer carries the Nicotinic acid, Pyridoxine
  hydrochloride, or `FeCl2 x 4 H2O` stock-strength anomaly rows.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

The current importer logic can identify rows with explicit `solution_id`
values, but HEPES buffer and KNO3 are also stock volume additions even though
MediaDive serializes them as compounds with molarity attributes. A future
import repair should handle those `ml` plus molarity rows without assuming a
gram-per-liter final concentration.
