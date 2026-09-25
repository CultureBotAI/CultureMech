# YAML Record Review: Bacillus AA Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
- Started UTC: 2026-09-21T17:21:21Z
- Finished UTC: 2026-09-21T17:24:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009980 |
| Generated record | data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml |
| Label | Bacillus AA Medium |
| Source identity | TOGO M584, imported from JCM_M579 / JCM GRMD=579 |
| Merge state | Single-source merge from `TOGO_M584_Bacillus_AA_Medium` |

The reviewed file is a derived merge artifact. Future edits should be made in
`data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`, then
`data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml` and page/browser products
should be regenerated.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

I ran the schema, strict, reference, and term checks through an offline
`uv --no-project` Python 3.11 tool environment because direct project `just`
validation attempts currently enter the Python 3.13 dependency resolver and
fail while building `llvmlite==0.46.0`, before the target-specific validation
code runs.

## Identity and Grounding

- **Medium identity is correct.** The stable ID, filename, `media_term`
  (`TOGO:M584` / Bacillus AA Medium), notes, and TOGO M584 metadata all point
  to JCM GRMD=579, "Bacillus AA Medium".
- **TOGO-to-JCM provenance agrees.** The inspected TOGO M584 API record reports
  `original_media_id: JCM_M579` and
  `src_url: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579`, matching
  the generated record's `notes`.
- **Chemical grounding is only partial.** Simple salts with exact forms such as
  NaCl, KH2PO4, K2HPO4, KCl, MgCl2*6H2O, CaCl2, CO2, and N2 have plausible
  CHEBI groundings. The source stock solutions, however, are modeled as either
  unresolved top-level ingredients or misleading global `mediadive.solution`
  terms rather than local sub-recipes of JCM 579.

## Evidence

- **The high-level ingredient labels are source-derived but the record loses
  the source's stock boundaries.** JCM 579 and TOGO M584 describe Solution A as
  a 1 L stock containing KH2PO4 0.3 g, K2HPO4 0.3 g, NH4Cl 1.0 g, NaCl 1.0 g,
  KCl 0.1 g, yeast extract 1.0 g, 10 ml trace minerals, and water to 1 L. They
  describe a separate 10 ml Solution B stock containing CaCl2 0.1 g,
  MgCl2*6H2O 0.5 g, and water.
- **The final additions are per 10 ml, not grams per liter.** The JCM page says
  to add 0.1 ml Solution B, 0.2 ml 1.0 M sodium acetate, and 0.4 ml 5% NaHCO3
  solution to complete each 10 ml of medium; TOGO M584 exposes those as `ml`
  additions.
- **The current `mediadive.solution:5342` / `5343` links are not evidence for
  this recipe.** The local `Solution A` and `Solution B` blocks in JCM 579 have
  no MediaDive accessions. The repository's `mediadive_5342_Solution_A.yaml`
  and `mediadive_5343_Solution_B.yaml` contain unrelated Solution A/B recipes,
  for example a 500 ml stock with yeast extract, casamino acids, glutamate,
  citrate, sulfates, KCl, and 100 g/L NaCl for `5342`, and an 80 g/L Na2CO3 plus
  100 g/L NaCl stock for `5343`.
- **The trace-minerals reference is resolvable but not represented.** JCM 579
  points to JCM Medium No. 151. TOGO M584 normalizes the same cross-reference as
  `reference_media_id: M142`, and inspected TOGO M142 maps to
  `original_media_id: JCM_M151`. The current Bacillus AA record only keeps an
  empty `Trace minerals (see Medium [M142])` solution at `10 G_PER_L`.
- **Preparation evidence is dropped.** JCM 579 states pH 7.2, a 4:1 N2-CO2 gas
  mixture while dispensing into sealed tubes before autoclaving, aseptic
  post-autoclave additions per 10 ml, and autoclaving Solution B under N2.
  None of those preparation, pH, or anaerobic atmosphere details are structured
  in the generated record.

## Completeness

- The generated merge omits structured `source_data`, `references`, pH,
  atmosphere, and `preparation_steps`.
- The four entries in `solutions` are all incomplete or wrong for JCM 579:
  sodium acetate and NaHCO3 are additions of defined filter-sterilized stocks,
  the two named solutions are local JCM 579 stocks, and trace minerals should
  resolve through TOGO M142 / JCM 151.
- `target_organisms`, growth metrics, incubation temperature, light, salinity,
  and storage are empty. I did not count those as defects because the inspected
  JCM and TOGO recipe pages describe the formulation but do not assert a tested
  organism or incubation condition for this record.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_AA_MEDIUM` and `Bacillus AA Medium` found no prior review report
  before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | JCM 579 stock components are flattened into final-medium ingredients. The 1 L Solution A stock and 10 ml Solution B stock are mixed into one ingredient list, which makes water `11.0 G_PER_L`, treats Solution B calcium/magnesium salts as if they were final g/L components, and duplicates dinitrogen as both `Nitrogen gas` and `N2`. | Inspected JCM GRMD=579 and TOGO M584 split the recipe into Solution A, final per-10-ml additions, and Solution B. `data/import_tracking/reports/merged_duplicates.tsv` also flags this record's distilled-water value as a sum of differing 1.0 and 10.0 parts. | `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`; if importer-owned, the TOGO subcomponent importer and solution migrator. |
| Major | Per-10-ml liquid additions are stored with `G_PER_L` units. The generated record has `0.2 G_PER_L` for 1.0 M sodium acetate, `0.4 G_PER_L` for 5% NaHCO3, `0.1 G_PER_L` for Solution B, and `10 G_PER_L` for trace minerals. | JCM 579 and TOGO M584 state all four of those quantities as milliliters, and the sodium acetate, NaHCO3, and Solution B additions are specifically added to each 10 ml of the basal medium. | `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`; likely TOGO unit import/migration. |
| Major | `Solution A` and `Solution B` are grounded to unrelated global MediaDive solution records. | JCM 579's Solution B is CaCl2, MgCl2*6H2O, and 10 ml water; `data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml` is Na2CO3 and NaCl. JCM 579's Solution A is the basal Bacillus stock; `mediadive_5342_Solution_A.yaml` is a different eight-component 500 ml stock. | Remove those mediadive solution links from `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`; adjust any migration rule that maps generic local sub-solution labels to global MediaDive IDs. |
| Major | The M142/JCM 151 trace-minerals stock is unresolved and empty. | TOGO M584 references M142 for the 10 ml trace-minerals addition; TOGO M142 maps to JCM GRMD=151 and includes a distinct 1 L `Trace minerals` stock with NTA, MgSO4*7H2O, MnSO4*xH2O, NaCl, FeSO4*7H2O, CoSO4*7H2O, CaCl2*2H2O, ZnSO4*7H2O, CuSO4*5H2O, AlK(SO4)2, H3BO3, Na2MoO4*2H2O, and water. | `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`, plus a maintained cross-reference representation for TOGO M142 trace minerals. |
| Major | Anaerobic preparation and pH are missing. | JCM 579 gives pH 7.2, N2-CO2 at 4:1 while dispensing and sealing under butyl rubber, autoclaving of the basal tubes, aseptic completion additions, and Solution B autoclaving under N2. The record has no pH, atmosphere, or preparation steps. | `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`. |
| Minor | Source provenance is mostly stringified into `notes`. | The JCM and TOGO URLs are preserved in `notes`, but the record has no structured `source_data` or `references` block tying imported components and preparation text to TOGO M584 / JCM 579. | `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`
   so JCM 579's Solution A, Solution B, 1.0 M sodium acetate, 5% NaHCO3, and
   trace-minerals additions are represented as stocks or final-medium additions
   with milliliter units and explicit per-10-ml dilution context.
2. Remove `mediadive.solution:5342` and `mediadive.solution:5343` from the
   Bacillus AA record unless a curated local mapping proves those exact global
   IDs are the intended JCM 579 sub-solutions. The inspected files show they are
   compositionally different and should not be reused on the shared names
   alone.
3. Resolve the `Trace minerals (see Medium [M142])` addition against the
   inspected TOGO M142 / JCM 151 trace-minerals subcomponent. The normalized
   Pyrococcus M142 record has its own stock-flattening artifacts, so copy from
   the inspected M142 source subcomponent rather than copying the full flattened
   normalized medium.
4. Add source-supported preparation detail for pH 7.2, the 4:1 N2-CO2
   atmosphere during dispensing, butyl-rubber-stopper sealing, autoclaving, the
   aseptic final additions per 10 ml, and Solution B autoclaving under N2.
5. Convert the TOGO/JCM provenance from free-text `notes` into the narrowest
   structured slots available for source accessions, source URLs, retrieval
   metadata, and claim evidence.
6. Regenerate merge and page outputs from the normalized owner; do not edit
   `data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml` directly.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml`.
- Regenerate the merge products and verify the generated
  `data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml` no longer contains
  `mediadive.solution:5342`, `mediadive.solution:5343`, the summed
  `Distilled water` value of `11.0 G_PER_L`, duplicate dinitrogen rows, or
  milliliter additions encoded as `G_PER_L`.
- Re-fetch TOGO M584 and JCM GRMD=579 and compare every ingredient, quantity,
  solution boundary, pH, atmosphere, and preparation step claim against the
  curated YAML.
- Re-fetch TOGO M142 or JCM GRMD=151 while resolving the trace-minerals stock,
  and verify the curated cross-reference uses only the trace-minerals
  subcomponent, not the whole Pyrococcus medium.

## Additional Notes

- The maintained normalized owner currently matches the generated merge except
  for merge-only provenance fields, so every scientific issue above is already
  present upstream of generation.
- The exact local search that found no prior BACILLUS_AA review was run with
  `--no-ignore --hidden`, so ignored report files were included.
- This record validates structurally because the schema can represent generic
  ingredients and empty solution compositions; the failures are stock identity,
  dimensional arithmetic, and missing source-supported preparation claims.
