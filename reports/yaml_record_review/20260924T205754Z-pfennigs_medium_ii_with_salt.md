# YAML Record Review: PFENNIG'S MEDIUM II WITH SALT

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_ii_with_salt.yaml
- Started UTC: 2026-09-24T20:57:54Z
- Finished UTC: 2026-09-24T20:57:54Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_ii_with_salt.yaml`, the merged KOMODO/direct-DSMZ record for DSMZ Medium 40 / PFENNIG'S MEDIUM II WITH SALT.

The merged record combines `KOMODO_40_PFENNIG_S_MEDIUM_II_WITH_SALT` and `pfennigs_medium_ii_with_salt`, both tracing to DSMZ Medium 40.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_ii_with_salt.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The source identity is DSMZ Medium 40, which the DSMZ PDF defines as Medium 29 plus 1% NaCl. The top-level 10 g/L NaCl row is source-faithful.

The rest of the ingredient list is not grounded to the correct DSMZ 40 scope. DSMZ 40 should inherit the DSMZ 29 solution hierarchy, but the MediaDive graph also exposed a `Main sol. 28` branch and the normalized record flattened both branches into final top-level rows. As a result, Solution A, bicarbonate, heterotrophic salts, resazurin, vitamin B12, and trace-stock rows are duplicated or taken from the wrong Pfennig stock.

The `parent_media` metadata also points at `data/normalized_yaml/bacterial/pfennigs_medium_ii_with_salt.yaml`, one of this record's own merged sources, so the retained `SOURCE_DUPLICATE` relationship is redundant after merge.

## Evidence

- Fetched the DSMZ Medium 40 PDF and confirmed its complete formula is "To medium 29 add 1% NaCl."
- Fetched MediaDive medium 40 and confirmed `Main sol. 40` is represented as `Main sol. 29` plus 1% NaCl.
- Inspected the MediaDive graph and observed that it also exposes `Main sol. 28` and its SL-12 B trace solution, which are not part of DSMZ 40 except by an over-broad traversal.
- Compared that graph with the merged ingredient list and confirmed many concentrations are sums of the DSMZ 29 branch and the extra DSMZ 28 branch.

## Completeness

The target preserves the 10 g/L NaCl addition but does not preserve DSMZ 29, the only recipe DSMZ 40 references. It omits the inherited DSMZ 29 pH range of 6.8-7.1 and the nested Solution A-F / SL-10 B / sulfide solution scopes.

Because the wrong inherited branch is flattened, the record includes SL-12 B components such as Na2-EDTA and MnCl2 x 2 H2O while omitting the correct DSMZ 29 SL-10 B aliquot and its HCl stock component.

## Findings

- Medium 29 and Medium 28 branches were both flattened, causing doubled values such as `60.0 G_PER_L` NaHCO3, `0.2 G_PER_L` vitamin B12, `1.086956 G_PER_L` CaCl2 x 2 H2O, and `1.086956 G_PER_L` yeast extract.
- Heterotrophic-salts components from two related but distinct stocks were summed, yielding non-source values such as `27.4615 G_PER_L` ammonium chloride and `39.2308 G_PER_L` MgSO4 x 7 H2O.
- The trace-stock block is wrong for DSMZ 40. DSMZ Medium 40 inherits Medium 29's SL-10 B through Medium 29, but the target contains SL-12 B rows including Na2-EDTA and MnCl2 x 2 H2O.
- The 1.5% sulfide stock and 3% neutralized sulfide feed were merged into one `44.8148 G_PER_L` Na2S x 9 H2O row.
- Stock concentrations are represented as final concentrations throughout the ingredient array.
- The inherited pH range 6.8-7.1 is missing.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.
- The first `curation_history` timestamp is malformed: `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Re-normalize DSMZ Medium 40 as DSMZ Medium 29 plus 1% NaCl.
- Traverse only the DSMZ 29 branch needed to define Medium 40; do not flatten `Main sol. 28` as a separate sibling branch.
- Preserve DSMZ 29's Solution A-F, Trace element solution SL-10 B, and Neutralized sulfide solution as scoped intermediates.
- Remove SL-12 B-only rows from the DSMZ 40 final formula.
- Carry the inherited 6.8-7.1 pH range.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.
- Repair the malformed KOMODO curation timestamp.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated DSMZ 40 record.
- Verify the regenerated DSMZ 40 record contains one 10 g/L NaCl addition over DSMZ 29, not a sum of Medium 29 and Medium 28 stock rows.
- Confirm no Na2-EDTA or SL-12 B-only components remain in the Medium 40 formula.
- Search with ignored files included for `DSMZ_Medium40`, `komodo.medium:40`, and `mediadive.medium:40` to confirm KOMODO and direct DSMZ source duplicates still converge while retaining clear provenance.

## Additional Notes

Empty optional fields were not treated as defects. The `SOURCE_DUPLICATE` link is conceptually correct before merge; the issue is that a pointer to a merged source survived inside the merged canonical record.
