# DSMZ 1399: Stock Boundary And Drop-Unit Conflict

Status: **applied locally and verified**. The receiving recipe has one new
[per-record review](medium.md); the [standalone stock follow-up](stock-followup.md)
extends its earlier report without creating a duplicate coverage target. This
repairs two records but adds only one unique reviewed/edited record to the totals.
The all-record objective remains incomplete.

## Exact Targets

- Receiving recipe: [DSMZ 1399](../../../data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml),
  `CultureMech:000252`, pre-repair SHA256
  `fd3f20aadf89a81037ca0aa3b83c0791da7f930c27aa55b694a74a75db2911d5`.
- Related standalone stock: [Total Salts](../../../data/normalized_yaml/bacterial/mediadive_2838_Total_Salts.yaml),
  `CultureMech:012117`, source `mediadive.solution:2838`, pre-repair SHA256
  `d8bd7590843678515ad808708d60fa995e0b8ec789a3b1f2c34ea8b6edfe27da`.
  Its earlier [source-pass report](../20261007-mediadive-solutions-2000-2500/records/bacterial/mediadive_2838_Total_Salts.yaml.md)
  retained the iron attribute/drop context as unresolved.

## Inspected Evidence

The original [DSMZ 1399 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1399.pdf)
was retrieved on 2026-10-07 and its single page was visually inspected. The
[official MediaDive medium response](https://mediadive.dsmz.de/rest/medium/1399)
identifies DSMZ 1399, the same title, and that exact PDF URL. It explicitly links
main solution 2837 to stock 2838. No name-only or cross-medium match was used.

| Capture | SHA256 |
| --- | --- |
| Original DSMZ PDF | `c76a8a1d8c4e5da897b13caa810918454efc9258b0b78a433aa14032c3ed8d3e` |
| MediaDive medium/1399 JSON | `692c728d98d3ba582110c22429da51aaa29ff7d6ea11d9fd8fe8a42c2a978e85` |

Sources were discovered through the existing record's source accession/URL.
Source types are an official culture-collection recipe and a DSMZ dataset;
individual authors and publication year were not established. The PDF's 2012
copyright notice alone is not used as a publication date.

## Findings Before Repair

1. The PDF's iron row states `FeCl3 x 6 H2O (0,5 %) 9 drops`, under the
   **Total Salts** heading. MediaDive corroborates compound 82, attribute
   `0,5 %`, amount `9`, unit `drops`, at
   `$.data.solutions[1].recipe[7]`. The receiving record instead has
   `ingredients[11].concentration = {value: '9', unit: G_PER_L}`. That is not
   supported by either inspected source.
2. Seven preceding salt concentrations were also flattened into receiving-medium
   `ingredients[4:11]`. The primary recipe uses 666 mL of a separately prepared
   Total Salts stock; the API gives its exact stock ID and dose at
   `$.data.solutions[0].recipe[3]`. Its main-medium volume is 1000 mL. Values
   reported within stock 2838 are not automatically concentrations in medium 1399.
3. The standalone stock retains `9 VARIABLE` without the drop unit or the
   iron-solution attribute on that ingredient. Its new mass/water evidence does
   not resolve this iron row. The schema has no drop unit, and neither source
   specifies drop volume or an unambiguous percentage basis. No mL, g/L, or
   molarity conversion is justified.

## Applied Correction

The [hash-pinned plan](plan.json) restores eight flattened entries into
`solutions[0].composition`, retaining every original chemical form, identifier,
and older provenance entry. Seven numeric salt concentrations are unchanged but
now scoped to the correct stock. The iron row loses its unsupported `9 G_PER_L`
in the receiving recipe and `9 VARIABLE` in the standalone stock. Both preserve
the exact nine-drop dose and `0,5 %` source attribute in evidence-backed notes;
drop volume, percentage basis, and final iron concentration remain unasserted.

Three missing source volume additions are represented explicitly: 0.666 L of
Total Salts per receiving batch, 0.333 L main-batch water, and 1 L stock-batch
water. The separate main-medium make-up instruction remains unchanged. Four
existing main-medium concentrations gain evidence; the peptone manufacturer and
agar's solid-medium condition are retained. Sixteen new evidence entries, four
bibliography entries, and two append-only curation events were added.

The maintained [guarded repair](../../../scripts/repair_dsmz1399_stock_boundary.py)
defaults to preview. It pins source and before/result hashes, checks exact
source/formulation/ingredient identities, validates both target classes, and
preflights both records before either write. Existing plans and prior source-pass
reports remain historical snapshots. Later verification accepts the stock's
successor only through the explicit hash-linked plan and still checks all eight
previously accepted stock quantities and snippets.

## Verification

- Two-record apply and read-back passed; all sixteen new snippets match the
  pinned source response. A second apply changed zero records.
- Open-schema baseline/post checks passed for both records. Closed-schema
  validation passed all 15,910 normalized records with zero errors. The ID gate
  also passed, using the isolated Python 3.11 environment.
- The full relevant regression selection passed **215 tests**, including source,
  identity, amount, stock-dose and strength guards; both-record preflight;
  idempotence; and explicit successor checks that reject damage to older claims.
- The [independent diff audit](../20261007-diff-audit-after-1399.json), implemented
  [here](audit_diff.py), inverts the stock relocation and checks prior metadata,
  quantities, and provenance. It reconciles the cumulative worktree without
  treating relocation as eight unrelated ingredient deletions/additions.
- Regenerating the medium's actual fingerprint group through the maintained
  merger [preserved all ingredients, solutions, evidence, and references](merge-retention.json).
  Full merge gates still report 1,247 name conflicts and 3,286 fingerprint issues.
  The [freshness counts](merge-freshness.json) match the previous drift counts;
  these global failures have not been fixed. No generated files were hand-edited
  or copied into the worktree.
- The reference validator remains unavailable (`linkml-reference-validator`
  cannot be spawned). The ontology-product check is not counted as a pass when
  its `oaklib` adapters cannot load. Source checks are separate from these tools.

The iron dose is represented faithfully in notes because the schema has no drop
unit. The standalone legacy placeholder remains explicitly unsupported. Neither
is silently turned into a guessed concentration or a claim of full-corpus review.

The maintained importer also requires regression coverage: its PDF fallback and
`_normalize_unit` currently default unknown units to `G_PER_L`, while some amount
paths assume a per-liter denominator. Inspection establishes this current risk,
not the exact historical execution path that produced the existing record.

Searches included ignored/hidden normalized YAML. Exact accession/PDF/stock-ID
matches returned the two targets above. Other similarly named records inspected
identify DSMZ 1125, KOMODO 1125, or DSMZ 1400; their names do not justify applying
the 1399 recipe. This finding does not claim a corpus-wide equivalence search.
