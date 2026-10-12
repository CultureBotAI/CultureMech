# Medium-436 Review Handoff

Read-only preparation, not applied curation or a completed cohort review. The
full 15,910-record objective remains unchanged. Thirteen exact tracked records
are frozen in `next-436-context-approved.json`; the source inspection inventories
184 API/HTML rows and 149 existing quantity fields. No medium-436 YAML changed.
The original DSMZ PDF page was visually inspected; its hash and rendered image
are recorded in `next-436-inspection.json`.

`next-436-preparation.json` pins all 26 passing baseline commands and identifies
eleven existing canonical reports. M694 and M2636 still need new canonical
reports after complete review. `next-436-old-slot-mapping.json` accounts for
113 source-mapped quantity fields and 36 comparison, copied-LB or placeholder
fields. Zero unmatched fields is not a completion claim: K3037 has no current
quantity fields because its imported ingredient list is empty.

`next-436-row-decisions.json` distinguishes all 184 API/HTML rows and 21
original-PDF rows by preparation scope. It preserves the exact extracted PDF
lines alongside whitespace-normalized excerpts and records thirteen existing
supported evidence entries that must survive unchanged. The variant's two
explicit supplement rates are supported by its own title and ingredient rows;
they do not establish a denominator for the other batch inputs. Field lineage,
metadata decisions, the guarded proposal and independent audit remain pending.

## Access And Scope

Fourteen official sources were captured successfully. The restricted-network
attempt is retained in `next-436-context-initial.json`. The approved public GET
attempt returned HTTP 403 for KOMODO 3037; that record is not source-verified.
Searches including ignored files located its earlier catalog mapping and review
plan, but a catalog mapping is not ingredient-amount evidence. Do not borrow
another stock's concentrations merely because the names match.

J675 is an unchanged comparison record. `next-436-J675-comparison.json` verifies
its exact applied bytes against the earlier independent auditor, with both
official sources freshly retrieved and byte-identical. All 42 reference checks
pass. Its historical 40 evidence entries are not new additions in this batch.

## Source-Specific Findings

- DSMZ436 separates basal ingredients, two mineral stocks and a fatty-acid
  stock. Water and stock doses are batch inputs, not a verified final-volume
  denominator. The six mineral percentages omit their basis. Preserve that
  ambiguity instead of silently choosing w/v. See the [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium436.pdf)
  and the exact page text in the frozen capture.
- The DSMZ original visibly prints calcium chloride with seven waters; JCM675
  specifies the dihydrate. TOGO M2636 repeats the seven-water name but its GMO
  label says hexahydrate. These are source/form discrepancies, not permission
  for molecular-weight conversions or invented ontology matches.
- KOMODO436 has nineteen table rows with its own displayed precision and
  nulls. Its strain variant has the same rows plus `maltose` and `starch`, each
  displayed as 1.00 g/L. Existing YAML omits both, and its exact-duplicate link
  is unsupported. The variant's pH metadata is null; copied pH must not be
  treated as source-verified. Exact row excerpts and metadata are in
  `next-436-inspection.json`, including the variant comparison.
- KOMODO3017 explicitly lists four fatty-acid-stock components with null
  amounts. Restore source identity only after a guarded proposal; do not turn
  the SEED aggregate's molar numbers into ingredient amounts. KOMODO3037 remains
  access-blocked separately.
- TOGO M694 identifies JCM675 as its original, while M2636 links DSMZ436 and
  explicitly names maltose and starch supplementation. Do not overwrite both
  with the same base formulation. In the inspected current YAML, each has
  1190 g/L water formed by summing different preparation stages, 500 g/L
  cysteine from a 500 mg input, and stock doses represented as mass rates.
  These need separate stage-aware, snippet-backed proposals.
- The M2636 link to MediaDive solution 4674 is not an identity match. That
  official solution uses dibasic phosphate and different sulfate/calcium
  quantities; M2636's own mineral-stock rows differ. Correct the receiving
  record's link or composition, not the independently supported S4674 values.
- S882 retains seven qualified provider-rate evidence entries; S4674 retains
  six. Preserve all thirteen exactly. S882 still lacks its three source-listed
  stock inputs and has an unsupported water percentage. S885 stores each acid
  as 100% and water as 700%; its source lists three 10 ml inputs and 70 ml water.
  This is a volume-input correction, not a density-based conversion.
- Supplier-tagged LB additions and their root notes are absent from the exact
  captured recipes. Guard removal by source and original-node identity; keep
  legitimate source tryptone, yeast extract and salt distinct from the copied
  commercial expansion. Never rewrite earlier curation events.

## Before Applying

Complete all per-field decisions and source links, freeze a guarded proposal,
and independently audit source scope, nulls, variants, prior evidence and
history. Retain one canonical report per exact record path, including unchanged
or blocked records. Run preview schema/reference/preservation checks and show
the complete old/new evidence-linked ledger before applying any new recipe.
The successful captures and baseline checks do not establish that this work
has already been completed.
