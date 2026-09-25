# YAML Record Review: atribacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml
- Started UTC: 2026-09-21T16:35:20Z
- Finished UTC: 2026-09-21T16:37:35Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml`, a
generated `MediaRecipe` with stable ID `CultureMech:002438`, normalized name
`atribacterium_medium`, original name `ATRIBACTERIUM MEDIUM`, category
`bacterial`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`,
`physical_state: LIQUID`, `ph_value: 7.0`, media term
`mediadive.medium:J1272`, and merge fingerprint
`1e9c1fd952b3ccaf40a2203845061d340028e53ec9020fe591570a3f3dd8c1e3`.

The merge was generated from exactly one maintained source,
`data/normalized_yaml/bacterial/atribacterium_medium.yaml`. Future curation
must change that normalized owner, the related MediaDive solution imports, or
the importer rules that flatten those solutions, then regenerate
`data/merge_yaml/merged/`; the generated merge file should not be edited
directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml --out /private/tmp/atribacterium_medium__1e9c1fd9.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The generated record identity is internally consistent as a MediaDive-derived
JCM J1272 import: both the generated target and its normalized owner use
`CultureMech:002438`, `JCM Medium J1272`, `mediadive.medium:J1272`, and the
JCM GRMD 1272 URL.

The current public JCM GRMD URL did not independently resolve the underlying
primary recipe during this review. Fetching
`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1272` returned a small JCM
`Medium data` page that searched for medium no. 1272 and reported
`Nothing found.` The TOGO Medium M1368 API copy of the same JCM recipe was
therefore used as the nearest live source for claim-level comparison, and Togo
identified that payload as `Atribacterium Medium` with original medium
`JCM_M1272` and pH 7.0.

A gitignore-independent exact search covered `data`, `reports`, `history`, and
`.claude` for `CultureMech:002438`, `mediadive.medium:J1272`, `J1272`,
`GRMD=1272`, `ATRIBACTERIUM MEDIUM`, and
`atribacterium_medium__1e9c1fd9`. It found the generated target, the maintained
owner, an older pre-rename `JCM_J1272_ATRIBACTERIUM_MEDIUM` path in archived
validation reports, a related `data/normalized_yaml/bacterial/mediadive_5414_Main_sol_J1272.yaml`
solution import, and the TOGO M1368 record tied to the same JCM GRMD 1272
URL. Exhaustive `find` checks confirmed the current normalized owners for
`atribacterium_medium.yaml`, `mediadive_5414_Main_sol_J1272.yaml`, and
`mediadive_5342_Solution_A.yaml`.

## Evidence

The JCM 1272 formulation in Togo M1368 starts with 1 L distilled water plus
3 g NaCl, 0.107 g NH4Cl, 0.15 g KCl, 0.3 g Na2SO4, and 1.38 g NaH2PO4, then
adds several stocks per liter after autoclaving. The generated MediaDive path
does not preserve those main-salt masses: `mediadive_5414_Main_sol_J1272.yaml`
states `Original volume: 1062 mL`, and the generated target has the same salts
divided by that synthetic volume, such as 3 g NaCl becoming 2.82486 g/L.

Togo M1368 adds 10 ml of 5% xylitol solution, 10 ml of 5% fucose solution,
10 ml of 1% yeast extract solution, and 2 ml of 5% Na2S x 9 H2O solution per
liter after cooling. The generated target instead stores those additions as
direct `Xylitol 10 G_PER_L`, `Fucose 10 G_PER_L`, `Yeast extract 10 G_PER_L`,
and `Na2S x 9 H2O 2 G_PER_L` ingredients, conflating stock-addition volumes
with final-medium mass concentrations.

Togo M1368 references 5 ml per liter of Mineral solution from M1029 and 5 ml
per liter of Trace vitamins from M190. The inspected M1029 and M190 Togo
payloads show that the generated target's EDTA, FeSO4, MnCl2, ZnSO4, CoCl2,
CuCl2, Na2MoO4, H3BO3, and vitamin amounts are stock-solution recipe amounts,
not final JCM 1272 amounts. For example, M1029 lists EDTA at 3.7 g per liter
of Mineral solution and M1368 adds only 5 ml of that stock per liter of final
medium; the generated target records EDTA itself as `3.7 G_PER_L`.

Togo M1368 embeds a local `Solution A` made from 10 ml distilled water,
0.123 g MgSO4 heptahydrate, and 0.015 g CaCl2 dihydrate, and adds 10 ml of
that local stock per liter. The generated target flattens the MgSO4 and CaCl2
rows into direct ingredients and leaves only a `Solution A` row at
`10 G_PER_L` pointing to `mediadive.solution:5342`. The resolved
`data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml` contains a
different 500 ml stock with yeast extract, casamino acids, glutamate, citrate,
MgSO4, CaSO4, KCl, and NaCl, so it is not JCM 1272's local two-salt
`Solution A`.

The generated preparation steps are partially useful because they retain the
pH 7.0 adjustment, N2 dispensing, serum bottle or Balch tube setup, and butyl
stopper pretreatment. They are still incomplete around `Solution A`: step 2 is
only the label `Solution A:`, step 3 adjusts that unnamed stock to pH 6.0 with
KOH, and the stock's actual water, MgSO4, and CaCl2 composition is missing
from the solution row it should describe.

## Completeness

The missing target organism and growth-evidence fields are not findings in
this source-only generated record: neither the inspected Togo payload nor the
unresolved live JCM URL provides strain-level growth evidence that would
support a `target_organisms` assertion.

Before writing this report, `find reports/yaml_record_review -maxdepth 1 -name
'*atribacterium_medium__1e9c1fd9.md' -print` covered ignored and unignored
files in the review-report directory and found no prior exact report for this
generated stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The main-salt amounts are normalized to a synthetic 1062 ml volume instead of preserving the JCM per-liter recipe basis. | JCM/Togo M1368 states the first solution in 1 L water with 3 g NaCl, 0.107 g NH4Cl, 0.15 g KCl, 0.3 g Na2SO4, and 1.38 g NaH2PO4; `mediadive_5414_Main_sol_J1272.yaml` records `Original volume: 1062 mL`; the generated record contains the divided salt concentrations. | `data/normalized_yaml/bacterial/atribacterium_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_5414_Main_sol_J1272.yaml`, and the MediaDive import conversion that computes the 1062 ml denominator. |
| Major | Stock additions for xylitol, fucose, yeast extract, and sodium sulfide are represented as direct grams per liter. | M1368 adds 10, 10, 10, and 2 ml of stock solutions per liter; the target records those same numbers as direct `G_PER_L` ingredient concentrations. | `data/normalized_yaml/bacterial/atribacterium_medium.yaml` and the MediaDive stock-flattening rule. |
| Major | M1029 mineral solution and M190 trace-vitamin stock ingredients are inflated to their stock concentrations in the final medium. | M1368 calls for 5 ml/L of each referenced stock; the target records M1029's EDTA, FeSO4, MnCl2, ZnSO4, CoCl2, CuCl2, Na2MoO4, and H3BO3 stock amounts and M190's vitamin stock amounts as direct final `G_PER_L` rows. | `data/normalized_yaml/bacterial/atribacterium_medium.yaml` and the MediaDive handling of cross-medium stock solutions. |
| Major | The `Solution A` reference resolves to the wrong stock recipe and the local JCM 1272 stock is flattened into direct ingredients. | M1368's local `Solution A` is MgSO4 plus CaCl2 in 10 ml water, added at 10 ml/L; the target points to `mediadive.solution:5342`, whose maintained record is an unrelated eight-component 500 ml stock. | Cross-source duplicate reconciliation between `data/normalized_yaml/bacterial/atribacterium_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml`, and the MediaDive solution ID mapping. |
| Major | The same JCM GRMD 1272 medium is split between two normalized owners and two generated merge records. | This target points at `GRMD=1272` as `mediadive.medium:J1272`; `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml` points at the same JCM URL as TOGO `M1368`, and generates `data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml`. | Cross-source duplicate reconciliation between the MediaDive and Togo normalized owners plus merge rules. |

No blockers or minor findings were found beyond those major curation issues.

## Recommended Edits

1. Reconstruct `data/normalized_yaml/bacterial/atribacterium_medium.yaml` from
   the JCM 1272 source without the MediaDive 1062 ml volume normalization:
   preserve the main 1 L solution, the post-cooling per-liter stock additions,
   and the local `Solution A` stock recipe as distinct formulation levels.
2. Replace the direct stock-derived ingredients for xylitol, fucose, yeast
   extract, Na2S x 9 H2O, the M1029 trace salts, and the M190 vitamins with
   proper nested solution references or with explicitly calculated final
   concentrations whose evidence notes state the source stock, addition volume,
   and arithmetic.
3. Remove the `mediadive.solution:5342` link from this medium unless an
   inspected MediaDive source proves that JCM 1272 truly references that
   eight-component 500 ml stock; the live JCM/Togo copy supports a different
   local `Solution A`.
4. Reconcile the duplicate `TOGO:M1368` and `mediadive.medium:J1272` records so
   the two imports for GRMD 1272 either merge into one canonical record or
   remain as explicitly distinguished source-version variants.

## Follow-up Checks

- Re-run open-schema LinkML, `scripts/validate_strict.py`, the reference
  validator, and the term validator against the edited normalized MediaDive
  owner and the regenerated `data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml`.
- Validate the referenced MediaDive solution records, especially
  `mediadive_5414_Main_sol_J1272.yaml` and
  `mediadive_5342_Solution_A.yaml`, if they remain in use after duplicate
  reconciliation.
- Manually compare any retained final concentrations against Togo M1368, Togo
  M1029, and Togo M190 to confirm that stock additions are represented either
  as `ML_PER_L` additions or as arithmetically diluted final amounts.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  the generated merge outputs.

## Additional Notes

The JCM GRMD endpoint was not usable for this record during review; it returned
a `Nothing found` page for medium no. 1272. Because the current live primary
was absent, every source-level mismatch above is framed as a conflict between
the maintained MediaDive import and Togo's JCM-derived API copy rather than as
a direct contradiction of live JCM HTML.
