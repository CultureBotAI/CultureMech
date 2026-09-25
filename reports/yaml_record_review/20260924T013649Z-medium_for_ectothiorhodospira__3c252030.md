# YAML Record Review: medium_for_ectothiorhodospira__3c252030

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_ectothiorhodospira__3c252030.yaml
- Started UTC: 2026-09-24T01:35:53Z
- Finished UTC: 2026-09-24T01:36:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008356 |
| Name | medium_for_ectothiorhodospira |
| Generated record | data/merge_yaml/merged/medium_for_ectothiorhodospira__3c252030.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1789_Medium_for_Ectothiorhodospira.yaml |
| Source identity | TOGO:M1789, original source NBRC_M1012 / NBRC Medium 1012 |

This generated record is a single-source merge of TOGO M1789, which in turn
imports NBRC Medium 1012, "Medium for Ectothiorhodospira." The generated YAML is
derived from the maintained TOGO owner; all recipe defects below are present in
that owner and must not be repaired directly in `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_ectothiorhodospira__3c252030.yaml` | Passed with no issues found. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_ectothiorhodospira__3c252030.yaml --workers 1` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator targets standalone `history/` files, not embedded generated-record history. |

The focused validators were run with Python 3.11 through `uv --no-project
--offline` to avoid the project-level Python 3.13 `llvmlite` build failure.

## Identity and Grounding

The TOGO M1789 API payload and the NBRC `NO=1012` HTML page agree on the source
medium name, original NBRC source, source URL, base salts, vitamin B12 stock,
SL-12B trace stock, neutralized sulfide stock, and pH 7.3 instructions. The
record ID, TOGO media term, source note, category, and liquid state therefore
identify the requested NBRC formulation.

A gitignore-independent exact scan for `TOGO:M1789`, `NBRC_M1012`, and the
NBRC `NO=1012` URL found only the TOGO owner, this generated record, and
normalized indexes. No other maintained record in the scanned data/report paths
claims the same TOGO or NBRC accession.

The normalized name `medium_for_ectothiorhodospira` is shared by two other
maintained records and one other generated record, `MEDIUM_FOR_ECTOTHIORHODOSPIRA`.
Those sibling records are KOMODO/DSMZ Medium 253 with pH 8.5 and a separate
MediaDive source identity. That is a label collision with a distinct source
medium, not evidence that TOGO M1789 already has a correct merge partner.

Two hydrate-specific ingredient labels are under-grounded: `CoCl2 x 6 H2O` is
linked to generic cobalt dichloride, and `NiCl2 x 6 H2O` is linked to generic
nickel dichloride.

## Evidence

The source recipe supports the base NBRC components CaCl2 x 2 H2O 0.25 g,
KH2PO4 0.34 g, NH4Cl 0.34 g, KCl 0.34 g, MgSO4 0.5 g, NaCl 30 g, NaHCO3
1.5 g, Na2S x 9 H2O 0.4 g, resazurin 0.5 mg, distilled water 998 ml, plus
1 ml each of vitamin B12 0.002 percent solution and Trace element solution
SL-12B.

The generated YAML does not preserve several of those source claims:

- `Resazurin` is 0.5 G_PER_L, although NBRC lists 0.5 mg.
- `Distilled water` is 1099.0 G_PER_L after summing the final medium's 998 ml,
  the trace stock's 1 L, and the neutralized sulfide stock's 100 ml.
- `Na2S x 9 H2O` is 1.9 G_PER_L after summing the final-medium 0.4 g and the
  neutralized sulfide stock's 1.5 g.
- `Vitamin B12 (0.002%) solution` and `Trace element solution SL-12B*` are stored
  as 1 G_PER_L solution rows, not 1 ml stock additions.
- The SL-12B stock components are flattened into final-medium ingredients, with
  mg stock values represented as G_PER_L rows: 18 mg Na2MoO4 x 2 H2O becomes
  18 G_PER_L, 300 mg H3BO3 becomes 300 G_PER_L, 190 mg CoCl2 x 6 H2O becomes
  190 G_PER_L, and the same unit error affects Ni, Cu, Zn, and Mn salts.
- The source's pH adjustment reagents are imported as variable final-medium HCl,
  H2SO4, and N2 ingredients even though NBRC uses HCl/Na2CO3 to adjust the final
  medium and sulfuric acid plus N2 in the neutralized sulfide stock workflow.

No target organisms are asserted. That is acceptable for a source-recipe import
whose inspected NBRC and TOGO records identify the medium but do not list a
specific strain.

## Completeness

The generated record omits every procedural detail that would let a curator
recreate the NBRC anaerobic workflow: final pH 7.3, trace stock pH 6, N2/CO2
80/20 dispensing before autoclaving, sterile anaerobic bicarbonate, vitamin, and
sulfide stock additions, bicarbonate/vitamin filter sterilization, final pH
adjustment with sterile 2 M HCl or Na2CO3, and the sealed-vessel neutralized
sulfide preparation with pH adjustment after autoclaving.

The stock solutions have empty `composition` arrays even though the trace stock
composition and neutralized sulfide composition are present in TOGO and NBRC.
The vitamin B12 stock is only described by concentration in the stock name, so
its empty composition is not independently defective.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | TOGO stock solution boundaries are not preserved. | The source adds 1 ml vitamin B12 stock and 1 ml SL-12B trace stock, and defines a separate neutralized sulfide stock. The generated record stores two 1 G_PER_L solution rows and flattens trace and sulfide stock components into final-medium ingredients. | `data/normalized_yaml/bacterial/TOGO_M1789_Medium_for_Ectothiorhodospira.yaml`; TOGO importer and solution-migration code. |
| major | Several quantities are dimensionally wrong. | NBRC's 0.5 mg resazurin is 0.5 G_PER_L; SL-12B mg quantities such as 18 mg molybdate, 300 mg borate, and 190 mg cobalt salt are G_PER_L rows; final and stock water rows are summed to 1099.0 G_PER_L; final and stock sulfide rows are summed to 1.9 G_PER_L. | TOGO normalized owner and duplicate-merging logic. |
| major | pH and anaerobic preparation instructions are absent or represented as final ingredients. | NBRC lists final pH 7.3, trace stock pH 6, N2/CO2 dispensing, sterile anaerobic stock additions, and separate neutralized sulfide handling; the generated record has no `ph_value` or `preparation_steps` and instead adds variable HCl, H2SO4, and N2 ingredient rows. | TOGO normalized owner. |
| minor | Two hydrate-specific trace metals are grounded to less-specific anhydrous salts. | The labels `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are present, but their primary terms are cobalt dichloride and nickel dichloride rather than hexahydrate-specific terms. | TOGO normalized owner ingredient grounding. |

## Recommended Edits

1. Repair TOGO M1789 stock parsing so vitamin B12, SL-12B, and neutralized
   sulfide are retained as stock solutions or stock-addition preparation steps
   instead of final-medium G_PER_L ingredients.
2. Restore NBRC units: keep resazurin in milligrams, keep the SL-12B mg entries
   inside the SL-12B stock, keep neutralized sulfide at 1.5 g per 100 ml stock,
   and stop summing stock water or stock sulfide into the final medium.
3. Add the source pH and anaerobic workflow to the maintained record, including
   final pH 7.3, trace-stock pH 6, N2/CO2 80/20 dispensing, filter-sterilized
   bicarbonate and vitamin additions, and neutralized sulfide preparation.
4. Re-ground `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` to hydrate-specific CHEBI terms
   when such exact mappings are available.
5. Regenerate `data/merge_yaml/merged/medium_for_ectothiorhodospira__3c252030.yaml`
   from the repaired normalized owner.

## Follow-up Checks

- Run the focused open schema, strict, reference, and term validators on the
  corrected normalized owner and regenerated merge.
- Run `just verify-merges` to confirm the generated YAML is derived from the
  repaired owner.
- Repeat a gitignore-independent exact scan for `TOGO:M1789`, `NBRC_M1012`, and
  the NBRC `NO=1012` URL to confirm the accession still appears only on the TOGO
  owner, its generated artifact, and expected indexes.
- Manually compare the regenerated record against NBRC Medium 1012 to confirm
  the final pH, milligram and milliliter units, stock boundaries, and sterile
  anaerobic additions are preserved.

## Additional Notes

- Source checks used the TOGO M1789 SPARQList API, the NBRC `NO=1012` HTML page,
  and the MediaDive 253 REST record to distinguish NBRC Medium 1012 from the
  separate DSMZ/MediaDive Medium 253 sibling with the same normalized label.
- The exact TOGO/NBRC duplicate scan used `rg --no-ignore --hidden`, so ignored
  files were included.
