# YAML Record Review: bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml
- Started UTC: 2026-09-21T21:19:08Z
- Finished UTC: 2026-09-21T21:20:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009312 |
| Name | bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose |
| Original name | BHI w/ heat-inactivated Fetal Bovine Serum and Glucose |
| Category | bacterial |
| Source identity | TOGO Medium M2764, ATCC Medium 1827 |
| Reviewed artifact | `data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml` |
| Primary maintained owner | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` |
| Generated state | Derived merge from `TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose` and `bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose`, `merge_fingerprint: 6f37148f748d1f373d5e32255b512b96bab3aca595ed955288f16f321d6d7caf` |

`data/culturemech_id_registry.tsv` maps `CultureMech:009312` to
`data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml`.

The inspected TOGO `M2764` API payload and the inspected ATCC PDF both define
ATCC Medium 1827 as a base of 37 g Brain Heart Infusion in 850 ml DI Water,
autoclaved at 121 degrees C, then cooled to 50 degrees C and aseptically
supplemented with 100 ml heat-inactivated fetal bovine serum and 50 ml of a
filter-sterilized glucose stock made from 2 g glucose in 50 ml DI Water. The
final medium is prepared anaerobically under 80% N2, 10% CO2, and 10% H2.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml` | Passed; no issues emitted |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml --out /private/tmp/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 ERROR rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 reference checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded-`MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/` |

The direct `just validate-*` wrappers were not rerun for this record because
this checkout currently fails before target-specific validation while building
`llvmlite==0.46.0` under Python 3.13. The no-project commands above exercise
the same narrow validators under Python 3.11 from a cache outside the project
environment.

## Identity and Grounding

- **Record identity is coherent.** `TOGO:M2764`, the record label, and the
  ATCC PDF all identify BHI w/ heat-inactivated Fetal Bovine Serum and
  Glucose.
- **Brain Heart Infusion is over-expanded.** TOGO and ATCC list one 37 g Brain
  Heart Infusion product row, but the generated record replaces it with six
  full-strength Difco subcomponents from a secondary MicrobeNotes page.
- **Base water and stock water were summed into one dimensionally wrong row.**
  The source has 850 ml DI Water in the base plus 50 ml DI Water inside the
  glucose stock; the generated record has one `900.0 G_PER_L` DI Water row
  annotated as merged from 850.0 and 50.0.
- **The glucose-stock boundary is broken.** The source adds 50 ml of a stock
  made from 2 g glucose and 50 ml DI Water. The generated `solutions` entry
  has `Glucose Solution`, concentration 50 g/L, and an empty composition,
  while `Glucose` appears as a direct 2 g/L ingredient.
- **Heat-inactivated fetal bovine serum has the wrong unit.** The source lists
  a 100 ml additive, not 100 g/L.
- **Anaerobic gas ratios and preparation steps are missing.** The generated
  record keeps the N2, CO2, and H2 gas identities but not the 80:10:10 ratio,
  autoclaving, 50 degrees C cooling, aseptic serum/stock addition,
  filter-sterilized glucose stock, or anaerobic final preparation.

## Evidence

| Claim | Review |
|---|---|
| TOGO M2764 / ATCC Medium 1827 identity | Supported by the TOGO API payload and the ATCC PDF. |
| 37 g Brain Heart Infusion in 850 ml DI Water | Supported by TOGO M2764 and the ATCC PDF. |
| 100 ml heat-inactivated fetal bovine serum and 50 ml glucose stock | Supported by TOGO M2764 and the ATCC PDF. |
| Glucose stock of 2 g glucose in 50 ml DI Water | Supported by TOGO M2764 and the ATCC PDF. |
| Six expanded BHI constituents | Unsupported. The source lists one 37 g Brain Heart Infusion product row. |
| 80% N2 / 10% CO2 / 10% H2 | Supported by TOGO M2764 and the ATCC PDF; the generated record has only variable gas ingredient rows. |

## Completeness

- Empty organism and growth slots are acceptable because the inspected TOGO
  and ATCC recipe records do not assert growth outcomes.
- The reviewed merge has only free-text TOGO and ATCC URLs in `notes`; it has
  no structured `references` entries for the TOGO API payload, public TOGO
  page, or ATCC PDF.
- The duplicate source `data/normalized_yaml/bacterial/bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.yaml`
  mirrors TOGO `M2622` and has the same empty glucose solution, summed
  `900.0 G_PER_L` water row, BHI expansion, serum unit, and missing
  preparation defects.
- A gitignore-independent search with `rg --no-ignore --hidden` over `data`
  and `reports/yaml_record_review` for `CultureMech:009312`, `TOGO:M2764`,
  `bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose`, and the merge
  fingerprint found the expected normalized owner, duplicate M2622 normalized
  owner, generated merge, generated indexes, import-tracking reports, and no
  related prior review report. A `find` search over the ignored
  `reports/yaml_record_review` directory found no pre-existing
  `*-bhi_w_heat_inactivated_fetal_bovine_serum_and_glucose.md` report before
  this one was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source's 37 g Brain Heart Infusion product row is replaced by six unsupported full-strength BHI subcomponents. | TOGO M2764 and the ATCC PDF list Brain Heart Infusion (BD 237500) as one 37 g row. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |
| major | Base DI Water and glucose-stock DI Water are flattened into one wrong 900 g/L row. | The ATCC PDF and TOGO M2764 place 850 ml DI Water in the base and 50 ml DI Water in the Glucose Solution stock. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |
| major | The glucose stock solution lost its composition and the direct 2 g/L Glucose row erases the stock-addition boundary. | ATCC defines a 50 ml Glucose Solution containing 2 g Glucose and 50 ml DI Water; the generated `Glucose Solution` has empty `composition`. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |
| major | Heat-inactivated fetal bovine serum is encoded as 100 g/L instead of 100 ml/L. | TOGO M2764 and ATCC both list a 100 ml serum additive. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |
| major | Preparation and anaerobic gas-ratio instructions are missing. | ATCC and TOGO specify autoclaving at 121 degrees C, cooling to 50 degrees C, aseptic addition of serum and glucose stock, filter sterilization of the glucose stock, and final anaerobic preparation under 80% N2 / 10% CO2 / 10% H2. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |
| minor | Structured source references are absent. | The TOGO and ATCC URLs are present only in the free-text `notes`, and the TOGO API URL is not recorded. | `data/normalized_yaml/bacterial/TOGO_M2764_BHI_w_heat-inactivated_Fetal_Bovine_Serum_and_Glucose.yaml` and the duplicate M2622 owner |

## Recommended Edits

1. In both duplicate normalized owners, replace the six BHI decomposition rows
   with one 37 g/L Brain Heart Infusion (BD 237500) row.
2. Model the base as 850 ml DI Water plus 37 g Brain Heart Infusion, then add
   100 ml heat-inactivated fetal bovine serum and 50 ml of a Glucose Solution.
3. Populate Glucose Solution with 2 g Glucose and 50 ml DI Water and remove
   the flattened direct Glucose row from the base medium.
4. Encode serum as a volume addition, not `G_PER_L`.
5. Add preparation steps for autoclaving the base, cooling to 50 degrees C,
   aseptic additive addition, glucose-stock filter sterilization, and final
   80% N2 / 10% CO2 / 10% H2 anaerobic preparation.
6. Add structured references for the TOGO API payloads, public TOGO pages, and
   ATCC PDF, then regenerate the merge and generated media pages.

## Follow-up Checks

- Rerun schema, strict, term, and reference validation on both corrected
  normalized owners and on the regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare the regenerated merge against the ATCC PDF and TOGO `M2764`
  to confirm BHI, DI Water, serum, Glucose Solution, and gas-ratio claims
  preserve their source compartments.

## Additional Notes

None found.
