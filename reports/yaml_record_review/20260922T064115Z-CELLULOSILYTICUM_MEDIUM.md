# YAML Record Review: cellulosilyticum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml
- Started UTC: 2026-09-22T06:40:29Z
- Finished UTC: 2026-09-22T06:41:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001806 |
| Name | cellulosilyticum_medium |
| Original name | CELLULOSILYTICUM MEDIUM |
| Category | bacterial |
| Maintained owner | data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml |
| Generated record | data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml |
| Merge fingerprint | 2334b0055959208d5e840dc40ec056a4bc133604e243ea3149530ef2c13a4b31 |
| Merged from | cellulosilyticum_medium |

The record is generated from one MediaDive import of DSMZ Medium 666a,
CELLULOSILYTICUM MEDIUM. The live DSMZ PDF and the MediaDive JSON export both
resolve and identify the same DSMZ source.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml` | Passed |
| strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml --out /private/tmp/CELLULOSILYTICUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors |
| reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| embedded curation history | `just validate-history data/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.yaml` | Not checked: `just validate-history` validates standalone `history/` records against `HistoryRecord`, not `MediaRecipe.curation_history` blocks |

`just`-based validators were not used because the local project environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools.
The narrow validators above ran offline with Python 3.11.

## Identity and Grounding

The DSMZ 666a identity is correct and unique in the maintained corpus. The
listed salts, agar, indigocarmine, bicarbonate, cellobiose, L-cysteine HCl x
H2O, and DTT are grounded to appropriate CHEBI terms.

Yeast extract is correctly left ungrounded as an undefined component. Clarified
rumen fluid is not represented as either an ingredient or a solution despite
being the first DSMZ recipe row.

## Evidence

The live DSMZ PDF lists 400 ml clarified rumen fluid, 0.23 g K2HPO4, 0.23 g
KH2PO4, 0.45 g NaCl, 0.45 g `(NH4)2SO4`, 0.06 g CaCl2 x 2H2O, 0.09 g
MgSO4 x 7H2O, 1 g agar, 5 mg indigocarmine, 6.4 g NaHCO3, 2.5 g cellobiose,
5 g yeast extract, 0.3 g L-cysteine HCl x H2O, 0.3 g DL-dithiothreitol, and
600 ml distilled water for Medium 666a. The live MediaDive JSON has the same
composition in `Main sol. 666a` and explicitly links the 400 ml row to
solution 2618, `Clarified rumen fluid`.

The generated YAML contains every non-fluid component at the supported g/L
amount, and the DSMZ pH range 6.7-6.8 is retained. It omits the 400 ml
clarified rumen fluid and 600 ml distilled water rows. The clarified rumen-fluid
preparation instructions survive as an unreferenced `AUTOCLAVE` step, but no
structured row says that Medium 666a receives 400 ml of that prepared fluid.

## Completeness

A gitignore-independent exact search over `data`, `.`, YAML, JSON, and archived
reports found only one maintained `cellulosilyticum_medium.yaml` owner and one
generated `CELLULOSILYTICUM_MEDIUM.yaml` record for DSMZ 666a.

Empty optional organism and growth slots are acceptable because the inspected
DSMZ Medium 666a PDF gives a formula and preparation protocol but no
strain-specific growth measurement.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The required 400 ml `Clarified rumen fluid` addition is missing from structured `ingredients` or `solutions`, even though the record keeps the stock's preparation text. | data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml; MediaDive importer |
| Minor | The 600 ml `Distilled water` row is omitted. Final g/L values are still usable, but the DSMZ 600 ml plus 400 ml rumen-fluid volume relationship is no longer recoverable. | data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml |
| Minor | The stock-fluid preparation step is typed only as `AUTOCLAVE` even though it also filters, centrifuges, sparges with N2, dispenses into serum vials, and stores frozen at -20 C. | data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/cellulosilyticum_medium.yaml`, add a
   structured 400 ml/L addition of `Clarified rumen fluid` that links to or
   nests the prepared DSMZ solution 2618/from-medium-1310 stock.
2. Preserve the 600 ml distilled-water quantity or final-volume context so the
   400 ml + 600 ml recipe volume is explicit.
3. Split or reclassify the clarified-rumen-fluid preparation into steps for
   filtering, autoclaving, centrifuging, N2 sparging, dispensing, and frozen
   storage rather than one broad autoclave step.

## Follow-up Checks

1. Rerun LinkML, strict, term, and reference validation for the regenerated
   DSMZ 666a record.
2. Compare the regenerated record against the DSMZ PDF and MediaDive JSON,
   confirming that `Clarified rumen fluid` is present at 400 ml/L and the
   non-fluid ingredients remain unchanged.

## Additional Notes

The `1 G_PER_L` agar amount is unusual but source-supported: both the DSMZ PDF
and MediaDive JSON list 1 g agar in the 1 L main solution.
