# YAML Record Review: Hyphomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml
- Started UTC: 2026-09-23T14:05:20Z
- Finished UTC: 2026-09-23T14:07:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:010346 |
| Name | hyphomicrobium_medium |
| Original name | Hyphomicrobium Medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| Source identity | TOGO Medium M925; original source JCM Medium 884 |
| Generated path reviewed | data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml |

The reviewed file is generated from the maintained TOGO M925 import above.
Future fixes should update the normalized record or TOGO importer, preserve the
Visniac trace-elements stock boundary, then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml --out /private/tmp/hyphomicrobium_medium__42cb031d.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyphomicrobium_medium__42cb031d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:010346` is the TOGO M925 import
  of JCM Medium 884, and both the inspected TOGO payload and the live JCM 884
  page identify HYPHOMICROBIUM MEDIUM.
- A gitignore-independent exact search for `CultureMech:010346` over the
  maintained TOGO file, generated TOGO file, ID registry, TOGO indexes, and
  review manifest found only this JCM-owned record and its generated index rows.
- A gitignore-independent exact search for `TOGO:M925` over bacterial
  normalized records, generated records, and TOGO indexes found only this TOGO
  M925 record.
- The direct final-medium rows for K2HPO4, NaH2PO4, ammonium sulfate, MgSO4 x
  7H2O, methylamine hydrochloride, and agar match the JCM table.
- The Visniac stock rows retain their source names, but CoCl2 x 6H2O and
  ammonium molybdate hydrate are grounded generically.

## Evidence

- JCM 884 lists 2.5 g K2HPO4, 2.25 g NaH2PO4, 0.5 g ammonium sulfate, 0.2 g
  MgSO4 x 7H2O, 2 g methylamine hydrochloride, 15 g agar, 1 ml Visniac trace
  elements, and 1 L distilled water.
- The JCM Visniac trace-elements stock contains EDTA disodium salt, ZnSO4 x
  7H2O, CaCl2 x 2H2O, MnCl2 x 4H2O, FeSO4 x 7H2O, ammonium molybdate
  tetrahydrate, CuSO4 x 5H2O, CoCl2 x 6H2O, and 500 ml distilled water.
- The YAML records an empty `Visniac trace elements (see below)` solution as
  `1 G_PER_L` and also flattens all eight stock solutes into the final-medium
  ingredient list.
- The flattened Visniac component amounts are raw 500 ml stock recipe masses,
  not stock gram-per-liter values and not 1 ml final-medium concentrations.
- The final 1 L distilled-water row and the 500 ml stock water row are merged
  into a synthetic `501 G_PER_L` Distilled water ingredient.
- JCM Medium 884 has no pH statement and no formula-specific sterilization
  override, so the JCM default autoclave rule applies but is absent from the
  YAML.

## Completeness

- The 1 ml Visniac trace-elements stock needs to stay nested and populated.
- The final and stock distilled-water volumes need dimensional repair.
- The direct JCM 884 ingredient rows, including mandatory agar, are otherwise
  present.
- Empty optional fields for pH, target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Visniac trace elements is both empty as a solution and flattened into the final medium. | JCM 884 adds 1 ml Visniac trace elements and defines that stock separately; the YAML has an empty 1 `G_PER_L` solution and top-level EDTA, Zn, Ca, Mn, Fe, Mo, Cu, and Co rows. | `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml`; TOGO solution migration should preserve nested stock composition. |
| Major | Flattened Visniac amounts have the wrong basis. | The stock recipe masses are for 500 ml stock, but the YAML records values such as 5 g EDTA and 2.2 g ZnSO4 x 7H2O as final `G_PER_L` concentrations. | `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml`; TOGO stock concentration conversion. |
| Major | The final and stock water rows are merged into a mass concentration. | JCM has 1 L distilled water in the final medium and 500 ml in the stock; the YAML records `501 G_PER_L` Distilled water. | `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml`; TOGO volume handling and duplicate cleanup. |
| Major | The JCM default autoclave step is missing. | JCM 884 has no record-specific sterilization override, so JCM's default autoclave instruction applies; the YAML has no preparation steps. | `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml`; JCM default preparation import. |
| Minor | Some hydrate-specific stock groundings are generic. | CoCl2 x 6H2O is grounded to cobalt dichloride, and the ammonium molybdate hydrate is grounded to generic ammonium molybdate. | `data/normalized_yaml/bacterial/TOGO_M925_Hyphomicrobium_Medium.yaml`; hydrate-aware CHEBI mapping. |

## Recommended Edits

1. Restore Visniac trace elements as a 1 ml nested stock addition and move all
   eight trace rows under it.
2. Convert the Visniac 500 ml recipe masses to stock concentrations while
   preserving the source masses in provenance or notes.
3. Represent the 1 L final water and 500 ml Visniac water as volumes, not
   `G_PER_L`.
4. Add the JCM default autoclave instruction.
5. Re-ground CoCl2 x 6H2O and ammonium molybdate tetrahydrate to exact hydrated
   terms if CHEBI exposes them.
6. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M925 merged record.
- Manually compare final ingredients and nested Visniac stock rows against the
  TOGO M925 payload and live JCM 884 page.
- Verify that no stock ingredient remains as a top-level final-medium
  ingredient.

## Additional Notes

- This JCM 884 source has mandatory 15 g agar and 2 g methylamine
  hydrochloride; those rows should not be reconciled against the optional agar
  and methylamine-stock wording in the separate DSMZ 1355 medium.
