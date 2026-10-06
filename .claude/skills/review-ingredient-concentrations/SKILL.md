---
name: review-ingredient-concentrations
description: Review, add, or correct CultureMech ingredient concentrations using verified DOI or persistent-URL evidence and exact supporting text snippets. Use for missing amounts, concentration evidence gaps, units, final-volume arithmetic, and stock dilutions in medium or stock-solution records; not for guessing typical values or silently replacing a medium with a variant.
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review and add ingredient concentrations

Every added or corrected concentration must have a verified DOI or persistent
source URL **and an exact supporting text snippet**. A bibliography entry alone
is insufficient. Existing amounts without this evidence remain unverified, even
when they look plausible or pass schema validation.

## Scope and authority

- A review or audit is read-only. An add, correct, or apply request permits
  narrowly scoped local edits to the requested records. Batch work starts with
  a preview and requires explicit apply intent.
- Curate authoritative records under `data/normalized_yaml/`. Resolve merged
  records back to their source inputs; never hand-edit generated merges or
  pages. Preserve unrelated changes and permanent IDs.
- Cover direct ingredients, standalone stock `composition`, inline and nested
  stock compositions, and source-supported stock addition amounts. Inspect
  variants separately; evidence for one formulation is not evidence for another.
- This skill does not authorize new records, merging media, GitHub mutations,
  paid research, or contacting authors. Route genuine variants or new records to
  [create-recipe](../create-recipe/SKILL.md).

Read `CLAUDE.md`, the whole target record, and the relevant classes in
`src/culturemech/schema/culturemech.yaml`. Follow
[curate-yaml-record](../curate-yaml-record/SKILL.md) for general curation and
[the evidence contract](references/evidence-contract.md) for field mapping,
provenance, units, and dilution rules.

## 1. Establish the review inventory

Record the git commit, exact tracked path, stable record ID, record kind, source
accession/version, and parent/variant relationships. Use `git ls-files` for the
tracked inventory; filesystem case-insensitive matches do not prove exact path
identity. Inspect local source captures and prior reports as leads, including
ignored/hidden files (`rg --no-ignore --hidden`) before declaring evidence absent.

Read every ingredient and stock node in scope, including nested `solutions`.
Record the ingredient label/chemical form, ontology ID if present, and full field
path, for example `solutions[0].composition[2].concentration`. Check names/IDs
again before applying an index-based proposal so list reordering cannot change
the wrong ingredient. Detect cyclic stock references; never recurse indefinitely.

Capture the existing `value`, `unit`, `per_volume`, evidence, source amount, and
volume basis. Distinguish missing from zero, a numeric range from "as needed",
amount per batch from amount per final volume, and stock composition from stock
addition volume and final-medium concentration. A present but unsupported value
is still an evidence gap.

Run baseline checks and record pre-existing failures:

```bash
just validate-schema <record-path>
just validate-strict <record-path>
```

## 2. Inspect the exact source

Start with the original recipe/specification and source accession. Prefer the
original article's methods/supplement, an official culture-collection recipe, or
a versioned protocol/dataset. Searches and generated research reports locate
documents; they are not concentration evidence themselves.

Confirm the source describes this exact formulation, chemical form, preparation
stage, physical state, and version. A similarly named medium or shared ingredient
set is insufficient. Concentration-independent fingerprints do not prove identity.

For each source:

1. Resolve the DOI or persistent URL and inspect the actual content. Cached
   copies must be traceable to that identifier and source version.
2. Verify amount, unit, and final-volume/batch basis, including table headings,
   footnotes, and supplements. Inspect PDF page images when OCR, symbols,
   decimals, or column alignment are ambiguous.
3. Capture a short verbatim snippet and its page/table/section or stable locator.
   Inspect any separately quoted heading or volume statement too.
4. Capture title, authors, year, source type, discovery mode, and access date
   where available. Never manufacture missing bibliographic fields.

A search-result excerpt, ontology page, or another CultureMech record is not
primary evidence for a recipe amount. Unreadable sources remain unresolved;
do not claim they were verified.

## 3. Decide without guessing

Use these statuses in the report, not as new YAML fields:

| Status | Decision |
| --- | --- |
| `verified` | Existing value, unit, basis, and attached evidence match the source. |
| `add` | Missing concentration has complete source evidence. |
| `correct` | The exact recipe source supports correcting a transcription/unit error. |
| `evidence_only` | The value is supported, but its DOI/PURL, snippet, or claim linkage needs adding. |
| `not_quantified` | The source explicitly gives no fixed amount, such as titration to pH. |
| `unsupported` | Missing, inaccessible, ambiguous, or insufficient evidence; do not apply a number. |
| `conflict` | Sources disagree or describe different variants; preserve the disagreement. |
| `schema_gap` | Claim/evidence cannot be represented faithfully; do not invent slots. |

Never infer a missing value from common practice, a neighboring recipe, organism
requirements, or a stock name. Do not treat missing as zero, silently assume a
one-liter final volume, or invent an approximate amount. Keep existing unsupported
values unchanged in an audit; propose removal/correction explicitly.

Show all conversion inputs and arithmetic in the report and evidence
`explanation`, separate from literal quotations. Derived values are acceptable
only when every necessary input is verified for this formulation and conversion
is unambiguous. Unknown density, hydrate form, stock strength, or final volume
blocks conversion. Follow the evidence contract's unit/stock rules.

A different concentration in a real variant is not automatically an error in
the base recipe. Do not average conflicting sources or overwrite the base with
a study-specific formulation. Route variant decisions to the recipe workflow.

## 4. Preview and apply supported changes

Show each target path, ingredient identity, old/new value and unit, source
reference, exact snippet, locator, and calculation before writing. Apply only
`add`, `correct`, and `evidence_only` decisions with complete evidence.

Use existing `ConcentrationValue`, `EvidenceItem`, and `PublicationReference`
fields as mapped in the evidence contract. Add evidence for each changed claim
in the YAML itself, not only in a report. Preserve prior evidence and unrelated
role/growth claims. Deduplicate references within each evidence list without
losing their claims or supporting excerpts.

Use a scoped guarded mutator that asserts the record ID, ingredient identity,
and old values. Append an event with
`culturemech.curate.curation_event.record_curation_event` containing exact changes,
sources, and conversion notes. Use the agent's identity, not the user's identity.
No-op reruns must not add duplicate evidence or curation events.

Validate with `culturemech.validation.write_validated.validate_recipe` before
writing, selecting the correct `MediaRecipe` or `SolutionRecipe` target class.
Use round-trip helpers/ruamel.yaml to preserve presentation; the existing
`write_validated_recipe` helper is also available when its serialization preserves
the target's formatting. Inspect the diff and repair unrelated reflow. Do not
bypass validation to write an unsupported evidence field.

## 5. Verify and deliver per-record results

After edits, run:

```bash
just validate-schema <record-path>
just validate-strict <record-path>
just validate-references <record-path>
git diff --check
```

For changed merge inputs, run `just verify-merges` and
`just audit-merge-freshness`. Regenerate derived artifacts through the maintained
pipeline when required; never hand-patch them. Report unavailable validators and
existing failures separately from regressions.

Automated reference validation may not fetch a PURL, table, or supplement.
Manually verify the actual snippet and identify that check as manual; never claim
an unsupported automated pass. Re-read every changed claim, checking identifier,
quote, source/formulation scope, units, basis, and calculations. Schema validity
alone is not scientific verification.

Produce one result per exact record path, including unchanged records. Each
per-record result must contain exactly one `- Record: <exact tracked path>` line,
the ID and reviewed commit, and a row for every concentration claim in scope.
Include field path/ingredient, old and proposed amount/unit/basis, status,
DOI/PURL, snippet, locator, calculation, action taken, and validation. Unknown
report cells stay explicitly unknown, not filled with estimates.

For batches, report unique reviewed paths, changed/unchanged/blocked/failed
records, remaining scope, and unresolved issues. An interrupted or partially
failed run is not complete. Save reports at the requested location or an
established repository report destination; do not stage ignored research
captures/caches as curation output.
