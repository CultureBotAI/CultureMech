# YAML Record Review: medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml
- Started UTC: 2026-09-24T01:31:36Z
- Finished UTC: 2026-09-24T01:34:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008179 |
| Name | medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397 |
| Source identity | TOGO:M1624, original source NBRC_M824 |
| Maintained owner | data/normalized_yaml/archaea/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml |
| Generated artifact reviewed | data/merge_yaml/merged/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml |

The target is the generated merge for TOGO medium M1624, NBRC Medium 824, "Medium
for Co-culture of Strain JT with Methanospirillum hungatei NBRC 100397." TOGO's
`gmdb_medium_by_gmid?gm_id=M1624` API and the NBRC `NO=824` page both identify
the same medium and list the same base recipe, four stock-solution additions, and
vial-culture instructions.

The reviewed file is generated. Future fixes belong in the normalized TOGO owner,
in the TOGO stock-solution importer or migration logic, and in source
reconciliation against `data/normalized_yaml/bacterial/NBRC_825.yaml`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml --workers 1` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator is a standalone full-corpus check over `history/`, not over embedded `MediaRecipe.curation_history` events. |

All focused validators were run with Python 3.11 through `uv --no-project
--offline` because the project-level environment currently tries to build
`llvmlite` under Python 3.13 and fails in setuptools before these checks can
start.

## Identity and Grounding

The TOGO source ID, NBRC original source note, record label, `LIQUID` physical
state, and base medium identity agree with the inspected TOGO and NBRC source
records. An exact, gitignore-independent scan for `TOGO:M1624` found only this
TOGO owner, the generated target, and indexes, so the TOGO accession itself is
not split across another normalized TOGO record.

The broader NBRC identity is split: a gitignore-independent scan for the exact
NBRC `NO=824` URL and `nbrc.medium:824` found
`data/normalized_yaml/bacterial/NBRC_825.yaml`, a separately maintained NBRC
Medium 824 record. That record has the same authority source, a dedicated
`nbrc.medium:824` media term, nested vitamin/trace/Se-W/resazurin stock
solutions, and the NBRC preparation steps recovered from the source HTML. A
gitignore-independent `find` found `NBRC_825.yaml` only under
`data/normalized_yaml/` and found no exact `NBRC_825.yaml` or `825.yaml` peer
under `data/merge_yaml/merged`.

The generated target is stale relative to its owner:

- `organism_culture_type: community`, added to the normalized owner on
  2026-08-06, is absent from the generated record.
- The normalized owner collapsed four identical distilled-water duplicates back
  to 1.0 on 2026-09-02; the generated record still reports 4.0 G_PER_L and
  notes a merged 4.0 total.

## Evidence

The TOGO and NBRC source records support the medium label, the base
per-liter entries for sodium terephthalate, yeast extract, KH2PO4,
MgCl2 x H2O, CaCl2 x 2 H2O, NH4Cl, NaHCO3, Na2S x 9 H2O, Cysteine-HCl, and
distilled water, plus stock additions of 3 ml vitamin solution, 1 ml trace
element solution, 1 ml Se-W solution, and 1 ml resazurin solution.

The source records do not support several quantities in the generated YAML:

- The four stock additions are milliliter additions, not 3, 1, 1, and 1 G_PER_L.
- Vitamin stock components are mg/L stock-solution components, not final-medium
  g/L components.
- Several trace and Se-W stock components were flattened into final-medium
  G_PER_L rows and lost mg units; examples include 24 mg CoCl2 x 6 H2O becoming
  24 G_PER_L, 25 mg CuCl2 x 2 H2O becoming 25 G_PER_L, 10 mg H3BO3 becoming
  10 G_PER_L, 24 mg Na2MoO4 x 2 H2O becoming 24 G_PER_L, and 4 mg each of
  Na2WO4 and Na2SeO3 becoming 4 G_PER_L.
- The main medium's 0.15 g CaCl2 x 2 H2O and the trace stock's 0.1 g
  CaCl2 x 2 H2O were summed into one 0.25 G_PER_L final-medium row.
- The trace stock adjustment to pH 6.5 with KOH was imported as a variable
  final-medium KOH ingredient, rather than as stock preparation detail.

The DOI evidence for target organisms resolves through Crossref and PubMed to
PMID 15006786 / PMC368352, the Qiu et al. 2004 Applied and Environmental
Microbiology article. The PubMed abstract supports strain JT and a
Methanospirillum hungatei co-culture that converted terephthalate to acetate and
methane, and the NBRC page names M. hungatei NBRC 100397 in the medium title and
comment. The publisher PDF endpoint returned a Cloudflare JavaScript challenge,
so the exact `DSM 864`, `ATCC 27890`, and genome `CP000254` alias details in the
target-organism explanations were not verified from the cited full text.

## Completeness

The generated record omits the NBRC vial-culture procedure: dissolve most
ingredients up to 900 ml, flush with N2/CO2 80/20, autoclave, add
filter-sterilized Na2S x 9 H2O and Cysteine-HCl solutions separately, add
neutralized filter-sterilized 0.2 M sodium terephthalate, use 10 to 20 percent
inoculum, and expect growth after 3 to 4 weeks. The direct NBRC owner already
recovers these as maintained `preparation_steps`.

No pH is stated for the final medium. That is not independently a defect; the
consequential pH issue here is that the trace-stock pH adjustment is represented
as a final-medium variable KOH ingredient.

The generated record leaves publication-style references empty for the source
recipe, while the TOGO owner carries only source notes. The DOI-backed growth
evidence is attached narrowly to `target_organisms` and is appropriately
caveated as not verifying the TOGO/NBRC recipe itself.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | TOGO stock solutions were flattened and unit-shifted into final-medium ingredient rows. | TOGO and NBRC add 3 ml vitamin solution plus 1 ml each of trace, Se-W, and resazurin stock. The generated record instead stores those as G_PER_L `solutions` rows and also lifts stock components into final-medium ingredients, with mg values such as CoCl2 x 6 H2O 24 mg and CuCl2 x 2 H2O 25 mg converted to 24 and 25 G_PER_L. | `data/normalized_yaml/archaea/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml`; TOGO import and solution-migration code. |
| major | The same NBRC Medium 824 exists as a separately corrected direct NBRC owner and is not reconciled with the TOGO-derived record. | A gitignore-independent exact NBRC source scan found `data/normalized_yaml/bacterial/NBRC_825.yaml`, which uses `nbrc.medium:824` and preserves nested stock solutions. The TOGO owner still describes `Original source: NBRC - NBRC_M824`. | Source equivalence and merge ownership for `data/normalized_yaml/bacterial/NBRC_825.yaml` and the TOGO M1624 owner. |
| major | The generated target is stale relative to its TOGO owner. | The owner has `organism_culture_type: community` and a 2026-09-02 duplicate-water repair; the generated record lacks the community field and still reports distilled water as 4.0 G_PER_L. | Merge regeneration for `data/merge_yaml/merged/medium_for_co_culture_of_strain_jt_with_methanospirillum_hungatei_nbrc_100397.yaml`. |
| major | NBRC vial-culture preparation details are absent. | The NBRC page gives anaerobic vial preparation, gas flushing, autoclaving, separate filter-sterilized sulfide/cysteine/terephthalate additions, inoculum size, and growth timing; the generated TOGO record has only gas ingredients and no `preparation_steps`. | The TOGO normalized owner or the reconciled NBRC Medium 824 owner. |
| minor | Target-organism alias evidence is partly source-verified but over-specific. | PubMed and Crossref verify DOI 10.1128/AEM.70.3.1617-1626.2004 and its abstract-level support for strain JT with M. hungatei; the NBRC page names NBRC 100397. The inspected metadata do not verify the `DSM 864 = ATCC 27890` alias or genome `CP000254` in the evidence explanations, and the ASM PDF was not accessible for a full-text check. | `target_organisms` evidence on the normalized TOGO owner. |

## Recommended Edits

1. Reconcile NBRC Medium 824 ownership. Map TOGO M1624's original NBRC_M824
   identity to `nbrc.medium:824`, decide whether `NBRC_825.yaml` or the TOGO
   owner is authoritative, and make the two records merge to one generated
   product.
2. Fix the TOGO stock-solution import boundary for M1624. Preserve the four
   stock additions as ML_PER_L, keep stock recipes nested or linked, and stop
   emitting stock-only components as final-medium ingredients.
3. Correct the stock-unit conversions in the maintained record or importer:
   keep vitamin, trace, and Se-W stock mg/L entries as stock concentrations;
   keep G_PER_L entries inside their stock solution; and keep KOH as trace-stock
   pH adjustment detail.
4. Port NBRC vial-culture preparation detail from the source page or the
   recovered direct NBRC owner into the reconciled maintained record.
5. Regenerate the merge output so the reviewed generated record picks up
   `organism_culture_type: community`, the repaired 1.0 water row, and the
   reconciled stock/preparation changes.
6. Revisit the target-organism evidence text after inspecting Qiu et al. 2004
   full text or a collection source that proves the NBRC/DSM/ATCC type-strain
   equivalence and CP000254 genome accession.

## Follow-up Checks

- Run the focused open schema, strict, reference, and term validators on the
  corrected normalized owner and regenerated merged record.
- Run `just verify-merges` to confirm the generated record matches its
  maintained owner and the NBRC duplicate no longer leaks as an unmatched
  source-equivalent recipe.
- Repeat a gitignore-independent exact scan for `TOGO:M1624`, `NBRC_M824`,
  `nbrc.medium:824`, and the NBRC `NO=824` URL to ensure they point to the
  reconciled owner set and expected indexes only.
- Manually compare the regenerated YAML against TOGO M1624, NBRC Medium 824,
  and `data/normalized_yaml/bacterial/NBRC_825.yaml` to confirm that stock
  boundaries, milliliter additions, mg/L stock values, gas flushing, and
  post-autoclave additions survived regeneration.

## Additional Notes

- Source fetches used the TOGO M1624 SPARQList API and the NBRC `NO=824` HTML
  page because the TOGO public `/medium/M1624` route is a SPA shell.
- PubMed eutils returned PMID 15006786 for DOI
  10.1128/AEM.70.3.1617-1626.2004 and listed PMCID PMC368352.
- All negative duplicate checks cited above used `rg --no-ignore --hidden` or
  `find`, so ignored files were included.
