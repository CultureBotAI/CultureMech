# Adversarial Self-Review

This is local self-review using an independent checker and mutation tests,
not a separate human reviewer or a posted GitHub PR review.

## Reviewed Failure Modes

- Stock versus medium scope: M199's 17 g/L NaCl and 2.5 mg/L KI belong to
  its salt-base stock. Tests reject the old KI unit, inherited parent-stock
  amounts, and flattening these nodes into main ingredients.
- Unsupported final volume: M206/M207's 990 ml water and 10 ml stock are
  inputs, not a final-volume statement. Tests reject inferred main mass rates,
  per-liter stock doses and replacement of water input with a final liter.
- Separate sulfide: every 0.5 g row is a receiving-batch contribution to a
  separately prepared solution. Tests reject invented stock concentrations,
  addition volumes and altered sulfide masses. M207 cannot inherit a 5% label
  from M206; its original preparation is checked independently.
- Titration and atmosphere: tests reject fixed gas quantities, loss of M206's
  stated acid normality, transfer of that normality to M207, changed gas
  instructions, incorrect pressure and substitution of autoclaving for the
  source filtration instruction. No unspecified filtration pore size is added.
- Cross-reference membership: only the named M142 trace stock is expanded.
  Tests reject added or missing members and applying its pH instructions to
  the receiving medium. M199's unmodified salt-base rows are independently
  compared with the referenced parent stock, excluding its two explicit overrides.
- Evidence integrity: wrong or ambiguous original table amounts stop preview.
  Tests reject invented excerpts, bibliography years, duplicate evidence,
  missing old-quantity claims, altered chemical annotations and rewritten
  history. Every changed claim has a literal source excerpt in the YAML.

All 86 new tests passed before application. The checker does not invoke the
mutator's formulation builder. It independently reconstructs expected source
membership, quantity kind, old-node lineage and preparation boundaries, then
checks exact evidence attachments and append-only history. All 63 old quantity
fields and 105 source rows are accounted for. Additional excerpts sharing a
reference are retained with explicit field locators rather than duplicate
reference keys in the same evidence list.

## Application And Limits

The guarded path requires the pinned commit, exact tracked path/ID, full
before/after hashes, immutable source captures and schema validity. All targets
are checked before any write. Tests reject a concurrent edit, symlink target
or forged last-record claim set without changing earlier records. Application,
readback and no-op checks all pass.

The full normalized inventory is checked against git-tracked paths using an
ignored-file-inclusive traversal. Only the three reviewed YAMLs differ from
this cohort's baseline. Report uniqueness is also checked with ignored files
included. Four metadata indexes change only root ingredient/solution counts
for these three IDs. Unrelated worktree changes are retained.

Source batch masses are preserved but final concentrations remain unverified
where no final volume is supplied. Sulfide percentage basis and addition volume
remain unknown. Existing ontology annotations and growth claims are not
recertified. A shared trace stock alone does not justify a parent/variant link
between these media, and no such link is added.

Scoped generated-output retention does not recertify all merged outputs or
make failing corpus-wide publication gates pass. Fast/focused tests are not a
clean-CI full-suite run. No external issue comment, PR review, merge or branch
cleanup is claimed by this self-review.
