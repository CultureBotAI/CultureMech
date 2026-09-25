# YAML Record Review: Pfennig's medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pfennig_s_medium.yaml
- Started UTC: 2026-09-24T20:44:56Z
- Finished UTC: 2026-09-24T20:44:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/pfennig_s_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008863` |
| Name | `pfennig_s_medium` |
| Original name | `Pfennig's medium` |
| Media term | `TOGO:M2277` |
| Generated status | Generated merge output from `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` |

The target resolves to the TOGO M2277 import of Pfennig's medium. An
ignored-inclusive search over `data`, `src`, and `scripts` for `TOGO:M2277`,
`M2277`, `CultureMech:008863`, and `pfennig_s_medium` found no other M2277
owner in the merged YAML corpus.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pfennig_s_medium.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pfennig_s_medium.yaml --out /private/tmp/pfennig_s_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pfennig_s_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pfennig_s_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The TOGO identity is internally consistent: M2277 is named Pfennig's medium and
the local record points to `TOGO:M2277`. TOGO did not provide a non-TOGO
original URL in the live payload, so the source check was bounded to TOGO M2277
itself.

The top-level `medium_type: COMPLEX` and `composition_type: UNDEFINED` are not
supported by the inspected formulation. The recipe is fully itemized into salts
and defined small molecules; no yeast extract, peptone, or other undefined
complex component was found in the M2277 payload.

Several trace-salt groundings are missing because the imported labels spell
chloride with a capital `I`, for example `MnCI2.4H2O`, `CoCI2.6H2O`, and
`ZnCI2`. `Ethylenediamine-tetraacetate-di-Na-salt` is also ungrounded even
though it corresponds to the EDTA disodium salt in the SL 12 stock.

## Evidence

TOGO M2277 defines a final mixture of 951 ml Solution 1, 1 ml Solution 3
Vitamin B12 solution, 30 ml Solution 4 Na bicarbonate solution, and 10 ml
Solution 5 Sodium sulfide solution.

Solution 1 is a 950 ml base with 0.4 g MgSO4.7H2O, 0.05 g CaCl2.2H2O, 1 g
KH2PO4, 0.5 g NH4Cl, and 1 ml Solution 2 (SL 12). Solution 2 (SL 12) is a
1 L trace stock containing Na2MoO4.2H2O, H3BO3, FeSO4.7H2O, MnCl2.4H2O,
CoCl2.6H2O, NiCl2.6H2O, CuCl2.2H2O, ZnCl2, and EDTA disodium salt. Solution 3
contains Vitamin B12 in 100 ml water, and Solutions 4 and 5 are bicarbonate and
sulfide stock additions.

The generated record flattens Solution 1 and Solution 2 stock ingredients into
top-level `ingredients`, leaves Solutions 3 through 5 and Solution 2 as empty
solution stubs, and imports source volumes as `G_PER_L` concentrations. The
final 951 ml Solution 1 addition is represented as `951` g/L, the 30 ml
bicarbonate and 10 ml sulfide additions are represented as `30` g/L and `10`
g/L, and Vitamin B12 is represented as `2` g/L rather than a milligram-scale
stock component.

The generated `Distilled water` value is `1051.0` g/L from `[Merged 3
duplicates: 950.0, 1.0, 100.0]`, summing water rows from different source
scopes: the 950 ml Solution 1 base, 1 L Solution 2 trace stock, and 100 ml
Vitamin B12 stock.

The source preparation comments are absent. TOGO M2277 says the autoclaved
Solution 1, including Solution 2, should be cooled before sterile Solutions 3
through 5 are added aseptically while magnetically stirring; it also gives a pH
adjustment to 7.3 for purple sulfur bacteria or 6.8 for green sulfur bacteria,
an autoclaving note for Solution 1, a screw-cap-bottle autoclaving note for the
SL 12 salt solution, a filter-sterilization note for the 5% bicarbonate stock,
and a freshly autoclaved 6% sulfide stock with different purple/green sulfur
bacteria addition volumes.

## Completeness

The generated record lacks populated `solutions:` structures for Solution 1,
Solution 2 (SL 12), Solution 3 Vitamin B12 solution, Solution 4 Na bicarbonate
solution, and Solution 5 Sodium sulfide solution.

It lacks all source preparation and pH instructions, including the alternate pH
targets for purple versus green sulfur bacteria.

No empty optional field was material to this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Source solution scopes and aliquot volumes were flattened into final ingredients and empty solution stubs. | TOGO M2277 mixes 951 ml Solution 1, 1 ml Vitamin B12 solution, 30 ml Na bicarbonate solution, and 10 ml Sodium sulfide solution; the generated record encodes those as `G_PER_L`, flattens Solution 2 trace salts into top-level ingredients, and sums three water rows into `1051.0` g/L. | `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` and the TOGO import/solution migration path |
| Major | Preparation and pH instructions are missing. | TOGO M2277 has sterile addition, stirring, separate autoclaving/filtering, 5% bicarbonate, 6% sulfide, and organism-group pH comments, but the generated record has no `preparation_steps`, `ph_value`, or `ph_range`. | `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` and the TOGO importer |
| Minor | Several trace-salt labels are misspelled or ungrounded. | The generated record retains `MnCI2.4H2O`, `CoCI2.6H2O`, and `ZnCI2`, leaving those chloride salts ungrounded; the EDTA disodium salt is also ungrounded. | `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` |
| Minor | The top-level medium and composition type are too weak. | The inspected TOGO M2277 payload is fully itemized and does not show any complex undefined ingredient. | `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` from TOGO
   M2277 with separate Solution 1, Solution 2 (SL 12), Solution 3, Solution 4,
   and Solution 5 scopes.
2. Keep only the 951 ml, 1 ml, 30 ml, and 10 ml solution aliquots in the final
   recipe; move base, trace, B12, bicarbonate, and sulfide components into
   their stock scopes.
3. Restore water rows to their proper stock scopes rather than summing them
   into one `Distilled water` ingredient.
4. Add the TOGO pH and preparation comments, including the purple/green sulfur
   bacteria pH fork and the stock-specific sterilization instructions.
5. Correct imported `CI` spellings to `Cl` in manganese, cobalt, nickel, and
   zinc chloride labels and add exact CHEBI groundings; ground
   `Ethylenediamine-tetraacetate-di-Na-salt` to EDTA disodium salt.
6. Reclassify the medium as defined once every ingredient is grounded and the
   stock solution boundaries are explicit.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on the regenerated Pfennig's medium output.
2. Manually compare each regenerated solution scope with TOGO M2277 and verify
   that ml, L, mg, and g source units are preserved in the correct solution.
3. Use an ignored-inclusive exact search for `TOGO:M2277`, `M2277`,
   `CultureMech:008863`, and `pfennig_s_medium` under `data`, `src`, and
   `scripts` to verify that this source still has one maintained owner and one
   merged output.

## Additional Notes

No original non-TOGO URL or paper identifier was available in the live TOGO
M2277 payload, so external provenance remains unresolved.
