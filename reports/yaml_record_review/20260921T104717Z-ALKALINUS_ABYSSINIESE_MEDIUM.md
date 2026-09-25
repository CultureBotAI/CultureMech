# YAML Record Review: Alkalinus Abyssiniese Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
- Started UTC: 2026-09-21T10:46:00Z
- Finished UTC: 2026-09-21T10:47:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007539` |
| Name | `alkalinus_abyssiniese_medium` |
| Original name | `Alkalinus Abyssiniese Medium` |
| Category | `bacterial` |
| Generated status | Generated merge from one maintained normalized source |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` |
| Upstream source | TOGO `M1025`, imported from JCM `JCM_M974` |
| Merge fingerprint | `ec366397e2ef6eedf511c02d22c0b18269f82cdce02b84ab502c6afc43944cbf` |

The reviewed target is a generated merge. Future edits should repair the TOGO
M1025 normalized source or the importer and then regenerate the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml --out /private/tmp/ALKALINUS_ABYSSINIESE_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning |
| Embedded curation history | Not checked | No focused validator is documented for embedded `MediaRecipe.curation_history`; `just validate-history` validates standalone files under `history/` |

The usual `just` wrappers were not rerun here because target-specific `just
validate-schema`, `just validate-strict`, and `just validate-terms` currently
fail before target validation while the project `uv` environment attempts to
build `llvmlite==0.46.0` under Python 3.13. The no-project validator commands
above use Python 3.11 and the cached validator packages instead.

## Identity and Grounding

The generated target, its sole normalized parent, and the fetched TOGO record
all identify TOGO Medium M1025, `Alkalinus Abyssiniese Medium`, imported from
JCM `JCM_M974`. The live JCM GRMD 974 URL was checked and now returns a JCM
`Nothing found` page, so TOGO M1025 is the recoverable source inspected for the
formulation.

The exact ignored-files-including search:

```bash
rg -n "M1025|JCM_M974|GRMD=974|ec366397e2ef6eedf511c02d22c0b18269f82cdce02b84ab502c6afc43944cbf|ALKALINUS_ABYSSINIESE_MEDIUM" data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml --glob '*.yaml' --no-ignore --hidden
```

found this generated M1025 record, its maintained parent, a TOGO M1026 sibling
that points at `JCM_M974-2`, and a direct JCM-derived sibling for GRMD 974.
The reviewed target is not conflated with the M1026 or direct JCM sibling
records because it keeps the TOGO M1025 accession and a single `merged_from`
parent.

Base ingredient grounding for MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, and KH2PO4 is
compatible with the TOGO source. Some trace salts lose exact chemical form:
`CoCl2 x 6H2O` is grounded to anhydrous cobalt dichloride and `NiCl2 x 6H2O`
is grounded to nickel dichloride, even though the source specifies the
hexahydrates.

## Evidence

TOGO M1025 has three distinct recipe scopes:

| Source scope | Source content |
|---|---|
| Main 900 ml base | 900 ml water, MgSO4 x 7H2O 0.2 g, NaCl 117 g, CaCl2 x 2H2O 0.2 g, KH2PO4 0.1 g, yeast extract 5 g, peptone 5 g, and 10 ml trace mineral solution |
| Post-autoclave stocks | 100 ml 10% (w/v) Na2CO3 solution and 5 ml 10% (w/v) glucose solution, both separately autoclaved and added aseptically after cooling |
| Trace mineral stock | 1 L water, Na2MoO4 x 2H2O 3 mg, H3BO4 30 mg, MnCl2 x 4H2O 3 mg, CoCl2 x 6H2O 10 mg, NiCl2 x 6H2O 2 mg, ZnSO4 x 7H2O 10 mg, and CuCl2 x 2H2O 1 mg |

The generated record collapses those scopes into one object. It sums the
900 ml base water and 1 L trace-stock water into a single `901.0 G_PER_L`
water row, promotes every trace-stock milligram row to a final-medium
`G_PER_L` ingredient, and moves the three actual additions into empty solution
records with no composition.

The source preparation comment says to add the base components to distilled
water, bring the volume to 900 ml, optionally add 20 g/L agar for solid medium,
autoclave, cool, and then aseptically add the following separately autoclaved
solutions. The generated record has no preparation steps and no distinction
between the autoclaved base and the separately autoclaved Na2CO3, glucose, and
trace-mineral additions.

No inspected source supports final-medium `3 G_PER_L` sodium molybdate
dihydrate, `30 G_PER_L` boric acid, `3 G_PER_L` manganese chloride
tetrahydrate, `10 G_PER_L` cobalt chloride hexahydrate, `2 G_PER_L` nickel
chloride hexahydrate, `10 G_PER_L` zinc sulfate heptahydrate, or `1 G_PER_L`
copper chloride dihydrate. Those are milligram-per-liter stock recipe
quantities and then only 10 ml of that stock is used.

No claim-level `evidence` objects or structured `references` are present. The
TOGO/JCM provenance is retained only as free text in `notes`.

## Completeness

Consequential gaps:

- The main recipe, stock additions, and trace-mineral stock recipe are flattened
  into one final-medium ingredient list.
- Two water volumes from different scopes are summed into an invalid
  `901.0 G_PER_L` concentration.
- Seven trace-mineral rows are simultaneously in the wrong scope and
  dimensionally 1000-fold too large for the stock recipe itself.
- The 10 ml trace-mineral addition, 100 ml 10% Na2CO3 addition, and 5 ml 10%
  glucose addition are represented as empty solutions instead of composition-
  and amount-preserving stock additions.
- Base autoclaving, post-autoclave cooling, separate stock autoclaving, and
  aseptic addition steps are missing.
- The optional 20 g/L agar variant is not recorded as a conditional solid
  variant.
- TOGO/JCM provenance is not structured.

Empty optional slots that are not automatic defects:

- `target_organisms` and `growth_metrics` can remain empty. TOGO M1025 is a
  source formulation, not a strain-specific growth record.
- Undefined supplier-specific yeast extract and peptone do not need ChEBI
  terms.

The prior-report search:

```bash
find reports/yaml_record_review -name '*ALKALINUS_ABYSSINIESE_MEDIUM*' -print
```

included ignored report files and found no existing report for this exact
generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The trace-mineral stock recipe was flattened into the final medium. The seven trace-salt rows are stock ingredients, not final-medium ingredients, and their stock amounts were changed from mg/L to g/L. | TOGO M1025 nests these rows under `Trace mineral solution` with `unit: "mg"` and adds only 10 ml of that stock to the main recipe. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`, or the TOGO importer |
| Major | Water rows from incompatible scopes were summed into `901.0 G_PER_L`. | TOGO M1025 has 900 ml water in the base medium and 1 L water inside the trace-mineral stock recipe. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`, or the TOGO importer |
| Major | The 10% Na2CO3, 10% glucose, and trace-mineral additions lost their stock boundaries, addition amounts, and compositions. | TOGO M1025 records 100 ml 10% Na2CO3, 5 ml 10% glucose, and 10 ml trace-mineral solution as post-autoclave additions. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`, or the TOGO importer |
| Major | Preparation context is missing. Autoclaving, cooling, separate stock sterilization, and aseptic post-autoclave addition are consequential to the recipe but absent. | TOGO M1025 contains a preparation comment with those operations. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` |
| Major | Exact hydrate grounding is wrong for cobalt and nickel trace salts. `CoCl2 x 6H2O` and `NiCl2 x 6H2O` are linked to anhydrous `CHEBI:35696` and `CHEBI:34887`. | TOGO M1025 explicitly names hexahydrate salts in the trace-mineral stock. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` |
| Minor | The optional solid formulation is omitted. TOGO M1025 states an optional 20 g/L agar addition for solid medium, but the record is only liquid. | TOGO M1025 has an explicit solid-medium note in its preparation comment. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` |
| Minor | Provenance is free-text only and JCM GRMD 974 now has no live formulation table. | The source URL is in `notes`; fetching JCM GRMD 974 returned `Nothing found`. | `data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. Reconstruct `Trace mineral solution` as a nested or referenced stock with
   its 1 L water and milligram-scale Na2MoO4 x 2H2O, H3BO4, MnCl2 x 4H2O,
   CoCl2 x 6H2O, NiCl2 x 6H2O, ZnSO4 x 7H2O, and CuCl2 x 2H2O rows.
2. Keep only the 900 ml base water and base salts/undefined nutrients in the
   basal medium, and add the trace-mineral stock as a 10 ml addition.
3. Replace the empty 10% Na2CO3 and 10% glucose solution placeholders with
   stock additions that preserve 100 ml and 5 ml respectively.
4. Add preparation steps for base mixing to 900 ml, autoclaving, cooling, and
   aseptic addition of separately autoclaved stock solutions.
5. Correct or remove hydrate-specific CHEBI groundings for CoCl2 x 6H2O and
   NiCl2 x 6H2O unless exact hydrate CURIEs are verified.
6. Preserve the optional 20 g/L agar solid variant without changing the liquid
   recipe identity.
7. Move TOGO M1025 and the unavailable JCM GRMD 974 source URL into structured
   reference/source fields.
8. Regenerate `data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml` and
   generated pages from the maintained source.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` after rebuilding the trace-mineral stock and exact hydrate terms.
- Run `just validate-references data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml` after adding structured TOGO/JCM provenance.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
- Manually compare the regenerated record with TOGO M1025 for the 900 ml base,
  10 ml/100 ml/5 ml stock additions, trace-mineral stock composition, and
  aseptic post-autoclave addition procedure.

## Additional Notes

- `data/merge_yaml/merged/alkalinus_abyssiniese_medium__27b83953.yaml` is the
  sibling TOGO M1026 recipe that reuses the M1025 trace-mineral stock; it
  should be reviewed independently.
- `high_metal: true` likely comes from flattened trace stock values. Recompute
  it after stock/final-medium scope is repaired.
