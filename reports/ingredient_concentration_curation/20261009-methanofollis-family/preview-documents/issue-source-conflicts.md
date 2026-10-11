# Medium161 Source Conflicts And Remaining Evidence Gaps

Local issue record only; no GitHub issue has been created.

| Finding | Evidence | Disposition |
| --- | --- | --- |
| Nominal final volume and liquid sum disagree | DSMZ161 states 1001 ml; its liquid rows sum to 1001.5 ml | Preserve nominal-volume calculation and explicit discrepancy. Do not substitute an inferred additive denominator. |
| Provider and original formulations differ | KOMODO161 gives source-specific rates, nulls and 300.00 g/L clarified fluid; DSMZ161 gives staged ingredients and 300 ml fluid | Preserve distinct source formulations and DERIVED_FROM provenance, not SOURCE_DUPLICATE. |
| Provider aerobic flag conflicts with original anoxic preparation | KOMODO161 metadata and DSMZ161 preparation paragraph | Record disagreement; no new biological cultivation or growth assertion. |
| Original mineral/vitamin stock final volumes unstated | DSMZ161 stock sections list water inputs, not final-volume makeup | Keep batch mass inputs in notes; do not invent stock concentrations. Provider-reported stock rates remain provider-qualified. |
| Titrant quantities unspecified | Mineral pH adjustment with KOH and fatty-acid adjustment with NaOH | Add source-backed unquantified inputs; never assign zero or a customary dose. |
| Clarified-fluid stock has no exact normalized record accession | Full filesystem and git inventory includes ignored files; source 2618 has nested references only | Preserve source name, dose and procedure. No fabricated ID or new standalone record. |
| Thiamine form differs from copied grounding | KOMODO explicitly names dihydrate; old grounding is anhydrous | Withdraw incompatible identity annotations with evidence; resolver candidate is documented separately, not newly asserted. |

Source receipts and literal snippets are in the
[preparation context](../20261009-rumen-bacteria-family/next-161-context-approved.json)
and [reviewed decisions](../20261009-rumen-bacteria-family/next-161-row-decisions-reviewed.json).
These limitations are not resolved by passing schema or reference validators.
Global merge verification/freshness and the remaining corpus work stay open.
