# YAML Record Review: CARCBOXYDOBRACHIUM PACIFICUM medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/carcboxydobrachium_pacificum_medium.yaml`
- Started UTC: 2026-09-22T04:19:45Z
- Finished UTC: 2026-09-22T04:22:17Z
- Verdict: needs curation

## Target

`carcboxydobrachium_pacificum_medium.yaml` is the generated single-source `MediaRecipe` for `CultureMech:006772`, `carcboxydobrachium_pacificum_medium`, sourced from KOMODO Medium 902.

The generated record was merged only from `data/normalized_yaml/bacterial/carcboxydobrachium_pacificum_medium.yaml` on fingerprint `cd390b71b8f24c8067658651f1108c47d830be8cff43817e86c6c4d608dd2f12`.

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The source identity points to KOMODO Medium 902. KOMODO 902 is labeled `CARCBOXYDOBRACHIUM PACIFICUM medium`, pH 7.0 with NaOH, and links directly to DSMZ Medium 902, so the generated record should be reconciled with the sibling DSMZ/MediaDive 902 record `CARCBOXYDIBRACHIUM_MEDIUM.yaml`.

The generated record failed to merge with DSMZ/MediaDive 902 because the KOMODO importer added a variable `NaOH` ingredient from the pH-buffer note. KOMODO lists NaOH with a null gram amount as a pH-adjustment / trace metabolite row, and DSMZ/MediaDive 902 describes NaOH only in the preparation text: adjust the basal solution to pH 7.0 with NaOH. It should not create a final variable-concentration recipe ingredient that changes the fingerprint.

The same grounding defects present in the DSMZ/MediaDive 902 owner are also present here: `Na2SiO3` is ungrounded, `NiCl2 x 6 H2O` points to anhydrous nickel dichloride, and `Sodium resazurin` plus `Calcium D-(+)-pantothenate` have primary terms without `mediaingredientmech_chebi_term` mirrors.

## Evidence

KOMODO Medium 902 links to the DSMZ Medium 902 PDF and gives final per-liter rows for the same basal recipe plus diluted trace/vitamin components. Its trace and vitamin component gram amounts are diluted final values, not one-liter stock strengths.

The normalized owner was later enriched from DSMZ Medium 902 and now carries the exact undiluted stock-row pattern from the DSMZ/MediaDive import:

- HCl is `2.5 G_PER_L` instead of KOMODO's diluted trace amount.
- FeCl2 x 4 H2O is `1.5 G_PER_L` instead of a milligram-per-liter final trace amount.
- NiCl2 x 6 H2O is `0.024 G_PER_L` instead of a microgram-to-milligram final trace amount.
- Biotin is `0.02 G_PER_L` instead of the diluted 1 ml Wolin-stock contribution.

The generated KOMODO record also lacks the DSMZ/MediaDive 902 anaerobic preparation instructions that explain N2 sparging, Hungate-type tubes or serum vials, autoclaving, filtered vitamins, anoxic reducing-agent stocks, the bicarbonate N2/CO2 stock, and final pH adjustment.

## Completeness

No structured solution additions remain for Trace element solution SL-10 or Wolin's vitamin solution (10x). The 1000 ml main water row is absent. No target organism or strain-specific evidence has been curated.

The `Aerobic: Yes` flag in the notes comes from KOMODO, but the DSMZ 902 preparation is explicitly anoxic and N2-sparged. That imported note should not be trusted over DSMZ's preparation conditions.

## Findings

- Needs curation: KOMODO 902 should merge as a source duplicate with DSMZ/MediaDive 902, but the importer promoted NaOH pH adjustment to a variable final ingredient and changed the merge fingerprint.
- Needs curation: Trace element solution SL-10 and Wolin's vitamin solution (10x) are flattened at undiluted DSMZ stock concentrations, in conflict with KOMODO's own final per-liter table and MediaDive's 1 ml stock additions.
- Needs curation: DSMZ/MediaDive 902 anaerobic preparation instructions were dropped from the KOMODO-derived record.
- Needs curation: the KOMODO note says `Aerobic: Yes` even though the linked DSMZ 902 preparation is anoxic.
- Minor: `Na2SiO3`, `NiCl2 x 6 H2O`, `Sodium resazurin`, and `Calcium D-(+)-pantothenate` need the same term cleanup as DSMZ/MediaDive 902.
- Minor: no source-backed target organism or growth evidence has been curated.

## Recommended Edits

- Reclassify the KOMODO `NaOH` row as pH-adjustment metadata instead of a final variable ingredient.
- Link `carcboxydobrachium_pacificum_medium.yaml` to `carcboxydibrachium_medium.yaml` as a `SOURCE_DUPLICATE` of DSMZ/KOMODO Medium 902 or otherwise make the merge fingerprint ignore pH-buffer metadata when formulas are the same.
- Rebuild the recipe with explicit 1 ml Trace element solution SL-10 and 1 ml Wolin's vitamin solution additions, or flatten those stocks to final concentrations before merging.
- Copy or inherit the DSMZ/MediaDive 902 preparation steps into the KOMODO 902 owner.
- Drop the misleading `Aerobic: Yes` note or replace it with source-backed anoxic preparation metadata.
- Apply the same `Na2SiO3`, nickel, sodium resazurin, and calcium pantothenate grounding fixes as the DSMZ/MediaDive 902 record.

## Follow-up Checks

- Regenerate both Medium 902 records and verify they collapse into one generated YAML or have an explicit duplicate relationship.
- Verify the regenerated formula against KOMODO Medium 902 and MediaDive medium 902 final-composition data.
- Run LinkML, strict, reference, and term validation after removing the variable NaOH ingredient and repairing stock concentrations.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to the normalized KOMODO 902 owner, its pH-buffer import handling, and the DSMZ/MediaDive 902 stock import before regenerating this output.
