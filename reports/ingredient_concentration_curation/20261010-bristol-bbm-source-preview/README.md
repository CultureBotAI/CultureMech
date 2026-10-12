# Bristol And Bold Basal Source Preview

Read-only preparation for the next curation batch. No recipes, IDs, history,
generated merges or canonical per-record reports are changed. Coverage increment
is zero. This is not a completed two-record review or an apply plan.

The [source preview](source-preview.json) pins the exact tracked Bristol and Bold
Basal records, eight public UTEX captures, and all 33 structured concentration
claims: seven Bristol and 26 Bold Basal. All four PDF pages were visually inspected
against the HTML sources. The later [variant methods preview](variant-source-preview.json)
adds four narrative-claim dispositions; growth claims and complete child
formulations remain outside these previews.

## Proposed Dispositions

- 26 evidence-only proposals: existing source-reported mineral molarities, stock
  inputs per litre and the explicitly approximate stock-drop doses.
- Six corrections proposed: remove fixed 1000 mL/L water values while retaining
  water nodes and make-up instructions. Final mixture volume is not solvent input.
- One unresolved conflict: the trace-stock source prints MnCl with tetrahydrate,
  while the record specifies MnCl2. Both HTML and PDF have the missing subscript;
  chemical form cannot be certified by guessing the intended formula.

The [Bold Trace stock page](https://utex.org/products/bbm-bold-trace-stock-solution)
contains inconsistent adjacent concentration columns. Its amount-per-litre
preparation must remain distinct from final-medium dosing. The preview records
diagnostic arithmetic without proposing new final concentrations. The
[iron-stock source](https://utex.org/products/bbm-iron-stock-solution) does not
explicitly state acid strength, so the existing concentrated-acid wording still
needs correction or separate support.

## Remaining Work

Resolve the BBM study's exact relationship to the UTEX parent, scope Bristol's agar
option and child formulations, resolve chemical-form/source conflicts, then build
and validate a guarded apply plan. No baseline schema or production-reference
pass is asserted by this source-only preview. UTEX recipe publication years remain
unknown; website and PDF copyright dates are not substituted for publication
dates. The article's 2022 publication year is verified. This preview does not
change the F/2 successor's frozen validation state.

The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/35807621/) confirms Kozlova
and Levin, 2022, DOI `10.3390/plants11131669`, and its figure caption describes
the estradiol range. Initial browser-based full-methods access failed:
PMC returned a browser-check page, DOI/MDPI returned HTTP 429, and Europe PMC
was inaccessible through the web tool. Those failures are retained as retrieval
history, not treated as evidence that the article is unavailable everywhere.

The public Europe PMC XML API subsequently returned the complete article,
version `PMC9269517.1`. Its captured DOI, title, authors and publication year
match the cited study. Sections 2.1-2.3 support the [four-claim preview](variant-source-preview.json):
assay pH, flask capacity, five discrete estradiol concentrations with a blank,
and 4.5 ppm NH4Cl in the pre-experiment stock culture. No conversion from ppm
is proposed, and flask capacity is not treated as culture volume. The article
cites Stein 1973 for BBM; equivalence to the current UTEX recipe is not established.
These are proposed variant evidence/wording changes, not applied edits.

Separate [child preparation triage](child-stage-notes.md) records preliminary
Botryococcus, Proteose and Bristol-NaCl observations. It is not included in the
33 structured claim rows or canonical review coverage.
