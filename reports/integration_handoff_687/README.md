# CultureMech → MIM → KGM handoff, 2026-11-19

Source-intake accounting is verified. **Final integration is pending**: the
active MIM campaign is not proven to cover the accepted v3 intake, and no final
certified supported/withheld campaign SSSOM has been selected. This report does
not authorize a release, mapping installation or merge.

Tracking: [CultureMech #687](https://github.com/CultureBotAI/CultureMech/issues/687).
Consumer reconciliation is owned by
[KGM #1879](https://github.com/Knowledge-Graph-Hub/kg-microbe/issues/1879), on the
existing dependent #1833 branch. Its native source review must consume the
integration evidence and bind the same evidence in `manifest.inputs`. An
unbound sidecar or a success flag cannot satisfy that gate.

## Exact accepted inputs

| Role | Revision or SHA256 |
|---|---|
| CultureMech producer | `6f1b1d18a5528532fa239400bd73c1a040fb78a0` |
| v3 `bundle/manifest.json` | `ede822e6424433644ae25f363cb5bfb88b154b453c1e954185ecc2c6cb3c829f` |
| Producer source archive | `a4538497c868191ad19eb4cddcfb0f416e2a6d4e700953600ba0e8f3d8c64687` |
| Source handoff JSON | `c011b4b6a2d4210c7ed0fb9dd0456f7e436e156f7aedb55dd6f4af5a12b34bfb` |
| Original queue | `dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca` |
| Source coverage summary | `512990326bf661668ffc4cb44f2448ceef7e59c3123d8d6a52e4a9c1b17e8e1c` |
| MIM reviewed consumer | `53b7237e941534ce53493fce705ef954d143f90d` |
| Prepared `intake.json` | `6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7` |
| Final binding review | `b548dbcb6271f59083693da632a2318bfbbf868b5b2a208e86a77bb4ae77fa4a` |
| Native `reviewed-intake.json` | `9fd1da62fad47c3b5b7290ea3f9fc2b687b23fc8c98e8dc926e1460572c3f1d8` |
| Transport `package.json` | `cf7e1f1434ab2dfc61922a47ae785f474c06cf4f88fbfd76d09e6b55993f70c8` |

The reviewed-intake manifest and package manifest are different artifacts.
Native acceptance must bind the former and its reviewed source products; the
transport manifest additionally protects delivery. All seven source products
and the reviewed binding/SSSOM companions are pinned in
[coverage-acceptance.json](coverage-acceptance.json).

Current CultureMech main was independently read as
`13c710defa9eddf17dab531f40b915e449f68663`. The normalized corpus is byte-identical
to the accepted producer, but three Python dependencies differ:
`src/culturemech/fetch/komodo_fetcher.py`,
`src/culturemech/fetch/komodo_web_fetcher.py`, and
`src/culturemech/import/komodo_importer.py`. Verification of this accepted
snapshot therefore uses the archived producer, never the current-main verifier.
Neither the accepted bundle nor its manifest was regenerated or restamped.

## Coverage and its limits

| Measurement | Count |
|---|---:|
| Source records | 15,915 |
| Base direct occurrences | 209,330 |
| Additional positive variant targets | 454 |
| Total positive inventory occurrences | 209,784 |
| Context-only mentions | 163 |
| Held mentions | 138 |
| Normalized inventory groups | 2,565 |

There are 492 change events and 617 descriptor rows. Actions are retained:
271 ADD, 38 REMOVE, 125 REPLACE, 8 SET_AMOUNT and 50 SET_CONCENTRATION events.
The two sides of every replacement remain distinct. Counts of grouped binding
cases below must not be read as counts of these change events.

| Binding disposition | Cases | Positive inventory occurrences | Context-only mentions | Held mentions |
|---|---:|---:|---:|---:|
| Supported identity | 623 | 16,732 | 30 | 2 |
| Withheld binding | 4,384 | 193,052 | 133 | 136 |
| Total | 5,007 | 209,784 | 163 | 138 |

The supported identity lane's two held mentions remain nonpositive: CO2 retains
an operation/headspace hold and defibrinated sheep blood retains a quantity
hold. Identity support does not resolve those source assertions. The native
review retains 174 authored scientific holds and 4,210 canonical-eligibility
withholds. The 797 eligible cases have authored dispositions; independent
scientific cross-reviews retain their actual sample limits.

Every consumer must retain source paths, recipe IDs, component and variant
coordinates, descriptor role, source hash, action, stage, quantity basis and
evidence. Do not collapse positive, context-only, held and withheld lanes.
`counts_as_presence` means inventory inclusion, including explicit zero targets;
it never independently grants a medium-presence or growth edge. Removed and
displaced ingredients are not positive additions. Variant operations are not
applied to parent recipes by this handoff. Literal batch amounts do not become
final concentrations; unspecified percentage bases remain unspecified.

The 2,565 groups are resolver/inventory groups, not a proof of complete chemical
identity deduplication. Name equivalence, case counts and occurrence counts are
different measures. Referenced stocks are not expanded into every medium;
remaining prose-only claims are outside structured extraction.

## Reproduce the accounting

Set `CM_V3` to the preserved v3 delivery directory and `MIM_PACKAGE` to the
preserved MIM verification package. Verify the independent pins above before
using those directories. The historical native commands and current replay
receipts are retained in the durable checkpoint; run them against their
archived producer/consumer, not an updated source tree.

After native verification, from this checkout's maintained Python environment:

```bash
python scripts/report_integration_handoff.py \
  --bundle "$CM_V3/bundle" \
  --intake "$MIM_PACKAGE/consumer/.temp/1453/candidate-v3-6f1b1d18a5" \
  --reviewed "$MIM_PACKAGE/consumer/.temp/1453/reviewed-intake-final-v3-r2" \
  --source-sha256 ede822e6424433644ae25f363cb5bfb88b154b453c1e954185ecc2c6cb3c829f \
  --intake-sha256 6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7 \
  --reviewed-sha256 9fd1da62fad47c3b5b7290ea3f9fc2b687b23fc8c98e8dc926e1460572c3f1d8 \
  --output .temp/new-coverage-report.json
```

The output must be new. This helper checks pins, exported product bytes,
partition equality and separate lane totals; it neither re-resolves identities
nor replaces native scientific/source validation. Its result always leaves
integrated-release readiness false. The accepted input need not be regenerated.

## Remaining acceptance gates

1. Preserve MIM's active application and frozen inputs. Its historical selected
   scope is 1,330 CM IDs / 2,911 occurrences plus 507 KGM IDs / 5,740 occurrences
   from the historical KGM source. Those inputs do not prove accepted v3 coverage.
   After verification, the MIM owner must reconcile via a native-bound successor.
2. In KGM #1879, consume the exact v3 intake and current selected KGM evidence
   through native source review, with identical `manifest.inputs` bindings.
   Reconcile literal files/rows and all source coordinates, including withheld
   and retained obligations. Test old intake, missing/unbound evidence, stale
   pins, duplicate/lost rows, wrong lanes and changed provenance.
3. Await certified supported and withheld SSSOM, exact release commit/archive,
   scientific review, dispositions, registry/lifecycle and required scoped
   companions. The packaged historical 1,739-supported / 1,275-withheld SSSOM
   snapshot is unchanged and is not the active campaign's final release.
4. Run KGM's existing candidate workflow against independently accepted pins;
   retain quarantine and independently supported claims. Require an actual
   final native-artifact canary before pinned transforms. Review paired supported
   mappings and unified candidate; do not install either alone.
5. Validate affected transforms, source-finalization receipts, consumed-input
   fingerprints, graph and archive outputs. Refresh CultureMech's packaged MIM
   index only in a separate reviewed change from the selected full MIM commit.
   Preserve this pre-curation snapshot.
6. Obtain separate owner merge/publication approval. No merge or final mapping
   publication is included in this handoff.

[NTA #792](https://github.com/CultureBotAI/CultureMech/issues/792) remains a separate
source-descriptor repair. Its conflicting source binding stays WITHHOLD in the
accepted intake. This branch changes no scientific recipes, MIM records,
production mappings or active campaign inputs.

## Bounded verifier repairs

[CM #801](https://github.com/CultureBotAI/CultureMech/issues/801) records acceptance
of empty/missing/duplicate headers in zero-row v3 products. The current verifier
now checks all five TSV schemas even when there are no rows; parity tests bind
them to the native writer.

[CM #802](https://github.com/CultureBotAI/CultureMech/issues/802) records product
drift after the original product hash pass. The current verifier rechecks the
seven products after the input/dependency pass. This detects persistent changes
across that window; it is not a filesystem lock or protection against malicious
change-and-restore races.

The 22 regression cases failed before these repairs. The focused bundle/variant
selection then passed 85 tests; the coverage helper passed nine tests. Exact
commands, exits, stream hashes, runtime limitations and final required fast-test
result are bound in the checkpoint. The current verifier changes are for future
snapshots and do not replace archived verification of accepted v3.
