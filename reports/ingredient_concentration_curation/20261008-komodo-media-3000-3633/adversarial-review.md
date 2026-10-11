# Source And Scope Review

This is a local adversarial review, not an independent reviewer or GitHub review.
The all-record curation objective and publication gates remain incomplete.

## Publication Blocker

The actual current merger retains only 126 of 226 complete concentration
evidence entries in canonical ingredient locations. Fourteen target records
lose full entries; twelve also lose one or more exact amount quotations in
those locations (139 of 226 amount quotations are retained). Eight records
lose their new mapping evidence, references and event from the corresponding
root fields. These are scoped retention failures, not proof that every item
has disappeared from every possible variant field. See
[merge-retention.json](merge-retention.json) for the exact groups and checks.

For example, current concentration-independent groups combine 1194, 1195 and
1213 despite their differing salt concentrations. A supported source quantity
must not be transplanted onto a different canonical formulation. Resolving this
requires formulation-aware merge/variant provenance handling and regeneration,
not hand-editing generated YAML. The normalized evidence remains intact, but
publication is gated.

Full citation validation also fails on 38 API title checks: the installed
validator returns each JSON endpoint's URL as its title, rather than the
descriptive MediaDive entry title. All 264 new excerpts pass the installed
source-text matcher, including 38 identity-only mapping excerpts. These are
separate outcomes. See [reference-validation.json](reference-validation.json);
the title failures were not suppressed or represented as a full citation pass.

## Findings Prevented From Receiving Support

Twenty source-pinned decisions in [withholdings.json](withholdings.json) veto
158 initially proposed evidence-only claims. Each decision records the exact
record ID, source hash, JSON pointer and excerpt; none authorizes a new amount.

- **Incorrect stock-dose encodings:** DSMZ 1157 specifies a 5 ml riboflavin
  stock addition, not the local 5 g/L. DSMZ 1164 specifies seven drops of an
  iron stock, not 7 g/L. The original PDFs corroborate these findings.
- **Omitted stock/preparation stages:** 1081, 1085, 1091, 1106, 1111, 1130,
  1175, 1184, 1185, 1204, 1233, 1248, 1265, 1288 and 1309 require separate
  preparation groups, stock additions or source-version resolution. Unknown
  strengths, percent bases and volumes must not be guessed.
- **Unquantified missing supplement:** 1216 requires a B12 stock addition in
  preparation text, but neither the original PDF nor API specifies its dose or
  strength. Its omission from the ingredient table does not establish zero.
- **Chemical-form disagreement:** 1270's original PDF visibly prints
  `Na2citrate x 2 H2O`; its API identifies trisodium citrate dihydrate. The
  actual PDF page image was inspected, not just extracted text. Resolve this
  discrepancy before endorsing the formulation.
- **Artificial seawater identity:** 1274 specifies 500 ml artificial marine
  water and 500 ml distilled water. The local 500 g/L seawater is not equivalent.
  The NBRC 1077 cross-reference and artificial-water composition need review.

The ten original-recipe byte hashes, retrieval metadata and extracted pages are
preserved in [original-recipe-captures.json](original-recipe-captures.json).
These checks confirm the issues; they do not correct the withheld YAML records.

## Remaining Findings In Partially Supported Records

- 1117 and 1252 encode 1000 ml water inputs as 1000 g/L. The PDF and API agree
  on the input volumes. A later guarded repair must preserve input-volume scope,
  inspect linked source records and add claim-specific evidence. Neither water
  concentration receives support in this pass.
- 1159's API agar row gives a 20 g amount but `g_l=15`. Its original PDF lists
  15 g agar. The inconsistent API row remains a conflict, not a numeric update.
- 1161's source preparation mentions a sterile filter-paper strip. The local
  record lacks that unquantified substrate/preparation detail. Evidence for
  listed basal ingredients does not establish a complete culture procedure.
- 1289 retains a conflicting legacy `kg_microbe_match` value of
  `mediadive.medium:101`. The primary KOMODO accession and captured mapping
  identify DSMZ 1289; this pass neither endorses nor edits that legacy field.
- Secondary ontology mappings, optional ingredients, supplier qualifiers and
  genuine variants are not validated merely by matching an amount or name.

## Safeguards

Only matching provider-declared main-recipe mass concentrations receive new
support. These are not independently measured final volumes. Every supported
claim has an exact source excerpt, persistent URL, field locator, retrieval
hash and scope explanation. Mapping-page evidence establishes source identity
only. Existing numeric values, physical states, ingredient lists, organism
associations and prior history remain unchanged.

The independent auditor accepts an explicit positive expected cohort size,
retaining the historical default of 500 while requiring 633 here. Regression
tests reject wrong sizes, verify all persisted claim excerpts and retain every
source-pinned withholding. Passing schema or snippet checks does not resolve
scientific completeness or failed publication gates.
