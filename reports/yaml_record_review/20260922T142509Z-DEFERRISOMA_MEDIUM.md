# YAML Record Review: deferrisoma_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml
- Started UTC: 2026-09-22T14:25:09Z
- Finished UTC: 2026-09-22T14:25:09Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:004165`, label
`deferrisoma_medium`, original name `DEFERRISOMA medium`, under
`data/merge_yaml/merged/`.

The record is the generated merge of:

- `data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml`
- `data/normalized_yaml/bacterial/deferrisoma_medium.yaml`

Future formula fixes belong in the maintained DSMZ 1451 owner and in the KOMODO
record that cites DSMZ 1451; the solution-boundary problem belongs in the DSMZ
copy/enrichment logic shared by both owners.

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml --out /private/tmp/DEFERRISOMA_MEDIUM.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/DEFERRISOMA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

Term validation emitted only the known `eutils` `pkg_resources` deprecation
warning.

## Identity and Grounding

The DSMZ parent resolves to MediaDive medium 1451, `DEFERRISOMA MEDIUM`. The
KOMODO parent explicitly cites the same DSMZ medium, and the two maintained
parents have identical ingredient and pH signatures, so the
`SOURCE_DUPLICATE` merge is locally supported.

The generated canonical record nevertheless inherits the KOMODO note
`Aerobic: Yes`. DSMZ 1451 says to sparge the medium with an 80% N2 / 20% CO2
mixture for 30-45 min to make it anoxic and then dispense under the same gas
atmosphere. The aerobic note is unsupported for this DSMZ 1451 recipe and
contradicts its preparation.

The exact ignored-file search
`rg --no-ignore --hidden -n "KOMODO_1451|mediadive.medium:1451|DSMZ Medium 1451|DEFERRISOMA medium|deferrisoma_medium" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found only the expected DSMZ 1451 owner, KOMODO 1451 owner, generated merged
record, and generated index entries for this exact identity.

## Evidence

DSMZ Medium 1451 supports a 1003 ml final volume with KH2PO4 0.33 g,
(NH4)2SO4 0.33 g, KCl 0.33 g, NaCl 18 g, CaCl2 x 2H2O 0.33 g, MgCl2 x 6H2O
4 g, yeast extract 0.20 g, Trace element solution SL-10 1 ml,
Selenite-tungstate solution 1 ml, ferric citrate 2.50 g, Na2CO3 1 g,
Wolin's vitamin solution (10x) 1 ml, and distilled water 1000 ml. The imported
main-row values are correctly normalized to 1003 ml: for example, 18 g NaCl is
17.9462 g/L and 2.5 g ferric citrate is 2.49252 g/L.

The generated record flattens the three 1 ml stocks. The source uses
Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin
solution (10x) as stock additions; the generated record has no `solutions`
array and promotes HCl, FeCl2 x 4H2O, ZnCl2, NaOH, selenite, tungstate,
biotin, folic acid, and the other stock children into top-level final-medium
ingredients at full stock concentration.

DSMZ also includes a strain-specific supplement note for DSM 103037: supplement
the autoclaved medium with acetate, formate, glucose, and Na2S x 9H2O from
sterile anoxic stocks, reduce carbonate to 0.50 g/L, and adjust final pH to
5.5-6.0. The generated record omits that conditional instruction.

## Completeness

Consequential gaps:

- Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin
  solution (10x) are missing as 1 ml solution additions.
- Stock recipe rows are unscaled final ingredients.
- The 1000 ml main distilled-water row and the three nested stock water rows are
  missing.
- The SL-10 stock preparation text is copied as final-medium step 2 without
  stock scope.
- The source-supported DSM 103037 supplement note is missing.
- The generated KOMODO note says `Aerobic: Yes`, contradicting the DSMZ anoxic
  sparging instructions that own the formula.

No growth rates are required for this DSMZ recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | Three DSMZ 1 ml stock solutions are flattened into the final ingredient list. | DSMZ 1451 lists SL-10, selenite-tungstate, and Wolin 10x vitamin stocks as separate 1 ml rows; generated output stores their unscaled children as final ingredients. | DSMZ/MediaDive import and KOMODO DSMZ-enrichment logic |
| Major | Water rows are missing. | DSMZ 1451 includes 1000 ml final water plus water rows in each 1 L stock; the generated record has no distilled-water ingredient. | `data/normalized_yaml/bacterial/deferrisoma_medium.yaml`; KOMODO enrichment copy |
| Major | The generated KOMODO evidence says the recipe is aerobic. | DSMZ 1451 instructs 80% N2 / 20% CO2 sparging to make the medium anoxic; the canonical generated notes retain `Aerobic: Yes`. | `data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml` |
| Minor | A stock-specific preparation step is not scoped to the stock solution. | The FeCl2/HCl dissolution step belongs to SL-10 but is emitted as final-medium step 2. | DSMZ preparation-step importer |
| Minor | The DSM 103037 conditional supplement is missing. | DSMZ 1451 gives strain-specific acetate, formate, glucose, Na2S, carbonate, and pH instructions. | DSMZ importer |

## Recommended Edits

- Keep SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as
  `1 ML_PER_L` solution ingredients or scale their children by 1/1003 while
  retaining stock provenance.
- Restore distilled-water rows in the main and stock-solution scopes.
- Remove or correct `Aerobic: Yes` in the KOMODO 1451 owner.
- Scope the FeCl2/HCl preparation note to SL-10.
- Capture the DSM 103037 supplement as a conditional strain-specific note or
  variant instead of dropping it.
- Regenerate the merged Deferrisoma record after both maintained parents are
  corrected.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated
  DSMZ 1451 and KOMODO 1451 records.
- Search ignored files for `mediadive.medium:1451`, `KOMODO_1451`, and
  `deferrisoma_medium` to verify that only the intended duplicate pair remains.
- Manually compare the regenerated formula, anoxic prep, and DSM 103037 note
  against DSMZ Medium 1451.

## Additional Notes

- The exact duplicate search included ignored and hidden files.
- `linkml-reference-validator` reported zero reference checks, so its pass does
  not exercise DSMZ, KOMODO, or MediaDive source identifiers.
