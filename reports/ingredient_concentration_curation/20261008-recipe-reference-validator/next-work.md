# Remaining Work

This pass does not complete the all-record ingredient review. The original
91-record M142-dependent queue remains unedited by the validator work.

Later follow-up: [M689 was repaired](../20261008-m689-stocks/README.md) with
source-backed stock doses/compositions. Its successor queue has 90 unchanged
records. The M689 inspection notes below describe the pre-repair state.

Subsequent [basal-makeup repairs](../20261008-basal-makeup/README.md) cover
M809, M823, M853 and M975, leaving 86 unchanged entries in that queue.

## Bibliographic Corrections

The read-only `earlier-cohort.json` report isolates two title mismatches:

- J151 `references[0].title`: `MediaDive medium J151` versus source
  `PYROCOCCUS MEDIUM` at `$.data.medium.name` in
  `https://mediadive.dsmz.de/rest/medium/J151`.
- M142 `references[0].title`: `TOGO Medium M142` versus source
  `Pyrococcus Medium` at `$.meta.name` in
  `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142`.

Both sources are frozen in the hash-verified
`../20261008-jcm-stock-preparations/next-j261-context.json`. The validator must
not accept descriptive labels merely to turn the gate green. Correct these
with source metadata quotations, preserved history and guarded before/after
hashes. The current source hashes and record hashes are in the regression report.

## Next Ingredient Repair: M689

The complete frozen baseline and TOGO response were inspected for
`bacterial/TOGO_M689_Spirochaeta_Caldaria_Medium.yaml`, ID
`CultureMech:010094`, baseline SHA256
`9309d0f582a86dde0b12529ad3a86789239c810eceb1aa3f200d8acb9355443a`.
Recheck the current file before editing. This is source inspection, not an
applied repair or completed per-record concentration review.

The original JCM670 page is in
`../20261008-j261-variant/next-m142-originals.json`, key `JCM670`, raw SHA256
`449b16a5fb1916d6fef5ba89893ac198b3b23cd585e363e69904a26d62bc367d`.
Its persistent URL is
`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=670`.

Inspected text: `add to the medium (per liter):`. The following four rows are
10.0 ml FeCl2 solution (JCM187/M180), 10.0 ml trace element solution
(JCM187/M180), 25.0 ml trace minerals (JCM151/M142), and 10.0 ml trace vitamins
(JCM197/M190). The existing four `G_PER_L` slots therefore need source-backed
`ML_PER_L` corrections. Expand only the appropriate stock sections, not entire
referenced media; their definitions are already captured in the 91-record queue.

The main batch lists `Resazurin 0.5 mg` and `Distilled water 1.0 L`, with glucose
2.0 g, tryptone 2.0 g and cysteine hydrochloride monohydrate 0.25 g. Water input
does not independently establish final prepared volume. Do not replace the
resazurin import's 0.5 g/L with a guessed final-medium mass rate. The source
also specifies N2 atmosphere and optional NaOH adjustment to pH 7.0, not fixed
amounts of either. Existing chemical mappings require separate identity review;
the ingredient names and formula punctuation must not be silently normalized.
