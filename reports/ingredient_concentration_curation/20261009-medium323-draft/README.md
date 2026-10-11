# Medium323 Source-Specific Drafts

**Superseded by the [second draft](../20261009-medium323-draft-v2/README.md).**
A later preservation check found that this version trimmed existing whitespace
from the DSMZ agar note. The failed `quantity-reference-checks-v3.json` is retained;
the successor preserves the original note verbatim. Neither draft was applied.
The results below describe this historical first version.

**Unapplied.** These four full-record drafts are not application authority and
are excluded from applied totals and canonical report coverage. Authoritative
YAML remains byte-exact to the recorded baselines.

| Source | Draft | Proposed Changes |
| --- | --- | --- |
| KOMODO323 | [K323](K323.proposed.yaml) | Restore the exact 21-row KOMODO formulation; correct its stated rates; withdraw copied DSMZ amounts, carbonate, agar and unrelated LB nodes; preserve null amounts and both source water rows. |
| MediaDive solution599 | [S599](S599.proposed.yaml) | Correct water units to ml/L; restore the 1.4 ml solution6552 addition with root evidence; add missing evidence; preserve nine earlier entries; correct the bibliography title and remove the importer placeholder. |
| MediaDive solution6552 | [S6552](S6552.proposed.yaml) | Replace 290% and 140% assertions with the exact 5.8 ml and 2.8 ml stock inputs; support the provider-reported stock mass rates and remove the placeholder. |
| DSMZ323 | [D323](D323.proposed.yaml) | Restore the fatty-acid stock boundary and missing constituent/dose/water; remove unrelated LB nodes; correct HEAT to STORE; retain the conditional agar source conflict. |

Each draft has a sibling `.diff`. [draft.json](draft.json) includes pinned
before/proposed bytes, the original quantity dispositions, lineage, source
hashes and explicit unresolved issues. No DOI, author or publication year was
invented. Original evidence and earlier history are preserved.

## Checks

The independent [quantity and reference checks](quantity-reference-checks-v2.json)
pass on all four drafts. They account for all **62 old quantity fields**, compare
complete source component sets and stage-specific quantities, verify preservation
of previous evidence/history and run **79 production reference checks** against
the five pinned official captures with network fallback disabled. All four
drafts pass the current closed-schema validator.

The first check receipt is retained as failed: its absolute tolerance was tighter
than the source-reported resazurin precision. The second check rounds the explicit
dilution calculation to that reported precision; no draft quantity was changed
to make it pass.

These checks are not a full inverse-diff audit or mutation-tested write path.
They do not prove source completeness merely because schema/reference checks
pass. The original DSMZ323 PDF page was visually reinspected, including the
1002 ml volume, 0.1% w/v resazurin input, fatty-acid stock and conditional agar.

## Remaining Decisions

- The required KOMODO `SOLID_AGAR` classification is retained but explicitly
  unverified. Its own table has no agar; the linked DSMZ formulation differs.
- KOMODO cysteine lacks explicit L stereochemistry. Local L-specific links
  are withdrawn in the draft, but the pinned MIM resolver still supplies them.
- Sodium-resazurin exact identity remains an upstream MIM issue even after
  local primary/secondary mapping withdrawal.
- The DSMZ table-derived agar rate is 11.976 g/L while preparation says
  12.00 g/L. The drafts preserve the conditional source conflict, not an average.
- S599's generic glucose secondary mapping is retained as a stated limitation,
  not newly certified as exact D-glucose identity.
- Full inverse-diff/mutation tests, source-specific relationship review,
  presentation review and explicit guarded application remain necessary.
  Draft-only wording in the proposed history must be replaced before application.

Builder: `/tmp/ingredient-media-20261007/draft_medium323.py`.
Independent checker: `/tmp/ingredient-media-20261007/audit_medium323_draft.py`.
These are preparatory artifacts for the unchanged four-record scope; the
all-record ingredient goal remains open.
