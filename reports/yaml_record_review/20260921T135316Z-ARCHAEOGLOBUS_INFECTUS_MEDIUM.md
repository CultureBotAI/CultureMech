# YAML Record Review: ARCHAEOGLOBUS INFECTUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml
- Started UTC: 2026-09-21T13:52:31Z
- Finished UTC: 2026-09-21T13:53:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000529 |
| Name | archaeoglobus_infectus_medium |
| Original name | ARCHAEOGLOBUS INFECTUS MEDIUM |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source | DSMZ / MediaDive medium 1098 |
| Source term | mediadive.medium:1098 |
| Generated record | data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml |
| Merge fingerprint | 3953d679f42c878975fa8c8895c44fe81edef6774b88e902956990f1bce25b19 |

The target is a generated duplicate merge from two normalized source records:

| Source role | Path | ID | Source ID |
|---|---|---|---|
| Canonical DSMZ/MediaDive owner | data/normalized_yaml/archaea/archaeoglobus_infectus_medium.yaml | CultureMech:000529 | mediadive.medium:1098 |
| KOMODO duplicate | data/normalized_yaml/bacterial/arc51_medium.yaml | CultureMech:003750 | komodo.medium:1098 |

Any fix to the DSMZ recipe should be made in both normalized owners, or in the
shared importer/repair path that generates them, and then propagated by
regenerating the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml --out /private/tmp/ARCHAEOGLOBUS_INFECTUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The canonical half of the merge identifies the expected DSMZ recipe: DSMZ
medium 1098, `ARCHAEOGLOBUS INFECTUS MEDIUM`, final pH 6.5, and the DSMZ PDF
URL all agree with the inspected DSMZ Medium 1098 PDF. The `arc51_medium`
KOMODO duplicate is already explicitly tied to the same DSMZ/MediaDive medium:
its notes say `DSMZ Medium: 1098 (mediadive.medium:1098)`, its 2026-08-15
history says it reproduces MediaDive medium 1098 across 31 shared compounds at
identical values, and the generated record preserves it as a `SOURCE_DUPLICATE`
synonym.

An ignored-file-inclusive bounded search for
`CultureMech:000529|mediadive\.medium:1098|ARCHAEOGLOBUS_INFECTUS_MEDIUM|archaeoglobus_infectus_medium\.yaml|arc51_medium\.yaml|komodo\.medium:1098`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found the canonical owner,
the KOMODO duplicate owner, the generated merge, and their registry, catalog,
manifest, and index rows. It did not find a third maintained source record for
DSMZ/MediaDive 1098 or KOMODO 1098 in the searched corpus.

The base-medium ingredients have appropriate groundings where a discrete ChEBI
identity is available. `Sea Salt` and yeast extract are mixtures and are
correctly left ungrounded.

## Evidence

The DSMZ Medium 1098 PDF supports the final recipe: final volume 1002 ml,
35 g Sea Salt, 0.10 g NH4Cl, 0.05 g KH2PO4, 1.60 g Na-acetate, 0.10 g yeast
extract, 1.00 ml Wolfe's mineral elixir, 0.50 ml 0.1% sodium resazurin,
2.00 g NaHCO3, 0.14 g 2-mercaptoethanesulfonate, 1.00 ml Seven vitamins
solution, 2.50 g `Na2S2O3 x 5 H2O`, 0.30 g DL-dithiothreitol, and 1000 ml
distilled water. The generated record has the correctly normalized gram-scale
base ingredients and correctly derives the resazurin mass from a 0.1% w/v
solution, but it omits the 1000 ml water row.

The same PDF defines two 1 ml/L stock additions. Wolfe's mineral elixir is a
1 L stock with magnesium, manganese, sodium, iron, cobalt, calcium, zinc,
copper, aluminum potassium sulfate, boric acid, molybdate, nickel, tungstate,
selenate, and water. Seven vitamins solution is a 1 L stock with vitamin B12,
p-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate, pyridoxine
hydrochloride, thiamine hydrochloride dihydrate, and water.

The generated merge still flattens all stock solutes as final `G_PER_L`
ingredients. Both maintained owners were partially repaired after this merge
was generated: they now move MnSO4, FeSO4, CoCl2, and ZnSO4 under Wolfe's
mineral elixir, and vitamin B12, nicotinic acid, pyridoxine hydrochloride, and
thiamine-HCl under Seven vitamins solution. Thirteen stock solutes remain at
top level in both owners: `MgSO4 x 7 H2O`, NaCl, `CaCl2 x 2 H2O`,
`CuSO4 x 5 H2O`, `AlK(SO4)2 x 12 H2O`, H3BO3, `Na2MoO4 x 2 H2O`,
`(NH4)2Ni(SO4)2 x 6 H2O`, `Na2WO4 x 2 H2O`, `Na2SeO4`,
p-aminobenzoic acid, `D-(+)-biotin`, and calcium pantothenate.

## Completeness

The record is complete enough for medium identity, final pH, gas handling,
post-inoculation pressure, and the gram-scale ingredients in DSMZ 1098's main
formulation. It is incomplete for stock representation and water:

- The generated merge lacks the Wolfe's mineral elixir and Seven vitamins
  solution structure that already exists in both maintained owners.
- Both maintained owners still keep most Wolfe and vitamin solutes as direct
  final-medium ingredients at stock strength.
- DSMZ 1098's 1000 ml distilled water row is absent from the generated record
  and both maintained owners.
- The stock water rows are not represented structurally; the stock
  `preparation_notes` say the stocks were prepared in 1000 ml, but there is no
  `Distilled water` component under either solution.
- The absent target organisms, variants beyond the KOMODO source duplicate,
  and primary growth references are not defects for this source recipe import;
  DSMZ medium pages define recipes and do not, by themselves, assert growth of
  one strain under one tested condition.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to both normalized owners. | The generated file was written on 2026-08-06 with all stock solutes flattened. `data/normalized_yaml/archaea/archaeoglobus_infectus_medium.yaml` was partially nested on 2026-08-07, and `data/normalized_yaml/bacterial/arc51_medium.yaml` was partially nested on 2026-08-15. | Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml` after curating both normalized owners. |
| Major | Thirteen Wolfe/vitamin stock solutes are still represented as final-medium `G_PER_L` ingredients instead of as 1 ml/L stock components. | DSMZ 1098 lists Wolfe's mineral elixir and Seven vitamins solution as 1.00 ml additions. The maintained owners still keep ten Wolfe solutes and three vitamin solutes at stock strength in `ingredients`. | `data/normalized_yaml/archaea/archaeoglobus_infectus_medium.yaml`, `data/normalized_yaml/bacterial/arc51_medium.yaml`, or the stock-nesting repair. |
| Major | The 1000 ml final-medium water row from DSMZ 1098 is missing. | DSMZ 1098 lists 1000.00 ml distilled water in the main formulation; neither normalized owner nor the generated merge contains a final-medium distilled-water ingredient. | The MediaDive/DSMZ import or both normalized owners. |
| Minor | The stock water rows are only implicit in preparation notes. | The inspected DSMZ PDF lists 1000.00 ml distilled water under both Wolfe's mineral elixir and Seven vitamins solution. Both normalized owners have `preparation_notes: Stock prepared in 1000 ml` but no water component in either `solutions[].composition`. | Both normalized owners, if the schema intends solution water to be explicit. |

No blockers found.

## Recommended Edits

1. Complete stock nesting in both normalized owners by moving the remaining
   Wolfe's mineral elixir and Seven vitamins solution solutes under the
   appropriate `solutions` entry at 1 ml/L.
2. Add the DSMZ 1098 main distilled-water row to both normalized owners.
3. Decide whether stock-solution distilled water should be explicit in
   `solutions[].composition`; if yes, add the 1000 ml water rows from the DSMZ
   stock tables.
4. Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml` and
   downstream pages/indexes from the maintained normalized records so the
   generated merge reflects the post-2026-08-15 owner state.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation for both normalized
  owners after curation.
- Re-run the merge generator and inspect
  `data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml` to confirm it has
  two stock solutions, no Wolfe or vitamin stock solutes at top level, and a
  main distilled-water row.
- Re-run the media-content manifest and confirm both owners no longer report
  `23` top-level ingredients and `8` nested ingredients.
- Inspect the rendered page and ensure Wolfe's mineral elixir and Seven
  vitamins solution appear as stock additions at 1 ml/L rather than as final
  grams-per-liter ingredients.

## Additional Notes

- The generated record's `parent_media.path` correctly points at
  `data/normalized_yaml/bacterial/arc51_medium.yaml`; this was verified with an
  ignored-file-inclusive exact search and `find data/normalized_yaml -name
  '*arc51*'`.
- `reports/media_content_review_manifest.tsv` marks both maintained owners as
  `PASS`, but that status is stale relative to the remaining stock-boundary
  and water findings.
