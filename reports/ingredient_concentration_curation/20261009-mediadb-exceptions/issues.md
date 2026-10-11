# MediaDB Review Issues

These are local issue records, not GitHub issues. No remote write was attempted.

## Resolved In This Batch

1. **Copied LB composition replaced real fatty acids.** Records 430/460 lacked
   the source's 10 mM 3-methylbutanoic acid; records 473/474 lacked the source's
   0.04896 mM 2-methylbutanoic and 3-methylbutanoic acids. All four contained
   Tryptone 10 g/L, Yeast extract 5 g/L and extra NaCl 10 g/L from an unrelated
   LB product expansion. Complete live tables and the dated SQL export support
   the correction. Six missing constituents are restored; twelve copied nodes
   and four commercial-product notes are removed with root evidence and history.
2. **Unknown amounts misrepresented as VARIABLE.** Six entries in record 288 and
   thirteen in 289 are NULL in the export and None in live tables. Their history
   identifies schema defaults, not observed variable doses. The concentration
   fields are withdrawn while ingredients, ontology mappings and earlier history
   remain. Exact source excerpts and unknown-amount notes are attached.
3. **Preview-plan integration defects caught before writes.** The first two
   preview attempts omitted the shared helper's version/claim fields. Both
   terminated before producing an application plan or changing recipes. The
   final plan has version 1 and a complete, revalidated claim inventory.

## Open: MediaDB Reference Adapter

The network-enabled production validator returns substring errors for all 156
recipe excerpts. Its generic URL cache contains raw HTML tags between ingredient
and amount cells; the published visible rows and the independently parsed live
captures contain the exact quoted text. It also cannot verify the descriptive
title attached to the gzip SQL export. See `references-live.json` and its six logs.

Required resolution: add narrowly scoped official MediaDB parsing with exact
accession/heading/compound-table verification, preserving case, decimals, units,
NULL/None and table boundaries. Reject wrong accession, missing/duplicate/hidden
tables, malformed rows and source errors. Verify versioned-export metadata with
its own format or retain an explicit unsupported result; do not whitelist quotes,
weaken literal matching globally, or overwrite failed receipts with manual passes.
The present 156 captured-source checks are separate evidence, not a substitute
claim that the production validator passed.

## Open: Future Imports Collapse NULL And Zero

`src/culturemech/fetch/mediadb_fetcher.py` currently converts NULL/empty amounts
to `0.0` in `_parse_media_compounds_insert`. The importer then tests concentration
truthiness, conflating explicit zero with unavailable. The reviewed SQL export
contains nineteen NULL amounts and no explicit zero rows. Current Song YAML had
VARIABLE defaults, not nineteen asserted zeros; that distinction matters.

Required resolution: preserve None through fetching/conversion/import, retain
explicit zero when the actual source reports it, reject malformed numeric data
explicitly, and add end-to-end tests. Do not regenerate or overwrite already
curated authoritative YAML as an importer fix.

The [temporary-fixture reproduction](importer-gap-reproduction.json) now proves
these two behaviors and an additional name-mapping defect. With correctly parsed
source rows, `_map_ingredients` still reads `chebi_id` as a common name: it emits
`preferred_term: '16643'` for L-methionine and `'26710'` for sodium chloride.
The stale-export guard accepts these correctly parsed inputs, so it does not
prevent this downstream regression. Fix the importer to use the actual `name`
field, and test the complete fetch-to-import boundary. The reproduction uses
two real source rows and one explicitly labeled synthetic zero boundary case;
it writes no normalized recipe data.

## Open: Primary-Article Amounts And Identity

The source tables justify database-scope curation, not independent article
verification. In particular, the nineteen Song amounts remain unresolved.
The publisher currently exposes subscription-preview metadata, not methods
quantities; the [KAIST record](https://pure.kaist.ac.kr/en/publications/development-of-chemically-defined-medium-for-mannheimia-succinici/)
also provides an abstract and DOI link, not a concentration table. The article is
[Song et al., 2008](https://link.springer.com/article/10.1007/s00253-008-1425-2).
No paywall bypass, purchase or author contact was attempted.

Each report lists current/source ChEBI differences as review flags. A generic
label with a hydrate-specific local term needs chemical-form verification; no
mass conversion is justified from that uncertainty. New fatty-acid labels remain
ungrounded until exact ontology correspondence is reviewed. Imported generic
filtration/pH steps, existing COMPLEX/UNDEFINED classifications and non-ingredient
claims are not certified by these tables.

## Open: Corpus And Publication

Only six of the 469 pending MediaDB comparison records are handled here.
The remaining 463 and the full 15,910-record objective remain in scope.
Global merge/freshness failures, earlier failed full-suite receipts and the
uncompleted GitHub workflow must remain visible; local corrections do not imply
publication readiness.

## Open: AMS1 Database Versus Primary-Article Formulation

Direct inspection of [Carini et al., Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3578571/)
(DOI `10.1038/ismej.2012.122`, online 2012, issue 2013) confirms magnesium sulfate
heptahydrate at 2.8 mM. All ten pending AMS1 database records instead contain
generic magnesium sulfate at 28 mM. The article also specifies calcium chloride
dihydrate, whereas these database records explicitly say anhydrous. This is not
resolved by the live/export comparison: both database representations agree.

Only records 475 and 477 link directly to that article in the export. Records
476/478 link to the 2014 thiamin-precursor study (PMID 24781899), while 479-484 link
to the distinct 2014 phosphorus study (PMID 25000228). Do not overwrite all ten
from the base table, conflate the study-specific supplements, or merge their
different phosphorus/vitamin formulations. The exact variant, chemical forms,
vitamin completeness and database maximum-dose annotations require disposition
before numeric corrections. No new quantities have been applied from this lead.

The primary article was retrieved directly as full HTML, not inferred from a
search excerpt. The local capture is outside the repository; the follow-up
assessment preserves its hash, bibliographic provenance and short table quotes.
