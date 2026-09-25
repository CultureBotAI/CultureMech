# YAML Record Review: HALOARCHAEAL medium MH-1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml
- Started UTC: 2026-09-23T09:34:05Z
- Finished UTC: 2026-09-23T09:38:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml`, a generated
`MediaRecipe` with `id: CultureMech:004114`, `category: archaea`,
`physical_state: SOLID_AGAR`, `ph_value: 4.5`, and
`media_term.term.id: komodo.medium:1396`.

The generated record is derived from these maintained inputs:

- `data/normalized_yaml/archaea/KOMODO_1396_HALOARCHAEAL_medium_MH-1.yaml`
- `data/normalized_yaml/archaea/haloarchaeal_medium_mh_1.yaml`
- `data/normalized_yaml/archaea/haloarchaeal_medium_mh_1_replace_mineral_salts_solution_for_solid_medium_medium_1396_with_mineral_salts_solution_for_liquid_medium_medium_1396.yaml`

Future edits should repair the normalized parents or the MediaDive/KOMODO import
and merge rules, then regenerate `data/merge_yaml/merged/`; the generated
review target should not be edited directly.

## Validation

All structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml --out /private/tmp/haloarchaeal_medium_mh_1.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone records under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The source identity is recoverable: the record is KOMODO Medium 1396, KOMODO
maps it to DSMZ/MediaDive Medium 1396, and MediaDive and the DSMZ PDF both name
the recipe `1396. HALOARCHAEAL MEDIUM MH-1`. Its solid physical state and pH
4.5 are also source-supported.

The formulation identity is not correct enough for an exact medium record. DSMZ
and MediaDive have a main solution containing 2 ml of `Trace Element Solution`
in 802 ml of final main-solution volume, and the stock solution itself is
prepared separately to 1000 ml. The generated record has no solution boundary
and instead places all 12 trace-stock ingredients in the final medium at their
stock concentrations.

Most major-ingredient ChEBI mappings are plausible, but at least three hydrated
salts are grounded to anhydrous salts or to a non-hydrate-specific salt:

- `FeSO4 x 6 H2O` is grounded as `CHEBI:75832`, `iron(2+) sulfate (anhydrous)`.
- `NiCl2 x 6 H2O` is grounded as `CHEBI:34887`, `nickel dichloride`.
- `CuCl2 x 6 H2O` is grounded as `CHEBI:49553`, `copper(II) chloride`.

`H3BO4` remains ungrounded. That is acceptable only if no exact verified
MIM/CHEBI term is available; it should not be force-grounded without checking
the packaged MediaIngredientMech label index.

## Evidence

Supported by the inspected DSMZ and MediaDive sources:

- Medium identity: DSMZ/MediaDive 1396 is `HALOARCHAEAL MEDIUM MH-1`.
- Recipe pH: the medium is pH 4.5.
- The main solution contains L-glutamic acid, trisodium citrate dihydrate,
  KH2PO4, NH4Cl, K2SO4, NaCl, casamino acids, yeast extract, `FeSO4 x 6H2O`,
  `Trace Elements (see below)`, agar, and distilled water.
- The 12 trace salts are members of a separate trace-element stock solution,
  not final-medium ingredients at stock concentration.
- The medium is adjusted to pH 4.5 with 40% KOH and autoclaved.
- The trace-element stock is adjusted to pH 4.0.

Unsupported or over-scoped claims:

- `CoCl2 x 6 H2O`, `MnCl2 x 4 H2O`, `ZnCl2`, `H3BO4`,
  `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `CuCl2 x 6 H2O`, `AlCl3`,
  `Na2WO4 x 2 H2O`, `CaCl2 x 2 H2O`, `BaCl2 x 2 H2O`, and
  `Na2S2O3 x 5 H2O` are not supported as final-medium components at 0.01 to
  2 g/L. Those values are stock concentrations before addition of 2 ml stock to
  the final medium.
- Distilled water is absent from both the main recipe and the trace stock.
- The generated record omits the KOH pH adjustment, autoclaving step, and
  pH 4.0 adjustment scoped to the trace stock.
- The DSMZ PDF's strain-scoped magnesium chloride note is not represented.
  That prose gives different `MgCl2 x 6H2O` concentrations for two strains and
  needs either separate strain-specific variants or an explicit unresolved
  discussion.
- The generated `parent_media.notes` claim that the KOMODO and DSMZ records'
  local physical-state, pH, ingredient, and concentration signatures "match
  exactly" is not source-supported as an evidence claim; it is only a statement
  about the current, already-flattened local YAML state.

## Completeness

- The record has enough provenance in `media_term` and `notes` to recover DSMZ
  Medium 1396 through KOMODO, but it lacks first-class `sources` entries for
  DSMZ and KOMODO.
- No `target_organisms` or `growth_metrics` are asserted, so no organism-growth
  evidence is missing from those slots.
- An exhaustive exact `rg --no-ignore --hidden` search over
  `data/merge_yaml` and `data/normalized_yaml` for the KOMODO and MediaDive
  accessions found the direct DSMZ record, the KOMODO record, and one KOMODO
  replacement variant.
- An exhaustive `find data/normalized_yaml` search for the two normalized
  duplicate filenames found them only under `data/normalized_yaml/archaea`, not
  under the `data/normalized_yaml/bacterial` paths embedded in the variant
  metadata.

## Findings

### Blocker

None found.

### Major

1. The trace-element stock was flattened into the final medium at stock
   concentration. The generated record lists all 12 stock ingredients as final
   g/L ingredients even though DSMZ and MediaDive define a separate 1000 ml
   trace stock and add only 2 ml of that stock to the 802 ml main solution.
   Owner: the two normalized DSMZ/KOMODO parents, the replacement variant, or
   the source import that materializes DSMZ subsolutions.

2. Required source material was lost during import and merge. DSMZ and
   MediaDive both carry distilled water in the main solution and in the
   trace-element stock; the generated record carries neither water row, carries
   no preparation steps, and drops the strain-specific `MgCl2 x 6H2O` note from
   the DSMZ PDF. Owner: the direct MediaDive parent plus the KOMODO
   DSMZ-enrichment path that copied DSMZ 1396 into KOMODO records.

3. Several hydrate-specific ingredients are grounded too broadly or to the
   wrong hydrate. `FeSO4 x 6 H2O` is explicitly not anhydrous, and both
   `NiCl2 x 6 H2O` and `CuCl2 x 6 H2O` need hydrate-specific resolution or
   should remain unresolved. Owner: the normalized parents' ingredient
   `term` and `mediaingredientmech_chebi_term` mappings, backed by the
   packaged MediaIngredientMech label index.

4. The generated duplicate relationship overstates the local records'
   equivalence and embeds stale owner paths. The KOMODO record points at
   `data/normalized_yaml/bacterial/haloarchaeal_medium_mh_1.yaml`, and the
   direct DSMZ record points at
   `data/normalized_yaml/bacterial/KOMODO_1396_HALOARCHAEAL_medium_MH-1.yaml`;
   exhaustive `find` found those files under `data/normalized_yaml/archaea`
   only. Owner: normalized `parent_media` / `variant_children` metadata and
   the merge logic that copies it into the generated canonical record.

### Minor

1. The generated record stores source accessions and the DSMZ PDF URL only in
   `media_term` and free-text `notes`. First-class `sources` entries would make
   provenance machine-checkable. Owner: the normalized parents or importers.

2. The direct MediaDive normalized parent appears to have copied the
   trace-stock pH 4.0 adjustment into the final medium's preparation steps.
   That step should be scoped to the stock solution once solution nesting is
   restored. Owner: `data/normalized_yaml/archaea/haloarchaeal_medium_mh_1.yaml`
   or the MediaDive solution importer.

## Recommended Edits

1. Represent DSMZ 1396 with the main solution plus a nested 1000 ml
   trace-element solution; keep the 2 ml stock addition in the final recipe
   instead of copying stock g/L values into the final medium.
2. Restore distilled water in the main solution and in the trace-element
   stock, with amounts matching DSMZ and MediaDive.
3. Add the pH 4.5 KOH adjustment and autoclaving instruction to the final
   medium; scope the pH 4.0 adjustment to the trace stock.
4. Model the DSMZ magnesium-chloride note as strain-specific variants if the
   schema can express them, or add a concrete discussion noting the unresolved
   strain-specific `MgCl2 x 6H2O` concentrations.
5. Recheck and correct the Fe, Ni, and Cu chloride/sulfate hydrate groundings
   against the packaged MIM label index and OAK; leave any exact hydrate
   without a verified term unresolved.
6. Rebuild or repair `parent_media`, `variant_children`, and
   `variant_modifications` so they point to the maintained archaeal YAML paths
   and no longer claim exact signature equivalence before solution nesting is
   represented correctly.
7. Regenerate `data/merge_yaml/merged/haloarchaeal_medium_mh_1.yaml` after the
   normalized inputs or importers are fixed.

## Follow-up Checks

- Re-run strict, term, and reference validation on each edited normalized
  parent.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge products.
- Re-open DSMZ_Medium1396.pdf and MediaDive REST medium 1396 to manually
  confirm the generated canonical record preserves the main solution, the
  trace-element stock, water rows, pH steps, and the strain-specific magnesium
  note.
- Run an ignored-file-inclusive exact search for `mediadive.medium:1396`,
  `komodo.medium:1396`, and `DSMZ Medium: 1396` to ensure only the intended
  normalized parents and generated duplicate remain after the repair.

## Additional Notes

- The public TogoMedium page was not needed for this record because the record
  names KOMODO and DSMZ/MediaDive, and the maintained parent set contained only
  KOMODO/DSMZ sources for accession 1396.
- The reported missing `data/normalized_yaml/bacterial/...` paths were checked
  with `find`; the search did not honor `.gitignore` and covered the whole
  `data/normalized_yaml` tree.
