# Concentration evidence contract

Read the current schema before applying; this contract does not add schema
fields or make a schema-valid claim scientifically supported.

## Required support for every assertion

- **Reference:** a verified `doi:10...` identifier or full persistent URL for
  the actual article, supplement, official recipe, protocol, or versioned data.
  Resolve DOI redirects and inspect the document. Prefer a PURL/permalink or
  archived version over an unstable download URL. A PMID can supplement the
  citation but does not replace the requested DOI/PURL requirement.
- **Snippet:** a nonempty exact quotation supporting this ingredient's amount.
  Verify units, denominator, and preparation stage in the same source, including
  relevant headers and footnotes. Record separately located exact excerpts and
  their locators in `explanation`; never splice them into a fabricated quote.
- **Claim scope:** explicitly name the ingredient, field path, medium/stock
  context, source version, and whether the value is directly reported or
  calculated. A citation about growth or ingredient function alone is not
  concentration evidence.
- **Source metadata:** title, authors, and year where available, with discovery
  mode, source type, access date, and locator. Unknown fields remain absent;
  explain important missing metadata in notes/report.

A ChEBI or unit-ontology PURL identifies a chemical or unit, not a recipe amount.
A journal homepage, generic search URL, transient signed link, or inaccessible
citation without inspected text does not meet the evidence requirement. A local
file path alone is not a persistent source identifier. Record source-access gaps
without inventing a DOI, PURL, quote, or publication date.

## Map to existing schema fields

| Claim or metadata | Storage |
| --- | --- |
| Ingredient amount | `IngredientDescriptor.concentration`: string `value`, `ConcentrationUnitEnum` `unit`, optional consistent `per_volume`. Applies to `ingredients[]`, stock `composition[]`, and nested compositions. |
| Evidence for that ingredient amount | The ingredient's `evidence[]`: `reference`, `supports: SUPPORT`, `snippet`, `explanation`. Explicitly scope the explanation to concentration, not just ingredient role. |
| Stock addition amount within a `MediaRecipe` | `solutions[...].concentration`, with evidence in the enclosing recipe's `evidence[]` and the full solution/field path in `explanation`. |
| Inline variant formulation | Evidence on the matching `variants[].evidence[]`, with the exact modification identified. Do not alter the parent's ingredient amount. |
| Bibliographic metadata | Root `references[]`: `reference`, `title`, `authors` (string), `year` (integer), and `notes`. |
| Discovery/source context | `references[].notes`: `source_type=...; discovery_mode=...; accessed_on=YYYY-MM-DD`, plus version/locator where useful. |
| Review/calculation context | `EvidenceItem.explanation`; use ingredient `notes` for preparation context. Do not put curator arithmetic inside `snippet`. |
| Audit trail | Append-only `curation_history[]`, with old/new amount, evidence reference, and reason. |

`EvidenceItem` supports formulation claims, although the ingredient's evidence
slot description currently mentions roles. Make the concentration claim explicit
and preserve any existing role evidence. A recipe-level formulation evidence
entry may also cover ingredient amounts when it unambiguously identifies every
supported field and ingredient.

`ConcentrationValue` has no `evidence`, `doi`, `purl`, or `snippet` slot.
`SolutionDescriptor` has no `evidence` slot. Do not add either. A standalone
`SolutionRecipe` has ingredient-level evidence on `composition[]`, but no root
`evidence` slot. For a stock-addition claim in that record, an existing,
appropriate `source_data.evidence[]` container may carry scoped evidence;
preserve its required `origin` and provenance meaning. If there is no appropriate
container, report `schema_gap` instead of fabricating one. Never infer a universal
stock working dose from how one receiving medium uses it.

Each `evidence[]` list uses `reference` as its identifier. Reuse/extend an entry
for the same reference without erasing its earlier claims. When one source
supports multiple claims, keep an exact snippet and explicitly label any other
short exact excerpts/locators and claim paths in `explanation`. The same source
can legitimately appear in separate ingredients' evidence lists. Do not add
fake URL fragments to evade duplicate-reference checks.

`supports: SUPPORT` requires support for the precise claim. `PARTIAL` or
`NO_EVIDENCE` must not be used as permission to insert a number. A conflict may
be reported or preserved as appropriately scoped counterevidence without claiming
it has been resolved.

## Provenance conventions

Use `reference: doi:<verified-doi>` for a DOI; use the full verified URL directly
for a PURL/permalink. The notation here is a placeholder, not a real citation.
Link the same reference in `references[]` to bibliographic context. When an
article DOI and a separate supplement URL are needed, retain both and identify
which inspected document contains the quote.

Suggested `source_type` values are `journal_article`, `culture_collection_page`,
`web_page`, `protocol`, and `dataset`. Suggested `discovery_mode` values are
`user_supplied`, `existing_record_reference`, `catalog_page`, `cross_reference`,
`pubmed_search`, and `manual_web_search`. These are notes conventions, not new
top-level fields or schema enums. Do not describe an AI-generated lead as the
information source when the evidence actually comes from a retrieved document.

## Units and preparation boundaries

- Preserve the source's stated range, precision, chemical form, and preparation
  stage. Do not replace a range by its midpoint or turn "as needed" into zero.
- Normalize to an existing enum such as `G_PER_L`, `MG_PER_L`, `MICROG_PER_L`,
  `MOLAR`, `MILLIMOLAR`, `MICROMOLAR`, `ML_PER_L`, or `MG_PER_ML`. Do not invent
  free-text units where the schema requires an enum.
- `G_PER_L` already denotes per liter. If `per_volume` is populated it must
  agree; never encode an amount per 100 mL as an unchanged `G_PER_L` value.
  Keep the original batch amount and basis in the evidence/explanation.
- Convert mass per batch only when the **final** volume is explicit:
  `g/L = mass_g / final_volume_L`. "Add to 1 L water" does not necessarily mean
  "make up to a final volume of 1 L" after other liquid additions.
- Percent needs a known basis: `PERCENT_W_V`, `PERCENT_W_W`, or `PERCENT_V_V`.
  An unexplained percent sign is ambiguous. Conversion between mass and volume
  percentages needs verified density; do not assume all liquids are water.
- Mass/molar conversion needs verified molecular weight for the exact salt,
  hydrate, and purity/form specified. Never use an anhydrous molecular weight
  for a hydrate or assign a molarity to an undefined mixture such as peptone.
- For a supported stock dilution, use
  `C_final = C_stock * V_added / V_final` with compatible units and evidence for
  all three inputs. Keep stock `composition` as stock concentrations and the
  addition dose separate. Do not replace stock composition by final-medium
  concentrations or double-count an expanded stock and its direct ingredients.
- A "100x" stock label alone does not establish how much was added to this
  medium. Nested dilutions require every dilution step and final volume; if any
  step is missing, leave the final concentration unresolved.
- `SolutionDescriptor.concentration_candidates[]` records proposals, not
  assertions. Existing `CROSS_MEDIUM_INFERENCE` or `TYPICAL_VALUE` candidates
  must not become `concentration` without evidence from this medium's source.
  Ingredient descriptors have no such candidate slot; keep their proposals in
  the review report. This skill does not generate typical-value guesses.
- A source-explicit nonnumeric dose may be documented in notes with evidence;
  omit a fixed concentration where the schema permits it. `VARIABLE` must not
  conceal a number that is merely missing or unverified.
