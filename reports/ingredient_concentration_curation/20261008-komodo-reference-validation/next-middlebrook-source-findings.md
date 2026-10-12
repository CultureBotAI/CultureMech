# Middlebrook Source Inspection Handoff

This is source inspection, not a completed per-record review or an applied
repair. All 24 candidate YAMLs remain unchanged. The immutable inventory,
exact paths and 28 captures are in
[`next-middlebrook-context.json`](../20261008-lactalbumin-formulations/next-middlebrook-context.json).
The full current DSMZ 645/857/911 YAMLs and their histories were read this turn;
the other 21 current YAMLs still need full inspection before edits. No record
has yet received a complete guarded proposal and validation in this cohort.

Inspected: all four one-page original DSMZ PDFs as rendered images, all three
MediaDive recipe responses, all nine KOMODO feature/ingredient tables and all
12 TOGO component/quantity groups and preparation comments. TOGO ontology
annotations were not recertified. Linked ATCC/NBRC sources and the literature
behind the TOGO growth quotations have not yet been inspected.

## Primary Preparation Boundaries

- [DSMZ 645](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium645.pdf):
  the commercial route uses 19 g 7H10 powder, 900 ml water, 5 ml glycerol,
  followed by 100 ml OADC. A separate from-scratch route lists a 1,000 ml
  water input. The source presents this as an alternative when commercial
  medium is unavailable.
  Do not add the commercial powder and all its from-scratch ingredients as
  simultaneous inputs or sum the two routes' water volumes. OADC contains
  5 g bovine albumin and 4 mg catalase with a 100 ml water input.
- [DSMZ 911](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium911.pdf):
  21 g commercial 7H11, 900 ml water, 5 ml glycerol and later 100 ml OADC.
  Its basal detail table also lists a 900 ml water input, pancreatic casein
  digest, and 15 g agar. The OADC table is separate. Preserve preparation
  scope instead of counting a powder and its expanded formula twice.
- [DSMZ 857](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium857.pdf):
  the prose explicitly names one liter of final medium and a 900 ml water
  input containing 2 ml glycerol, followed by 100 ml ADC. The API main table's
  1,000 ml water row conflicts with that preparation input. ADC's catalase
  amount is 0.0003 g, not the 4 mg OADC value from 645/911. Source quote:
  "To prepare one liter of final medium".
- [DSMZ 645a](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium645a.pdf):
  specifies 60 micromoles hemin and dissolution in 1N NaOH, but supplies no
  explicit hemin-volume denominator or NaOH dose. Do not turn a micromole
  amount into micromolar concentration or invent a base volume.

The four source PDF binaries and their hashes are pinned in the inventory.
Local one-page renders inspected during this turn are
`/tmp/ingredient-media-20261007/middlebrook-{645,645a,857,911}.jpg`.
System `sips` rendered the cached PDFs because `pdftoppm` was not on PATH.

## Local Record Findings

- `CultureMech:001782` (DSMZ 645) flattens commercial 7H10, its alternative
  from-scratch formula and OADC into one list. Its commercial powder is also
  grounded as pure agar. Glycerol's 5 ml input is incorrectly represented as
  5 g/L. False LB constituents replace albumin, and its exact-duplicate parent
  points to the hemin-containing KOMODO 645a rather than an identical recipe.
- `CultureMech:002016` (DSMZ 857) keeps the basal rates alongside ADC stock
  rates at root scope. The source's glycerol input is present only in prose,
  and false LB constituents replace albumin. Restore the explicit 100 ml ADC
  addition and its source-specific preparation without importing OADC amounts.
- `CultureMech:002079` (DSMZ 911) likewise flattens basal and OADC stock rates,
  maps the 5 ml glycerol input to 5 g/L, and contains false LB nodes. Its real
  pancreatic casein digest and real NaCl are separate from the false LB
  tryptone/NaCl entries and must survive. Its KOMODO exact-duplicate child link
  needs reconciliation against that child's own source table.

These findings do not authorize reusing indices across records. Guard each
original ingredient identity, quantity, supplier metadata, stable ID and hash.
Inspect reciprocal links before relationship changes. Preserve all unrelated
history and mappings; correct a product-as-pure-compound mapping only with its
own source-supported explanation, not with a guessed replacement identifier.

## KOMODO Source Conflicts

The nine actual detail tables all declare Gram/Mol amounts per liter, but that
does not establish agreement with the linked primary preparation.

- [K645](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=645)
  and each of its five captured strain-specific tables report albumin 2.49
  and agar 7.48 in the Gram Amount column. They are not the DSMZ stock rates.
- [K911](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=911)
  and its DSM 44536 table report albumin 2.49 and agar 8.31, again requiring
  explicit reconciliation with the linked preparation stages.
- [K645a](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=645a)
  reports albumin 5.00, agar 15.00 and hemin 0.04 in that column, with NaOH
  unquantified. Its original PDF's micromole amount must not be treated as an
  independently verified conversion to this rate.

These are observed database assertions and possible preparation-scope
conflicts, not evidence that arbitrary source amounts should overwrite primary
recipes. No mechanism producing the discrepancies has yet been proven.
Do not endorse a dilution factor, transfer pH from another version, or infer
growth from a strain-named source record. All nine pages report null PH Info.

## TOGO-Specific Decisions Still Needed

- M2328 and M2399 separate commercial 7H10 input from the 100 ml OADC addition.
  Retain those scopes and each source's own preparation instructions.
- M2397 and M2403 specify ADC with 3 mg catalase per listed 100 ml water input,
  unlike DSMZ 857's 0.3 mg. M2403 explicitly gives ADC as 10% (v/v), but its
  glycerol/Tween percentages have no explicit basis. Do not assign w/v by
  habit or borrow another source's catalase amount.
- M2400 and M2401 describe half-scale commercial powder inputs and separate
  50 ml ADC supplements, alongside full base-composition tables without an
  explicit table volume. Do not use those listed masses as direct 500 ml
  batch inputs or fabricate a stock dilution factor. Their cooling limits
  also differ and must remain source-specific.
- M1946 and M2407 have 1 L OADC subrecipes with 50 g albumin, 0.6 ml oleic
  acid and 0.03 g catalase, dosed at 100 ml. Their main water inputs differ
  (895 versus 900 ml), and the basal agar is 13.5 g. Preserve those details;
  neither the 15 g DSMZ agar formula nor oleic-acid density may be assumed.
- M2402 and M2404 separate OADC from commercial 7H9 and its detailed formula.
  M2402's prose mentions dissolving agar although its table describes broth;
  M2404 has a separate Mycobactin J/ethanol reconstitution note. Do not silently
  invent agar or omit the reconstitution-stage ambiguity.
- M2879's title/component table describes ADC/Tween on 7H10 plates, while its
  quoted cultivation sentence assigns OADC to plates using "respectively".
  M2880 is the related liquid recipe. The underlying publication is not
  identified or inspected here; do not resolve the plate conflict by guessing,
  or promote the quotation to new organism-growth evidence.

Use each entry's exact TOGO API URL and JSON locator in the pinned inventory.
No citation DOI, author, publication year or percentage basis was invented.
Next: read all current records, classify source conflicts separately from
supported corrections, inspect needed upstream links, then build guarded
previews with snippet evidence on every edited scientific claim.
