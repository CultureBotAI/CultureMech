# YAML Record Review: cellulomonas_fermentans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml
- Started UTC: 2026-09-22T06:37:41Z
- Finished UTC: 2026-09-22T06:38:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002652 |
| Name | cellulomonas_fermentans_medium |
| Original name | CELLULOMONAS FERMENTANS MEDIUM |
| Category | bacterial |
| Maintained owner | data/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml |
| Generated record | data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml |
| Merge fingerprint | 79f192cf6cad0aa0291cc8dce5c5ff0395e7e4799c4def7b11d1041e3e438792 |
| Merged from | JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM |

The record is generated from one MediaDive JCM import of JCM medium 295. The
live JCM page at `GRMD=295` is CELLULOMONAS FERMENTANS MEDIUM and supports the
source identity recorded as `mediadive.medium:J295`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml` | Passed |
| strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml --out /private/tmp/CELLULOMONAS_FERMENTANS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors |
| reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| embedded curation history | `just validate-history data/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.yaml` | Not checked: `just validate-history` validates standalone `history/` records against `HistoryRecord`, not `MediaRecipe.curation_history` blocks |

`just`-based validators were not used because the local project environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools.
The narrow validators above ran offline with Python 3.11.

## Identity and Grounding

The source identity is correct: the record denotes JCM 295, CELLULOMONAS
FERMENTANS MEDIUM. The listed inorganic ingredients are grounded to the
matching supplied hydrates or salts.

The JCM source's carbon source is not grounded because the 50 ml of 10 percent
cellobiose solution mentioned in `preparation_steps` is absent from
`ingredients` and `solutions`.

## Evidence

The live JCM 295 source lists 2.21 g K2HPO4, 1.5 g KH2PO4, 1.3 g
`(NH4)2SO4`, 0.1 g MgCl2 x 6H2O, 0.02 g CaCl2 x 2H2O, 1.25 mg FeSO4 x 7H2O,
5.0 g yeast extract, 0.8 g NaHCO3, and 950 ml distilled water. It then directs
the curator to adjust to pH 7.4 and aseptically add 50 ml of separately
sterilized 10 percent cellobiose solution.

The generated MediaDive record divides all base ingredients by 0.95: K2HPO4 is
2.32632 rather than 2.21 g/L, yeast extract is 5.26316 rather than 5 g/L, and
the same inflation is applied to the other base ingredients. It also omits the
50 ml 10 percent cellobiose stock, which should contribute the supported
carbon source.

## Completeness

A gitignore-independent exact search over `data`, `.`, YAML, JSON, and archived
reports found a TOGO M289/JCM 295 duplicate at
`data/normalized_yaml/bacterial/TOGO_M289_Cellulomonas_Fermentans_Medium.yaml`
and `data/merge_yaml/merged/cellulomonas_fermentans_medium__5efe74b8.yaml`.
The search also found DSMZ/KOMODO 350 records with the same medium name; those
are related but contain additional DSMZ-only resazurin, L-cysteine, anaerobic
N2, and NaOH facts, so they should remain a distinct source variant unless a
curator records an evidence-backed equivalence.

Empty optional organism and growth slots are acceptable for the reviewed JCM
295 record because the inspected JCM recipe gives no growth measurements.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | MediaDive divided base masses by `0.95`, inflating every base concentration relative to JCM 295. The final liter is produced by 950 ml water plus 50 ml of 10 percent cellobiose solution, not by rescaling the base recipe to 950 ml. | data/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml; MediaDive importer |
| Major | The 50 ml 10 percent cellobiose stock is not represented as an ingredient or solution, leaving the JCM 295 carbon source out of the structured recipe. | data/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml; MediaDive importer |
| Major | The same JCM 295 source is also imported through TOGO M289 as a separate maintained and generated record with a different CultureMech ID and fingerprint. | data/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M289_Cellulomonas_Fermentans_Medium.yaml; merge reconciliation |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml`,
   restore the JCM 295 base amounts to 2.21, 1.5, 1.3, 0.1, 0.02, 0.00125, 5,
   and 0.8 g/L rather than the 0.95-divided values.
2. Add the 50 ml 10 percent cellobiose stock as a solution addition or as a
   supported 5 g/L final cellobiose ingredient with preparation evidence.
3. Reconcile the MediaDive JCM and TOGO M289 maintained inputs so the merge
   emits one generated record for JCM `GRMD=295`.
4. Keep the DSMZ/KOMODO 350 formulation distinct unless a curator adds explicit
   evidence that the anaerobic resazurin/cysteine/NaOH version and JCM 295 are
   the same source variant.

## Follow-up Checks

1. Rerun the merge and verify that JCM `GRMD=295` emits one generated record.
2. Rerun LinkML, strict, term, and reference validation for the regenerated
   JCM 295 record.
3. Compare the regenerated record against live JCM 295 and live TOGO M289,
   confirming that the base salts are no longer divided by 0.95 and that the
   cellobiose stock remains represented.
4. Verify that DSMZ/KOMODO 350 still has a distinct generated record if its
   resazurin, L-cysteine, anaerobic preparation, and NaOH pH adjustment remain
   source-supported.

## Additional Notes

None found.
