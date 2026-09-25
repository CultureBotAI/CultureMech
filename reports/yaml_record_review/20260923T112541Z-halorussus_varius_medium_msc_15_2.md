# YAML Record Review: HALORUSSUS VARIUS MEDIUM (MSC 15.2)

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml`
- Started UTC: 2026-09-23T11:24:19Z
- Finished UTC: 2026-09-23T11:25:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:001167` |
| Name | `halorussus_varius_medium_msc_15_2` |
| Original name | `HALORUSSUS VARIUS MEDIUM (MSC 15.2)` |
| Category | `archaea` |
| Physical state | `SOLID_AGAR` |
| Generated from | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` |
| Source accession | `mediadive.medium:1685` |
| Source PDF | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1685.pdf` |
| Merge fingerprint | `8dc5c04a75a507b80d51a08cacf9e240550acea34010b7ee861a4de1f8ae1aed` |

I reviewed the generated merged record, its direct MediaDive/DSMZ normalized
owner, the DSMZ Medium 1685 PDF, the MediaDive 1685 REST payload, and a rendered
PNG of the DSMZ PDF to confirm a formula conflict in the extracted text.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `halorussus_varius_medium_msc_15_2`,
`HALORUSSUS VARIUS MEDIUM`, `mediadive.medium:1685`, `DSMZ Medium 1685`, and
`DSMZ_Medium1685`. Ignored files were included. The search found only the
normalized DSMZ 1685 owner and the generated merge for this medium.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml --out /private/tmp/halorussus_varius_medium_msc_15_2.strict.tsv --workers 1 --quiet` exited 0 and wrote a header-only TSV. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record identity matches MediaDive medium 1685,
`HALORUSSUS VARIUS MEDIUM (MSC 15.2)`, and the normalized/generated record is a
single-source MediaDive import. The current DSMZ Medium 1685 PDF has the same
title, FeEDTA solution, and trace element solution, but its main-solution
formula no longer matches the MediaDive payload that was imported.

Several exact chemical forms are under-grounded. The generated rows preserve
labels such as `CaCl2 x H2O`, `MgSO4 x 6 H2O`, and `NiCl2 x 6 H2O`, but their
ontology links are generic calcium dichloride, magnesium sulfate, and nickel
dichloride or otherwise not exact to the supplied hydrate form.

## Evidence

The generated record follows MediaDive 1685 for `NaCl` 210.21 g/L, `MgCl2 x 6
H2O` 23.4 g/L, `NaNO3` 9.44 g/L, `CaCO3` 0.015 g/L, and pH 6.9. The current
DSMZ Medium 1685 PDF instead lists 110 g NaCl, no MgCl2 row, no NaNO3 row,
2.80 g CaCO3, 3.00 g `MgSO4 x 6 H2O` rather than MediaDive's 4.49 g, 0.60 g
`SrCl2 x 6 H2O` rather than MediaDive's 0.63 g, and instructs adjustment to
pH 5.0-8.5.

Within the MediaDive payload, the main medium references 1 ml FeEDTA solution
and 1 ml trace element solution. The generated record flattens both stock
recipes into top-level ingredients at stock concentrations:

| Stock | Source addition | Flattened generated rows |
|---|---:|---|
| `FeEDTA solution` | 1 ml/L | `FeSO4 x 7 H2O` 1.54 g/L and `Na-EDTA` 2.06 g/L |
| `Trace element solution` | 1 ml/L | Nitrilotriacetic acid, Fe ammonium sulfate, sodium selenate, Co, Mn, Mo, W, Zn, Al, Ni, B, Cu, and MnCl2 at stock g/L |

The generated record also drops the 1000 ml distilled-water rows from the main
solution, FeEDTA stock, and trace element stock. The trace element stock
preparation steps are present, but they are stored as main-medium steps, so pH
6.5/7.0 KOH adjustments that apply only to the trace stock are no longer scoped
to that solution.

## Completeness

The target organism backfill contains only `HALORUSSUS VARIUS` as a
`preferred_term`. The medium title supports an association with H. varius, but
the generated record does not ground that organism to a taxon ID or provide
growth evidence.

No incubation temperature, atmosphere, or storage conditions are present in the
MediaDive 1685 payload. Their absence is not a defect.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The imported MediaDive main-solution formula conflicts with the current DSMZ 1685 PDF. | Current DSMZ 1685 lists 110 g NaCl, no MgCl2, no NaNO3, 2.80 g CaCO3, and pH 5.0-8.5; the generated record has MediaDive's older/different NaCl, MgCl2, NaNO3, CaCO3, and pH 6.9 values. | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` or the DSMZ/MediaDive import snapshot |
| Major | FeEDTA and trace element stocks were flattened into the main ingredient list. | MediaDive references each stock at 1 ml/L from the main solution, while the generated record imports every stock component as a top-level g/L ingredient. | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` or the MediaDive importer |
| Major | Water and stock-solution boundaries are missing. | MediaDive contains 1000 ml water in the main solution and both stocks. The generated record has no water rows and no FeEDTA or trace solution references. | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` or the MediaDive importer |
| Major | Trace-stock pH steps are attached to the medium instead of the trace element solution. | `First dissolve nitrilotriacetic acid...` and `Final pH 7.0 (with KOH).` are steps of MediaDive solution 3063, not final-medium preparation steps. | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` or the MediaDive preparation importer |
| Minor | Several hydrated or legacy ingredient groundings are stale or too broad. | `KNO3` and `NaNO3` still carry legacy `mediaingredientmech_term` fields; `MgSO4 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to generic salts. | MIM/CHEBI refresh logic or the normalized record |
| Minor | The target organism is not taxon-grounded. | The record names `HALORUSSUS VARIUS` but has no NCBITaxon term or growth evidence. | `data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml` |

## Recommended Edits

1. Reconcile MediaDive 1685 against the current DSMZ Medium 1685 PDF, either
   by updating the normalized record to the current PDF values or by adding
   explicit version provenance if the MediaDive values reflect a retained older
   DSMZ formulation.
2. Preserve FeEDTA and trace element solution recipes as stock solutions and
   reference each from the main medium at 1 ml/L.
3. Restore 1000 ml distilled water to the main solution and both stock
   solutions.
4. Scope the nitrilotriacetic-acid/KOH preparation steps to the trace element
   solution only.
5. Refresh KNO3 and NaNO3 MIM/CHEBI fields and either exact-ground or
   explicitly unground ambiguous supplied hydrates such as `MgSO4 x 6 H2O` and
   `NiCl2 x 6 H2O`.
6. Ground `HALORUSSUS VARIUS` to the correct taxon and add source-scoped
   evidence if it remains as a target organism assertion.
7. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halorussus_varius_medium_msc_15_2.yaml` directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml`
   after the normalized DSMZ 1685 record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/archaea/halorussus_varius_medium_msc_15_2.yaml`
   to confirm nitrate, hydrate, stock-ingredient, and target-organism grounding.
3. Run `just verify-merges` to prove the generated DSMZ 1685 branch
   regenerates from the corrected normalized owner.
4. Manually compare the regenerated record with the current DSMZ Medium 1685
   PDF and MediaDive 1685 to make sure any retained formula/version conflict is
   explicitly documented.

## Additional Notes

None found.
