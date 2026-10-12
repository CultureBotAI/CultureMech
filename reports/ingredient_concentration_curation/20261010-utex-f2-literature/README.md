# F/2 Inline Variant Evidence Follow-Up

## Historical Source Preview

The source proposals below led to the
[applied two-record successor](../20261010-utex-f2-followup/README.md).
This directory retains its original read-only snapshots and does not add
canonical report coverage. Statements below about unchanged recipes describe
the preview state, before that application.

This is a source-research follow-up, not an applied recipe batch. The parent
`data/normalized_yaml/algae/F_2_Medium.yaml` retains its three existing variants
unchanged. [Retrieval results](retrieval.json) pin successful captures and retain
the unsuccessful full-text request. No canonical coverage increment is claimed.
[The claim-level preview](source-review-preview.json) pins the current record,
source hashes, bibliography, exact excerpts and four proposed dispositions.
It verifies that all 15,910 normalized records remain unchanged and explicitly
distinguishes the manually inspected PMC text from downloaded captures.

## Tetraselmis Nitrogen Repletion

The retrieved Europe PMC record for PMID 28456040 identifies
[doi:10.1016/j.biortech.2017.04.008](https://doi.org/10.1016/j.biortech.2017.04.008),
*Nitrogen or phosphorus repletion strategies for enhancing lipid or carotenoid
production from Tetraselmis marina* (2017), by I. Dahmen-Ben Moussa, H. Chtourou,
F. Karray, S. Sayadi and A. Dhouib.

The inspected abstract explicitly supports the first seven-day F/2 stage and
the second three-day nitrogen-replete treatment. The short source excerpt is
"N-replete condition (4.41mM NaNO3)" after HTML subscript rendering. This supports
the existing 4.41 mM study-specific nitrate claim, not a change to canonical
UTEX F/2 or a strain-specific assertion. A later guarded edit can add the DOI
and bibliography context while preserving the existing PMID evidence.
The complete methods were not retrieved; no broader formulation is certified.

## Modified F/2ASW Sodium Response

The [publisher article](https://link.springer.com/article/10.1007/s10126-021-10037-4)
confirms the title, six authors, 2021 publication, and link to the public
[Table S1 supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs10126-021-10037-4/MediaObjects/10126_2021_10037_MOESM1_ESM.pdf).
The one-page supplement was downloaded, hashed and visually inspected. The
main article exposes only abstract/metadata without subscription access.

Table S1's trace-element heading is "Trace elements (µM)" and its Na2SeO3 row
gives 0.001. That is **1 nM**, not the current variant's **10 nM**. Its basal
seawater table separately gives sodium metasilicate nonahydrate as 0.1 mM,
supporting the existing silicate amount. The NaCl footnote specifies the
experimental concentration choices as 0, 10, 20, 50, 200 or 423 mM.

Do not turn the table into a generic sodium-selenite addition to UTEX F/2.
The study table is a complete modified artificial-seawater formulation and
also uses potassium nitrate/phosphate and its own trace/vitamin composition.
The 10 nM statement lacks support in the inspected supplement; reconcile the
main methods or explicitly scope a correction to Table S1, preserving any
source disagreement rather than averaging it. UTEX LB2658 is not identified
by the inspected supplement/abstract, so the strain claim remains unverified.

## Aquaporin Study

Initial PMC and publisher requests failed, and the Europe PMC fullTextXML
endpoint returned HTTP 500; those failed requests remain in the retrieval log.
A later web-tool retrieval of the [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6130027/)
succeeded. Its Materials and Methods, Cells and Culture Conditions section was
inspected directly, not inferred from search excerpts. It states "artificial
seawater supplemented with one-half-strength Guillard’s f solution" and confirms
the existing 20 C, continuous 30-75 micromol photons per square meter per second,
and air/1% CO2 culture conditions. It separately names P. tricornutum UTEX 642
and T. pseudonana CCMP1335.

This supports adding the missing formulation snippet to the existing
DOI:10.1104/pp.18.00453 variant evidence entry. It does not equate this artificial
seawater with UTEX's natural-seawater F/2 recipe. The same methods distinguish
experimental nitrogen conditions (1.8 mM NH4Cl and 18 micromolar NaNO3), which
must not be collapsed into the general maintenance formulation. This success
is a manually inspected web-text result, not a complete HTTP capture or a
passing automated reference gate.

## Next Action

After the current applied-batch validation finishes, prepare an append-only
follow-up for the F/2 parent and NH4 child: source-scoped literature evidence,
the NH4 exact-snippet spacing repair, and its two retained flask-volume
descriptions. Revalidate the full changed records and preserve the applied
batch's existing source ledger and curation history.
