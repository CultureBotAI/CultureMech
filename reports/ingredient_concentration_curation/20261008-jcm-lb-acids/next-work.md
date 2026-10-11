# Remaining Ingredient Work

J201 and J220 have now been repaired in
[the next batch](../20261008-jcm-albumin-inputs/README.md). Its
[handoff](../20261008-jcm-albumin-inputs/next-work.md) supersedes the immediate
albumin-candidate instructions below and retains 115 unchanged identity candidates.
The frozen 117-record and two-candidate contexts below remain historical; do not
reapply their J201/J220 baselines.

The all-record goal is active. Coverage remains 11,781 of 15,910 normalized paths,
with 4,129 outside follow-up reports and unresolved claims within covered records.
J266/J675/J1203 are applied; do not reuse their former baseline hashes.

## Frozen Queues

`next-lb-identity-context.json` retains 117 unchanged identity candidates:
76 acid-name and 41 albumin-name substitutions. Its SHA256 is
`4941fec87aab585f6456d3c5e5cda64a076a2ad32dde19926a280537c266d506`.
It links to the historical 120-record context without overwriting that snapshot.
The separate `remaining-queue.json` retains 71 unchanged M142-dependent records.
The queues are disjoint; neither count should be added to uncovered-path totals.

## Next Albumin Candidates

The complete current J201 and J220 YAMLs and four fetched response bodies were
read. `next-albumin-context.json` pins the two unchanged baselines and responses.
SHA256: `1d17c31b8c9f8b24725bfd290a9a096ff9db44c0ff6c3f12a142785929a761cb`.
This is source preparation, not an applied repair or completed review.

J220 is the next directly corroborated target:
`data/normalized_yaml/bacterial/JCM_J220_SC_MEDIUM.yaml`, `CultureMech:002582`.
Baseline SHA256:
`ee03836449e7e5c52d6d59e829aed749c6210e1a6c91e2eb502584cd759ffe54`.

- MediaDive solution 3888 has ten rows, all nonoptional. The original JCM220
  table matches those inputs. Its 1 L water input plus liquid doses does not
  establish a measured 1036 ml final volume.
- Remove only the false LB supplier nodes at root indices 6, 7 and 8. Restore
  bovine serum albumin fraction V as a 10 ml dose of the source-labeled 20%
  preparation. Do not infer the percentage basis or a chemical ID.
- Hemin is a 15 ml input of a source-labeled 0.1% solution in 0.05 N NaOH,
  not 15 g/L hemin. Preserve the normality label without converting to molarity.
- Glucose is 1 ml of source-labeled 50% preparation; cysteine is 10 ml of 10%
  preparation. The albumin, glucose and cysteine solutions are separately
  filtered and added aseptically. No pore size or percentage basis is given.
- The five main solid inputs are batch masses, not independently supported
  final g/L values. Retain pH 6.6 and source preparation order. Corn meal agar
  currently has an inherited agar grounding; preserving it is not recertifying
  that a formulated commercial product is chemically identical to pure agar.

J201 needs an explicit source-availability decision:
`data/normalized_yaml/bacterial/JCM_J201_BSK_MEDIUM.yaml`, `CultureMech:002564`.
Baseline SHA256:
`33ec2493040b89eb09fc14de4ab7af25b101f0112c13a03568f756cdfc4a635d`.

The official JCM201 endpoint currently returns "Nothing found." This response
is captured under `source_issues`, not accepted as evidence. MediaDive J201 is
available and has solution 3866, ten recipe rows, and the full preparation text.
It identifies 50 g bovine albumin fraction V (not LB), CMRL 1066 as a 100 ml
product input (not 100 g/L), and 900 ml water. Preparation additionally lists
200 ml of 7% gelatin and sterile rabbit serum at final 6%, without percentage
bases. Do not assume the reported 1000 ml API volume covers those later additions.
The false LB nodes are indices 2, 3 and 4. A source-specific provider-backed
repair can be considered with the unavailable original disclosed; do not claim
original-page corroboration or use J220's formulation as substitute evidence.

Before either application, create a new guarded preview from these baselines,
verify every claim, run baseline gates, independently audit the whole graph,
and attach snippets to the YAML. Preserve IDs, old annotations and history.

## Other Outstanding Work

The earlier reducing-stages context still contains M247, M272, M273 and M274
source-inspected baselines. The M273/M274 FeSO4 amount disagreement, sulfur and
maltodextrin distinction, and existing M345 variant link remain unresolved.
J151/M142 bibliography gaps remain in the recipe-reference-validator handoff.
Global merge/freshness checks remain separate from runtime target retention.

Publication remains incomplete. The issue #150 progress draft was not posted
after an external-disclosure rejection; no new authorization has arrived.
The historical LB issue draft also remains local. Do not bypass the rejection
through another channel. Local evidence-backed curation can continue.
