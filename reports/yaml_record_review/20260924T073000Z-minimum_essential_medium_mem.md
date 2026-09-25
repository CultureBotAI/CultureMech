# YAML Record Review: minimum_essential_medium_mem

- Repository: CultureMech
- Record: data/merge_yaml/merged/minimum_essential_medium_mem.yaml
- Started UTC: 2026-09-24T07:30:00Z
- Finished UTC: 2026-09-24T07:31:08Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001122`
- Generated name: `minimum_essential_medium_mem`
- Generated source file: `data/merge_yaml/merged/minimum_essential_medium_mem.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/minimum_essential_medium_mem.yaml`
- Upstream source: DSMZ/MediaDive medium `1638`, `Minimum Essential Medium (MEM)`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/minimum_essential_medium_mem.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive medium `1638`.
- The `media_term` points to `mediadive.medium:1638`.
- `MEM-Medium` is an unmapped commercial product-style ingredient and has no term grounding.
- The record is categorized as `bacterial`, but the source is a canine macrophage cell-line cultivation medium.

## Evidence

- MediaDive REST for medium `1638` defines one `Main sol. 1638` solution with `MEM-Medium`, attribute `Gibco 31095-029`, amount `1`, and unit `x`.
- The DSMZ PDF for medium 1638 lists Minimum Essential Medium for DH82 canine macrophage cells and names `MEM (1x)` with product `Gibco 31095-029`.
- Neither MediaDive nor the DSMZ PDF discloses the internal commercial MEM formulation.
- The September 2026 normalized owner already replaced the old `MEM-Medium` 1 g/L row with `MEM (1x) Gibco 31095-029` at `VARIABLE`.

## Completeness

- The generated merged file is stale relative to `data/normalized_yaml/bacterial/minimum_essential_medium_mem.yaml`.
- The generated record does not preserve the September 2026 `ingredients_curated` and `has_unmapped_ingredients` flags.
- The generated record does not preserve the September 2026 PDF `references` entry.
- The generated record still places the DH82 cell-line sentence in `preparation_steps`; the source text is context for use, not a preparation operation.

## Findings

- High: The generated record misstates a 1x commercial MEM reagent as `1 G_PER_L`. DSMZ/MediaDive provide only the product and `1 x`, with no gram amount or internal formulation.
- Medium: The generated record is stale relative to the normalized source that already fixed the product quantity, notes, references, and quality flags.
- Medium: The `bacterial` category is not supported by the DSMZ 1638 source, which describes a canine macrophage cell-line medium rather than a bacterial growth medium.
- Low: The source context was imported as a `MIX` preparation step even though it is not a mixing instruction.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/minimum_essential_medium_mem.yaml` from `data/normalized_yaml/bacterial/minimum_essential_medium_mem.yaml` so the product placeholder, source note, quality flags, and PDF reference reach the generated output.
- Review whether a cell-line MEM record belongs in CultureMech's bacterial category, or should be moved to a more accurate category if one exists.
- Move the DH82/canine-macrophage phrase out of `preparation_steps` and into a source-context field if the schema supports one.

## Follow-up Checks

- Re-fetch MediaDive medium `1638` and confirm the curated row remains a 1x Gibco product with a variable concentration.
- Re-render the DSMZ PDF text and confirm no disclosed internal formula was missed.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
