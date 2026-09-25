# YAML Record Review: thioglycolate_medium_merck_108190

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioglycolate_medium_merck_108190.yaml
- Started UTC: 2026-09-25T13:02:15Z
- Finished UTC: 2026-09-25T13:02:39Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 153 THIOGLYCOLATE MEDIUM (MERCK 108190) import.
- The record was merged from `thioglycolate_medium_merck_108190`.
- The checked sources were MediaDive 153 and DSMZ Medium 153.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 153, THIOGLYCOLATE MEDIUM (MERCK 108190).
- MediaDive and DSMZ agree on the DSMZ 153 identity and pH 7.1.
- No conflicting duplicate merge was observed.

## Evidence

- DSMZ 153 lists 15 g Trypticase, 0.5 g L-cystine, 2 g glucose, 5 g yeast extract, 2.5 g NaCl, 0.5 g Na-thioglycolate, 0.5 ml 0.1% sodium resazurin, optional 15 g agar, and 1000 ml distilled water.
- DSMZ 153 says to sparge the medium with 100% N2 for 30 to 45 min, adjust to pH 7.1 with 5% Na2CO3 if needed, dispense under the same gas atmosphere, and autoclave.

## Completeness

- The formula, optional agar, pH value, and anaerobic autoclaving instruction are mostly present.
- The 1000 ml distilled-water row is missing.
- `Trypticase` is grounded to CHEBI:78018, dodecylphosphocholine, which is not a Trypticase term.

## Findings

- The `Trypticase` primary `term` is wrong even though the ingredient label was preserved.
- The DSMZ 153 water row is omitted.

## Recommended Edits

- Remove or replace the incorrect `CHEBI:78018` grounding for `Trypticase`.
- Restore the 1000 ml distilled-water row from DSMZ 153.
- Keep optional agar marked as optional unless a solid-only variant is created.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Add a focused term-grounding regression for `Trypticase` if CHEBI enrichment is repaired.

## Additional Notes

- None found.
