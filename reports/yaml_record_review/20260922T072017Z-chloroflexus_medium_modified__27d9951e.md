# YAML Record Review: CHLOROFLEXUS MEDIUM (modified)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_medium_modified__27d9951e.yaml
- Started UTC: 2026-09-22T07:19:40Z
- Finished UTC: 2026-09-22T07:20:24Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002038 |
| Label | CHLOROFLEXUS MEDIUM (modified) |
| Generated record | data/merge_yaml/merged/chloroflexus_medium_modified__27d9951e.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chloroflexus_medium_modified.yaml |
| Source | DSMZ Medium 87 through `mediadive.medium:87` |

The reviewed file is a generated one-source merge of the direct DSMZ/MediaDive
normalized record. Future fixes belong in
`data/normalized_yaml/bacterial/chloroflexus_medium_modified.yaml` or in the
MediaDive import that produced it rather than in
`data/merge_yaml/merged/chloroflexus_medium_modified__27d9951e.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chloroflexus_medium_modified__27d9951e.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The record identity is correct: `CultureMech:002038`,
`CHLOROFLEXUS MEDIUM (modified)`, and `mediadive.medium:87` all point to DSMZ
Medium 87.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
merge fingerprint, and DSMZ import note found this generated record, its
normalized owner, normalized index entries, and the TOGO M3141 record that
cites the same DSMZ Medium 87 formulation through a separate import path.

## Evidence

The DSMZ Medium 87 PDF supports the record's parent pH of 8.2 and its core
parent-medium inputs after concentration normalization: yeast extract,
glycyl-glycine, `Na2HPO4 x 2 H2O`, `MgSO4 x 7 H2O`, `KNO3`, `NaNO3`, `NaCl`,
`CaCl2 x 2 H2O`, 5 mL Fe(III) citrate solution, 1 mL trace element solution
SL-6, and distilled water. DSMZ Medium 27 supports the delegated SL-6 stock
composition.

The imported ingredient list flattens three stock recipes into direct
ingredients. `Fe(III) citrate` is present at the stock row amount, `Na2S x 9
H2O` is present at the neutralized-sulfide stock strength, and all SL-6 salts
are present at their DSMZ Medium 27 stock strengths. The reviewed record has no
`solutions` array that would preserve Fe(III) citrate solution, Trace element
solution SL-6, or Neutralized sulfide solution as distinct nested stocks.

The source preparation was only partially captured. The DSMZ PDF instructs the
curator to distribute 90 mL medium into 100 mL screw-capped bottles and then
inject 1.0 mL neutralized sulfide solution into each bottle after autoclaving;
the record instead says 10 mL in 15 mL Hungate tubes and 0.1 mL sulfide into
each tube. Those scaled tube values are not in the cited DSMZ PDF. The record
also omits the medium storage statement, the 50 C 300-500 lux incubation
condition, the optional 0.1% yeast-extract supplement for heavy cell
suspensions, and the second neutralized-sulfide note about avoiding elemental
sulfur precipitation.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this imported source record.

The formula is incomplete as structured data until all three DSMZ stock
solutions are represented as nested solutions and linked from the parent
medium. The preparation is incomplete until the unsupported tube scaling is
either sourced or reverted to the cited DSMZ bottle protocol and the dropped
source notes are represented or explicitly judged out of scope.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Fe(III) citrate solution, neutralized sulfide solution, and SL-6 are flattened into direct ingredients at stock strength. **Owner:** `data/normalized_yaml/bacterial/chloroflexus_medium_modified.yaml` or the direct DSMZ/MediaDive importer. |
| Major | The record has no `solutions` entries for the three DSMZ stock solutions. **Owner:** the importer that maps DSMZ nested recipes into CultureMech `solutions`. |
| Major | Preparation steps rescale the cited 90 mL bottle protocol to a 10 mL Hungate-tube protocol and 0.1 mL sulfide addition without support from the cited DSMZ Medium 87 PDF. **Owner:** the direct DSMZ/MediaDive importer. |
| Minor | Secondary MediaIngredientMech links for `KNO3` and `NaNO3` remain on the deprecated `MediaIngredientMech:NNNNNN` identifier scheme despite available primary CHEBI terms. **Owner:** the MediaIngredientMech-to-CHEBI migration. |

## Recommended Edits

1. Update the direct DSMZ/MediaDive import path to preserve Fe(III) citrate
   solution, Trace element solution SL-6, and Neutralized sulfide solution as
   nested `solutions` rather than flattening their members into parent
   `ingredients`.
2. Attach DSMZ Medium 27's SL-6 recipe to the SL-6 solution and add it to the
   parent medium at the 1.00 mL source volume.
3. Represent the neutralized-sulfide stock as 3.00 g `Na2S x 9 H2O` in 100.00
   mL water, with 1.0 mL injected post-autoclave to each 90 mL parent-medium
   bottle.
4. Either source the 10 mL Hungate-tube scaling now in the record or restore
   the cited DSMZ Medium 87 90 mL bottle protocol.
5. Preserve or deliberately omit with a curation note the DSMZ storage,
   incubation, heavy-cell-suspension, and sulfide-stock clarity instructions.
6. Refresh `KNO3` and `NaNO3` secondary links so they use id-safe CHEBI link
   fields consistently with their primary terms.

## Follow-up Checks

Run the narrow generated-record validators after regenerating this record:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated YAML against DSMZ Medium 87 and DSMZ
Medium 27 to confirm the nested stocks, parent pH, bottle volumes,
post-autoclave sulfide addition, and retained preparation text.

## Additional Notes

The TOGO M3141 import of DSMZ Medium 87 is reviewed separately because it has a
different maintained owner and a different merge fingerprint.
