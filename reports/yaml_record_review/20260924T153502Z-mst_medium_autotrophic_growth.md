# YAML Record Review: mst_medium_autotrophic_growth

- Repository: CultureMech
- Record: data/merge_yaml/merged/mst_medium_autotrophic_growth.yaml
- Started UTC: 2026-09-24T15:35:02Z
- Finished UTC: 2026-09-24T15:35:39Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mst_medium_autotrophic_growth.yaml`.

The generated record is `CultureMech:004143` and keeps the KOMODO source copy as
canonical:

- `media_term`: `komodo.medium:1416`
- `name`: `mst_medium_autotrophic_growth`
- `original_name`: `MST-MEDIUM, AUTOTROPHIC GROWTH`
- `ph_range`: 7.5-8.0
- `ingredients`: 14
- `merged_from`: `KOMODO_1416_MST-MEDIUM_AUTOTROPHIC_GROWTH`,
  `medium_1416_modified_for_dsm_25733`, and `mst_medium_autotrophic_growth`

The maintained owners involved in the merge are:

- `data/normalized_yaml/bacterial/KOMODO_1416_MST-MEDIUM_AUTOTROPHIC_GROWTH.yaml`
  with `id: CultureMech:004143` and `media_term: komodo.medium:1416`.
- `data/normalized_yaml/bacterial/medium_1416_modified_for_dsm_25733.yaml`
  with `id: CultureMech:004142` and `media_term: komodo.medium:1416_25733`.
- `data/normalized_yaml/bacterial/mst_medium_autotrophic_growth.yaml`
  with `id: CultureMech:000878` and `media_term: mediadive.medium:1416`.

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record has the right MST-MEDIUM name, DSMZ/MediaDive pH range, main salts,
and exact source-duplicate relationships, but the canonical survivor is the
KOMODO copy rather than the richer DSMZ/MediaDive owner. The KOMODO owner says
it came from KOMODO ID 1416 and explicitly cites DSMZ Medium 1416; the
strain-specific KOMODO owner says the same for ID `1416_25733`; the
MediaDive/DSMZ owner is the direct `mediadive.medium:1416` record and carries
the same local ingredient signature plus DSMZ preparation steps.

An exact ignored-file-inclusive search for `CultureMech:004143`,
`CultureMech:004142`, `CultureMech:000878`, `komodo.medium:1416`,
`komodo.medium:1416_25733`, and `mediadive.medium:1416` found these active
normalized owners, their generated merge, and registry/catalog/report mentions.
It did not show another active normalized owner for this same provider identity
outside the three known source records.

Most direct ingredient groundings match the chemical strings after hydration
normalization. `NiCl2 x 6 H2O` is the exception: the record grounds it to
generic `CHEBI:34887` / `nickel dichloride`, while the source string is the
hexahydrate salt and should remain hydrate-specific.

## Evidence

MediaDive REST and HTML for medium 1416 currently describe DSMZ
`MST-MEDIUM, AUTOTROPHIC GROWTH` with pH 7.5-8.0. The main 1000 ml solution
contains `Na2S2O3 x 5 H2O` 5 g, `NH4Cl` 1 g, `MgSO4 x 7 H2O` 0.5 g,
`K2HPO4` 4 g, `KH2PO4` 1.5 g, 1 ml `Trace element solution SL-10`, and
1000 ml distilled water. Its preparation step says to prepare the sodium
thiosulfate and magnesium sulfate as separate solutions, adjust to pH 7.5-8.0,
autoclave, then add sterile trace-element solution after autoclaving and
combining the solutions.

MediaDive solution 595, `Trace element solution SL-10`, is a 1000 ml stock with
10 ml 25% `HCl`, 1.5 g `FeCl2 x 4 H2O`, 70 mg `ZnCl2`, 100 mg
`MnCl2 x 4 H2O`, 6 mg `H3BO3`, 190 mg `CoCl2 x 6 H2O`, 2 mg
`CuCl2 x 2 H2O`, 24 mg `NiCl2 x 6 H2O`, 36 mg `Na2MoO4 x 2 H2O`, and
990 ml distilled water. Because the main solution uses only 1 ml SL-10 in
1000 ml final medium, every SL-10 ingredient in the final recipe is diluted
1:1000 from those stock concentrations.

The generated YAML instead lists the SL-10 stock concentrations as final g/L:
for example, it lists `FeCl2 x 4 H2O` at 1.5 g/L instead of 0.0015 g/L and
`NiCl2 x 6 H2O` at 0.024 g/L instead of 0.000024 g/L. It also omits the main
`Trace element solution SL-10` addition and the stock-water context that are
needed to reconstruct the DSMZ recipe hierarchy.

## Completeness

The generated record carries the DSMZ pH range and the full set of dissolved
compounds from the main solution and SL-10 stock, but it is not complete enough
to reproduce the medium because the nested stock is flattened at stock
strength. It also drops the two preparation steps that survive on the
MediaDive normalized owner:

- Prepare sodium thiosulfate and magnesium sulfate as separate solutions,
  adjust to pH 7.5-8.0, autoclave, combine, and add sterile trace-element
  solution.
- Dissolve `FeCl2` in HCl before diluting, adding the other SL-10 salts, and
  bringing the stock to 1000 ml.

`target_organisms` and structured `references` are absent. They are useful
future enrichment targets but were not treated as defects for this generated
record because the source duplicate merge and the imported MediaDive payload
already encode the medium identity and source URL.

## Findings

- The merge chose `CultureMech:004143` / `komodo.medium:1416` as canonical even
  though that record is a KOMODO source duplicate of DSMZ Medium 1416. The
  direct DSMZ/MediaDive owner, `CultureMech:000878`, contains the same local
  ingredient signature plus preparation steps, so the generated record loses
  source-native identity and preparation evidence.
- The generated record flattens `Trace element solution SL-10` at stock
  strength. The main DSMZ recipe adds 1 ml SL-10 per 1000 ml final medium, so
  `HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`,
  `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and
  `Na2MoO4 x 2 H2O` are all 1000x too concentrated.
- The generated record cannot represent the DSMZ stock hierarchy. It has the
  dissolved SL-10 salts as if they were direct ingredients, but no 1 ml/L
  `Trace element solution SL-10` edge and no stock-level distilled water entry.
- The generated `NiCl2 x 6 H2O` ingredient keeps the hydrate in
  `preferred_term` but grounds it to generic `CHEBI:34887` / `nickel
  dichloride`.
- The two KOMODO owners still carry malformed `komodo-web-import` timestamps
  such as `2026-01-27T01:15:02.fZ`, and the merged record inherits one of
  them.

## Recommended Edits

- Repair the maintained MediaDive owner and its KOMODO source duplicates, then
  regenerate `data/merge_yaml/merged/mst_medium_autotrophic_growth.yaml`.
- Prefer `data/normalized_yaml/bacterial/mst_medium_autotrophic_growth.yaml`
  as the canonical owner for DSMZ/MediaDive Medium 1416 so the generated
  record keeps `CultureMech:000878`, `mediadive.medium:1416`, and the DSMZ
  preparation steps.
- Preserve the SL-10 stock hierarchy if the schema can carry solution
  components. If it cannot, scale every SL-10 stock solute by 0.001 into final
  g/L while retaining notes that those values come from 1 ml/L
  `Trace element solution SL-10`.
- Ground `NiCl2 x 6 H2O` to an exact hydrate term instead of generic
  `CHEBI:34887`.
- Normalize the malformed KOMODO import timestamps to valid UTC datetimes.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record keeps the DSMZ/MediaDive preparation steps.
- Confirm the regenerated final SL-10 concentrations are 0.0015 g/L
  `FeCl2 x 4 H2O`, 0.00007 g/L `ZnCl2`, 0.0001 g/L `MnCl2 x 4 H2O`,
  0.000006 g/L `H3BO3`, 0.00019 g/L `CoCl2 x 6 H2O`, 0.000002 g/L
  `CuCl2 x 2 H2O`, 0.000024 g/L `NiCl2 x 6 H2O`, and 0.000036 g/L
  `Na2MoO4 x 2 H2O`.
- Run an ignored-file-inclusive exact search for `komodo.medium:1416_25733`
  after repair to make sure the strain-specific duplicate still points at the
  intended canonical owner.

## Additional Notes

The current local `medium_1416_modified_for_dsm_25733.yaml` ingredient list is
identical to KOMODO 1416 and DSMZ/MediaDive 1416. No external KOMODO record for
`1416_25733` was used in this review, so the `1416_25733` record was evaluated
only as a local source duplicate and not as a separately confirmed strain
variant.
