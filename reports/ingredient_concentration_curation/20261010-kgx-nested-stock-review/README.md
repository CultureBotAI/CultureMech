# Adversarial KGX Stock Review

Local findings against the applied volume-basis consumer fix on 2026-10-10.
These are local issue records, not GitHub issues or publication claims.

## Applied Resolution

The v3 fix is now installed as part of the [eighteen-record follow-up](../20261010-next-utex-applied/README.md).
Installed regressions and a fresh installed-wheel smoke pass. The actual DAS
record emits both child-stock nodes and their scoped 25%/75% links. Stock
ingredient publications and volume qualifiers survive the installed exporter.
The evidence below describes the earlier isolated review. General snippet export,
enclosing-recipe stock-dose evidence, Koza TSV integration and a full-suite rerun
after installation remain outside the verified result.

## Findings

1. **High: nested component stocks disappear from KGX.** `transform()` and
   `nodes()` traverse only the first solutions list. In the current Dasycladales
   record, the DAS Macro Solution contains two component stocks, but neither
   child node nor parent-child edge is emitted. The HTML renderer handles these
   children; that does not establish KGX coverage.
2. **High: stock identity ignores preparation bases and nested composition.**
   `_solution_fingerprint()` hashes only flat component identity/value/unit.
   Different `per_volume` values, nested stock doses and nested component
   strengths therefore produce the same stock node ID and can collapse in a
   deduplicated graph.
3. **Medium: stock ingredient edges drop source references.**
   `solution_to_ingredient_edge()` omits the ingredient evidence publications
   that the direct-medium ingredient exporter preserves.

## Proposed Resolution

An isolated patch recursively traverses inline stocks, stops at explicit
standalone-record references, includes nested composition/doses and component
volume bases in synthetic stock identities, and retains stock ingredient
publications. Flat unqualified stock IDs remain unchanged. Receiving-medium
doses do not change stock identity. Inline cycles raise an explicit error.

Fourteen regression tests cover these cases. The original code fails eleven
and passes three. The proposed code passes all fourteen and 71 existing tests;
one Koza integration module is unavailable. The [final isolated receipt](validation-v3/preview-validation.json)
also passes Ruff, Black, actual-DAS two-node/two-edge checks and patch application
checking. The [patch](validation-v3/fix.patch) remains unapplied; no installed fix
or full-suite pass is claimed. The first combined test invocation failed
during collection because pytest scanned an inaccessible sibling under `/tmp`;
the corrected runner separates temporary and repository test collections. A
second run passed tests but stopped on test import ordering; the next run fixes
that formatting issue without changing the proposed exporter.

The [read-only corpus preview](corpus-preview.json) checks all 15,910 normalized
records and unchanged input hashes. In 175 affected records, per-record transforms
add 510 edges, including 152 nested-stock links, and add publications to 2,027
edges. Ninety-one stock occurrences change synthetic identity; 7,222 flat
unqualified stock occurrences preserve their existing IDs. These are occurrence
counts before cross-record graph deduplication, not unique published edges or
taxa-media associations. All emitted synthetic stock endpoints resolve to emitted
nodes, and every traversed stock dose retains its own value, unit and basis.

The ongoing full-suite run retains its original frozen code. This patch remains
unapplied until that run finishes. Full evidence snippets and enclosing-recipe
stock-dose evidence still lack a general KGX export representation; this patch
does not claim to implement those separate surfaces.
