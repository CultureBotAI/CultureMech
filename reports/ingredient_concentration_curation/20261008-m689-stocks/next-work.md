# Next Ingredient Work

Later follow-up: [M809, M823, M853 and M975 were repaired](../20261008-basal-makeup/README.md).
Their applied plans preserve basal makeup separately from later supplements.
The successor queue has 86 unchanged records. The M809 notes below describe
the pre-repair state and are retained as historical inspection context.

The remaining 90 M142-dependent baselines are hash-checked in
`remaining-queue.json`, not counted as completed reviews. Original source captures
remain in `../20261008-j261-variant/next-m142-dependents-context.json` and
`next-m142-originals.json`; extra stock captures remain in the original
`../20261008-m142-nested-traces/remaining-m142-context.json`.

## M809 Preparation Boundary

Inspected the complete baseline for
`data/normalized_yaml/bacterial/TOGO_M809_Modified_Haloanaerobium_Medium.yaml`,
ID `CultureMech:010221`, and rechecked its current SHA256:
`9c41c18581599575447f3992f9520775d1cd854bb2f23803f66b8432d3f33d61`.
It has not been edited or counted as reviewed in this pass.

Official source:
[JCM779](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=779), frozen raw SHA256
`839f4955a74001e505d79b399aa2f028430abcc1f2186f2e333408e12468b7c3`.
The source was also inspected through the web tool during this pass.

The one-liter makeup applies to the basal preparation, BEFORE the later 25 ml
glucose and 25 ml thioglycolate-ascorbate additions. It is not independently a
final receiving-medium volume, and the TOGO 1 L water row is not an absolute
water input: the original table has no fixed water row at that stage.

The existing water quantity 26 g/L combines incompatible 1 L and 25 ml stages.
Preserve the original annotation/history but separate those scopes. Restore
sodium thioglycolate and sodium ascorbate to the reducing-stock composition
(0.5 g each plus 25 ml water). That stock is freshly prepared and filtered;
its 25 ml water input does not independently establish final stock volume.

Vitamin and trace-mineral additions belong to the basal makeup stage; glucose
and reducer additions occur after autoclaving/cooling. The glucose stock's
10% label has no explicit percentage basis. Do not convert it to a mass rate
or assume a precise final 1.05 L after pH adjustment and heating. Consider a
source-faithful basal preparation boundary rather than asserting basal rates
as final-medium rates. Expand only M190 vitamins and M142 trace minerals.

Before applying: reread the live record and original sources, preview the entire
formulation graph, independently account for every old quantity and source row,
attach source excerpts to each change, validate, and preserve history.

## Other Outstanding Work

The prior bibliography-title mismatches for J151 and M142 are documented in
`../20261008-recipe-reference-validator/next-work.md`. The larger corpus coverage
gaps and global merge/freshness issues remain. Do not merge or publish merely
because a local cohort passes schema and source checks.

The issue #150 progress comment in this folder was not posted. The approval
checker rejected publication of local results; do not retry or route around the
rejection without new approval or evidence satisfying the permission requirement.
This does not block continued local ingredient review.
