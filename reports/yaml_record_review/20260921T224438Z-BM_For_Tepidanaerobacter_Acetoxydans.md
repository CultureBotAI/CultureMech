# YAML Record Review: bm_for_tepidanaerobacter_acetoxydans

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml`
- Started UTC: 2026-09-21T22:44:39Z
- Finished UTC: 2026-09-21T22:45:44Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:010170` |
| Generated label | `bm_for_tepidanaerobacter_acetoxydans` |
| Original name | `BM For Tepidanaerobacter Acetoxydans` |
| Source term | `TOGO:M763` / `BM For Tepidanaerobacter Acetoxydans` |
| Original source | `JCM_M738` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml` |
| Generated status | Derived from one active normalized TOGO/JCM input by `merge_recipes.py`; future fixes belong in normalized YAML or TOGO import/solution-migration rules, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:010170`, `TOGO:M763`,
`M763`, and `JCM_M738` found one active normalized owner for this TOGO record
plus generated normalized-index and merged-record copies. Other `M763` hits were
source references or unrelated JCM numbers with `763` prefixes and suffixes, not
duplicate maintained TOGO M763 owners.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml --out /private/tmp/BM_For_Tepidanaerobacter_Acetoxydans.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used directly because this checkout's
project `uv` environment currently tries to build `llvmlite==0.46.0` under
Python 3.13 and fails inside `setuptools` before a target-specific check runs.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- TOGO M763 identifies `BM For Tepidanaerobacter Acetoxydans` and records its
  original JCM source as `JCM_M738`.
- The current JCM `GRMD=738` URL returned a `Nothing found` page; TOGO M763 was
  used as the inspected grouped source copy.
- The generated merge is stale. The active normalized owner was repaired on
  Sept 11 with expanded stock-solution wrappers, corrected units, preparation
  steps, references, quality flags, and a source-duplicate link to the direct
  JCM J738 owner.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/togo-M763.json` | TOGO M763 identity, main rows, stock additions, glucose substitution comment, gas phase, and preparation comment |
| `/private/tmp/jcm-738.html` | Original JCM URL; checked and returned `Nothing found` |
| `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml` | Maintained owner state after the Sept 11 M763 stock-expansion repair |

Supported:

- TOGO M763 supports the same base recipe pattern as M762 and supports swapping
  JCM 737's L-sodium lactate stock for a 100 ml/L 0.1 M glucose stock.
- The Sept 11 normalized repair preserves the main ingredients, represents
  trace metal, selenite-tungstate, bicarbonate, glucose, sulfide, phosphate,
  and trace-vitamin stocks with compositions, records anaerobic preparation
  steps, and keeps JCM/TOGO source references.

Unsupported or over-scoped in the generated merge:

- The generated merge still stores the seven solution additions as empty
  `Unknown solution` stubs with `G_PER_L` units.
- Resazurin remains inflated from 0.5 mg to `0.5 G_PER_L`.
- Distilled water remains `830 G_PER_L` rather than `830 ML_PER_L`.
- N2 and CO2 still carry non-English gas-property notes from the raw TOGO
  import and have no curated source notes.
- The generated merge lacks the Sept 11 source-duplicate relationship to the
  direct JCM J738 owner.

## Completeness

- Complete enough upstream: the maintained normalized TOGO owner now expands or
  cross-references the M288, M431, M762, and M190 stock recipes needed by M763.
- Consequentially incomplete in the generated layer: the generated record
  predates that repair and still publishes empty stock-solution stubs.
- Consequentially incomplete in the generated layer: the generated record
  lacks the repaired references and `data_quality_flags` that tell users the
  ingredients were source-curated.
- Bounded search: ignored files were included in the exact M763/JCM_M738 search
  described under `Target`, and no duplicate maintained TOGO M763 owner was
  found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated merge is stale and still publishes the pre-Sept empty solution wrappers, wrong stock-addition units, wrong resazurin unit, and missing preparation steps. | TOGO M763 API JSON; Sept 11 curation in `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml`. | No normalized TOGO edit is needed for this defect; regenerate `data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml` from the repaired normalized owner. |
| minor | The generated merge is also missing the Sept 11 source-duplicate relationship from TOGO M763 to the direct JCM J738 record. | Repaired normalized owner. | Regenerate the derived merge after normalized repair. |

## Recommended Edits

1. Rerun merge generation so `BM_For_Tepidanaerobacter_Acetoxydans.yaml`
   inherits the Sept 11 stock-solution expansion, corrected `ML_PER_L` and
   `MG_PER_L` units, source references, `ingredients_curated` flag,
   preparation steps, and source-duplicate relationship from
   `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml`.
2. Do not patch `data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml`
   directly; it is a derived record.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml`.
- Run the same validators on
  `data/merge_yaml/merged/BM_For_Tepidanaerobacter_Acetoxydans.yaml` after
  merge regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch TOGO M763 and manually verify the regenerated merge against the
  repaired normalized owner, especially glucose-vs-lactate substitution and the
  seven stock additions.

## Additional Notes

- `find reports/yaml_record_review -name '*BM_For_Tepidanaerobacter_Acetoxydans.md'`
  returned no path before this report was created.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
