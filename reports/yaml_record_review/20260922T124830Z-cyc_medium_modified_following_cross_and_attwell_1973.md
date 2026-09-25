# YAML Record Review: CYC-MEDIUM (modified following Cross and Attwell,1973)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml
- Started UTC: 2026-09-22T12:45:16Z
- Finished UTC: 2026-09-22T12:48:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005999 |
| Name | cyc_medium_modified_following_cross_and_attwell_1973 |
| Source | KOMODO Medium 550 copied from DSMZ / MediaDive medium 550 |
| Media term | komodo.medium:550, CYC-MEDIUM (modified following Cross and Attwell,1973) |
| Generated record | data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml |
| Maintained inputs | data/normalized_yaml/bacterial/KOMODO_550_CYC-MEDIUM_modified_following_Cross_and_Attwell_1973.yaml; data/normalized_yaml/bacterial/cyc_medium_modified_following_cross_and_attwell_1973.yaml; data/normalized_yaml/bacterial/medium_550_modified_for_dsm_17572.yaml |

The generated record merges three same-signature maintained inputs: one KOMODO
`550` record, one DSMZ / MediaDive `550` record, and one KOMODO `550_17572`
record that also records DSMZ medium 550 provenance. Future fixes belong in
those normalized records and in the shared merge projection.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml --out /private/tmp/cyc_medium_modified_following_cross_and_attwell_1973.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing validators prove that the generated YAML is schema-valid. They do
not check source-level completeness or whether complex product rows were
grounded to overly broad ChEBI terms.

## Identity and Grounding

The generated record's primary identity is internally consistent with the
canonical KOMODO input. `CultureMech:005999` is the stable ID of
`data/normalized_yaml/bacterial/KOMODO_550_CYC-MEDIUM_modified_following_Cross_and_Attwell_1973.yaml`,
and that record explicitly states DSMZ / MediaDive medium 550 provenance.
DSMZ and the live MediaDive REST API confirm the DSMZ 550 title and pH 7.2.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found all three
normalized duplicate inputs and no exact raw capture for `komodo.medium:550` or
`mediadive.medium:550` under `data/raw`. A `find` over `data/raw` also found no
filename containing `550`, including ignored files.

One ingredient grounding is wrong. The record grounds `Czapek Dox agar` to
`CHEBI:2509` / agar even though DSMZ and MediaDive list `Czapek Dox agar
(Merck)` as a 48 g component and list a separate 20 g `Agar` component. The
vendor Czapek-Dox agar row denotes a complex medium product, not plain agar.

## Evidence

The current DSMZ PDF and the live MediaDive REST export agree on these
components for 1 L:

| Source component | Source amount | Record amount |
|---|---:|---:|
| Czapek Dox agar (Merck) | 48 g/L | 48 g/L |
| Yeast extract (Oxoid) | 2 g/L | 2 g/L |
| Casamino acids (Difco) | 6.1 g/L | 6.1 g/L |
| Tryptophan | 0.02 g/L | 0.02 g/L |
| Distilled water | 1000 ml/L | missing |
| Agar | 20 g/L | 20 g/L |

The generated record preserves five of six source rows and keeps pH 7.2 as
`ph_value: 7.2`. The distilled-water omission is present in all three
maintained duplicate inputs and therefore appears to predate the August merge.

The generated record drops the only preparation step from the DSMZ-derived
input. That step is weakly structured as `MIX` with description `pH 7.2`, but
it did preserve the source pH instruction in addition to the scalar `ph_value`.

## Completeness

- The record has no `references`, `source_data`, `target_organisms`, or
  `growth_metrics`. Empty target-organism and growth-metric slots are
  acceptable because DSMZ Medium 550 is a recipe record, not an
  organism-specific growth assay.
- The missing distilled-water row is consequential because the source recipe
  includes it as a required 1000 ml component.
- The lack of structured `references` means reference validation has no DSMZ,
  MediaDive, or KOMODO source URL to check.
- The KOMODO records' specific `komodo.medium:550` and
  `komodo.medium:550_17572` public pages were not independently checked; the
  review verified the DSMZ / MediaDive medium 550 source that both KOMODO
  records claim as their copied composition.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Distilled water is missing from the merged recipe. | DSMZ and MediaDive both list 1000 ml distilled water; all three normalized inputs and the generated merge omit that row. | The three normalized inputs for DSMZ/KOMODO medium 550 |
| major | `Czapek Dox agar` is incorrectly grounded to ChEBI agar. | The source has separate `Czapek Dox agar` and `Agar` rows; grounding both to `CHEBI:2509` makes the 48 g/L Merck product look like additional plain agar. | The three normalized inputs for DSMZ/KOMODO medium 550 |
| minor | The generated record dropped pH preparation text and structured source references. | The scalar `ph_value` survived, but the DSMZ-derived normalized input's pH step and the DSMZ PDF URL are absent from the generated output. | Merge projection for duplicate MediaRecipe records |

## Recommended Edits

1. Add `Distilled water` at `1000 ML_PER_L` to the maintained DSMZ/KOMODO
   medium 550 inputs before regenerating the merged record.
2. Remove the `CHEBI:2509` grounding from `Czapek Dox agar` and leave that
   Merck product ungrounded or map it to a product-level vocabulary term; keep
   `CHEBI:2509` only on the separate `Agar` row.
3. Preserve or explicitly normalize the pH 7.2 preparation statement during
   duplicate merging.
4. Add structured `references` for the DSMZ Medium 550 PDF, the MediaDive
   medium 550 endpoint, and any KOMODO page or raw KOMODO row that proves
   `komodo.medium:550` and `komodo.medium:550_17572`.
5. Regenerate
   `data/merge_yaml/merged/cyc_medium_modified_following_cross_and_attwell_1973.yaml`
   after repairing the maintained inputs.

## Follow-up Checks

- Re-run open-schema, closed-schema, reference, and term validation on each
  repaired normalized input and on the regenerated merged record.
- Diff the regenerated record against DSMZ Medium 550 and MediaDive medium 550
  to verify the six required component rows and pH 7.2.
- Confirm that `Czapek Dox agar` and `Agar` no longer share the same ChEBI
  grounding.
- Re-run `rg --no-ignore --hidden` for `komodo.medium:550`,
  `komodo.medium:550_17572`, and `mediadive.medium:550` across
  `data/normalized_yaml` and `data/raw` after the repair to ensure there are no
  unhandled split copies.

## Additional Notes

- The duplicate merge itself is plausible by composition: the three maintained
  inputs contain the same five visible ingredient rows and state DSMZ medium 550
  provenance directly or indirectly.
- The generated canonical ID follows the KOMODO `550` record rather than the
  DSMZ / MediaDive `550` record, so the merged output keeps a KOMODO
  `media_term` even though DSMZ is the underlying recipe source.
