# CultureMech Media Recipe Validation Template

This is a **recipe-validation** deep-research prompt (distinct from the
organism-discovery flow in `media_growth_research.md`). It does not look
for new organisms. It audits the *formulation* of one CultureMech medium
record and **each of its modeled variants** against authoritative sources,
and returns curator-ready corrections.

## Target Medium

- **Record path:** {record_path}
- **CultureMech ID:** {media_id}
- **Name:** {media_name}
- **Original/source name:** {original_name}
- **Category:** {category}
- **Medium type (deprecated):** {medium_type}
- **Composition type:** {composition_type}
- **Nutritional class:** {nutritional_class}
- **Functional role:** {functional_role}
- **Physical state:** {physical_state}
- **Media term (authoritative source ref):** {media_term}
- **Synonyms:** {synonyms}
- **Ingredients (preferred_term (ontology id): value unit):** {ingredients}
- **Solutions / stocks:** {solutions}
- **Conditions (pH, temperature, salinity, atmosphere, light, ...):** {conditions}
- **Inline variants (variants[]):** {variants}
- **Cross-record variant set (parent_media / variant_children / this record's variant role):** {variant_records}
- **Existing evidence:** {evidence}
- **Notes/provenance:** {notes}

## Research Objective

Independently validate the recipe above against primary and authoritative
secondary sources. Validate the medium as a **family**: the base/parent
formulation **and each variant set** listed in *Inline variants* and
*Cross-record variant set*. A variant is NOT validated by validating the
parent — each variant has its own claimed source, modifications, and
relationship type that must be confirmed on its own.

If the *Cross-record variant set* names a parent or child record by path
(e.g. `data/normalized_yaml/.../foo.yaml`), treat that linked record as a
separate validation unit and validate the relationship in both directions.

## What to Validate

### A. Source provenance (do first)
- Locate the authoritative source named in **Media term** (MediaDive/DSMZ,
  JCM/RIKEN GRMD, ATCC, UTEX/CCAP/SAG, or the cited DOI/PMID) and quote its
  recipe.
- Confirm this record actually corresponds to that source medium (right
  name, right medium number). Flag mismatches, dead, or ambiguous refs.

### B. Base recipe
- **Ingredient identity** — does each listed component exist in the
  authoritative recipe? Flag missing, extra, or misnamed ingredients.
  Sanity-check that each ontology grounding (CHEBI/FOODON/UBERON/ENVO/
  mediadive.compound) actually denotes the named substance and that the
  printed `label` matches the ID's canonical label.
- **Amounts & units** — compare each `value` + `unit` + `per_volume`
  against the source. Normalize units before comparing (g/L vs mg/L vs
  % w/v vs molar, using molar mass). Report any value differing beyond
  rounding, and any hydrate/anhydrous mismatch that changes the effective
  amount of the active species.
- **Conditions** — verify pH (value/range), physical state (broth/agar/
  semisolid/biphasic), sterilization method/temperature, final-volume
  basis, and gas/atmosphere/temperature against the source.
- **Solutions** — for each stock, verify composition and the dilution/
  volume into the final medium.

### C. Variant-set validation — do this SEPARATELY for EACH variant
Treat every *Inline variants* entry and every parent/child link in
*Cross-record variant set* as its own validation unit:

- **Relationship-type correctness** — independently determine the true
  relationship between the variant and its base, then check it against the
  asserted `relationship` / `variant_relationship` value. Permissible
  `MediaVariantRelationshipEnum` values: `CONCENTRATION_VARIANT`,
  `PHYSICAL_STATE_VARIANT`, `SUPPLEMENTED_VARIANT`,
  `OMITTED_COMPONENT_VARIANT`, `SUBSTITUTED_COMPONENT_VARIANT`,
  `PH_VARIANT`, `SALINITY_VARIANT`, `STRAIN_SPECIFIC_VARIANT`,
  `SOURCE_DUPLICATE`, `DERIVED_FROM`, `UNCERTAIN`. Flag wrong types, and
  over-generic `DERIVED_FROM`/`UNCERTAIN` where a specific type is provable.
- **Modification accuracy** — verify every claim in `modifications` /
  `variant_modifications` against a source. The variant should differ from
  its base ONLY in the stated ways. Catch *undeclared* differences (variant
  changes something not mentioned) and *false* differences (a stated
  modification the source does not support).
- **Variant evidence** — check each variant `evidence` reference (PMID/DOI):
  does the publication exist, and does it actually support that this
  variant/condition is real (right organism, right condition, right
  formulation)? Flag snippets that do not match or do not support the claim.
- **Cross-variant consistency** — across the whole set, flag: duplicate
  variants that are really the same formulation; a `SOURCE_DUPLICATE` that
  is actually a genuine formulation difference (or vice-versa); broken
  bidirectional links (a `parent_media` whose target does not list this
  record in `variant_children`, or vice-versa); and contradictory amounts
  between a variant and its declared base.

## Rules

- Prefer primary literature and the named source database; use secondary
  sources only to corroborate. Cite every claim with a resolvable
  URL/DOI/PMID and a verbatim quoted line — uncited assertions are not
  acceptable.
- Distinguish "the source disagrees" (a discrepancy) from "no source
  found" (unverifiable). Never invent a recipe to fill a gap.
- Normalize units and account for hydrate water before declaring an amount
  wrong.
- Do not propose changing a CultureMech `id`. Do propose changes to labels,
  amounts, units, relationship enums, modifications, and evidence.

## Output Format

Return a curation-focused Markdown report with these sections, in order:

### 1. Verdict table
One row per validation unit (`BASE`, then each variant by name / child
record path), each with: status `CONFIRMED | DISCREPANCY | UNVERIFIABLE`,
relationship as-asserted vs as-found, and a one-line summary.

### 2. Findings
Grouped by validation unit. Each finding:
- `field` — e.g. `ingredients[3].concentration.value`,
  `variants[1].relationship`, `parent_media.relationship`
- `asserted` (what the record says) vs `found` (what the source says)
- `source` — URL/DOI/PMID + verbatim quoted line
- `severity` — **P1** factual error in identity/amount/relationship,
  **P2** ontology-grounding/label or evidence mismatch, **P3**
  completeness / under-specification
- `proposed fix` — concrete value

### 3. Proposed YAML changes
One ```yaml``` block per change, ready to paste into `{record_path}` (or
the linked variant record's path), as a minimal edited fragment.

### 4. Identifier resolution status
Which ontology IDs / source medium numbers were verified against a source
vs. asserted only. Note conflicts.

### 5. Unresolved gaps & warnings
Anything no accessible source could settle (with what evidence would
resolve it), paywalled sources, and claims that should NOT be curated.
