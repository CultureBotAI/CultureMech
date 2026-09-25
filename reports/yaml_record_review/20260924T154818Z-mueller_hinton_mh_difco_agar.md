# YAML Record Review: mueller_hinton_mh_difco_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/mueller_hinton_mh_difco_agar.yaml
- Started UTC: 2026-09-24T15:48:18Z
- Finished UTC: 2026-09-24T15:49:31Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mueller_hinton_mh_difco_agar.yaml`.

The generated record is a merge of two TOGO sources:

- canonical `id`: `CultureMech:009481`
- canonical `media_term`: `TOGO:M2957`
- canonical `name`: `mueller_hinton_mh_difco_agar`
- canonical `original_name`: `Mueller-Hinton (MH; Difco) agar`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `SOLID_AGAR`
- `ingredients`: 4
- `merged_from`: `TOGO_M2984_Mueller-Hinton_broth` and
  `mueller_hinton_mh_difco_agar`

## Validation

- Open schema validation: Passed with `No issues found`.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated record incorrectly merges two distinct commercial Mueller-Hinton
products:

- `data/normalized_yaml/bacterial/mueller_hinton_mh_difco_agar.yaml`:
  `CultureMech:009481`, TOGO M2957, `Mueller-Hinton (MH; Difco) agar`.
- `data/normalized_yaml/bacterial/TOGO_M2984_Mueller-Hinton_broth.yaml`:
  `CultureMech:009505`, TOGO M2984, `Mueller-Hinton broth`.

An exact ignored-file-inclusive search for `CultureMech:009481`,
`TOGO:M2957`, `TOGO:M2984`, `M2957`, and `M2984` found only those two active
normalized owners, their generated merge, and registry/catalog entries in
current `data/` scope.

Both source owners share the same manually researched beef/casein/starch/agar
ingredient list. That fingerprint is not source-faithful for either record and
caused a broth source to be merged into an agar source.

## Evidence

The current TOGO M2957 API has no original source URL. It lists one component:
1 L `Mueller-Hinton (MH; Difco) agar`, labeled by GMO as `Difco` Mueller
Hinton agar and marked as an undefined complex component. The comment says MH
Difco agar was used for routine growth of bacterial strains, resistant
population selection, and vancomycin population analysis profiles.

The current TOGO M2984 API also has no original source URL. It lists one
component: 1 L `Mueller-Hinton broth (Becton, Dickinson)`, labeled by GMO as
BBL Mueller Hinton broth and marked as an undefined complex component. The
comment says `S. aureus` ATCC 29213 was grown overnight at 37 C in that broth.

The generated YAML does not preserve either source as a 1 L undefined
commercial product. It replaces both with a constituent list for
Mueller-Hinton Agar from an external Microbe Notes page that cites BD 211443
and Sigma 70191, even though M2957 says Difco agar and M2984 says Becton
Dickinson broth.

## Completeness

The generated record is not complete enough to represent either source. It
drops the complete TOGO M2957 commercial component and hides the complete TOGO
M2984 broth component behind a synonym. It also drops the source-supported
context that M2984 was used for overnight growth at 37 C.

## Findings

- TOGO M2957 agar and TOGO M2984 broth were merged despite naming different
  commercial products and different physical states.
- The generated M2957 recipe replaces the source 1 L `Mueller-Hinton
  (MH; Difco) agar` component with a beef/casein/starch/agar decomposition
  that is not in TOGO M2957.
- The M2984 broth source was collapsed into the same agar decomposition,
  including a 17 g/L agar row, even though TOGO M2984 names 1 L
  `Mueller-Hinton broth (Becton, Dickinson)`.
- The supplier catalog notes cite BD 211443 and Sigma 70191 via an external
  Microbe Notes page; neither live TOGO source cites that supplier/catalog set.
- The M2984 source context, overnight growth at 37 C, is not preserved.

## Recommended Edits

- Re-curate both maintained owners from their own TOGO payloads.
- Keep TOGO M2957 as an undefined 1 L `Mueller-Hinton (MH; Difco) agar`
  source record unless direct Difco formulation evidence is added.
- Keep TOGO M2984 as a separate undefined 1 L
  `Mueller-Hinton broth (Becton, Dickinson)` source record and do not add agar
  to it.
- Remove the `SOURCE_DUPLICATE`-by-fingerprint merge between M2957 and M2984.
- Drop or replace the unsupported Microbe Notes supplier decomposition.
- Regenerate merged YAML after repairing the owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML files.
- Confirm an ignored-file-inclusive exact search for `TOGO:M2957` and
  `TOGO:M2984` finds two separate generated records.
- Confirm no regenerated M2984 broth record contains a pure agar ingredient.

## Additional Notes

None.
