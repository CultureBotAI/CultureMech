---
name: culturemech-add-paper-citation
description: Add a DOI- or PMID-identified paper to an existing CultureMech record, with claim-level excerpts, recipe-variant accounting, and scientific names grounded to NCBI Taxonomy or explicitly documented parent ranks. Use for paper-to-record curation, not bulk literature discovery or automatic growth assertions from organism mentions.
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a paper citation

Accept an existing CultureMech record path/ID and a DOI, PMID, or corresponding
article URL. Add the verified citation and only the formulation and organism
claims supported by inspected text. A citation request permits these local
curation edits, not GitHub actions, merging media, or publishing generated data.
For a preview/review request, return a proposal without changing recipe YAML.
For a single-record citation request, ask for any missing target record or paper
identifier before curation. Broader citation discovery needs an explicit scope.

Work inside the CultureMech checkout. Read `CLAUDE.md`, the complete target,
and the relevant classes in `src/culturemech/schema/culturemech.yaml`.
Read [field mapping](references/field-mapping.md) before preparing edits; it
also documents taxonomy and exporter limitations. Repository paths below are
relative to the checkout, not the installed skill directory.

## Resolve the record and paper

1. Resolve exactly one authoritative record in `data/normalized_yaml/`.
   Record its exact tracked path, ID, record kind, and parent/variant links.
   Resolve a merged-record request to its normalized inputs; ask if there are
   multiple defensible owners. Do not edit generated merges, raw captures, or
   pages. Stock solutions must not silently become growth media.
2. Inspect existing references, evidence, variants, and organism assertions.
   Search DOI/PMID aliases, source IDs, names, and candidate formulations,
   including hidden and ignored files (`rg --no-ignore --hidden`). Parse YAML
   for comparisons; a filename or ingredient-set fingerprint is not proof of
   exact formulation identity.
3. Normalize a PMID to `PMID:<digits>` and a DOI to `doi:<resolved-doi>`.
   Verify identity against PubMed and/or the publisher: title, authors, year,
   DOI, and PMID where available must identify the same paper. Do not confuse
   a PMCID with a PMID, or strip meaningful DOI punctuation. Check corrections
   or retraction notices that affect the proposed claim.
   If the paper, correction, and bibliographic authorities disagree, retain
   their provenance and the unresolved discrepancy in citation notes. Verify
   publication identity separately from disputed metadata; do not silently
   reorder authors or describe a disputed value as corrected.
4. Retrieve the relevant methods, tables, supplements, or explicit abstract
   statement. Record the inspected version, stable URL, access date, and text
   locator. Search snippets, generated reports, and metadata alone are not
   scientific evidence. With metadata-only access, a relevant bibliography
   entry may be added with that limitation; formulation/growth claims remain
   unresolved. Do not attach an unrelated paper just because its title matches
   a medium name.

Keep one bibliography entry per publication, reusing its existing valid
identifier. Deduplicate DOI/PMID aliases only after verifying their equivalence;
retain the alternate identifier in `references[].notes`. Do not rewrite unrelated
citations. The [PMC ID converter](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/)
only supplies related identifiers for articles in PMC; a miss is not evidence
that a DOI has no PMID.

When source archiving is requested, follow the [archive mapping](references/field-mapping.md#source-archives).
Preserve the retrieved source and an attributable Markdown conversion; distinguish
an abstract, full text, selected excerpts, and metadata-only access. Archiving is
not scientific approval or permission to publish the source files.

## Compare the study formulation

Compare ingredients and chemical forms, amounts/units, stock additions and final
volume, omissions/substitutions, supplements, pH, physical state, preparation,
and cultivation conditions. Record each supported difference and any field that
the paper leaves unspecified. "Medium X" alone does not establish that every
detail equals the current local recipe.

Compare each distinct assay separately. General cultivation, inoculum preparation,
growth tests, and analytical assays can use different formulations within one
paper; do not combine their amounts or transfer an outcome between them. When
the paper cites a base recipe, inspect that source before inheriting its details,
then apply only the overrides explicitly stated for the relevant assay. Record
conflicts between methods, figures, and supplements instead of silently choosing
one formulation.

| Finding | Action |
| --- | --- |
| Same supported formulation | Add citation/evidence to the existing recipe; no new variant. |
| Existing matching inline or linked variant | Reuse it; add study evidence without widening its scope. |
| Recognizable base with study-specific differences | Add an inline `variants[]` entry with evidence and explicit modifications; preserve the base. |
| Distinct, fully specified reusable formulation needing its own record | Propose a linked child; create it only when new-record curation is requested. Use the repository `create-recipe` and `manage-identifiers` skills. |
| "Modified" recipe with unspecified changes | Preserve the observation in `references[].notes` as formulation-unresolved. Do not create or assign a resolved variant or positive growth entry until its identity/differences are supported. |
| Ambiguous medium identity or incompatible formulation | Keep the candidate unresolved; do not force a parent link or attach a growth assertion to this recipe. |

For inline variants use `name`, `relationship` when supported, `description`,
`modifications`, `purpose` when stated, and `evidence`. Compare against existing
variants before naming one; do not create a duplicate per paper. A supported
study-specific difference need not establish every detail of the formulation:
retain unspecified fields explicitly. If an ingredient identity or conflicting
formulation prevents assigning the study to a particular variant, keep the
observations in citation notes until resolved; do not label that variant exact.
A changed incubation condition alone is not necessarily a different recipe: retain the
study condition in evidence or an appropriate growth-metric field, and label a
condition-specific variant explicitly if one is needed to preserve claim scope.
Do not infer an optimum or a universal cultivation requirement.

For a linked child use `parent_media`, `variant_relationship`, and
`variant_modifications`, with the parent's reciprocal `variant_children` link.
When reusing an existing linked child, inspect that complete record and put its
study citation and variant-specific growth evidence on the child. Do not leave
the child's evidence dependent on a bibliography entry found only on the parent.
Update the parent only for claims or links that actually belong there.
Never hand-pick an ID. A citation-only request does not authorize a new parent,
record merge, or corpus-wide variant reassignment.

If adding or correcting concentrations, also follow the repository skill
`.claude/skills/review-ingredient-concentrations/SKILL.md`. Each amount needs
DOI/PURL evidence plus an exact snippet; a verified stable article/supplement
URL can accompany a PMID-only citation. Keep stock and final concentrations
distinct, and arithmetic outside quotations. A study variant's amount must not
overwrite the canonical recipe.

## Capture organisms without inventing growth

Inventory each organism mentioned in the inspected, medium-relevant passages,
including background mentions, negative results, and co-cultures. Preserve the
reported spelling and strain/isolate designation, expand abbreviated scientific
names only when unambiguous, and distinguish each organism's experimental role.
Do not claim an exhaustive whole-paper inventory if full text was inaccessible.

For each named organism, check NCBI Taxonomy using the reported name, documented
synonyms, strain information, and lineage. Capture the scientific name, current
`NCBITaxon:<digits>` identifier, canonical label, rank, lookup URL/date, and
mapping decision. The [NCBI taxonomy guide](https://www.ncbi.nlm.nih.gov/guide/taxonomy/)
links the taxonomy browser and lineage resources. Do not guess an ID or choose
the first fuzzy hit. Check taxon merges/deletions and synonym ambiguity.

- Exact taxon or unambiguous synonym: use the verified ID and canonical label;
  retain the paper's name and strain separately. Species-level identification
  is not proof of an exact strain match.
- Only a parent rank is verified: use the most specific defensible verified
  parent and include its scientific name, ID, and actual rank, explicitly
  labeled `parent_rank_only`, with the reason the reported organism could not
  be matched. Do not relabel the species with its
  genus ID or assert growth of every member of the parent taxon. Follow the
  fallback storage rule in the field mapping.
- No defensible exact or parent match: retain the reported name, mark the
  lookup unresolved, and leave the ontology term absent. Never invent a
  binomial from a genus-only label or mixed-community description.

Add `target_organisms[]` only for an explicit cultivation/growth relationship
to the resolved recipe or variant. Merely mentioning, sequencing, isolating
from a habitat, or discussing an organism is insufficient. Put mention-only,
negative-growth, and unresolved-medium observations with their names, taxonomy
assessment, snippet, and locator in the paper's `references[].notes` instead
of a positive target-organism entry. A consortium's growth does not establish
that each member grows alone.

For variant-only growth, set `scoped_to_variant` to the exact inline variant
name, or attach the organism to the matching full child record. Never upgrade
that evidence into parent-medium growth. Preserve strain and condition scope;
do not combine different strains, variants, or negative/positive results merely
because they share a taxon ID. If existing identifier constraints prevent
separate assertions, report the schema gap instead of overwriting one.

## Attach evidence and apply

Use `references[]` for verified title, authors (string), year (integer), and
provenance notes: source type, discovery mode, alternate identifiers, access
date, and inspected location. Use `EvidenceItem` at the narrowest supported
claim: recipe formulation, variant modification, organism growth, growth metric,
or ingredient concentration. Each new scientific assertion needs a verified
reference, nonempty exact `snippet`, support classification, and `explanation`
that connects that text to this organism/formulation/condition. Short quotations
must remain verbatim; put interpretation, separately located excerpts, and
conversion arithmetic in the explanation.

Preview the record/field, citation, old/new claim, recipe differences, organism
mapping, scope, and unresolved limitations. For authorized edits, assert the
expected ID and old values and build the candidate in memory. Deduplicate
citations, evidence excerpts, and labeled note observations using publication,
organism/strain, formulation scope, and locator; do not collapse distinct assays.
Compare substantive content before appending history. If unchanged, do not
write or create an event, including an access-date-only refresh.

For an actual change, append an event with
`culturemech.curate.curation_event.record_curation_event`, attributed to the
actual agent, not the user. Its `skip_if_recent` flag compares only curator and
action, not content; it is not a substitute for change detection. Validate the
complete candidate, including history, with
`culturemech.validation.write_validated.validate_recipe`. It returns an error
list rather than raising on invalid data: require an empty list before writing.
On any errors, report them and leave that owner unchanged. Write valid candidates
through the repository round-trip YAML helpers. Preserve existing history and evidence.
No-op reruns must not duplicate references, snippets, organisms, variants, notes,
or events. Apply the same change detection, history, and validation rules
separately to every affected owner, including an existing linked child.

## Verify and report

For a preview, report proposed checks separately from checks actually run; do
not describe an uncreated candidate as validated. For an explicitly read-only
request, inspect command side effects before execution: `validate-strict` writes
a report, and reference/term checks may update caches. Run only checks verified
to respect the requested boundary, or use a permitted isolated scratch location.
Otherwise list those checks as not run; a preview does not require curation,
history events, report files, or generated outputs.

For authorized curation, run baseline and post-edit checks on each affected
normalized record:

```bash
just validate-schema <record-path>
just validate-strict <record-path>
just validate-references <record-path>
just validate-terms <record-path>
git diff --check
```

Run `just validate-media-variant-links` when full parent/child links change.
For normalized inputs, follow `CLAUDE.md` merge checks; do not claim generated
merges/pages were refreshed unless actually regenerated and verified.
Reference and term checks may require network/caches. Re-read each quote and
mapping manually; schema validity or a citation resolving is not scientific
verification. Report unavailable checks and pre-existing failures separately.

Return the exact record path, publication identifiers, bibliography additions,
evidence added, formulation differences and variant destination, and each
organism's scientific name, taxon ID/rank, match status, and growth-versus-mention
disposition. Separate citation counts from supported taxa-medium association
counts. State access gaps, unresolved matches, export limitations, and checks
run. Do not describe this focused citation task as a full record review.
