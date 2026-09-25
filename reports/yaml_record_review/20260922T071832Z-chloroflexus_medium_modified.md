# YAML Record Review: chloroflexus_medium_modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_medium_modified.yaml
- Started UTC: 2026-09-22T07:16:41Z
- Finished UTC: 2026-09-22T07:18:48Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009609 |
| Label | Chloroflexus Medium (modified) |
| Generated record | data/merge_yaml/merged/chloroflexus_medium_modified.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M3141_Chloroflexus_Medium_modified.yaml |
| Source | TOGO Medium M3141, derived from DSMZ Medium 87 |

The reviewed file is a generated one-source merge of the TOGO M3141 normalized
record. Future fixes belong in
`data/normalized_yaml/bacterial/TOGO_M3141_Chloroflexus_Medium_modified.yaml`,
the TOGO solution migration logic, or the TOGO importer rather than in
`data/merge_yaml/merged/chloroflexus_medium_modified.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chloroflexus_medium_modified.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO API request failed on DNS resolution inside the sandbox and then
passed when retried directly. DSMZ Medium 87 and DSMZ Medium 27 were fetched
and read from their source PDFs.

## Identity and Grounding

The record identity is correct. `CultureMech:009609`, the name
`Chloroflexus Medium (modified)`, `TOGO:M3141`, and the cited DSMZ Medium 87
PDF all denote the same modified Chloroflexus medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the exact CultureMech
ID, TOGO source ID, normalized owner stem, and merge fingerprint found this
generated record, the TOGO M3141 maintained owner, normalized index entries, and
a separate direct MediaDive/DSMZ-87 record for the same DSMZ formulation.

## Evidence

TOGO M3141 and the DSMZ Medium 87 PDF both support the parent medium members:
1.00 g yeast extract, 1.00 g glycyl-glycine, 0.10 g `Na2HPO4 x 2 H2O`, 0.10 g
`MgSO4 x 7 H2O`, 0.10 g `KNO3`, 0.50 g `NaNO3`, 0.10 g `NaCl`, 0.05 g
`CaCl2 x 2 H2O`, 5.00 mL Fe(III) citrate solution, 1.00 mL trace element
solution SL-6, and 1050.00 mL distilled water. The source also supports pH 8.2
for the parent medium.

The imported ingredient list is over-flattened. Its 2250 g/L distilled-water
row sums the 1050 mL parent water, 100 mL Fe(III) citrate stock water, 100 mL
neutralized-sulfide stock water, and 1000 mL SL-6 stock water even though only
the first quantity is a direct parent-medium ingredient. The 0.1 g Fe(III)
citrate, 3 g `Na2S x 9 H2O`, 2 M `H2SO4`, and all SL-6 salts are likewise stock
solution members rather than direct parent-medium ingredients.

The generated `solutions` entries for `Neutralized sulfide solution`,
`Fe(III) citrate solution`, and `Trace element solution SL-6` retain the stock
labels but have empty compositions and `Unknown solution` names. The sulfide
entry uses 0.03% as if it were the stock concentration; in the source, 0.03% is
the end concentration after injecting 1.0 mL of a 3 g/100 mL sulfide stock into
each 90 mL bottle.

The record omits every TOGO comment and DSMZ Medium 87 preparation instruction:
the pH 8.2 adjustment, boiling under nitrogen, distribution into 90 mL
bottles, nitrogen gassing, autoclaving at 121 C for 15 min, post-autoclave
neutralized-sulfide injection, storage note, 50 C low-light incubation, heavy
cell-suspension yeast-extract supplementation, and the two neutralized-sulfide
stock preparation notes.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO source record.

The composition is incomplete as structured data until the Fe(III) citrate,
neutralized-sulfide, and SL-6 stocks carry their source compositions and are
linked from the parent recipe at their source volumes. The preparation is also
incomplete because TOGO and DSMZ both expose operational instructions that are
absent from the normalized owner and generated merge.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Subsolution water and stock members are flattened into the parent `ingredients`, producing unsupported direct concentrations such as 2250 g/L distilled water and direct SL-6 salts. **Owner:** `data/normalized_yaml/bacterial/TOGO_M3141_Chloroflexus_Medium_modified.yaml`, the TOGO importer, or both. |
| Major | Migrated `solutions` preserve only the names and coarse concentrations of Fe(III) citrate solution, neutralized sulfide solution, and SL-6; their `composition` arrays are empty. **Owner:** the TOGO solution migrator/importer and the maintained TOGO M3141 YAML. |
| Major | The neutralized sulfide stock is misrepresented as 0.03% instead of a 3 g/100 mL stock injected post-autoclave to a 0.03% end concentration. **Owner:** the TOGO importer and solution migration logic. |
| Major | All source preparation instructions are dropped even though TOGO preserved them as comments. **Owner:** the TOGO importer that maps source comments into `preparation_steps`. |
| Minor | `MgSO4 x 7 H2O` has primary `term` CHEBI:31795 but stale `mediaingredientmech_chebi_term` CHEBI:32599, and `KNO3` plus Fe(III) citrate retain legacy `mediaingredientmech_term` identifiers despite available CHEBI primary terms. **Owner:** the MediaIngredientMech-to-CHEBI migration. |

## Recommended Edits

1. Update the maintained TOGO import path so only true parent-medium inputs stay
   in the parent `ingredients` array.
2. Populate `Fe(III) citrate solution`, `Neutralized sulfide solution`, and
   `Trace element solution SL-6` with their source compositions and link them
   from the parent recipe at 5.00 mL, 1.0 mL, and 1.00 mL respectively.
3. Represent neutralized sulfide as a 3 g/100 mL `Na2S x 9 H2O` stock with
   post-autoclave addition to the parent recipe; reserve the 0.03% value for
   end-concentration context.
4. Preserve the TOGO M3141 preparation comments as structured preparation
   steps, including the pH adjustment, nitrogen handling, autoclaving,
   post-autoclave sulfide addition, incubation, storage, and sulfide-stock
   handling.
5. Refresh the enrichment/migration step so the `MgSO4 x 7 H2O`, `KNO3`, and
   Fe(III) citrate secondary ingredient links agree with their primary CHEBI
   terms.

## Follow-up Checks

Run the narrow generated-record validators after regenerating this record:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually recompare the generated record against TOGO M3141, DSMZ Medium
87, and DSMZ Medium 27 to ensure nested stocks, pH/preparation comments, and
post-autoclave addition semantics have not been flattened.

## Additional Notes

The normalized direct MediaDive/DSMZ-87 record has the same biological source
but a different source path and merge fingerprint. Keep it in the comparison
set when this TOGO import is repaired so the two DSMZ-87 imports do not drift
unnecessarily.
