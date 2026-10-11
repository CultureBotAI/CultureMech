# Remaining Ingredient Work

Subsequent status: M199, M206 and M207 were applied in
[the filtered-media follow-up](../20261008-filtered-sulfide-media/README.md).
Its handoff supersedes this queue count. The M199 notes below remain the
historical pre-application assessment.

The all-record goal is not complete. Current follow-up reports cover 11,769
of 15,910 exact normalized paths, leaving 4,141 outside that report set. A
report is not proof that all its scientific claims are resolved.

`remaining-queue.json` contains 83 hash-checked, unchanged records from the
M142-dependent queue. M196, M197 and M198 have now been applied and removed
from that pending queue. Their earlier frozen context remains unchanged as
historical evidence; the current `plan.json` and application report document
the applied state.

## Next Candidate

M199/JCM206 is an unresolved lead at
`data/normalized_yaml/bacterial/togo_medium_m199.yaml`. Read the entire current
record and refresh its sources before proposing changes. Earlier source
inspection identified these boundaries, not a completed review:

- Main inputs include prepared salt base and M142 trace minerals. Do not
  inherit the complete M142 main medium or infer final volume from salt base.
- Its salt base modifies JCM151 with explicit final stock rates of 17 g/L
  NaCl and 2.5 mg/L KI. Preserve those specific rates separately from inherited
  unqualified batch masses and from final-medium rates.
- Sulfur sterilization, sulfide preparation, atmosphere, titration and
  post-inoculation pressure need separate source-scoped decisions. The 5%
  sulfide label alone does not specify a percentage basis.

Earlier source leads are in
`../20261008-j261-variant/next-m142-dependents-context.json`,
`../20261008-j261-variant/next-m142-originals.json` and
`../20261008-m142-nested-traces/remaining-m142-context.json`.
Source captures and plausible boundaries are not authorization to skip the
preview, fresh evidence, baseline checks or independent audit.

## Other Outstanding Work

J151 and M142 bibliography-title mismatches remain documented in
`../20261008-recipe-reference-validator/next-work.md`. The metadata generator's
top-level-only hierarchy flag limitation remains documented in
`../20261008-basal-makeup/adversarial-review.md`.

Global merge verification and freshness still fail. No tracked merged YAML
was rewritten by this repair, and scoped retention is not global publication
readiness. The requested commit, push, PR, issues, fixes, merge and branch
cleanup workflow remains unfinished.

The issue #150 progress draft remains unposted after its external-disclosure
approval rejection. Do not retry through a different channel without new
authorization. Local ingredient curation can continue.
