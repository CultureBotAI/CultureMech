# YAML Record Review: LACTOBACILLUS MEDIUM I

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml
- Started UTC: 2026-09-23T18:19:55Z
- Finished UTC: 2026-09-23T18:20:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml`; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:002368` |
| Name | `lactobacillus_medium_i` |
| Original name | `LACTOBACILLUS MEDIUM I` |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Source accession | `mediadive.medium:J11` |
| Merge fingerprint | `9d32eca6620b3b3fc94a0fc6cedb5f6dacf26dae3cb460d9c730088b98a4b266` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml` |

The reviewed YAML is the generated MediaDive/JCM `J11` representation of
Lactobacillus Medium I. It is a stale merge with respect to September 13 exact
MIM-index mappings, and its maintained owner still needs source curation for
source units, missing water, and the parallel TOGO `M4` import of the same JCM
recipe.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml` | Passed; no output |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml --out /private/tmp/lactobacillus_medium_i__9d32eca6.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:002368` and `mediadive.medium:J11` identify MediaDive's JCM
  Medium J11 import, named `LACTOBACILLUS MEDIUM I`, with pH 6.0.
- The original JCM URL for `GRMD=11` currently returns an HTML `Nothing found`
  page. The live MediaDive REST payload for `J11` still resolves and reports
  the full medium as `Main sol. J11`.
- TOGO `M4` is a same-original sibling for JCM `GRMD=11`, stored separately at
  `data/normalized_yaml/bacterial/TOGO_M4_Lactobacillus_Medium_I.yaml` and
  generated as `data/merge_yaml/merged/LACTOBACILLUS_MEDIUM_I.yaml`.
- The generated target is stale for five local ingredient mappings now present
  in the normalized owner: Tryptone `MICRO:0000182`, Tryptose `MICRO:0000183`,
  Yeast extract `FOODON:03315426`, Tomato juice `FOODON:03301454`, and Liver
  extract concentrate `MICRO:0001363`.
- The generated CHEBI mappings for polysorbate 80, glucose, lactose, and agar
  match the literal MediaDive `J11` ingredient labels.

An ignored-inclusive exact search was run with digit boundaries around
`mediadive.medium:J11` and `GRMD=11` over `data/normalized_yaml`,
`data/merge_yaml`, and `reports/archive`. It found the reviewed generated
target, its normalized MediaDive owner, normalized source indexes, the
same-JCM TOGO `M4` owner, and the separate generated `LACTOBACILLUS_MEDIUM_I`
TOGO output. A looser search for plain `J11` had overmatched `J110` through
`J1199`; those results were discarded before judging duplicates.

## Evidence

Supported in inspected sources:

- MediaDive `/rest/medium/J11` reports `complex_medium: yes`, `source: JCM`,
  the JCM link, pH 6.0, and one 1200 ml solution containing Tryptone 20 g,
  Tryptose 5 g, Yeast extract 5 g, Tomato juice 200 ml, Liver extract
  concentrate 1 g, Tween 80 50 mg, Glucose 3 g, Lactose 2 g, Agar 15 g,
  Distilled water 1000 ml, and one step to adjust pH to 6.0.
- The MediaDive-derived generated target preserves the MediaDive 1200 ml
  mass-normalized values for Tryptone, Tryptose, Yeast extract, Liver extract
  concentrate, Tween 80, Glucose, Lactose, and Agar.
- TOGO M4 also cites JCM `GRMD=11`, names the source as `JCM_M11`, reports pH
  6.0, and exposes the nominal recipe with 1 L distilled water, 200 ml filtered
  pH 7.0 tomato juice, and the same dry ingredients.

Unsupported or stale in the generated target:

- Distilled water is absent from the MediaDive/JCM target even though the live
  MediaDive `J11` payload includes `Distilled water`, 1000 ml, as recipe order
  10.
- The generated `Tomato juice` row is encoded as `200 G_PER_L`, but MediaDive
  reports 200 ml and no `g_l` normalized value for that volume ingredient.
- The target still lacks the September 13 exact ingredient groundings now
  present in `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml`.
- The target has no `references` list and its sole human JCM link now fails to
  retrieve the medium.

## Completeness

Consequential gaps:

- Source units for volume components need curation; water is missing and tomato
  juice has a mass concentration that is not in the inspected source.
- The TOGO `M4` and MediaDive `J11` imports are parallel representations of the
  same JCM medium but remain separate CultureMech records with divergent amount
  normalization and duplicate generated outputs.
- Current source recovery is incomplete. MediaDive REST and TOGO API both carry
  cached or transformed JCM `GRMD=11` data, but the current JCM page itself did
  not return the recipe text.

Empty or absent fields that are not defects for this generated source recipe:

- `target_organisms`, growth metrics, genome assembly, atmosphere, storage, and
  shelf-life fields can stay empty until strain-level evidence is curated.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | The MediaDive/JCM record omits the source water ingredient. | MediaDive `/rest/medium/J11` includes `Distilled water`, 1000 ml, as recipe order 10; neither the generated target nor `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml` has a water ingredient. | `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml`, or the MediaDive import transform if it systematically drops JCM water rows. |
| Major | The tomato juice volume was converted to an unsupported mass concentration. | MediaDive reports 200 ml tomato juice and no `g_l` for that row; the generated target records `200 G_PER_L`. | `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml`, and the importer if ml rows are being forced through `G_PER_L`. |
| Major | The generated target is stale relative to its normalized owner. | The normalized owner has a September 13 mapping event and five additional local ingredient groundings absent from the August generated merge. | Regenerate `data/merge_yaml/merged/` with `just merge-recipes`; if the mappings are lost, fix `src/culturemech/merge/merge_recipes.py`. |
| Major | JCM `GRMD=11` is duplicated as separate MediaDive `J11` and TOGO `M4` CultureMech records. | Ignored-inclusive search found `data/normalized_yaml/bacterial/TOGO_M4_Lactobacillus_Medium_I.yaml`, and live TOGO M4 reports `original_media_id: JCM_M11` with the same JCM URL as the reviewed MediaDive owner. | Reconcile `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml` and `data/normalized_yaml/bacterial/TOGO_M4_Lactobacillus_Medium_I.yaml` through the normalized merge/source-identity path. |
| Minor | The only human source URL in the generated notes no longer serves the recipe. | Fetching `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=11` returned a JCM page saying nothing was found for medium no. 11. | Add recoverable source references or cached upstream provenance to the normalized owner while preserving the original JCM URL as historical source metadata. |

## Recommended Edits

1. Add the `Distilled water` row from MediaDive `J11` to
   `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml` without
   guessing a mass concentration.
2. Correct the `Tomato juice` row so its 200 ml source quantity is not expressed
   as `200 G_PER_L`.
3. Reconcile MediaDive `J11` with TOGO `M4`; choose and document either the
   1200 ml MediaDive normalization or the nominal TOGO/JCM 1 L water recipe, then
   merge or cross-link the duplicated CultureMech IDs accordingly.
4. Add a recoverable reference path for the inspected MediaDive REST and TOGO
   API data because the live JCM `GRMD=11` page is no longer sufficient by
   itself.
5. Regenerate `data/merge_yaml/merged/` and confirm the September 13 local
   ingredient mappings appear in
   `data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml`.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against
  `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml` after water,
  tomato, and provenance edits.
- Run `just merge-recipes`, then rerun the focused validators against
  `data/merge_yaml/merged/lactobacillus_medium_i__9d32eca6.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated file
  is no longer drifted.
- Re-query MediaDive `J11`, TOGO `M4`, and JCM `GRMD=11` while reconciling the
  duplicated source records.
- Search with ignored files included for exact `GRMD=11` and
  `mediadive.medium:J11` after duplicate reconciliation to confirm only the
  intended owners remain.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, its normalized MediaDive owner, live
  MediaDive `J11`, live JCM `GRMD=11`, the TOGO `M4` API payload, and the
  normalized/generated TOGO `M4` sibling.
- The archived March validation reports still reference the old
  `JCM_J11_LACTOBACILLUS_MEDIUM_I.yaml` path; current ownership is
  `data/normalized_yaml/bacterial/lactobacillus_medium_i.yaml`.
