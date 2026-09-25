# YAML Record Review: bicarbonate_buffered_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml
- Started UTC: 2026-09-21T21:36:25Z
- Finished UTC: 2026-09-21T21:38:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml` |
| ID | `CultureMech:007689` |
| Label | `bicarbonate_buffered_medium` |
| Category | `bacterial` |
| Maintained owners | `TOGO_M1165_Bicarbonate_Buffered_Medium.yaml`, `TOGO_M1166_Bicarbonate_Buffered_Medium.yaml`, `TOGO_M1167_Bicarbonate_Buffered_Medium.yaml`, `TOGO_M1168_Bicarbonate_Buffered_Medium.yaml` |
| Source | TOGO M1165-M1168, all from JCM Medium 1095 variants |
| Merge fingerprint | `4ddd819e05bf44db252392aa52e80725847d54bba5b933622ae7b546b209f682` |

The reviewed file is a derived merge record generated from four Togo source
records.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml --out /private/tmp/BICARBONATE_BUFFERED_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | `just validate-history` | Not checked: the documented focused history validator targets standalone files under `history/`; no documented record-local embedded `curation_history` validator exists for one merge record |

Direct `just` validation remains blocked by the project environment's Python
3.13 build of `llvmlite==0.46.0` before those recipes reach this file; the
no-project Python 3.11 commands above exercised the same focused validators.

## Identity and Grounding

- The merge was built from `CultureMech:007689` through `CultureMech:007692`,
  which map to Togo M1165, M1166, M1167, and M1168 Bicarbonate Buffered Medium
  imports from JCM Medium 1095 variants.
- The Togo SPARQList API payloads for M1165, M1166, M1167, and M1168 confirm
  the shared bicarbonate-buffered base recipe and the source-specific substrate
  solutions.
- M1165 and M1166 carry `glycerin solution`; M1167 carries
  `trisodium citrate solution`; M1168 carries `maltose solution`.
- The ignored-file-inclusive exact search for the four CultureMech IDs, four
  normalized owner filenames, and the merge fingerprint covered the registry,
  catalog, normalized bacterial YAML, this generated merge, and review reports;
  it found the expected four normalized owners and this one generated
  pre-repair merge.

## Evidence

- The source base lists 930 ml Distilled water, 0.1 g Yeast extract, 0.3 g
  NaCl, 0.41 g KH2PO4, 0.3 g NH4Cl, 0.5 mg Resazurin, 0.53 g
  Na2HPO4.2H2O, 1 ml FeCl2 solution from M180, 1 ml Trace element solution
  from M180, and 0.5 ml Selenite--tungstate solution from M431.
- The source then adds 50 ml 8% NaHCO3, 1 ml 10% CaCl2.2H2O, 1 ml 10%
  MgCl2.6H2O, 10 ml Trace vitamins from M190, and 10 ml source-specific
  substrate solution.
- The final reductant is 10 ml 5% Na2S.9H2O solution.
- The generated merge predates `repair_togo_m1165_m1168_score15.py`: it still
  has `Distilled water` as `930 G_PER_L`, `Resazurin` as `0.5 G_PER_L`,
  `Na2HPO4.2H2O` grounded to anhydrous `CHEBI:34683`, empty solution
  compositions, default `Unknown solution` names, and only one generic
  `glycerin solution` substrate.

## Completeness

- The current generated record is stale relative to all four maintained owners,
  each of which now has the September 11 repair event and populated stock
  compositions.
- The generated record has no target-organism or growth-metric claims.
- The source distinguishes gas atmosphere in preparation comments; the old
  generated record keeps only variable N2 and CO2 ingredient rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and still contains pre-repair unit and stock-solution defects. | All four normalized owners now use `930.0 ML_PER_L` water, `0.5 MG_PER_L` Resazurin, `CHEBI:91258` for disodium hydrogenphosphate dihydrate, and populated FeCl2/trace/selenite-tungstate/vitamin/bicarbonate/calcium/magnesium/sulfide/substrate solution compositions; `BICARBONATE_BUFFERED_MEDIUM.yaml` still has `930 G_PER_L` water, `0.5 G_PER_L` Resazurin, anhydrous `CHEBI:34683`, and empty `composition: []` rows named `Unknown solution`. | Regenerate `data/merge_yaml/merged/` from the repaired normalized Togo M1165-M1168 owners |
| Major | The old merge conflates substrate variants from distinct JCM 1095 strain records. | Togo M1167's substrate is 1 M trisodium citrate solution and Togo M1168's substrate is 1 M maltose solution; the reviewed merge collapses M1165-M1168 into one record with only `glycerin solution`, losing the citrate and maltose alternatives. | Merge rules after regenerating from `TOGO_M1165_Bicarbonate_Buffered_Medium.yaml` through `TOGO_M1168_Bicarbonate_Buffered_Medium.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/BICARBONATE_BUFFERED_MEDIUM.yaml` from
   the repaired September 11 normalized owners so units, hydrated phosphate
   grounding, stock names, stock compositions, source references, and
   preparation notes reach the generated layer.
2. Revisit merge canonicalization for M1165-M1168 so glycerin, trisodium
   citrate, and maltose substrate variants are represented distinctly rather
   than one pre-repair glycerin row standing for all four source records.

## Follow-up Checks

- Run `just verify-merges` and `just audit-merge-freshness` after regenerating.
- Re-run focused schema, strict, term, and reference validators on any
  regenerated Bicarbonate Buffered Medium merge products.
- Compare regenerated products against live Togo M1165, M1166, M1167, and M1168
  payloads to confirm 930 ml water, 0.5 mg Resazurin, the three source-specific
  substrate solutions, and cross-referenced M180/M431/M190 stock recipes remain
  intact.

## Additional Notes

- `data/merge_yaml/merged/bicarbonate_buffered_medium__ba0ab5a1.yaml` is a
  separate direct JCM import with a different stale representation: it flattens
  stock recipes into final ingredients and appears next in sorted order.
