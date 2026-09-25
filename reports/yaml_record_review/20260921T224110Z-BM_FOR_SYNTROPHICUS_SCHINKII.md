# YAML Record Review: bm_for_syntrophicus_schinkii

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml`
- Started UTC: 2026-09-21T22:41:11Z
- Finished UTC: 2026-09-21T22:42:18Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:010169` |
| Generated label | `bm_for_syntrophicus_schinkii` |
| Original name | `BM For Syntrophicus Schinkii` |
| Source term | `TOGO:M762` / `BM For Syntrophicus Schinkii` |
| Original source | `JCM_M737` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |
| Generated status | Derived from one active normalized TOGO/JCM input by `merge_recipes.py`; future fixes belong in normalized YAML or TOGO import/solution-migration rules, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:010169`, `TOGO:M762`,
`M762`, and `JCM_M737` found one active normalized owner for this medium plus
generated normalized-index and merged-record copies. Other hits were downstream
recipes that cite M762 as a stock-solution source, not duplicate owners of
`BM For Syntrophicus Schinkii`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml --out /private/tmp/BM_FOR_SYNTROPHICUS_SCHINKII.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used directly because this checkout's
project `uv` environment currently tries to build `llvmlite==0.46.0` under
Python 3.13 and fails inside `setuptools` before a target-specific check runs.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- TOGO M762 identifies the intended `BM For Syntrophicus Schinkii` recipe and
  records its original JCM source as `JCM_M737`.
- The current JCM `GRMD=737` URL returned a `Nothing found` page; the TOGO API
  is the inspected source of the grouped formulation.
- The direct main-medium identity is largely preserved, but source boundaries
  for gas phase, post-autoclave solution additions, and the phosphate stock are
  not preserved.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/togo-M762.json` | TOGO M762 identity, main solution rows, post-autoclave solution additions, phosphate-solution composition, gas phase, and preparation comment |
| `/private/tmp/jcm-737.html` | Original JCM URL linked by TOGO; checked and returned `Nothing found` |
| `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml` | Local repaired representation of the M762 phosphate solution as a 25 ml/L stock addition |

Supported:

- TOGO supports the main-solution rows for 830 ml distilled water, 0.2 g yeast
  extract, 0.85 g NaCl, 0.1 g CaCl2.2H2O, 0.85 g NH4Cl, 0.5 mg resazurin, and
  0.28 g MgCl2.6H2O.
- TOGO supports 1 ml trace metal solution from M288 and 1 ml
  selenite-tungstate solution from M431 in the pre-autoclave main solution.
- TOGO supports adding 40 ml 8% NaHCO3, 100 ml 0.1 M L-sodium lactate, 5 ml 5%
  Na2S.9H2O, 25 ml phosphate solution, and 1 ml trace vitamins from M190 after
  cooling.
- TOGO supports the phosphate stock as a separate 100 ml solution containing
  0.41 g KH2PO4 and 0.43 g Na2HPO4.

Unsupported or over-scoped:

- Distilled water is `930 G_PER_L`, an invalid sum of 830 ml final-medium water
  plus 100 ml phosphate-stock water.
- KH2PO4 and Na2HPO4 are direct final-medium ingredients, but the source lists
  them inside the phosphate stock.
- Every `solutions` entry has `composition: []`, `name: Unknown solution`, and
  a `G_PER_L` unit even though TOGO gives milliliter additions or points to
  cross-referenced media.
- Resazurin is inflated from 0.5 mg to `0.5 G_PER_L`.
- N2 and CO2 are modeled as variable-concentration ingredients even though the
  source scopes them to an `N2--CO2 (80:20, v/v)` gas mixture.
- The source preparation workflow for gas replacement, autoclaving, cooling,
  and anaerobic addition of filtered or autoclaved stock solutions is missing.

## Completeness

- Consequentially incomplete: all seven migrated solution rows lack
  compositions or resolvable internal references.
- Consequentially incomplete: the phosphate stock defined by this source is
  present only as flattened final-medium KH2PO4 and Na2HPO4 rows.
- Consequentially incomplete: trace metal, selenite-tungstate, and trace
  vitamin cross-references to M288, M431, and M190 still need to be fetched and
  represented as stock references.
- Empty organism-growth slots are acceptable; TOGO M762 is a recipe page and
  does not assert a growth experiment.
- Bounded search: ignored files were included in the exact M762/JCM_M737 search
  described under `Target`, and no duplicate maintained owner for TOGO M762 was
  found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The phosphate solution was flattened into the final recipe, summing its 100 ml water into the main water and promoting KH2PO4 and Na2HPO4 to direct final-medium ingredients. | TOGO M762 API JSON; repaired M763 use of M762's phosphate stock. | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |
| major | Seven solution rows are empty `Unknown solution` stubs with mass-per-volume additions; TOGO gives milliliter additions and cross-references M288, M431, and M190 for several stocks. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |
| major | Resazurin is off by three orders of magnitude at `0.5 G_PER_L`; TOGO gives 0.5 mg. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |
| major | N2 and CO2 are encoded as variable ingredients instead of the 80:20 v/v gas phase used during anaerobic preparation. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |
| major | The record omits the source preparation instructions for mixing under N2-CO2, autoclaving under that gas mixture, cooling, and aseptically and anaerobically adding the stock solutions. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml` |

## Recommended Edits

1. Rebuild the M762 final-medium ingredient list around the 830 ml main solution
   and remove phosphate-stock water, KH2PO4, and Na2HPO4 from direct
   final-medium ingredients.
2. Model the phosphate stock from M762 with 100 ml water, 0.41 g KH2PO4, and
   0.43 g Na2HPO4, and reference it as a 25 ml final addition.
3. Replace all `G_PER_L` solution additions with the source milliliter amounts:
   1 ml trace metal solution, 1 ml selenite-tungstate solution, 40 ml 8%
   NaHCO3, 100 ml 0.1 M L-sodium lactate, 5 ml 5% Na2S.9H2O, 25 ml phosphate
   solution, and 1 ml trace vitamins.
4. Fetch and wire the M288, M431, and M190 stock recipes instead of leaving
   those solution compositions empty.
5. Correct resazurin to `0.0005 G_PER_L`.
6. Move N2 and CO2 out of direct `ingredients` if the schema can represent the
   80:20 gas phase; otherwise leave an explicit quality flag that they belong
   to the preparation atmosphere.
7. Add preparation steps that preserve the N2-CO2 mixing atmosphere,
   autoclaving, cooling, and anaerobic stock addition sequence.
8. Regenerate merge outputs so `BM_FOR_SYNTROPHICUS_SCHINKII.yaml` reflects
   the normalized repair.

## Follow-up Checks

- Fetch and inspect TOGO M288, M431, and M190 before filling the
  cross-referenced stock compositions.
- Run focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/TOGO_M762_BM_For_Syntrophicus_Schinkii.yaml`
  and any newly repaired stock records.
- Run the same validators on
  `data/merge_yaml/merged/BM_FOR_SYNTROPHICUS_SCHINKII.yaml` after merge
  regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch TOGO M762 and manually verify final-medium rows, all seven solution
  additions, the phosphate-stock composition, resazurin units, and gas-phase
  preparation scoping.

## Additional Notes

- `find reports/yaml_record_review -name '*BM_FOR_SYNTROPHICUS_SCHINKII.md'`
  returned no path before this report was created.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
