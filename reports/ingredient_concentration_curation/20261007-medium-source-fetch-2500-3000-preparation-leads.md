# Next JCM Cohort: Unapplied Preparation Leads

This is a handoff, not a completed per-record source review or an applied batch.
[Acquisition](20261007-medium-source-fetch-2500-3000.json) covers 500 JCM
records, J507 through J1009 in the frozen inventory order, with zero failures
and matching baseline hashes. Eighty-one API responses contain no recipe table.

The temporary mechanical preview is
`/tmp/ingredient-media-20261007/media-2500-3000-preview.json`.
It proposes 358 evidence-only claims in 68 records before scientific decisions.
No YAML or canonical per-record report was produced for this cohort. All 68
candidates' main preparation texts were read; complete amount tables were
subsequently inspected for J611, J654, J896 and J975. The other amount tables,
local record contexts and original-source checks remain to be reviewed.

## Priorities

- **J896, MODIFIED BSK MEDIUM:** the API volume is 40 ml, apparently counting
  rabbit serum alone; the original recipe explicitly makes the mixture to
  **584 ml**. Its six mechanically eligible concentrations must not be endorsed
  using 40 ml. The original table also names TC Yeastolate where the dataset
  says yeast extract with a TC attribute; resolve that source identity before
  changing the mixture row. The original page was inspected:
  [JCM 896](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896).
- **J611:** a 900 ml base receives 100 ml carbonate stock, which is absent from
  the API table. Do not support the base-volume rates as the complete medium.
  The original page confirms the later addition, but does not specify the
  percentage basis: [JCM 611](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=611).
- **J542:** preparation may remove a precipitate; inspect affected ingredient
  identities and retained-amount scope rather than assuming all input masses
  remain dissolved.
- **J559, J626, J634, J646, J719, J811, J997:** preparation adds separate stocks;
  inspect dose and volume accounting before any support. J526 and J557 also
  separately filter-sterilize an addition and need preparation-stage review.
- **J653, J654, J698, J725, J744, J766, J975:** prose interleaves following
  solutions with base rows. Inspect recipe order and attributes, not just
  ingredient names. J654's table includes 900 ml water plus a 100 ml lactate
  solution. J975's source makes a 970 ml base and lists a 30 ml 10% w/v
  carbonate addition, a possible positive control rather than an automatic veto.
- **J595, J615, J660, J698, J735, J809:** preserve variant-specific and
  strain-specific preparation distinctions. Do not combine alternatives or
  propagate a solid/semisolid instruction to every formulation.
- **J888:** potato extraction and sieving need recovered-volume review, as in
  the earlier J30 finding. No final makeup is stated in the API preparation.
- **J890/J891:** solvent additions are explicit; inspect their table volumes
  before deciding whether the denominator includes them.

Before applying, freeze source-pinned withholding decisions and a canonical
cohort plan, then independently preflight it. For J896, prefer a source-backed
numeric repair through an explicit successor after the cohort baseline is
established; do not mutate the frozen inventory or silently accept the bad rate.
This cohort remains within the 8,630 paths outside completed follow-up reports.

## Inspected Original Captures

The three official JCM HTML pages were retrieved and inspected on 2026-10-07.
Local captures use `/tmp/ingredient-media-20261007/JCM_GRMD<number>.html`.
J975 confirms the explicit 970 ml base plus 30 ml 10% w/v carbonate solution;
it is not an omitted-stock example like J611.

| Original page | Capture SHA256 |
| --- | --- |
| [J611](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=611) | `71203704c1c615954224c874c8382037656635e26769cf38d09abc1e64300127` |
| [J896](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896) | `c6e814a8bff1580ddd42179b7d401a204ae19469786fdafd140408d1522f03c8` |
| [J975](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=975) | `2a8afe08ba5171456e2a19df2bc570263510f8c29254c92fda73184404e982e5` |
