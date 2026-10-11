# Original-Recipe Agar Follow-up

Read-only source investigation on 2026-10-07 (America/Los_Angeles), after the
water corrections. No agar quantity or evidence was changed by this follow-up.
It supplements the three agar leads in [remaining-handoff.json](remaining-handoff.json).

The complete text of each one-page official DSMZ PDF was inspected through the
web reader. Screenshot requests did not expose images in this tool session, so
this is text inspection, not a claimed visual review. New local PDF captures
and byte hashes have not been made for this follow-up.

## Exact Sources

| Solution | Original recipe | Exact amount excerpt, page 1 | Separate water excerpt, page 1 | Preparation excerpt, page 1 |
| --- | --- | --- | --- | --- |
| 856, Main sol. 426 | [426. ORGANIC MEDIUM 79](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium426.pdf) | `Agar 15.0 g` | `Distilled water 1000.0 ml` | `Adjust pH to 7.8.` |
| 1387, Main sol. 656 | [656. YEAST-STARCH-AGAR(B)](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium656.pdf) | `Agar 15.0 g` | `Distilled water 1000.0 ml` | `Adjust pH to 7.4.` |
| 1389, Main sol. 658 | [658. HICKEY-TRESNER-AGAR](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium658.pdf) | `Agar 15.0 g` | `Distilled water 1000.0 ml` | `Adjust pH to 7.2.` |

Source type: official culture-collection recipe. Discovery mode: cross-reference
from the corresponding inspected MediaDive medium response's `medium.link`.
The responses identify these exact solution IDs, names and preparation steps.
Each PDF carries a 2007 copyright notice, not an independently established
publication year; individual authors and publication year remain unknown.

## Decision

All three original recipes support a literal 15 g agar input per listed recipe.
Their solution API rows instead contain `amount: 20`, `unit: g`, `g_l: 15`.
The complete conflicting rows, source hashes, current target hashes and locators
are retained in the handoff; the original PDFs support the lower input amount,
not a reconciliation of the API's internal fields.

None of the inspected PDFs explicitly instructs make-up to a final 1 L. The
separate water input does not establish a measured final volume. Consequently,
this source investigation does not newly verify the existing `15 G_PER_L` or
authorize changing it to `20 G_PER_L`. The current concentration enum also has
no mass-only grams value; a later guarded curation must represent the supported
batch input in notes/evidence or resolve its volume basis without inventing a
unit. Do not add a concentration claim solely to make the arithmetic gate pass.

Before applying an agar follow-up, inspect the complete current targets and
their prior ingredient evidence, capture/verify these exact source documents,
and review related receiving-medium copies separately. Preserve the conflicting
API provenance and existing history. These are source leads, not three newly
completed record reviews or additional curation changes.
