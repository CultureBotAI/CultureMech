# YAML Record Review: Archaeoglobus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml
- Started UTC: 2026-09-21T13:58:09Z
- Finished UTC: 2026-09-21T13:58:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008134 |
| Name | archaeoglobus_medium |
| Original name | Archaeoglobus Medium |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source | TOGO:M1584 / NBRC_M392 |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml |
| Generated record | data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml |
| Merge fingerprint | 4c1aa7de2807908784127e7ceeac8a1a41499959e0edd38f581b954d3f78f0f3 |

The target is a generated one-source merge whose maintained input is
`data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml`. Any fix
should be made in that normalized owner or in the TOGO/NBRC import transform and
then propagated by regenerating the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml --out /private/tmp/archaeoglobus_medium__4c1aa7de.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The generated record identifies the expected NBRC/TOGO recipe. `media_term.id`
is `TOGO:M1584`, `media_term.label` is `Archaeoglobus Medium`, and the
inspected TOGO M1584 API names NBRC_M392 as its original medium. The live NBRC
Medium 392 page was also fetched and lists `<i>Archaeoglobus</i> Medium`.

An ignored-file-inclusive bounded search for
`CultureMech:008134|TOGO:M1584|TOGO_M1584_Archaeoglobus_Medium|archaeoglobus_medium__4c1aa7de`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found one maintained owner,
the generated merge, registry/catalog/manifest/index rows, one
`INDICATOR_UNIT_SLIP` diagnostic, and two `DIFFERING_PARTS` diagnostics. It did
not find a second maintained normalized record for `TOGO:M1584` in the searched
corpus.

Most simple ingredient groundings match the source chemical forms. Three
grounding gaps remain: `NiCl2*6H2O` links to `CHEBI:34887`, labeled nickel
dichloride rather than nickel chloride hexahydrate; `Na2WO4*H2O` still has a
legacy `MediaIngredientMech:000309` link instead of a ChEBI term; and the
`Trace element solution*` stock links to `mediadive.solution:6187`, which is
not the same formula as the inline NBRC 392 stock table.

## Evidence

The inspected TOGO M1584 API and NBRC Medium 392 page agree on the core
formulation: 1 L distilled water, 3.45 g `MgSO4*7H2O`, 18 g NaCl, 0.14 g
`CaCl2*2H2O`, 0.25 g NH4Cl, 0.14 g K2HPO4, 1 mg resazurin, 4 g
`MgCl2*6H2O`, 0.5 g `Na2S*9H2O`, 0.34 g KCl, 3 g NaHCO3, 1.5 g sodium
lactate, 2 mg `Fe(NH4)2(SO4)2*7H2O`, 0.5 g Bacto Yeast Extract, and 10 ml
`Trace element solution*`.

The generated merge and normalized owner do not preserve that structure. Three
stock rows are summed into separate base-medium rows:

| Component | NBRC 392 base row | NBRC trace-stock row | Record row |
|---|---:|---:|---:|
| MgSO4*7H2O | 3.45 g | 3.0 g per liter of stock | 6.45 `G_PER_L` |
| NaCl | 18.0 g | 1.0 g per liter of stock | 19.0 `G_PER_L` |
| CaCl2*2H2O | 0.14 g | 0.1 g per liter of stock | 0.24000000000000002 `G_PER_L` |

The source stock table also contains milligram rows that were converted to
grams per liter without scaling the numeric value: 4 mg
`KAl(SO4)2*12H2O`, 0.8 mg `Na2SeO3*5H2O`, and 0.8 mg `Na2WO4*H2O` appear as
4, 0.8, and 0.8 `G_PER_L` respectively. The main-medium resazurin and ferrous
ammonium sulfate milligram rows were imported as 1 and 2 `G_PER_L`.

The NBRC page carries two procedural paragraphs. The final-medium paragraph
boils the base ingredients except bicarbonate and sulfide, cools under
`N2/CO2` 80/20, adds bicarbonate, adjusts to pH 6.9, dispenses under the same
gas into serum bottles, pressurizes to 2 bar overpressure, autoclaves, and
reduces before use with sterile anaerobic sodium sulfide stock. The
trace-stock paragraph dissolves nitrilotriacetic acid first and adjusts pH
with KOH. The record drops both paragraphs and keeps only variable placeholder
rows for sodium bicarbonate, carbon dioxide gas, nitrogen gas, and KOH.

## Completeness

The record is complete enough for source identity and for several base-medium
gram quantities. It is incomplete for source units, trace-stock structure, and
preparation:

- The generated merge is stale relative to its owner: it still has a 2.0
  `G_PER_L` water row, while the owner collapsed the duplicate 1 L water rows
  back to one row on 2026-09-02.
- The 10 ml trace stock is represented as a 10 `G_PER_L` `Unknown solution`
  linked to the wrong MediaDive solution.
- The NBRC trace-stock solutes are flattened at full stock concentrations.
- The source milligram rows are represented as grams per liter.
- The NBRC gas, pressure, pH, bicarbonate, autoclave, sulfide-addition, and KOH
  instructions are missing.
- The absent target organisms, variants, and primary growth references are not
  defects for this source recipe import; NBRC medium pages define recipes and
  do not, by themselves, assert strain-level growth outcomes.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale for the water row. | The generated file still has `Distilled water` at 2.0 `G_PER_L`. The maintained owner was repaired on 2026-09-02 to collapse two identical duplicate 1 L rows into 1.0. | Regenerate `data/merge_yaml/merged/archaeoglobus_medium__4c1aa7de.yaml` from `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml`. |
| Major | The NBRC inline trace stock is flattened into the final medium and linked to the wrong stock identity. | NBRC 392 and TOGO M1584 list `Trace element solution*` as a 10 ml addition with an inline source-specific composition. The YAML links it to `mediadive.solution:6187`, leaves the solution composition empty, and stores the trace-stock solutes as top-level ingredients. | `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml` or the TOGO/NBRC importer. |
| Major | Source milligram rows were imported as grams per liter. | NBRC 392 lists 1 mg resazurin, 2 mg `Fe(NH4)2(SO4)2*7H2O`, 4 mg `KAl(SO4)2*12H2O`, 0.8 mg `Na2SeO3*5H2O`, and 0.8 mg `Na2WO4*H2O`; the record stores them as 1, 2, 4, 0.8, and 0.8 `G_PER_L`. `concentration_plausibility.tsv` already flags the resazurin row. | `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml` or the TOGO/NBRC importer. |
| Major | Duplicate cleanup summed trace-stock solutes with base-medium solutes. | `MgSO4*7H2O`, NaCl, and `CaCl2*2H2O` each occur once in the base medium and once in the trace stock; the record sums the two contexts into one final-medium row. `merged_duplicates.tsv` flags MgSO4 and NaCl as differing-part sums; the CaCl2 row carries the same `[Merged 2 duplicates: 0.14, 0.1]` note in the YAML. | `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml`; also audit the duplicate-merge rule that ran before stock boundaries were represented. |
| Major | NBRC preparation text was dropped. | The live NBRC page describes N2/CO2 gassing, bicarbonate addition, pH 6.9 adjustment, 2 bar bottle pressure, autoclaving, reduction with sterile sodium sulfide, and the KOH-adjusted trace-stock protocol; none of those are represented as preparation steps. | `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml` or the TOGO/NBRC importer. |
| Minor | Some trace-stock groundings are incomplete or too broad. | `NiCl2*6H2O` is linked to nickel dichloride rather than an explicit hexahydrate, and `Na2WO4*H2O` still has only a legacy MediaIngredientMech link. | `data/normalized_yaml/archaea/TOGO_M1584_Archaeoglobus_Medium.yaml`. |

No blockers found.

## Recommended Edits

1. Regenerate the generated merge after the 2026-09-02 water repair so it no
   longer publishes 2.0 `G_PER_L` water.
2. Replace the empty `mediadive.solution:6187` solution with a source-specific
   10 ml/L `Trace element solution*` containing the NBRC 392 inline formula.
3. Move trace-stock solutes out of top-level `ingredients`, split MgSO4, NaCl,
   and CaCl2 back into final-medium and trace-stock rows, and correct all
   milligram rows to the proper unit scale.
4. Add NBRC-backed preparation notes for the main medium and for the KOH-adjusted
   trace stock.
5. Re-ground `NiCl2*6H2O` and `Na2WO4*H2O` to exact ChEBI terms if those exact
   hydrates are available.
6. Regenerate downstream merged YAML and pages/indexes from the maintained
   normalized owner.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation for the normalized
  owner after curation.
- Re-run duplicate-merge and concentration-plausibility diagnostics and confirm
  this record no longer has stock/final sums or indicator milligram unit slips.
- Inspect the regenerated `archaeoglobus_medium__4c1aa7de.yaml` to confirm the
  source-specific trace stock appears once at 10 ml/L and the final water row is
  no longer duplicated.
- Inspect the rendered page and ensure the NBRC final-medium and trace-stock
  preparation paragraphs are attached to the correct scopes.

## Additional Notes

- The NBRC source page for medium 392 was fetched directly; it still contains
  the full Archaeoglobus Medium recipe and inline `*Trace element solution`
  table.
- `reports/media_content_review_manifest.tsv` correctly marks the normalized
  owner as `NEEDS_REVIEW`.
