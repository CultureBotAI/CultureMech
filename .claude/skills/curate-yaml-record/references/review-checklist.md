# CultureMech record review checklist

Use this for claim-level review of one `MediaRecipe` or `SolutionRecipe`. Empty
optional fields are not automatically defects.

## Evidence standard

- Put evidence on the narrowest representable claim and verify identifiers and
  source text before citing them.
- A source recipe establishes what it says, not that every organism grows or
  grows optimally in the formulation.
- A search result is discovery metadata. Inspect the database record, paper,
  or source document before using it.
- Preserve conflicting formulations or version differences explicitly; do not
  blend them into an unsupported synthetic recipe.
- State bounded negative searches as “not found,” never “does not exist.”

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | ID, lineage token, name, source accession, record kind, and category identify one medium or stock solution. | No similarly named medium, variant, or solution is being conflated. |
| Source provenance | `sources`, `source_data`, import metadata, references, and retrieval/version detail agree. | A reader can recover the authoritative formulation and distinguish imported from curator-added content. |
| Ingredients | Ingredient identity, exact supplied form, quantity, unit, role, and order/grouping match the source. | Every stated component is supported; unresolved ingredients remain explicit. |
| Solutions | Referenced stock solution, amount, concentration, nesting, and preparation boundary are correct. | Stock and final-medium quantities are not conflated and references resolve. |
| Arithmetic | Totals, dilutions, concentration conversions, and final volume are dimensionally consistent. | No conversion assumes an unstated density, stock strength, or final volume. |
| Conditions | pH, temperature, salinity, light, atmosphere, vessel, and physical state retain source context. | Values are scoped to preparation, incubation, or storage correctly. |
| Preparation | Step order, sterilization, cooling, post-autoclave additions, storage, and shelf life match the protocol. | Following the record would not materially change the source recipe. |
| Organisms/growth | Taxon or strain, growth outcome, conditions, medium variant, and evidence are aligned. | Growth claims do not generalize beyond the tested organism and conditions. |
| Classification | Medium type, nutritional class, functional role, applications, parents, and variants are source-supported. | Filing choices do not erase alternate roles or imply unsupported equivalence. |
| Evidence | Reference identifiers resolve; snippets are exact; notes distinguish interpretation. | Every consequential curator claim is traceable to an inspected source. |
| Discussions/flags | Each item names a concrete conflict, uncertainty, or next curation action. | No placeholder task or coverage-filling prose remains. |
| Audit | `curation_history` describes only the actual change and preserves older entries. | Provenance is append-only and names the acting curator/process honestly. |

## Data ownership

- Curate authoritative records under `data/normalized_yaml/`.
- Fix imported/source-owned claims in their maintained input or importer when a
  direct normalized edit would be overwritten.
- Regenerate `data/merge_yaml/merged/` and page/browser outputs; never curate
  them directly.
- Use the repository's ID allocator for new IDs and the packaged MIM index for
  publication-time ingredient resolution.
