# Methanogen Concentration Repair

Applied locally to three normalized media, not a claim of all-record completion.
The frozen [plan](plan.json) has 79 claim rows and pins the full before/after
records to fifteen inspected source captures. The [independent audit](audit.py)
checks source amounts, preparation boundaries, evidence coverage and inversion
of all permitted edits without using the mutator as its expected answer.

## Applied Changes

- TOGO M1038: correct 960 ml water input and six stock batch additions to liters;
  encode the separately instructed sulfide-stock dose as 8 ml/L. Withdraw seven
  unsupported mass-per-liter values, preserving the actual source batch masses
  in evidence-backed notes. Resazurin is 1 mg per batch, not the former 1 g/L.
- TOGO M1039: correct the base-medium input from 1 g/L to 1 L; attach evidence
  for the unchanged 3 g/L trimethylamine hydrochloride supplement and identify
  the referenced M257/JCM265 base. Restore the source preparation instructions.
- MediaDive J986: add the missing 3 g/L trimethylamine hydrochloride supplement.
  Replace 37 flattened copied base entries with a source-backed JCM265 reference.
  This does not exclude the base constituents: they remain in the linked base
  record. Their inherited concentrations are not recertified. JCM986 does not
  specify a numeric base input volume, so the TOGO-specific 1 L is not copied.

The applied audit counts nine quantity corrections, one new quantity slot,
44 withdrawals (including the 37 copied entries), 19 evidence entries, eight
references and three appended Codex events. Evidence includes batch masses,
preparation, conflicts and identity, not only concentrations. No organism-medium
growth associations, IDs, ontology mappings or existing conditions were changed.

[M1038](records/M1038.md) and [M1039](records/M1039.md) are new exact-path reports.
[J986](records/J986.md) supplements its existing report in
`20261007-mediadive-media-2500-3000`; it is not a second unique review.
The earlier [two-record source handoff](../20261008-togo-next-pair-handoff.md)
remains a historical, pre-application snapshot.

## Unresolved Evidence

TOGO M1038 labels trimethylamine stock **3%**; the same JCM985 recipe preserved
by MediaDive labels it **30%**. Both specify a 10 ml addition. The stock label
and conflict are preserved; neither a percentage basis nor a unified stock
strength is invented. The captured original JCM985 endpoint returned
`Nothing found.`; it is not cited as concentration verification.

The linked TOGO M190/M180/M431 and original JCM197/JCM187/JCM431 stocks were
inspected. Their listed water inputs and batch masses do not independently
establish final stock or receiving-medium volume. This repair leaves inline
compositions unexpanded. Retained gas `VARIABLE` placeholders remain unverified;
the stated gas ratio is not an absolute gas amount.

Next source-backed work is the flattened MediaDive J985 record, followed by the
referenced JCM265 base and FeCl2 stock. J985's API arithmetic uses 1011 ml despite
the separate per-liter sulfide instruction. JCM187 explicitly describes the HCl
input as 7.7 M, but local stock 3846 still has an unresolved 2.5 g/L HCl encoding.
Those records and their dependencies were not edited by this patch.

The additional [stock captures](followup-stock-sources.json) inspect JCM151,
TOGO M142 and MediaDive solution 3846. They establish that JCM265's referenced
trace-mineral batch contains the salts incorrectly summed into its main recipe;
they do not justify copying those stock masses into final-medium concentrations.
JCM151's KOH adjustment is unquantified. The fresh 3846 response still explicitly
lists a 10 ml input of `7.7 M, 25%` HCl alongside the conflicting provider-derived
2.5 g/L value. These are next-repair sources, not extra completed record reviews.

A bounded additional literature search located Cha, Min, Kim, Yim, Roh and Rhee
(2013), *Methanomethylovorans uponensis sp. nov., a methylotrophic methanogen
isolated from wetland sediment*, DOI
[10.1007/s10482-013-0020-4](https://link.springer.com/article/10.1007/s10482-013-0020-4).
The inspected publisher page supplies metadata and an abstract, but its methods
require subscription access. This lead does not resolve the 3%/30% recipe
conflict and was not inserted as recipe evidence. The
[JCM bibliography](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_ref?REF=9921) confirms
the citation; bibliography identity alone is not concentration support.

## Validation

Baseline schema, full-corpus strict validation and 73 focused tests pass.
The terminal post-apply [validation journal](validation.json) records passing
readback, no-op rerun, independent audit, schema, full-corpus strict validation
of 15,910 records, IDs, variant links and 92 focused tests. The fast suite passes
7,808 tests (16 skipped, 1,889 deselected). Product validation exits 0 with 91
warnings and 96,063 no-adapter skips. Global merge verification fails with 1,247
name conflicts and 3,287 fingerprint issues. The [freshness audit](merge-freshness.json)
also fails: 6,320 tracked versus 6,499 freshly generated recipes, with 3,724
tracked-only, 3,903 fresh-only, 1,710 changed shared and 886 unchanged paths.
Tracked derived YAML was not overwritten by this audit.

The installed citation validator exits 1: six API-title mismatches and five
snippet matches fail. Its separate text matcher passes 14 of 19 entries. Four
failures involve rendered JCM text spanning an HTML link/entity, while its cache
retains raw HTML; the fifth strips `[M257]` from a TOGO JSON excerpt before
matching. All literal snippets are independently checked against captured JSON
or rendered HTML. Original snippets, source titles and caches are not altered
to force a green gate. See [reference-validation.json](reference-validation.json).

### Merge Retention Failure

The [actual retention check](merge-retention.json) fails for M1038 and passes
for the other two singleton groups. M1038 is grouped with
`bacterial/TOGO_M781_Geobacter_Daltonii_Medium.yaml` and
`bacterial/modified_bn_medium_for_m08dhb.yaml`. Its fingerprint is identical
before and after this repair:
`330432bf555bfb3d42ef54b34eda236a3b0c2cc369fe73f9ebf19049d63b210b`.
Thus this patch did not introduce the grouping collision.

The canonical result takes the modified BN recipe's stocks and has no root
evidence or references. It loses M1038's seven complete stock entries and its
new curation event. The current fingerprint walker only extracts inline stock
components, so reference-only stocks contribute no identifying signature; the
multi-record merger retains canonical root provenance rather than all source
provenance. Preserving both recipes' stock lists in one asserted mixture would
also be scientifically wrong. This needs a formulation-aware grouping and
provenance fix, not an edit to generated YAML or removal of supported source
evidence. The check remains failed and publication is blocked by it.

Next integration priority: add a regression for this concrete three-record
collision and fix formulation grouping/provenance retention before publishing.
Preserve the pre-existing edits in the shared merge modules. Ingredient-set
similarity can identify candidates; it cannot by itself justify merging their
different stocks or concentrations. After that, continue the J985, FeCl2 and
JCM265 source-backed repairs and the remaining full-corpus review inventory.

These checks use the partial locked Python 3.13 environment, not full CI.
Publication remains gated. No commit, push, PR merge or branch deletion is
represented by this local repair.
