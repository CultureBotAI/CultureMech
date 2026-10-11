# Remaining Ingredient Work

The active objective covers all 15,910 normalized records. Neither completion of
medium212 nor preparation of medium323 completes that objective. This checkpoint
does not apply recipes, add taxa-media associations, or publish GitHub changes.

## Medium212

The controlling proposal is `plan-v2.json`, SHA256
`496c0f734f231756ee97a80021429802c1af9136472b77798c9f2162ad4b2d4c`.
It contains 22 records, 21 proposed edits and one byte-exact no-op (S608).
The normalized corpus remains at SHA256
`3e69263bb0c82e782c51c5a994945630fbf3a3b9f685248e16d7daf3367f05fc`.
Use the terminal receipts, not a progress-log percentage, to decide which gates
finished. Do not overwrite the original preview, failed tests or source captures.

1. Verify the frozen `validation-preview.json` and its successor receipt hashes
   before proceeding. The fast tier finished with 13,255 passes, 16 skipped,
   2,243 deselected and two warnings; this is not a clean-CI or full-suite result.
2. Review and implement an explicit hash-bound application gate. The current
   builder deliberately rejects application and verification modes. Preserve
   exact before-record guards, path/ID checks, source hashes and no-op behavior;
   add regression tests before enabling writes.
3. Apply only the reviewed successor, then read every changed claim back from
   authoritative YAML and confirm the S608 no-op. Preserve the nine explicit
   nickel-form withdrawals without accepting the rejected MIM replacement ID.
4. Run schema, strict and reference checks on actual written records. BacDive's
   primary HTML needs the separately documented manual literal check; the
   production validator has no page adapter. No versioned DOI-PDF verification
   has been performed. Preserve this distinction in the results.
5. Run corpus strict/ID/product and merge-retention checks, followed by maintained
   merge verification and freshness gates. Record old failures separately from
   regressions. Do not hand-edit generated merge records.
6. Reconcile canonical reports and indexes, then recalculate cumulative edits,
   evidence additions and exact path coverage. Original and successor preview
   ledgers currently coexist with canonical reports for the same 22 paths; the
   duplicate-rejecting coverage command is not a current pass. Preserve the
   historical preview artifacts while making the canonical/current distinction
   explicit. Proposed additions are not applied additions.

## Medium323

Four exact records are prepared in `next-323-local-preparation.json`: K323,
D323, S599 and S6552. Five captured primary sources, one visually inspected PDF
page, twenty PDF table rows, twenty-one KOMODO rows, 62 old quantity fields and
nine existing evidence entries are documented. All eight baseline schema/strict
commands pass. This checkpoint has not created a guarded proposal or changed
recipes for this family.

Resolve the decisions in `next-323-source-inspection.json` and
`next-323-identity-inspection.json` before building its proposal:

- Use the original's explicit final-volume statement, not an additive-liquid
  assumption. Separate fatty-acid stock doses and resazurin reagent strength
  from final-medium solute concentrations.
- Preserve the conditional agar table/procedure discrepancy rather than
  silently choosing or averaging the quantities. Review physical-state metadata
  after removing copied agar from source formulations that do not list it.
- Restore each provider's own formulation, including KOMODO's nine nulls and
  its bicarbonate rather than the original's carbonate. Do not convert nulls to
  zero or transfer ontology IDs between different chemical forms.
- Correct unsupported stock percentages using explicit liquid inputs without
  inventing densities. Do not automatically declare provider-reported mass rates
  false; distinguish their scope from original batch doses.
- Preserve the nine supported S599 evidence entries and restore its omitted
  stock input. Adjudicate D-glucose using the source's full identity fields,
  including KOMODO's semi-unique name, not only its displayed label.

## Full Corpus

The last applied checkpoint remains 5,258 edited records and 35,769 added
evidence entries. Exact follow-up reports cover 11,802 paths, with 4,108 outside
them; a report does not certify every concentration. The 33 acid-name candidates,
separate 71-record queue and all other unresolved records remain in scope.

Local HEAD is `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; upstream was not
refreshed. The earlier outbound GitHub-write denial remains unresolved and must
not be retried through another route. Public-source read approval is separate
from repository publication authority. PR, remote issue, merge and branch-cleanup
work is not complete.
