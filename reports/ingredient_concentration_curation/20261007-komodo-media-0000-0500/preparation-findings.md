# KOMODO source-scope findings, first 500 pending paths

The frozen inventory selects 500 exact paths, from KOMODO accession 1 through
92 in natural accession order. It includes 77 exact base accessions and 423
variant accessions. A variant's original-recipe link is not evidence for the
variant's amounts, even when an earlier local annotation says SOURCE_DUPLICATE.

All 28 preliminary candidate recipe tables, preparation steps and local
ingredient contexts were inspected. The full parsed before-records and source
responses are preserved in [inspected-candidate-context.json](inspected-candidate-context.json),
with source hashes and retrieval metadata. This does not claim manual inspection
of every sentence for all 500 selected records or every original PDF.

## Withheld candidates

- **KOMODO 9a:** the local yeast and agar quantities are 5 and 15 g/L, whereas
  the reduced recipe gives 2.5 g yeast and 8 g agar per source batch. The
  [original DSMZ 9a recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium9a.pdf)
  confirms those reduced amounts and a separately prepared yeast suspension.
  The exact API recipe-table quote is frozen in [withholdings.json](withholdings.json).
  All four local claims remain unchanged; the two initially eligible matching
  claims are not endorsed pending formulation/version and stock review.
- **KOMODO 61:** local pH extends to 7.8, whereas the API and
  [original DSMZ 61 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium61.pdf)
  specify 6.8-7.5. The PDF also names separate strain-specific substrate
  replacements. The new condition guard withholds this record rather than
  assuming that shared amounts establish the same formulation.
- **KOMODO 70:** local pH is 1.4, whereas the API and
  [original DSMZ 70 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium70.pdf)
  specify 1.8. The sulfuric-acid carrier is also wrongly represented locally
  as a mass concentration. No concentration or pH replacement is made here.

These checks remove eleven preliminary evidence-only claims across three
records. They identify unresolved work; withholding is not a scientific repair.

## Retained scope and remaining work

The retained 137 claims are provider-declared main-recipe concentrations.
Their amount/unit/volume arithmetic and exact ingredient labels agree. They
are not independently measured final-volume concentrations, stock compositions,
or assertions that the full record is correct. Twenty-five separate root
evidence entries establish KOMODO-to-original-recipe identity only; mapping
rows are never used as amount evidence.

Examples requiring further curation include:

- KOMODO 34's 10 mM Tris-HCl carrier is locally encoded as 1000 g/L. Only other,
  independently supported ingredient rows receive evidence in this pass.
- KOMODO 57/59 retain liquid additions incorrectly represented as mass rates;
  these liquid rows receive no new support. Their other accepted rates use
  the provider's explicit 1001 ml basis, not an assumed 1 L denominator.
- KOMODO 80's 150 ml soil-extract addition is locally encoded as 150 g/L.
  The extract preparation, input loading and recovered liquid must remain
  distinct. The soil-extract row receives no concentration support here.
- KOMODO 3/36/38/48 and other recipes include separate sterilization or stock
  preparation steps. Scoped dataset rates do not fill unreported stock
  strengths, doses, preparation volumes or water makeup.
- Conditional or branded ingredients (including casein peptone attributes,
  optional agar, calcium carbonate and Titriplex) remain unsupported where the
  local form/context has not been established. Their existing values remain.
- KOMODO 67/90 retain other historical cross-resource matches; those matches
  are not used as identity evidence. Secondary chemical mappings, including
  previously identified molybdate-form conflicts, are not validated by an
  amount quote and are unchanged.

The DSMZ medium 72 amount endpoint returned HTTP 404 on re-fetch. The exact
negative response is hash-pinned in the source cache and its metadata is in
[source-captures.json](source-captures.json). The affected record has an
unchanged unsupported result; no recipe text or quantity is invented from the
mapping. There are 77 accessible distinct source responses and one unavailable
source among the 78 mapped endpoints represented by this batch.

All remaining variant, stock-topology, missing-inventory and source-only rows
have explicit per-record results. None is silently counted as resolved.
