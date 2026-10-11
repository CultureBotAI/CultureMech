# M1308 Nested Stock Evidence Follow-up

Status: **applied locally; partial resolution, not a completed medium review**.
This revisits `CultureMech:007843`, already counted in the initial JCM batch.
It adds no new unique reviewed or edited record to the cumulative inventory.
The existing [per-record report](../20261007-jcm/TOGO_M1308_Methylotroph_Medium.md)
retains the first-pass history and links to this follow-up.

## Applied Scope

The [pinned plan](plan.json) records twelve evidence-only claims: two components
of `solutions[1]` (Se/W) and ten components of `solutions[2]` (trace vitamins).
All existing `MG_PER_L` quantities remain unchanged. Each ingredient gains its
own official recipe URL, exact source JSON row, locator, arithmetic, source hash,
and an exact additional excerpt establishing the receiving recipe's stock link.
Three bibliography entries and one append-only `codex` curation event were added.
No ingredient identity, membership, dose, variant, organism, or growth claim changed.

## Source Scope

The original [JCM 1219 recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219)
links its Se/W stock to [JCM 284](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284)
and its vitamin stock to [JCM 197](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197).
Those original pages and exact ingredient forms/amounts were inspected again.
The [MediaDive J1219 response](https://mediadive.dsmz.de/rest/medium/J1219)
identifies that original recipe and explicitly links 10 mL each of stocks
[3981](https://mediadive.dsmz.de/rest/solution/3981) and
[3861](https://mediadive.dsmz.de/rest/solution/3861). Their embedded ingredient
rows agree with the separately captured stock responses.

The stock responses explicitly declare `g_l` values and a 1000 mL stock volume.
The existing mg/L values equal `g_l * 1000`, also checked against stock mg amounts
and the provider-declared volume. Evidence is scoped to those declared stock
concentrations, not to a measured final volume or a concentration after dilution
into M1308. The original pages alone did not establish this denominator in the
first pass; the newly linked API evidence is additional, not retroactive proof
that the earlier unsupported decision was wrong. All three response hashes are
pinned in the plan. Source organization, type, discovery mode, and access date
are recorded; individual authors and publication year were not supplied.

## Verification And Remaining Work

- Exact tracked path, stable record ID, TOGO/JCM lineage, local baseline hash,
  source hashes, stock links/doses, ingredient order/forms, units, quantities,
  and pre-existing evidence are guarded before mutation.
- Closed-schema baseline, proposed, and read-back checks passed as MediaRecipe.
- All twelve persisted snippets matched their captured sources. A second apply
  changed nothing and added no duplicate evidence or history.
- Focused original-JCM and follow-up tests: **26 passed**, including rejection
  of source/lineage/dose/form/amount drift, preview-only default, and no-op reruns.
- Six main-medium mass-denominator gaps and both inline variants remain open.
  Existing batch doses and main-medium concentrations were not recalculated.
- Merge gates and the final corpus/regression checks are recorded in the
  cumulative [status](../README.md). No generated files were hand-edited.

The full merge gates were rerun after this follow-up. `verify-merges` still
reports 1,247 canonical-name conflicts and 3,286 fingerprint issues in the
untouched derived corpus. The [freshness result](merge-freshness.json) retains
the earlier drift counts: 6,320 tracked / 6,461 generated, 3,723 only tracked,
3,864 only generated, 1,469 changed, and 1,128 unchanged. These failures are not
claimed fixed. A separate scan of all tracked normalized inputs identified
M1308's actual fingerprint group and regenerated that group through the maintained
merger. Its [retention check](merge-retention.json) confirms exact preservation
of the curated solutions, doses, twelve stock evidence entries, and bibliography.

The guarded implementation is
[`repair_jcm_m1308_stock_evidence.py`](../../../scripts/repair_jcm_m1308_stock_evidence.py).
It defaults to preview, requires the three hash-pinned source captures, and
requires explicit `--apply` against its saved plan. It does not copy another
CultureMech record's evidence or infer equivalence from a stock name alone.
