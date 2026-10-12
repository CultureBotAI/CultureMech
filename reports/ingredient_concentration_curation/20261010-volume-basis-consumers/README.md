# Volume-Basis Consumer Findings

Status: **v3 applied locally with installed-code and wheel checks**.
The all-record ingredient goal remains incomplete. No published page, GitHub issue
or PR was changed. Historical isolated-preview receipts remain below.

## Findings

1. **Major: KGX drops `per_volume`.** The real curated `for_dsm_9468` stock dose
   is 50 mL per liter of prepared MS-medium before iron-stock addition. The
   exporter emits bare `50 ML_PER_L` text and a numeric pair without that basis.
2. **Major: ingredient tables omit the volume basis.** The quantity cell displays
   value and unit but not `per_volume`.
3. **Major: nested stock fields are omitted.** The solution template reads legacy
   `name` and `ingredients`, not schema-native `preferred_term`, `concentration`,
   `composition`, or nested `solutions`.
4. **Major: standalone stock composition is omitted.** Native solution records use
   `composition` and `preferred_term`, often without `record_kind`. Conversely,
   some curated `record_kind: SOLUTION` records retain MediaRecipe-shaped
   `ingredients`. Rendering must preserve both shapes and the stock's visible name.

The [reproduction](reproduction.json) pins the real input record and maintained
consumer files for findings 1-3. The fourth finding is also reproduced by the
new standalone-stock test in the [red run](red-v2.log).

## Applied Fix

The current v3 [patch](consumer-fix-v3.patch) preserves explicit bases in KGX text
and does not emit a bare arithmetic pair for such quantities. This intentionally
avoids treating a qualified carrier dose as an unqualified final concentration;
ordinary quantities without a basis retain their existing numeric export.

A shared escaped quantity template displays value, unit and basis together.
Stock rendering handles schema-native nested compositions and doses, retains
legacy field compatibility, and displays standalone solution composition.

## Verification

- [Red/green receipt](preview-validation-v3.json): original code has fifteen failures
  and three passes; isolated proposed code passes all eighteen new tests.
- The proposed code also passes 61 existing regression tests. One Koza TSV
  integration module is skipped because Koza is unavailable; this is not a TSV
  integration pass.
- The [v2 rendered-record check](render-preview.json) was insufficient: its test
  expectation repeated the same `record_kind` assumption as the template, omitting
  32 legacy stock quantities. Its 62-cell result must not be treated as complete
  composition coverage. The corrected [v3 check](render-preview-v3.json) counts
  actual root fields independently of the template's shape-selection rule and
  verifies all **94 quantity cells and fifteen basis cells** across seventeen
  records. It also checks each record's visible name. No visual browser or
  composition-graph inspection is claimed.
- Ruff passes on the changed Python files. The proposed tests were formatted
  using the repository Black configuration. Installed source hashes match v3.
- [Installed-code checks](../20261010-utex-j-das/preview.json) pass 115 guard,
  consumer and regression tests, with one unavailable Koza module skipped.
- [Actual renderer check](render-applied-v3.json) retains all 94 quantity cells
  and fifteen bases. [Wheel checks](../20261010-utex-j-das/wheel.json) verify the
  packaged templates, CLI, renderer, nested stock and concentration qualifier.

## Remaining Work

The code defects are fixed locally. Full generated-web coverage passes for all
15,910 normalized records. The full suite is running under the
[applied J/DAS batch](../20261010-utex-j-das/README.md). Real Koza TSV integration
and visual browser inspection remain unavailable. Publication readiness and source
completion are not implied by these passes.

The earlier v1/v2 patches and receipts are historical previews, not the current
application target. V2's stock-shape assumption is superseded by v3.
