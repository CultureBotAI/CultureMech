# Candidate Inspection And Withheld Claims

The frozen initial preview proposed 325 concentration-evidence entries across
54 records. All 54 complete local records and full API responses were inspected,
including ingredient identity, preparation, optional ingredients, source/accession
context, pH, parent/child relationships and prior history. The lossless
`candidate-inspection-view.json` factors 113 ingredient templates and 356 distinct
history entries; reconstruction was checked against every complete local record.
The 367 history occurrences additionally reduce to 33 reversible text templates.
These are inspection aids, not evidence sources. Complete inputs and exact claims
are retained in `inspected-candidate-context.json`.

The final preview withholds 75 initially proposed entries across 11 records.
It leaves 250 evidence-only entries on 43 records; no quantity is changed.
`withholdings.json` pins each decision to its exact API source hash, pointer,
verbatim snippet, record ID and formulation-specific reason. Every other record
still receives an unchanged report with its unresolved claims.

## Whole-Record Withholdings

| DSMZ/KOMODO accession | Unresolved boundary |
| --- | --- |
| 805 | Iron is a 1 ml stock labelled 2% without a percent basis, not a verified direct mass concentration. |
| 844 | Magnesium and calcium are separate post-autoclave 5% w/v stock additions. |
| 917 | Calcium stock is sterilized separately; strength and dose are not given. |
| 923 | Carbonate and agar must not be autoclaved together; the mixing stage is absent locally. |
| 959 | Current source uses 15 g NaCl, local SL uses 26 g/L; source name and anoxic maltose/sulfide stocks require version reconciliation. |
| 964 | Peptone, yeast and sulfide are late anoxic stocks; the table also contains a resazurin stock. |
| 971 | NaCl and carbonate are separately autoclaved and mixed with organic components. |
| 983 | TAPSO is locally grounded to a diclocymet term; the original PDF supplies no water/final-volume statement. |
| 990 | Yeast, peptone and sulfide stock strengths and addition stages are flattened. |
| 1038 | Glucose and yeast stocks are added after acidic basal sterilization. |
| 1052 | The cross-reference to 585 A/B requires separate preparations and unresolved water allocation, not wholesale import of 585. |

## Original-Recipe Cross-Checks

Seven official PDFs were retrieved directly with HTTP 200 and their full bytes,
hashes, timestamps and extracted page text were captured in
`original-recipe-captures.json`. Page images of 877, 983, 1027, 1048 and 585 were
rendered locally and inspected after the browser screenshot tool returned no
usable image. These are bounded checks, not a claim to have read 500 original PDFs.

- [805](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium805.pdf), page 1:
  the iron row says `2% FeSO4 x 7 H2O 1.00 ml`; its percent basis is unspecified.
  Direct retrieval succeeded after the browser fetch failed.
- [877](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium877.pdf), page 1:
  `Agar 1.5 g` and `Distilled water 100.0 ml`. The API rescales other inputs
  consistently to its declared 1000 ml basis, but its agar amount is 20 g and
  `g_l` is 15. Agar remains a conflict, unchanged and without new API support.
- [1027](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1027.pdf) and
  [1048](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1048.pdf), page 1:
  each lists 15.0 g agar and 1.0 l water. Their API agar rows likewise have
  inconsistent 20 g amounts and `g_l=15`. No API-derived agar endorsement is added.
  These water inputs are not asserted to be independently measured final volumes.
- [983](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium983.pdf), the
  complete single page: contains `TAPSO 1.30 g` but no water or final-volume
  declaration. The API's 1000 ml water row therefore needs provenance beyond
  this PDF. Neither this gap nor the wrong local TAPSO identity is silently fixed.
- [1052](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1052.pdf), page 1,
  refers to A/B of [585](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium585.pdf).
  Each of those preparations has 490 ml water and separate sterilization. This
  does not authorize the distinct C/D supplements of 585 or prove the 1052
  recipe's intended final-volume allocation.

## Other Retained Limitations

Supported entries describe only the API provider's declared main-recipe mass
concentrations for exact labels/forms, with the literal ingredient row, arithmetic
and captured response hash. They do not independently establish final volume,
secondary ontology mappings, historical source-version identity, growth,
incubation conditions or equivalence of linked variants.

Examples left unresolved include tap/seawater and Tween 80 encoded as mass rates,
unqualified percentages, branded/optional rows, inherited default VARIABLE
amounts, hydrate/mixture grounding gaps and wrong medium cross-links. The
inherited aerobic notes on 934 and 957 disagree with their source's anoxic
preparation; amount evidence is not support for those notes. No growth association
is added. SOURCE_DUPLICATE annotations do not authorize transferring quantities
to accession-suffixed variants.

New plans freeze the actual captured HTML title,
`KOMODO - the Known Media Database`, and check it again during apply/verify.
Historical plans retain their old title only for deterministic reproduction;
the earlier title-repair handoff remains open. No historical references or
curation events were silently rewritten.
