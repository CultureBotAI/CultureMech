# YAML Record Review: n_z_amine_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/n_z_amine_medium.yaml
- Started UTC: 2026-09-24T16:21:50Z
- Finished UTC: 2026-09-24T16:23:16Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:006003` for
`n_z_amine_medium`, a generated four-way merge currently canonicalized to
KOMODO `komodo.medium:554`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/n_z_amine_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The DSMZ 554 and KOMODO 554 identities are tied together correctly: KOMODO 554
explicitly cites DSMZ Medium 554, and MediaDive medium 554 is the same
`N-Z-AMINE-MEDIUM` base recipe.

The generated four-way merge is too broad. It also absorbs JCM J437,
`N-Z AMINE WITH SOLUBLE STARCH AND GLUCOSE`, as a synonym even though the live
JCM 437 page uses 15 g agar and DSMZ 554 uses 20 g agar. It further treats
KOMODO 554_44396 as a source duplicate even though that owner carries a
strain-specific pH range, 7.5-8.0, for `MEDIUM 554 MODIFIED FOR DSM 44396`.

The exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files also found two
unlinked TOGO mirrors: TOGO M2370 for a DSMZ 554 URL and TOGO M437 for the JCM
437 source.

## Evidence

MediaDive DSMZ 554 reports a 1000 ml main solution at pH 7.2 with:

- 10 g Glucose
- 20 g Starch, soluble
- 5 g Yeast extract
- 5 g N-Z amine
- 1 g CaCO3
- 20 g Agar
- 1000 ml Distilled water

JCM `GRMD=437` reports the same glucose, soluble starch, yeast extract, N-Z
Amine type A, and CaCO3 quantities, but uses 15 g agar plus 1 L distilled water
and an explicit `Adjust pH to 7.2.` step.

TOGO `M2370` is labeled `N-Z-Amine-Medium` and points to the DSMZ 554 PDF, but
its API lists 15 g agar and 1000 ml distilled water. TOGO `M437` mirrors the
JCM 437 source and lists 1 L distilled water.

## Completeness

The generated canonical record has the six non-water DSMZ 554 ingredients and
DSMZ pH 7.2, but it omits `Distilled water`, 1000 ml. It also erases the pH
7.5-8.0 distinction from the 554_44396 strain-specific variant and erases the
15 g agar distinction from JCM 437 by collapsing both into the 20 g agar DSMZ
554 fingerprint.

Two TOGO imports with matching source URLs remain active and generated
separately, so the source-equivalence graph is incomplete.

## Findings

1. DSMZ 554 water is missing from the generated canonical record.

2. JCM J437 is incorrectly merged as a source duplicate of DSMZ 554 even though
   JCM has 15 g/L agar and DSMZ has 20 g/L agar.

3. KOMODO 554_44396 is treated as a `SOURCE_DUPLICATE` and loses its
   strain-specific pH range of 7.5-8.0.

4. TOGO M2370 and TOGO M437 are active, source-related records but are not
   linked to the corresponding DSMZ 554 and JCM 437 families.

5. TOGO M2370 and TOGO M437 import water with mass units (`1000 G_PER_L` and
   `1 G_PER_L` respectively), so the unlinked duplicate owners also need unit
   repair.

6. The KOMODO owners carry malformed `.fZ` import timestamps.

## Recommended Edits

Repair the source families before regeneration:

- Add the 1000 ml `Distilled water` ingredient to the DSMZ 554 and KOMODO 554
  duplicate family.
- Keep DSMZ 554/KOMODO 554 separate from JCM 437 because of the 20 g/L versus
  15 g/L agar difference.
- Reclassify KOMODO 554_44396 as a pH variant or another non-duplicate variant
  that preserves pH 7.5-8.0.
- Inspect the DSMZ PDF behind TOGO M2370 and reconcile its 15 g agar against
  MediaDive DSMZ 554's 20 g agar before linking it.
- Link TOGO M437 to the JCM 437 family after correcting its 1 L water unit.
- Normalize the malformed KOMODO import timestamps.

## Follow-up Checks

- Regenerate merged YAML and confirm DSMZ 554, JCM 437, and KOMODO 554_44396
  are not all collapsed into one fingerprint.
- Confirm the regenerated DSMZ 554 record has seven source rows including
  distilled water.
- Re-run LinkML, strict, reference, and term validation on all regenerated
  affected records.

## Additional Notes

None found.
