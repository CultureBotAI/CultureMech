# Remaining Ingredient Work

Follow-up: J266, J675 and J1203 have now been repaired in
[the next batch](../20261008-jcm-lb-acids/README.md). Its
[handoff](../20261008-jcm-lb-acids/next-work.md) supersedes the immediate J266
instructions and reduces the unchanged identity queue to 117. The frozen
120-record context below remains historical and must not be reapplied blindly.

The all-record goal is active and incomplete. Current follow-up coverage is
11,781 of 15,910 exact normalized paths, with 4,129 outside the report set.
Covered records can still contain unresolved claims. Two records are repaired
in this batch; the counts below are candidate inventories, not new reviews.

## Priority: Non-LB Identity Substitutions

The historical scan found 122 non-LB-name substitutions among 145 LB expansions:
80 acid-related and 42 albumin-related. M258 is repaired here, and M2366 already
has restored albumin in a previous stock-boundary repair. The remaining 120
current records retain the LB trio at the root. Ninety have prior follow-up
reports and 30 are outside coverage; this queue does not overlap the remaining
71-record M142 queue. Do not add these counts to the uncovered-record count.

Frozen context: `next-lb-identity-context.json`

SHA256:
`37528355c4266d9b419c40b6d3967b068e6acd7e5514c95086df2206f7a700a4`

The context includes 120 full current baselines, historical removed names,
exact current paths/IDs, six previously inspected TOGO/JCM captures, and a
fresh MediaDive J266 response. No candidate YAML was edited or counted as
scientifically complete. Other candidates' individual source recipes have
not yet been fetched by this follow-up. See the local-only issue draft for
the shared matching failure and required regression cases.

## Immediate Candidate: J266

Current target:
`data/normalized_yaml/archaea/JCM_J266_METHANOMICROBIUM_MOBILE_MEDIUM.yaml`

ID: `CultureMech:002623`

Baseline SHA256:
`26396a258d205586c0c5ecdf9d47d6a12e57e990601b1038866fc93d07d86bbf`

All 38 ingredients/quantity fields, four existing preparation steps and seven
history events were read. There are no existing solution descriptors. The
record has the same erroneous LB expansion as M258, plus flattened fatty-acid,
trace-mineral and vitamin compositions. Root pH 7.5 is the fatty-acid stock's
pH, whereas the main preparation explicitly specifies 6.5.

Fresh source: `https://mediadive.dsmz.de/rest/medium/J266`

Capture SHA256:
`83e78d50d0292fd28ad47e76b9f45204090825f59c6e83313a7c97bf8cd7fa79`

The entire fresh source was inspected. Its linked original is JCM266. Source
solution IDs are `[3953, 3954, 3804, 3861]`, with row counts `[18, 5, 13, 11]`.
Their roles are main medium, fatty-acid stock, trace minerals and vitamins.
Every row has `optional: 0`; rumen fluid alone has `condition: " clarified"`,
a material qualifier to preserve, not a reason to reject the entire graph.

Important mapping constraints:

- Genuine yeast extract at `ingredients[9]` is 1 g in the main recipe. The
  erroneous LB yeast extract at `ingredients[17]` is a separate 5 g/L node
  with supplier provenance. Remove only the reviewed LB nodes at indices
  16-18. Do not use a single preferred-term-to-node map for these duplicates.
- The removed alpha-methylbutyric acid belongs in stock 3954 at source input
  0.5 g. MediaDive reports stock `g_l: 25`; that is not a final-medium rate.
  The original JCM source supplies 20 ml stock water, not an independently
  measured final stock volume. Do not restore the old numeric field blindly.
- Four current nodes combine main and trace-stock scopes: NaCl, MgSO4
  heptahydrate, CaCl2 dihydrate and FeSO4 heptahydrate. Preserve old annotations
  as historical context while separating each source occurrence and amount.
- Restore missing main water (660 ml), fatty-stock water (20 ml), trace water
  (1 L) and vitamin water (1 L) in their own scopes. The main stock doses are
  trace minerals 10 ml, vitamins 10 ml and fatty acids 20 ml. Rumen fluid is a
  300 ml input with separately described extraction, not an extra 300 ml
  unquantified product dose.
- Trace-stock pH 6.5 then 7.0 and fatty-stock pH 7.5 must not remain root
  preparation steps. Document the metadata pH 7.5 disagreement explicitly.
  Preserve overnight, two separately autoclaved 5% reducing preparations,
  N2 context and 200 kPa H2-CO2 instructions without inferring percentage
  basis, dose, solvent volume, or dissolved-gas concentrations.
- Keep evidence from actual API/original captures, not from the newly repaired
  M258 record. Preserve stable ID and append-only history. Do not invent
  chemical IDs for the restored acid or use an unverified old ID as proof.

Before applying, recheck baseline hashes, select a new pinned context, preview
all claims, run baseline gates and an independent graph/identity audit, and
test duplicate-label disambiguation and all-target write guards.

## Other Outstanding Work

`remaining-queue.json` preserves the 71 unchanged M142-dependent records.
The prior `../20261008-reducing-stages/next-six-context.json` still holds
source-inspected M247, M272, M273 and M274 baselines. Its M258/M260 baselines
are now superseded and must not be reapplied. The prior handoff records the
M273/M274 tenfold FeSO4 disagreement, sulfur/maltodextrin variant distinction
and existing M345 pH-variant link; those remain unresolved.

J151/M142 bibliography-title gaps remain described in
`../20261008-recipe-reference-validator/next-work.md`. Global merge verification
and generated-data freshness still fail; no tracked merged YAML was patched.
Legacy chemical identities are not all recertified.

The issue #150 progress draft remains unposted after the external-disclosure
rejection; no new approval has arrived. This batch also has a local-only issue
draft about LB identity substitutions. Do not post either through another
channel to bypass the rejection. Commit/push/PR/merge/branch cleanup remains
unfinished. Local evidence-backed curation can continue.
