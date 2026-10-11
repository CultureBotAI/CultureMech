# AMS1 Primary-Source Follow-Up

Read-only comparison of all ten held MediaDB AMS1 inputs: **200 ingredient
claims**, with **zero recipe edits, evidence additions or canonical reports**.
This does not increase applied totals or completed-review coverage.

[source-review.json](source-review.json) pins each current record and the captured
2013 article, retains every current ingredient node, and compares matching labels
against Table 1's explicit final-concentration column. Conversions preserve its
mM, micromolar, nanomolar and picomolar scales. Numeric agreement is deliberately
not a certificate of supplied chemical identity or exact variant identity.

The comparison flags **17 base-table discrepancies**: magnesium sulfate in all
ten records, and thiamine in seven. These are comparison flags, not seventeen
approved corrections. The original table also specifies hydrate forms, vitamins
and preparation stages that the flattened database records do not fully capture.
Pyruvate, glycine/serine, methionine, HMP and alternate phosphorus inputs require
experiment-specific review. Database annotations describe some concentrations as
maxima, not necessarily amounts used together in a single experiment.

## Source Access

- The actual [2013 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3578571/),
  doi:10.1038/ismej.2012.122, was re-read from its pinned full-HTML capture.
  Its base table and separate acclimation, substitution and cell-division
  experiments must not be collapsed into one formulation.
- The 2014 thiamine paper, doi:10.1038/ismej.2014.61, remained inaccessible in
  attempted full-text reads: PMC presented a browser challenge, Nature exposed
  a subscription preview, Europe PMC XML returned HTTP 500, and the Oxford
  article endpoint could not be opened. Search excerpts are not recipe evidence.
- The [2014 phosphorus paper](https://ftp.soest.hawaii.edu/dkarl/misc/dave/DOP/New%20papers%20for%20Refs/2014NatComm5-4346-Carini.pdf),
  doi:10.1038/ncomms5346, was readable as PDF-extracted text through the web tool.
  Its page 5 cultivation and page 6 microarray methods describe different
  formulations. However, the extractor renders several micro symbols as `m`.
  Direct PDF capture timed out and visual screenshot verification did not
  succeed. No numerical correction is approved from that extraction. Its text
  explicitly cites the 2013 AMS1 article as reference 39 (page 7).

## Next Curation Decisions

1. Resolve the exact experimental scope of each database variant, including
   whether a reported maximum has been mistaken for a fixed formulation.
2. Obtain a readable primary copy of the 2014 thiamine paper and visually verify
   the phosphorus paper's unit symbols before using their numerical values.
3. Decide hydrate, vitamin-membership and preparation changes explicitly. Do not
   add the older base table's B1 to an HMP substitution variant without evidence.
4. Prepare source-specific, guarded previews and per-record dispositions before
   any application. All ten records remain in the full ingredient-review goal.

The script and this report are source-review artifacts, not production changes
covered by the concurrently running fast test tier.
