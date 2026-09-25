# YAML Record Review: anoxybacillus_tunisiense_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml
- Started UTC: 2026-09-21T13:18:16Z
- Finished UTC: 2026-09-21T13:19:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003050 |
| Label | anoxybacillus_tunisiense_medium |
| Original label | ANOXYBACILLUS TUNISIENSE MEDIUM |
| Source term | mediadive.medium:J704 |
| Maintained owner | data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml |
| Generated record | data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml |

This is a generated merge record. Future fixes should land in the normalized
MediaDive/JCM owner or the MediaDive import/stock-solution transform that
produced it, then the merge products should be regenerated.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The record correctly identifies JCM Medium 704, `ANOXYBACILLUS TUNISIENSE
MEDIUM`, as imported through the MediaDive `J704` accession. Its cited JCM URL
is live and returns medium 704 with the same title. TOGO Medium M726 is a
duplicate view of the same JCM `GRMD=704` source and agrees that the source
identity is JCM M704.

Ingredient grounding is mixed. Most hydrate-specific salts in the MediaDive
record are grounded to hydrate-specific ChEBI terms, including magnesium
chloride hexahydrate, calcium sulfate dihydrate, disodium hydrogenphosphate
dihydrate, iron(II) chloride tetrahydrate, manganese(II) chloride tetrahydrate,
cobalt chloride hexahydrate, copper(II) chloride dihydrate, sodium molybdate
dihydrate, and iron(III) chloride hexahydrate. The `NiCl2 x 6 H2O` row is
grounded to anhydrous `CHEBI:34887` / nickel dichloride, and `Trisodium citrate
x 2 H2O` is grounded to broader `CHEBI:53258` / sodium citrate.

## Evidence

The live JCM page supports 100 ml Base solution A, 20 ml Base solution B, 2.5 g
Tryptone, 2.5 g Yeast extract, and 880 ml distilled water in the top-level
recipe; Base A as its own 1 L solution containing 1.32 g NTA, 0.2 g
MgCl2.6H2O, 0.4 g CaSO4.2H2O, 5 ml Trace elements, 5 ml Fe citrate solution,
and 990 ml distilled water; Base B as its own 1 L phosphate solution; Trace
elements as its own 1 L trace-salt stock; and Fe citrate as its own 1 L stock.

The generated record only partially preserves that evidence:

- The top-level 2.5 g/L tryptone and 2.5 g/L yeast extract rows are source
  supported.
- The phosphate buffer, Base A minerals, Trace elements, and Fe citrate
  components are all stock-solution ingredients in the JCM source, not direct
  final-medium ingredients at the stock concentrations shown in this record.
- The `Nitrilotriacetic acid` row sums the 1.32 g/L Base A concentration and
  the 12.8 g/L Trace elements concentration into a single unsupported
  `14.120000000000001 G_PER_L` top-level value.
- `ph_value: 6.2` is not the final-medium pH in the source. JCM and TOGO both
  give 8.0 for the top-level medium, 7.2 for Base solution A, and a 6.0-6.5
  range for Trace elements.
- The three pH comments are real source comments, but the generated
  `preparation_steps` list attaches all three to the top-level medium instead
  of preserving the solution boundary for the 7.2 and 6.0-6.5 adjustments.

## Completeness

The consequential missing representation is the stock/solution hierarchy. The
record has no `solutions` entries for Base solution A, Base solution B, Trace
elements, or Fe citrate solution, so a downstream reader cannot reconstruct the
JCM recipe or distinguish final-medium components from stock components.

An ignored-inclusive exact search for
`CultureMech:003050|mediadive.medium:J704|anoxybacillus_tunisiense_medium__3d9581d2|GRMD=704`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the normalized owner, generated merge, registry/catalog entries,
archived validation reports, and the duplicate TOGO/JCM M704 sibling, but no
other maintained owner for this same MediaDive `J704` record.

The absence of `target_organisms` is not by itself a defect: this source recipe
establishes the formulation of JCM M704, not a strain-specific growth claim.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| major | Stock solutions are flattened into final-medium ingredients at stock concentration. | JCM M704 uses Base solution A and Base solution B as 100 ml and 20 ml top-level additions; Base A itself consumes 5 ml Trace elements and 5 ml Fe citrate solution. The generated record has no solution records and lifts each Base/Trace/Fe-citrate component into top-level `G_PER_L` rows. | `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`; likely source-specific importer or solution migration logic |
| major | NTA is duplicate-merged across distinct stock scopes. | The JCM source has 1.32 g NTA in Base solution A and 12.8 g NTA in Trace elements; the record stores one `14.120000000000001 G_PER_L` row with `[Merged 2 duplicates: 1.32, 12.8]`. | `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`; duplicate-merge rule |
| major | The top-level pH is unsupported and pH adjustment comments are unscoped. | The source top-level medium says pH 8.0, Base A says pH 7.2, and Trace elements says pH 6.0-6.5. The record has `ph_value: 6.2` and three top-level `ADJUST_PH` steps. | `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`; MediaDive/JCM import mapping |
| major | Two hydrate-specific ingredients are grounded to broader or anhydrous ChEBI identities. | `NiCl2 x 6 H2O` uses anhydrous `CHEBI:34887`; `Trisodium citrate x 2 H2O` uses `CHEBI:53258` for sodium citrate rather than a verified trisodium citrate dihydrate term or an explicit unresolved value. | `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml` |
| minor | The same JCM M704 source exists as a second unmerged TOGO record. | The ignored-inclusive exact search found TOGO Medium M726 / `CultureMech:010134` in `data/normalized_yaml/bacterial/TOGO_M726_Anoxybacillus_Tunisiense_Medium.yaml`, generated as `data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml`, and that record points to the same JCM `GRMD=704` page. | Merge fingerprinting after the two imports preserve the same stock hierarchy |

## Recommended Edits

1. In the maintained MediaDive/JCM owner or its importer, restore JCM M704 as a
   recipe with four solution boundaries: Base solution A, Base solution B,
   Trace elements, and Fe citrate solution.
2. Keep final-medium additions separate from 1 L stock ingredients. In
   particular, do not merge the two NTA rows or any stock-specific waters across
   Base A, Base B, Trace elements, and Fe citrate.
3. Store `ph_value: 8.0` for the top-level medium and scope the pH 7.2 and
   6.0-6.5 adjustment comments to Base solution A and Trace elements.
4. Re-ground `NiCl2 x 6 H2O` and `Trisodium citrate x 2 H2O` to exact,
   hydrate-specific ChEBI identities only if such terms are verified; otherwise
   leave those rows explicitly unresolved.
5. After both the TOGO and MediaDive JCM M704 records preserve equivalent stock
   structure, regenerate merges and confirm the two imports collapse or are
   otherwise marked as the same formulation instead of publishing duplicate
   generated records.

## Follow-up Checks

- Re-run `just validate data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`,
  `just validate-strict data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`,
  `just validate-terms data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`,
  and `just validate-references data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml`
  after the normalized owner or importer is changed.
- Re-run `just verify-merges` after regenerating `data/merge_yaml/merged/`.
- Manually compare the regenerated J704 merge against the live JCM GRMD=704
  page or the TOGO M726 API and verify all pH statements remain attached to the
  correct stock recipe.
- Re-run an ignored-inclusive exact search for JCM `GRMD=704`, `J704`, and
  `M726` before closing the duplicate-record follow-up so ignored generated
  pages and prior reports are included in the duplicate sweep.

## Additional Notes

`data/import_tracking/reports/concentration_plausibility.tsv` already flags the
1 g/L `FeCl2 x 4 H2O` and 2.7 g/L `FeCl3 x 6 H2O` rows in this record as
trace-salt stock magnitudes. Those are symptoms of the same missing-stock
boundary defect, not independent source concentrations to curate as top-level
final-medium values.
