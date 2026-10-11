# OTEB Source Conflicts

Local issue only; no GitHub issue was created. The six-record applied repair exposes
these conflicts without claiming to resolve what the sources do not establish.

## Volume And Stock Scope

The original recipe gives basal masses and liquid inputs separately. Those
liquid inputs total 1003.1 ml; the API declares 1000 ml. The original also prints
`Final volume 7.0 ml +/- 0.7.` That statement is retained, but is not used as
the formulation batch denominator or interpreted as a new dispensing command.
The stock's 1000 ml water is likewise an input, not an explicit make-up-to-final-
volume instruction. Original masses stay in evidenced batch notes without
invented g/L. Source-explicit volumes use L input quantities.

The vitamin-K1 input is 0.1 ml of `1% soln`. Neither original nor API establishes
w/v, w/w or v/v. The API's `g_l: 0.001` is preserved as source context, not an
asserted vitamin mass. Stock solvent and final vitamin concentration remain
unknown. The standalone stock keeps prior explicitly qualified provider rates
without pretending the original independently establishes their denominator.

## Serum And Maltose

The original says inactivated calf serum; the API says fetal bovine serum.
D1245 retains the original label and records the disagreement. S2474 retains
its own provider's label with the original as countervailing context. No
biological interchangeability is asserted.

K1245 displays calf serum 99.70 g/L. The DSM18691 variant retains that row and
adds fetal bovine serum 100.00 g/L; it is not a substitution or exact duplicate.
The reciprocal family links are recorded as source derivation and a
strain-specific variant, not as new taxon-growth evidence.

The original and API each list two separate maltose rows of 8 g in the sugar
stock. Preserve both rows and their order without deciding whether duplication
was intentional. KOMODO independently displays 16.00 g/L in its stock and
1.60 g/L in its medium. Those provider rates do not resolve the original's
ambiguity and are not curator-derived sums.

## Identity And Procedures

Copied monobasic phosphate annotations conflict with the explicit dibasic
source. Withdraw those annotations without inventing replacement ontology IDs;
the standalone solution's already correct dibasic annotation remains unchanged.
The KOMODO thiamine-pyrophosphate name and Thiamine-HCl alias conflict. Keep
that disagreement explicit and withdraw unverified chloride-specific links.
No molecular-weight conversion is used to choose a chemical form.

The original's 25 C is a pH measurement condition, not HEAT or incubation.
Its descriptive anoxic handling paragraph is not POUR_PLATES. The repair
preserves all descriptive text in notes and removes those unsupported action
assignments without inventing replacement preparation instructions.

## Evidence And Closure

Exact excerpts, locators, source URLs and captured hashes are in
`source-review.json`, the exact applied YAML in `plan.json`, and `applied-records/`.
The sources are the official DSMZ1245 PDF, medium/1245 and solution/2474/5688
APIs, and exact KOMODO1245/1245_18691/6000 tables.

Application fixes the local transcription/scope errors while leaving the
documented upstream ambiguities open. This issue must not be labeled fully
resolved merely because schema and reference validators pass.
