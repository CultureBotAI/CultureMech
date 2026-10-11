# Medium212 Family: Source Preparation, Not Applied Review

The [ignored-inclusive inventory](next-212-local-preparation.json) pins 22
unchanged records and 259 existing quantity fields. It includes DSMZ212,
DSMZ212a, KOMODO212, the linked DSM2805-specific record and eighteen standalone
stocks. Existing canonical records and previously curated stocks remain intact.
This inventory does not add completed reviews or narrow the full corpus scope.

## Retrieved Evidence

The [approved discovery](next-212-discovery-approved.json) retains three newly
retrieved public originals: KOMODO212 and the DSMZ212/212a PDFs. The separate
[initial failure](next-212-discovery-initial.json) records all three sandbox
network errors. No repository contents were sent, and no GitHub writes occurred.
The two MediaDive parent captures are dated 2026-10-07; S608 is a separately
hash-verified cached source. These three older captures were not refreshed.

- [KOMODO212](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=212)
  has 32 displayed ingredient rows with four null quantities. Its per-liter
  table includes bicarbonate at 3.48 g/L and butyric acid at 1.69 g/L. The local
  medium currently has 44 direct ingredients plus two inline stocks. Restore only
  its own source formulation after mapping every existing field; do not copy
  amounts or chemical forms from the modern original.
- [DSMZ212](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium212.pdf)
  assembles six solutions, A through F. Solution C uses sodium butyrate, while
  its DSM2805 note specifies sodium propionate replacement plus glucose. The
  separately curated DSM2805 record must retain that strain-specific boundary.
- [DSMZ212a](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium212a.pdf)
  assembles nine solutions, A through I, including separate starch, glucose,
  sugar mix, pyruvate and dithiothreitol inputs. It is not the same formulation
  as the KOMODO212 table or original212. The current SOURCE_DUPLICATE link is
  therefore a high-priority source-identity defect to resolve with full evidence.

The source table assembly doses are not permission to infer all final chemical
concentrations. Check final-volume statements, nested stock boundaries, precise
chemical forms and source-specific rates separately. A 30% tube-fill instruction
is vessel context, not concentration. Both originals also describe semisolid
shipping/inoculation handling and strain-specific modifications; these must not
silently become the base formulation.

## Remaining Work

The first canonical-cache inventory had twenty read errors. Three originals
and then [seventeen standalone sources](next-212-stocks-approved.json) were
retrieved successfully. The [initial stock-fetch failures](next-212-stocks-initial.json)
remain archived. There are now 23 captures with explicit retrieval dates, not
23 newly retrieved sources. Failure to read a canonical cache file was not proof
that no local evidence existed.

[Source inspection](next-212-source-inspection.json) records 83 standalone
ingredient/stock-input rows and 32 KOMODO rows. All 21 stock-to-parent comparisons
match in name and every non-null recipe field, preserving row order. Explicit
null versus omitted null is the only permitted normalization. This establishes
source correspondence, not the correctness of denominator assumptions.

[Visual inspection](next-212-visual-review.json) now covers all seven original
PDF pages and locates 123 table rows. Column alignment, mg/g/ml distinctions,
split tables, hydrate forms and separate strain modifications were checked.
The PDFs lack a general final-volume makeup statement; only the SL-10 stock
explicitly supplies one. Do not turn the sum of receiving doses into an
unqualified final-volume assertion.

Read all 22 complete records and source histories, verify the DSM2805-specific
BacDive evidence, reconcile shared stock sources and preserve earlier evidence
paths. Then prepare independent
per-field decisions, complete preview ledgers and guarded tests. No medium212
ingredient edit or completed scientific review is claimed here.

## DSM2805 Web-Reader Check

The [BacDive16667 page](https://bacdive.dsmz.de/strain/16667) was accessible through
the web reader during this continuation. The reader reported a crawl from two
weeks earlier, not a new raw HTTP capture. Its culture-medium table explicitly
identifies a strain-specific DSMZ212 formulation and displays, for example,
"Na-propionate 1.49551 g/l" and "D-Glucose 0.997009 g/l". These source-specific
values must not be replaced by the rounded nominal original-PDF variant doses
without a documented source decision. No record was edited from this check.

The page displays DOI `10.13145/bacdive16667.20260601.11`, but the initial DOI
open returned a web-reader accessibility error. The initial DSM2805 catalogue
open also returned an accessibility error. These historical failures are not
proof that either identifier is invalid.

The subsequent [raw source capture](next-212-DSM2805-source-capture.json)
successfully retrieved both the BacDive strain page and the DSMZ catalogue page
on 2026-10-09, with HTTP 200 responses and saved byte hashes. The DOI request
returned HTTP 302 to a BacDive versioned PDF endpoint; that redirect was recorded
but not followed. Thus DOI redirection is confirmed, but the versioned PDF has
not been retrieved or checked. No recipe, taxonomy or growth claim was applied.
Complete field-by-field comparison remains required before a guarded repair.

The subsequent [quantity comparison](next-212-DSM2805-comparison.json) checks all
32 existing ingredient amounts and units against the saved BacDive table, with
an exact snippet and field path for each. All 32 match the provider rates; none
of these ingredient nodes has attached evidence. The source also lists distilled
water without an amount, which is not a zero or a calculable dose. This read-only
comparison changes no record and does not certify chemical groundings, final
volume arithmetic, preparation completeness or organism-growth assertions. The
complete guarded review remains pending.
