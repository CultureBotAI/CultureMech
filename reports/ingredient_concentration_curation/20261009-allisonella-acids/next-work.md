# Remaining Ingredient Work

The full objective remains 15,910 normalized records, each changed scientific
claim backed by an exact snippet and DOI or persistent source URL. The two
Allisonella edits are a completed local application, not all-record completion.
See the [batch validation receipt](validation.json) for terminal gate results.

## Preserved Scope

- 74 unchanged acid-name candidates remain in `next-lb-identity-context.json`.
- The independent `remaining-queue.json` retains 71 M142-dependent records;
  these queues are not additive coverage totals.
- The refreshed ID-resolved family inventory has 40 candidate components,
  one additional family neighbor, and 21 stale exact-path references. ID
  fallback is not evidence that supplied paths are current or relationships
  scientifically valid. Carry forward the existing stale-path issue.
- The additional neighbor is
  `data/normalized_yaml/archaea/methanobacterium_medium_vi.yaml`,
  `CultureMech:002222`, source `mediadive.medium:J1038`. Include it when reviewing
  its J872/J1038 family even though it was not an acid-name candidate.
- 4,112 exact normalized paths remain outside these follow-up reports.
  Follow-up presence for the other 11,798 paths does not establish that every
  concentration is verified or every review comment resolved.

## Next Medium-119 Family

`next-119-family-context.json` captures 19 unchanged records across the connected
KOMODO 119 family and DSMZ 119/119a/119b/119c. All 23 requested public sources,
including four original PDFs, were retrieved successfully. This is preparation,
not an applied batch or a count of completed reviews.

The [read-only preflight](next-119-family-preflight.json) extracts 645 source
rows, inventories the existing ingredient nodes and finds 17 stale exact-path
references with no external family neighbors after ID resolution. Its initial
PDF-visual status is superseded by the later
[nine-page visual inspection](next-119-pdf-visual-review.json). These preparations
do not yet adjudicate all 645 rows or certify the copied chemical annotations.
The [partial implementation findings](next-119-decisions.md) document six full
record reads, confirmed stage/identity errors, conversion boundaries and required
regressions. The remaining thirteen full record reads and complete adjudication
are still pending.

Important source distinctions already visible in the captures:

1. The current DSMZ 119 PDF explicitly states final volume 1,003 ml. Do not
   blanket-withhold a denominator that this exact source actually supplies.
   This statement does not establish final volumes for 119a, 119b or 119c.
2. SL-10 explicitly makes up to 1,000 ml. Preserve its stock basis, receiving
   dose and preparation separately. Other stock water inputs and titration
   additions do not automatically establish measured final volume.
3. Sludge fluid and clarified rumen fluid are prepared materials, not guessed
   mass concentrations. The rumen-fluid API entry has preparation but no
   `recipe` rows; do not crash, synthesize composition or silently omit it.
4. KOMODO variants are not interchangeable with the current DSMZ strain notes.
   For example, KOMODO 119_6216 reports Na-acetate 3.99 g/L while the original
   says to increase it to 3.00 g/L. KOMODO 119_11977 retains reducing agents
   that the current original's corresponding strain instructions omit.
5. KOMODO 119.1 combines two strain names whose current DSMZ instructions
   differ. Preserve source/version conflicts; do not manufacture a single
   interchangeable variant or infer organism growth from its title.
6. Recheck every existing parent/child source identity and exact path. Some
   links currently connect KOMODO 119 to DSMZ 119b and stale bacterial paths.
   Determine relationships from source evidence, not the copied fingerprints.

Read all 19 records fully, inspect all source rows against the reviewed PDFs, map all old
quantity slots, then build a guarded evidence-backed preview and independent
audit. Preserve prior history. Include reciprocal neighbors and regression tests
before applying; do not count captures alone as completed record reviews.

Global merge verification/freshness and publication remain separate unfinished
work. Do not hand-edit generated merged YAML or publish around the unresolved
outbound approval. No commit, push, PR, public issue, merge or branch cleanup
was attempted in this batch.
