# YAML Record Review: archaeoglobus_profundus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`
- Started UTC: 2026-09-21T14:11:15Z
- Finished UTC: 2026-09-21T14:12:22Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| ID | `CultureMech:002576` |
| Name | `archaeoglobus_profundus_medium` |
| Original name | ARCHAEOGLOBUS PROFUNDUS MEDIUM |
| Category | `archaea` |
| pH | 6.9 |
| Source identity | `mediadive.medium:J214`, JCM Medium 214 |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214` |
| Merge fingerprint | `62508380c2b7872b89d55d6faf7496d538786b224800d044d6c8e6d55235f7b5` |
| Merged from | `JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM` |

The generated merge has one normalized owner:
`data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml --out /private/tmp/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: no focused validator is documented for one generated merge record. |

## Identity and Grounding

The record identifies the intended source. MediaDive `J214` names ARCHAEOGLOBUS
PROFUNDUS MEDIUM, points to JCM GRMD 214, and matches the JCM title and
formulation for the main solution.

An ignored-inclusive exact search across `data/normalized_yaml`,
`data/merge_yaml`, `data/culturemech_id_registry.tsv`,
`data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`, `data/raw`, and the import
tracking duplicate and plausibility reports found one owner for
`CultureMech:002576` / `mediadive.medium:J214`, this generated merge, the
expected registry/catalog/index entries, and two duplicate-merge diagnostics
for MgSO4 x 7H2O and NaCl. No exact second owner for `CultureMech:002576` or
the `JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM` source stem was found in that
searched set.

Groundings for the main formula are mostly exact. The unresolved row is
`MnSO4 x n H2O` from JCM Medium 151 / MediaDive solution 3804: it points to a
generic manganese(II) sulfate ChEBI term and has no `mediaingredientmech_chebi_term`.

## Evidence

JCM Medium 214 is a one-liter medium with 10 ml `Trace minerals` from JCM
Medium 151. MediaDive represents the same shape as `Main sol. J214` plus a
nested `Trace minerals` solution and exposes both the stock recipe and a
final-composition export.

The CultureMech recipe has no `solutions` section and flattened the 10 ml
Trace minerals stock into top-level final ingredients using stock recipe
concentrations:

- JCM and MediaDive put 3.45 g MgSO4 x 7H2O in the final medium and 3.0 g/L in
  the Trace minerals stock. The final MediaDive composition is 3.48 g/L after
  the 10 ml addition; CultureMech stores the undiluted sum, `6.45 G_PER_L`.
- JCM and MediaDive put 18 g NaCl in the final medium and 1.0 g/L in the Trace
  minerals stock. The final composition is 18.01 g/L; CultureMech stores
  `19.0 G_PER_L`.
- The Trace minerals stock rows such as Nitrilotriacetic acid, MnSO4 x n H2O,
  FeSO4 x 7H2O, CoSO4 x 7H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, H3BO3,
  and Na2MoO4 x 2H2O are present at 1 L stock concentrations instead of their
  10 ml/L final concentrations.

The import also dropped the JCM final 990 ml distilled-water row and the Trace
minerals 1000 ml stock water. Final-medium milligram rows were handled
correctly: `Fe(NH4)2(SO4)2 x 6 H2O`, `(NH4)2Ni(SO4)2 x 6 H2O`, and resazurin
are each expressed as their proper gram-per-liter equivalents.

The main JCM preparation text and the MediaDive Trace minerals pH-adjustment
text are preserved, but the trace preparation is a top-level step rather than
stock-local preparation.

## Completeness

Consequential gaps:

- The 10 ml Trace minerals addition is not represented as a solution addition.
- Trace-stock solutes are not nested and are too concentrated for a flat final
  recipe.
- Both final and stock water rows are absent.
- The stock-local Trace minerals preparation is not scoped to its stock.

Empty target-organism and growth-evidence fields are acceptable for this source
recipe because the JCM and MediaDive records are medium formulas, not growth
assays.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The JCM/J214 Trace minerals stock was flattened into the final formula at stock concentration. | MediaDive J214 adds 10 ml of solution 3804; the final composition export has 0.015 g/L NTA and 0.001 g/L FeSO4 x 7H2O, while this record stores 1.5 and 0.1 `G_PER_L`. | Fix the MediaDive/JCM importer and repair `data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`. |
| Major | Final rows with the same names as trace stock rows were summed incorrectly. | `MgSO4 x 7H2O`, `NaCl`, and `CaCl2 x 2H2O` combine main-medium values with undiluted trace-stock values; `merged_duplicates.tsv` already flags MgSO4 and NaCl for this owner. | Restore the source main rows and model trace minerals separately or use MediaDive final composition values. |
| Major | Water volumes are missing. | JCM 214 has 990 ml distilled water and Trace minerals has 1000 ml water; neither appears in the CultureMech record. | Import final water and stock water under the correct recipe boundaries. |
| Minor | Trace-mineral preparation is mis-scoped. | The second preparation step describes dissolving nitrilotriacetic acid and minerals for Trace minerals, but the record has no trace stock to own that step. | Move the step to the Trace minerals stock during the stock-boundary repair. |
| Minor | `MnSO4 x n H2O` remains generically grounded. | The exact hydration state is unspecified in the source label, and the row lacks a MIM CHEBI link. | Recheck this label with the packaged MIM index and avoid forcing a specific hydrate. |

## Recommended Edits

1. Update the MediaDive/JCM import path so solution additions such as
   `Trace minerals` remain stock references or are replaced by the diluted
   final-composition values from `/download/composition/J214/json`.
2. Repair `data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`
   so 10 ml Trace minerals is represented explicitly, the duplicate MgSO4,
   NaCl, and CaCl2 rows are split by recipe boundary, and stock-only rows are
   nested under Trace minerals.
3. Restore the JCM 990 ml final water row and the 1000 ml stock water row.
4. Scope the nitrilotriacetic-acid pH adjustment step to Trace minerals.
5. Recheck the generic `MnSO4 x n H2O` grounding without inventing a more
   specific hydrate.
6. Regenerate the merge layer.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`
  and `just validate-strict data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`.
- Rerun `just validate-terms data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`
  after the MnSO4 grounding decision.
- Rerun `just verify-merges` and `just audit-merge-freshness` after
  regenerating `data/merge_yaml/merged/`.
- Compare the repaired record against the JCM 214 page and the MediaDive
  `/download/medium/J214/json` plus `/download/composition/J214/json` exports.
- Rerun the duplicate-merge report; `CultureMech:002576` should no longer be
  flagged for summed MgSO4 or NaCl rows.

## Additional Notes

The media content review manifest marks this normalized owner as `PASS`, but
that manifest did not account for stock ingredients imported with undiluted
stock `g_l` values.
