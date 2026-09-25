# YAML Record Review: mycobacterium_medium__7c2577c5

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycobacterium_medium__7c2577c5.yaml
- Started UTC: 2026-09-24T16:09:20Z
- Finished UTC: 2026-09-24T16:10:41Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:009855` for
`mycobacterium_medium`, a single-source generated record from
`TOGO_M467_Mycobacterium_Medium.yaml` grounded to `TOGO:M467`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycobacterium_medium__7c2577c5.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO identity is internally consistent: `TOGO:M467` is `Mycobacterium
Medium`, cites original source `JCM_M466`, and points to JCM `GRMD=466`.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files found the same
`GRMD=466` source represented separately as the active
`data/normalized_yaml/bacterial/JCM_J466_MYCOBACTERIUM_MEDIUM.yaml` owner and
generated separately as `data/merge_yaml/merged/MYCOBACTERIUM_MEDIUM.yaml`.
Those two records are not linked to this TOGO import.

## Evidence

The TOGO API for `M467` gives:

- Name: `Mycobacterium Medium`
- Original source: `JCM_M466`
- Source pH: `7.0`
- Distilled water: 1 L
- MgSO4 x 7H2O: 0.6 g
- KH2PO4: 1 g
- Tween 80: 0.5 g
- Glycerol: 50 ml
- Na2HPO4 x 12H2O: 2.5 g
- Trisodium citrate: 1.5 g
- Agar: 15 g
- Yeast extract (BD-Difco): 2 g
- Proteose peptone No. 3: 2 g
- Casein peptone, tryptic digested: 2 g

TOGO also carries the source comment `Adjust pH to 7.0.` The original JCM
`GRMD=466` URL currently returns `Nothing found`, so TOGO is the available live
source for this JCM-derived import.

## Completeness

All eleven TOGO component rows are present, but two liquid quantities were
normalized incorrectly. `Distilled water` became `1 G_PER_L` instead of 1 L,
and `Glycerol` became `50 G_PER_L` instead of a 50 ml addition. The generated
record also preserves the top-level `ph_value` only indirectly through the
source import and has no preparation step for the TOGO pH-adjustment comment.

The related direct JCM owner appears to have a different legacy import failure:
it lacks the water row and its dry ingredient concentrations were divided by
1.05 L, apparently counting the 50 ml glycerol addition in the denominator.

## Findings

1. `Distilled water` has the wrong unit. TOGO gives a 1 L water addition, but
   the normalized and generated YAML say `1 G_PER_L`.

2. `Glycerol` has the wrong unit. TOGO gives a 50 ml addition, but the
   normalized and generated YAML say `50 G_PER_L`.

3. The TOGO pH-adjustment comment is not modeled as a `preparation_steps`
   entry, so the generated recipe omits `Adjust pH to 7.0.`

4. The equivalent direct JCM `GRMD=466` record is active but remains unmerged,
   leaving two generated Mycobacterium Medium records for the same JCM source.

5. The `Na2HPO4 x 12H2O` row is grounded to anhydrous disodium
   hydrogenphosphate, `CHEBI:34683`; that is broader than the dodecahydrate
   specified by TOGO.

## Recommended Edits

Repair the normalized TOGO owner and reconcile its active JCM duplicate:

- Change `Distilled water` to a 1 L water addition.
- Preserve `Glycerol` as a 50 ml addition.
- Import the TOGO comment as `ADJUST_PH` preparation step text.
- De-duplicate or relate `TOGO_M467_Mycobacterium_Medium.yaml` and
  `JCM_J466_MYCOBACTERIUM_MEDIUM.yaml` instead of leaving the same JCM medium
  as two independent generated records.
- Revisit the `Na2HPO4 x 12H2O` grounding and either use a hydrate-specific
  term when available or leave the source hydrate ungrounded instead of
  silently broadening it to anhydrous `CHEBI:34683`.

## Follow-up Checks

- Regenerate generated YAML and confirm `TOGO:M467` carries the source water,
  glycerol, and pH-adjustment semantics.
- Confirm the active `GRMD=466` duplicate is merged, related, or otherwise
  intentionally kept separate with an explicit rationale.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.

## Additional Notes

None found.
