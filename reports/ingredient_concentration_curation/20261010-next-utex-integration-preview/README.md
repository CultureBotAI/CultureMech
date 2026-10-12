# Next UTEX Integration Preview

**Superseded by the [v3 packet](v3/README.md).** This original packet predates
five snippet corrections. V2 included an incompatible parser; v3 leaves that
parser isolated. Do not install this original packet.

The [validated packet](validation.json) combines three reviewed, unapplied recipe
batches with the isolated KGX nested-stock fix and cumulative-audit dispatches.
It changes no authoritative YAML or installed code.

- Eighteen distinct records and 67 claim rows: seven soil/seawater, five organic
  media (v2 history correction), and six prepared-medium blends.
- Sixty-nine proposed evidence entries, fourteen unsupported quantity slots
  removed, twelve preparation-volume qualifications and nine optional variants.
- Three real-schema dry runs: seven, five and six pending records, zero writes.
- All three audit-dispatch paths reproduce the reviewed counters. The combined
  nine-file patch passes application checking; original and proposed code hashes
  and the exact future applied-plan wrappers are pinned.

The first integration attempt stopped on an older receipt format before changing
anything. [Its disposition](attempt-01.json) is retained. The successful rerun
performs new real-schema dry runs and preserves the historical guard receipts.

Do not install the patch while the J/DAS full-suite run is live. First obtain its
terminal result and seal its unchanged inputs. Then recheck packet/code/record
hashes, install through the patch tool, apply each guarded plan and verify
readback/no-op behavior. Installed regressions, source checks, cumulative totals,
canonical reports, indexes and corpus/derived-output validation remain required.
No GitHub publication, complete scientific review or full-suite pass is claimed.
