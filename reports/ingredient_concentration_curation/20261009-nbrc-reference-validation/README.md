# NBRC Ingredient Evidence Validation

The NBRC 1219 table-matching defect is resolved locally. All **240 reference
checks** across the thirteen Middlebrook records now pass, including the
unchanged water quote that previously failed. All thirteen
`just validate-references` commands pass. The fifteen original sources were
refreshed byte-for-byte identically, including the NBRC HTML and DSMZ PDF.
See [live.json](live.json) for actual source metadata and individual checks.

No normalized recipe, concentration, snippet, reference or curation event was
changed by this parser repair. The original [239/240 failure receipt](../20261009-middlebrook-stages/live.json)
remains intact. The source-version conflict in TOGO M1946 remains explicit;
passing a quote check does not resolve that scientific disagreement.

## Parser And Tests

Exact HTTPS host, path and accession routing selects the official-source
cache. The parser requires the requested medium number, a nonempty medium
name, the catalogue title and the identified detail/composition table. It
preserves inline chemical subscripts, quantities, displayed precision and
units, while excluding navigation, unrelated page text and script content.
Hidden, duplicate, malformed or identity-mismatched sections fail closed.
No fuzzy matching, unit conversion, generic-cache fallback or silent network
transport fallback was added.

The [focused receipt](focused.json) passes lint, formatting and **523 tests**.
Tests cover the immutable real capture, the original failure, source identity,
table structure, hidden content, formula/unit/precision mismatches, redirects,
and existing DSMZ/TOGO/JCM/KOMODO behavior. This validates literal occurrence,
not scientific entailment, stock scope, final volume or concentration arithmetic.
The [new fast tier](fast.json) passes **9,913 tests**, with 16 skipped, 1,945
deselected and two warnings in 682.89 seconds. The [final receipt](validation.json)
reconciles all terminal checks, current code/capture hashes, unchanged corpus
bytes and the remaining failures. It does not reuse the previous batch's count.

## Scope And Remaining Work

The [exact-reference inventory](corpus-nbrc-inventory.json) scans all **15,910**
normalized YAMLs: **196 records** contain **199** reference entries across
**188** exact adapter-routed NBRC URLs. Only one entry has an explicit snippet
and one has a title. These are structural counts, not evidence verification.
Only NBRC 1219 was source-verified in this batch; the other 187 URLs were not.
Other NBRC layouts may fail closed and require separately inspected fixtures.
This inventory does not determine whether these records have adequate evidence
from other sources; it counts only exact NBRC `reference` fields.

Cumulative counts remain **5,187 edited records**, **33,319 added evidence
entries**, and **11,798** exact follow-up paths, with **4,112** outside those
reports. Follow-up presence does not establish that every claim is resolved.
The unchanged corpus retains the [previous strict/ID/product and merge results](../20261009-middlebrook-stages/validation.json).
Global merge/freshness failures, scientific uncertainties and publication remain
open. This is not clean CI, complete-suite validation or all-record completion.

The next eleven linked Middlebrook records remain unchanged. Their
[source rows and representation decisions](../20261009-middlebrook-linked/decisions.md)
separate commercial/fallback formulations and stock doses, preserve hemin and
chemical-form uncertainty, and propose reciprocal family-link corrections.
They still require a guarded mutator, independent audit, preview and validation.
The separate 76 acid-name and 71 M142 queues remain open; these are not additive
to the 4,112 paths outside follow-up coverage.

No commit, push, public issue submission, PR, merge or branch deletion occurred.
The earlier outbound-payload approval remains unresolved and was not bypassed.

Runtime: existing partial locked Python 3.13 environment.
