# YAML Record Review: HALORHABDUS UTAHENSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml`
- Started UTC: 2026-09-23T11:16:12Z
- Finished UTC: 2026-09-23T11:17:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002099` |
| Name | `halorhabdus_utahensis_medium` |
| Original name | `HALORHABDUS UTAHENSIS MEDIUM` |
| Category | `archaea` |
| Physical state | `LIQUID` |
| pH | `7.6` |
| Generated from | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` |
| Source accession | `mediadive.medium:927` |
| Source PDF | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium927.pdf` |
| Merge fingerprint | `605c91f2537fc09c296d737d91f2a012786b220058d8618619e63ecfd03001ed` |

I reviewed the generated merged record, its direct MediaDive/DSMZ normalized
owner, the DSMZ Medium 927 PDF, and the MediaDive REST payload for medium 927.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halorhabdus_utahensis_medium`,
`HALORHABDUS UTAHENSIS MEDIUM`, `mediadive.medium:927`, `DSMZ Medium 927`, and
`DSMZ_Medium927`. Ignored files were included. The search found the direct
MediaDive/DSMZ branch under review, separate KOMODO and Togo normalized
branches for DSMZ 927, and their generated outputs; only
`halorhabdus_utahensis_medium.yaml` feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml --out /private/tmp/halorhabdus_utahensis_medium_605c91f2.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The top-level record identity is correct: DSMZ and MediaDive both identify
medium 927 as `HALORHABDUS UTAHENSIS MEDIUM`, with pH 7.6 and DSMZ as the
source. The direct main-medium ingredients `NaCl`, `NaBr`,
`MgSO4 x 7 H2O`, `KCl`, `NH4Cl`, `Tris-HCl`, yeast extract, and glucose have
the correct DSMZ quantities before post-autoclave stocks are added.

Several ingredient rows have the wrong scope because stock ingredients were
flattened into the main medium. The record also grounds two unusual hydrated
chloride rows to generic salts: DSMZ names `FeCl2 x 7 H2O` and
`NiCl2 x 6 H2O`, but the generated CHEBI labels are only `iron dichloride` and
`nickel dichloride`.

## Evidence

DSMZ 927 defines a 1 L main solution containing 270 g `NaCl`, 0.1 g `NaBr`,
20 g `MgSO4 x 7 H2O`, 5 g `KCl`, 2 g `NH4Cl`, 12 g `Tris-HCl`, 1 g yeast
extract `(Difco)`, 2 g glucose, and 1000 ml distilled water. It then directs
the curator to prepare three stock solutions separately and, after autoclaving
and cooling the medium, add 2.5 ml phosphate solution, 0.5 ml calcium chloride
solution, and 0.25 ml Fe/Mn solution.

The generated record imports the stock ingredients themselves as unconditional
top-level ingredients:

| Generated ingredient | Generated amount | Source scope |
|---|---:|---|
| `KH2PO4` | 50 g/L | 5% w/v phosphate stock, used at 2.5 ml/L |
| `CaCl2 x 6 H2O` | 100 g/L | 10% w/v calcium chloride stock, used at 0.5 ml/L |
| `FeCl2 x 4 H2O` | 20 g/L | Fe/Mn stock, used at 0.25 ml/L |
| `MnCl2 x 4 H2O` | 100 mg/L | unsupported merge of a 20 g/L Fe/Mn stock row with the 100 mg/L SL-7 trace-stock row |

DSMZ 927 also says to add 2 ml/L trace elements SL-7 only for DSM 27208. The
generated record imports the SL-7 HCl, Fe, Zn, Mn, B, Co, Cu, Ni, and Mo rows
as unconditional top-level ingredients at their stock concentrations, and it
does not preserve the `for DSM 27208` condition or the 2 ml/L addition amount.

## Completeness

The generated record omits 1000 ml distilled water from the main solution and
from each of the phosphate, calcium chloride, Fe/Mn, and SL-7 stocks. It has
three generic `Prepare and sterilise separately` preparation steps, but those
steps are not tied to a named stock or its ingredients.

The record has no explicit target-organism assertion. The DSM 27208-specific
SL-7 exception should be represented as a conditional variant or a strain-scoped
addition before any growth claim for DSM 27208 is added.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Phosphate, calcium chloride, and Fe/Mn stock formulas were flattened into unconditional main-medium ingredients. | DSMZ adds 2.5 ml of 5% KH2PO4, 0.5 ml of 10% CaCl2, and 0.25 ml of Fe/Mn solution after autoclaving. The record instead stores 50 g/L KH2PO4, 100 g/L CaCl2, and 20 g/L FeCl2 as top-level ingredients. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the MediaDive importer |
| Major | The 20 g/L Fe/Mn-stock MnCl2 row was collapsed with the SL-7 trace MnCl2 row, then down-scoped to 100 mg/L. | DSMZ has 20 g `MnCl2 x 4 H2O` in the Fe/Mn stock and 100 mg `MnCl2 x 4 H2O` in SL-7. The curation history records a duplicate merge and unit-conflict resolution for this ingredient. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or duplicate-ingredient cleanup logic |
| Major | The SL-7 trace element stock is unconditional and 500-fold too concentrated for its only stated final-medium use. | DSMZ says `For DSM 27208 add 2ml/l trace elements SL-7`; the generated HCl, Fe, Zn, Mn, B, Co, Cu, Ni, and Mo rows are top-level ingredients with stock amounts and no DSM 27208 condition. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the MediaDive importer |
| Major | Water and stock boundaries are missing. | DSMZ gives 1000 ml distilled water in the main solution and in each stock solution. The generated record has no water rows and no solution references for the post-autoclave additions. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the MediaDive importer |
| Minor | Yeast extract lost its `Difco` qualifier. | DSMZ says `Yeast extract (Difco)`; the generated row is only `Yeast extract`. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the MediaDive ingredient importer |
| Minor | Two hydrated chloride rows are grounded to generic chlorides. | `FeCl2 x 7 H2O` is grounded to `iron dichloride`, and `NiCl2 x 6 H2O` is grounded to `nickel dichloride`. | `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the ingredient resolver |

## Recommended Edits

1. In `data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml` or the
   MediaDive importer, represent the 5% KH2PO4, 10% CaCl2, Fe/Mn, and SL-7
   recipes as separate stock solutions instead of flattening their ingredients
   into the main medium.
2. Reference the three unconditional post-autoclave stocks from the main
   medium with DSMZ's 2.5 ml/L, 0.5 ml/L, and 0.25 ml/L addition amounts.
3. Scope the SL-7 addition to DSM 27208 at 2 ml/L instead of making it an
   unconditional ingredient set.
4. Restore distilled water to the main solution and each stock solution.
5. Undo the cross-solution `MnCl2 x 4 H2O` merge so the Fe/Mn stock retains
   20 g/L and the SL-7 stock retains 100 mg/L.
6. Preserve the `Difco` qualifier on yeast extract and resolve exact hydrate
   groundings for `FeCl2 x 7 H2O` and `NiCl2 x 6 H2O`, leaving either term
   unresolved if no exact ontology match exists.
7. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halorhabdus_utahensis_medium__605c91f2.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml`
   after the normalized DSMZ 927 record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/halorhabdus_utahensis_medium.yaml`
   to confirm exact salt and hydrate identities.
3. Run `just verify-merges` to prove the generated DSMZ 927 branch regenerates
   from the corrected normalized source.
4. Manually compare the regenerated record against DSMZ Medium 927 and
   MediaDive 927 to confirm that the three post-autoclave stock additions and
   the DSM 27208-only SL-7 addition remain scope-preserving.

## Additional Notes

The Togo and KOMODO DSMZ 927 siblings were not used as formulation authority
for this direct MediaDive record. They should be reviewed separately because
they contain their own generated artifacts and may encode a different subset of
DSMZ's main recipe and post-autoclave additions.
