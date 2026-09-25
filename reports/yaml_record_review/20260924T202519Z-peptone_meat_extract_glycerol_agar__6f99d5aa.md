# YAML Record Review: peptone_meat_extract_glycerol_agar__6f99d5aa

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_meat_extract_glycerol_agar__6f99d5aa.yaml
- Started UTC: 2026-09-24T20:25:19Z
- Finished UTC: 2026-09-24T20:25:19Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:008915`, `peptone_meat_extract_glycerol_agar`, from the maintained TOGO owner `data/normalized_yaml/bacterial/TOGO_M2329_Peptone_Meat_Extract_Glycerol_Agar.yaml`.

The record represents TOGO M2329, Peptone Meat Extract Glycerol Agar, sourced from the DSMZ medium 250 PDF. Its generated recipe has 1000 g/L distilled water, 20 g/L glycerol, 15 g/L agar, 3 g/L meat extract, and 5 g/L Proteose peptone no. 3.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_meat_extract_glycerol_agar__6f99d5aa.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The source identity is clear: TOGO M2329 links directly to the DSMZ medium 250 PDF, which is PEPTONE MEAT EXTRACT GLYCEROL AGAR.

The same DSMZ medium 250 recipe is also represented by `data/merge_yaml/merged/peptone_meat_extract_glycerol_agar__14f6bae7.yaml`, which merges KOMODO medium 250 with a direct MediaDive/DSMZ 250 import. Those records are the same source family, but they cannot currently merge with this TOGO owner because of volume-unit differences and the unresolved 15 g versus 20 g agar conflict between the DSMZ PDF and MediaDive REST.

## Evidence

The DSMZ medium 250 PDF and TOGO M2329 both support 1000 ml distilled water, 20 ml glycerol, 15 g agar, 3 g meat extract, 5 g Proteose peptone no. 3, and pH adjustment to 7.0.

TOGO M2329 also carries pH 7.0 in its metadata and preserves the pH adjustment as a source comment. Both pH details are absent from this maintained owner and the generated record.

The ingredient grounding is otherwise reasonable: agar maps to `CHEBI:2509`, glycerol maps to `CHEBI:17754`, and the peptone and meat extract complex ingredients are left ungrounded.

## Completeness

The record has the full DSMZ/TOGO ingredient row set, but it has two volume rows represented with mass-concentration units and it drops the source pH metadata and pH-adjustment preparation instruction.

It is also split from the KOMODO / direct DSMZ generated record for medium 250, even though TOGO M2329 and those owners trace to the same DSMZ medium.

## Findings

1. Needs curation: `Distilled water` is encoded as `1000 G_PER_L`, but TOGO M2329 and the DSMZ PDF specify `1000 ml`.
2. Needs curation: `Glycerol` is encoded as `20 G_PER_L`, but TOGO M2329 and the DSMZ PDF specify `20 ml`.
3. Needs curation: the source pH 7.0 and `Adjust pH to 7.0` preparation instruction are missing from the maintained owner and generated record.
4. Needs curation: DSMZ medium 250 is split across this TOGO M2329 generated record and the KOMODO / direct DSMZ generated sibling. The split should be resolved after volume units and the DSMZ-PDF-versus-MediaDive agar disagreement are curated.

## Recommended Edits

1. Repair `Distilled water` and `Glycerol` in `data/normalized_yaml/bacterial/TOGO_M2329_Peptone_Meat_Extract_Glycerol_Agar.yaml` so their units remain source volume units.
2. Add `ph_value: 7.0` and a pH-adjustment preparation step from the TOGO metadata/comment and DSMZ PDF.
3. Reconcile the separate KOMODO / direct DSMZ medium 250 owners against the DSMZ PDF and MediaDive REST agar discrepancy.
4. Regenerate merged YAML and verify all DSMZ medium 250 source owners collapse into the expected source-duplicate merge.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M2329`, `DSMZ_Medium250`, `mediadive.medium:250`, and `komodo.medium:250` after regeneration to verify DSMZ medium 250 is no longer split unintentionally.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M2329`, `M2329`, `DSMZ_Medium250`, and `CultureMech:008915`.
