# Medium323 Revised Drafts

**Historical draft, superseded by the [applied successor](../20261009-medium323/README.md).**
The successor also corrects this draft's cysteine identity disposition: the
same source's SEED table supports retaining the pre-existing L-specific links.
The historical claims and receipts below describe the draft, not current records.

**Unapplied.** These four source-specific proposals are not application authority
and add nothing to applied totals or canonical report coverage. All four
authoritative records remain byte-exact to their recorded baselines.

| Source | Proposed Record | Scope |
| --- | --- | --- |
| KOMODO323 | [K323](K323.proposed.yaml) | Restore the exact source component set and rates; withdraw copied amounts and unrelated LB nodes; preserve unquantified inputs. |
| MediaDive solution599 | [S599](S599.proposed.yaml) | Correct water units, restore the evidenced stock addition and fill evidence gaps. |
| MediaDive solution6552 | [S6552](S6552.proposed.yaml) | Replace erroneous percentages with source input volumes; retain explicit provider stock mass rates. |
| DSMZ323 | [D323](D323.proposed.yaml) | Restore the fatty-acid stock boundary, missing component and water; correct storage action and retain the conditional agar conflict. |

Each proposal has a sibling `.diff`. [draft.json](draft.json) pins the original
and proposed bytes, source captures, quantity dispositions and lineage. This
version fixes the unrelated trimming of an existing agar note identified in the
[first draft](../20261009-medium323-draft/README.md); old note text is preserved
as an exact prefix.

## Verification

[Final independent checks](final-quantity-reference-checks.json) account for
**62 old quantity fields** and pass **79 production reference checks**, with
network fallback disabled. All four proposals pass closed-schema validation.
The checker tests component sets, quantity bases, source-row ownership,
preservation of earlier evidence/history, stock doses and unrelated metadata.

[Adversarial mutation checks](mutation-checks.json) reject **18 of 18** rehashed
forgeries, including incorrect amounts/bases, swapped source rows, changed
chemical identities, duplicate components, altered old notes/history and
fabricated old-quantity dispositions. These test the read-only draft checker,
not an application writer. They do not replace a full inverse-diff audit.

## Still Required

- Complete independent inversion of all proposed field changes and a guarded,
  mutation-tested writer with repeat-no-op, exact-path and concurrent-change checks.
- Replace draft-only history wording with complete field-level dispositions.
- Review source-specific relationships without merging distinct formulations.
- Preserve explicit limitations: KOMODO's required physical state is unverified;
  its cysteine lacks L stereochemistry; MIM still supplies unsupported cysteine
  and sodium-resazurin identities; the conditional agar sources disagree;
  solution599's generic glucose mapping is not newly certified as exact D-glucose.
- Inspect final presentation and run actual-written schema, strict, reference,
  corpus and regression gates before counting the batch as applied.

No missing DOI, author or year was invented. The preparatory scripts remain in
`/tmp/ingredient-media-20261007/`: `draft_medium323.py`,
`audit_medium323_draft.py` and `attack_medium323_draft.py`. Their products are
review artifacts only; the all-record ingredient goal remains open.
