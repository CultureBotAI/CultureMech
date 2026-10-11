# Medium330 Source Review Handoff

**Preparation only: thirteen records are unchanged; no new YAML evidence or
curation event is counted.** All records remain part of the full 15,910-record
objective. The [preparation receipt](next-330-preparation.json) pins exact
paths, IDs, source captures, checks and existing canonical reports.

## Cohort

| Source Key | Stable ID | Old Quantity Fields | Required Proposal Work |
| --- | --- | --- | --- |
| DJ1029 | CultureMech:002212 | 25 | Separate main ingredients, mineral stock and VFA stock; restore input units; explicitly retain the original-source access gap. |
| K330 | CultureMech:005024 | 28 | Restore 27 exact displayed source rows, including nulls; remove copied LB and stock-solvent claims; correct unsupported exact-duplicate links. |
| M1093 | CultureMech:007610 | 22 | Split 960 ml main water from 1 L stock water; correct mg and stock-dose units; restore linked VFA composition without importing Medium10. |
| S124 | CultureMech:010744 | 4 | Preserve supported hemin rate; represent 1 ml of 1 N NaOH separately from water added to make up 100 ml; remove false placeholder. |
| S3774 | CultureMech:012851 | 8 | Restore seven liquid VFA input volumes; do not claim percentages from assumed additive volumes. |
| S5080 | CultureMech:013996 | 15 | Preserve six qualified evidence entries at their existing paths; restore water and two missing stock inputs; distinguish provider rates from original-methods evidence. |
| S606 | CultureMech:014786 | 14 | Restore water, missing stock inputs and the resazurin stock dose/strength boundary; qualify provider rates separately from DSMZ's nominal-volume arithmetic. |
| S607 | CultureMech:014792 | 7 | Preserve all six supported composition entries; remove the contradictory placeholder and correct source-title metadata. |
| S608 | CultureMech:014795 | 8 | Restore seven acid input volumes; do not treat density-derived provider fields as unqualified physical measurements. |
| K330_17630 | CultureMech:005023 | 28 | Restore 28 displayed rows, including 16 changed rates and rumen fluid; retain strain-specific relationship and unknown provider pH. |
| K3032 | CultureMech:004812 | 0 | Restore six source rows; expose the provider's contradictory DSMZ3032 Instructions link rather than asserting equivalence. |
| D330 | CultureMech:001429 | 28 | Restore original PDF stages, source-stated nominal final-volume arithmetic, missing input nodes and strain supplement context; remove copied LB. |
| K3131 | CultureMech:004979 | 0 | Restore seven source-named acids with null amounts; expose the provider's contradictory DSMZ3131 Instructions link. |

The [old-field mapping](next-330-old-slot-mapping.json) accounts for 187 fields:
170 have inspected source-row candidates, and 17 are copied LB ingredients,
placeholders or copied stock-solvent claims. This is not an executable guarded
proposal. New-node completeness, metadata changes and every final evidence
path still require independent review.

## Source Boundaries

1. DSMZ330 explicitly states a nominal final volume of 1003 ml. Its listed
   liquid inputs sum arithmetically to 1003.6 ml. Preserve that discrepancy;
   do not assume volume additivity or silently replace the stated denominator.
   Eleven main batch-mass rows can be expressed using the stated nominal
   denominator, with the exact calculation and rounding disclosed.
2. The original main resazurin input is 0.5 ml of a 0.1% w/v stock, while
   hemin is supplied as 2 ml of a 0.05% w/v stock. Strength, stock addition,
   final-medium concentration and standalone stock composition are distinct.
3. The mineral stock lists batch masses and 1000 ml water, not an explicit
   make-up instruction. Its existing provider-qualified rates are not proof
   of measured final volume. Preserve the six supported S607 entries.
4. The hemin-stock procedure explicitly makes up to 100 ml. Its table's water
   entry must not become another 100 ml fixed input. The existing 0.5 g/L
   stock hemin evidence remains supported; it is not a final-medium dose.
5. KOMODO's base resazurin amount and hemin amount differ from original DSMZ
   representations. The DSM17630 variant has 16 changed displayed rates and
   one additional rumen-fluid row. Keep provider precision and nulls; do not
   infer rumen-fluid density from its Gram Amount column or from DSMZ's ml/l.
6. JCM1029's live fetch returned no recipe, despite an earlier web-cache view
   showing content. A [separate diagnostic](next-330-JCM1029-diagnostic.json)
   retained the actual HTTP 200 response: the requested accession and "Nothing
   found", without the recipe heading. This is not just a parser failure.
   Neither the earlier cached view nor API agreement constitutes successful
   current original-source verification. Keep this gap explicit and scope
   available evidence to the inspected datasets.
7. The [linked-stock review](next-330-linked-stock-review.json) verifies
   M1093 -> M124 -> JCM133 and all seven VFA inputs. The remaining 24 JCM133
   table rows belong to other Medium10 stages and are excluded. M124 is a
   source comparison, not another record selected for editing.

Sixteen official captures succeeded across the primary and linked-source
fetches; JCM1029 remains unavailable. Both PDF pages were visually inspected.
All 26 baseline schema/strict commands pass. Thirteen prior supported evidence
entries must be retained with their old snippets, timestamps, qualifiers and
field paths. No chemical identifier or publication year is inferred.

The first PDF row-extraction guard rejected the final-volume header as an
extra ingredient-like row before any report or recipe write. The corrected
inventory excludes that header from the 32 ingredient rows and keeps it as
separate denominator evidence. The initial sandbox network failures are also
retained separately from successful public-source captures.

Next: implement a preview-only guarded builder with full old/new claim lineage,
independent source projection and adversarial tests. Validate every snippet,
bibliographic title, preparation stage and conversion before applying. The
existing 12 canonical reports are pinned; M1093 has no canonical concentration
follow-up report yet in the ignored-inclusive inventory. Do not create duplicate
Record markers or count preview claims as applied evidence.
