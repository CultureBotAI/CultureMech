# Medium-119 Source Conflicts and Representation Limits

Local curation issue, not a published GitHub issue. The proposed repair retains
source-specific data; the following disagreements are not silently resolved.

## Source Disagreements

- KOMODO 119_6216 reports sodium acetate 3.99 g/L; the linked original DSMZ 119
  strain instruction says 3.00 g/L. Preserve both with explicit source scope.
- Current DSMZ instructions for DSM 11977, 11978, 11995 and 16643 replace the
  basal reducing agents with vitamins, dithiothreitol and coenzyme M. The matching
  KOMODO tables retain the basal reducing agents. KOMODO 119_11977 additionally
  reports NH4Cl 10.40 g/L. Do not overwrite either source's formulation.
- KOMODO 119.1 combines DSM 16632 and 16643, whereas the original distinguishes
  their modifications. Preserve the provider-specific record and the original's
  separate conditional recipes, without inferring new growth associations.
- DSMZ 15163 instructions omit sulfide and add 0.3 g dithiothreitol; its KOMODO
  table retains sulfide. The original gives a batch mass, not 0.3 g/L.
- KOMODO 119/119.1 aerobic metadata disagree with the original's anoxic
  preparation. Their pH 7.5 also differs from original complete-medium pH 6.8-7.0.
  The fatty-acid stock's pH 7.5 must not be confused with complete-medium pH.
- KOMODO 119_7256 reports rumen fluid under Gram Amount, 200.00 per liter.
  This does not verify a density or authorize conversion to 200 ml.

## Quantities Without a Verified Denominator

DSMZ 119 explicitly states final volume 1003 ml; this supports only that base
recipe's direct basal mass conversions. The inspected 119a/b/c PDFs do not state
the same denominator. Their exact batch masses remain in evidence-backed notes.

SL-10 explicitly makes up to 1000 ml, supporting its stock mass concentrations.
Its 25% HCl lacks an explicit percentage basis. Keep the 10 ml input and qualifier
without a density or percentage conversion. The ferrous-sulfate stock explicitly
states 0.1% w/v; its 1000 ml of 0.1 N H2SO4 is a carrier input, not 1000 g/L.

Sludge processing includes incubation, centrifugation and autoclaving. Starting
yeast mass is not evidence of an unchanged final-medium yeast concentration.
Rumen-fluid preparation supplies no component recipe; keep its preparation and
receiving dose without inventing a composition.

## Family and Identity Limits

The copied K119/DSMZ119b exact-duplicate assertion is unsupported. K119 explicitly
links DSMZ119, not 119b. The preview removes the false edge reciprocally and
records source derivation from DSMZ119 instead. Strain-labelled KOMODO records
remain separate, including records whose displayed ingredient rows are equal.

The existing DSMZ119-to-119c candidate link does not establish derivation
direction, and the recipes differ in both bicarbonate and gas preparation. The
preview marks that existing relation UNCERTAIN rather than inventing lineage.

Copied nickel anhydrous annotations do not establish the source hexahydrate;
copied sodium-resazurin and L-cysteine identities must not be imposed on less
specific KOMODO labels. Withdraw unsupported annotations without inventing new
ontology IDs. Other retained annotations are not recertified by this review.

Exact source captures, PURLs, excerpts and locators are in `context.json`,
`plan.json` and the per-record preview ledgers. Closing this issue requires
source/version reconciliation where applicable, not merely passing schema or
quote-matching tests. The issue remains open.
