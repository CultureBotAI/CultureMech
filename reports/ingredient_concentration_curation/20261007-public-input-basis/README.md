# P7/P10 Input-Basis Curation

Applied scope: two exact normalized records, not completion of the all-record
ingredient objective. This work is local and uncommitted. See `validation.json`
for terminal results of all three baseline jobs and twenty post-apply jobs.

## Sources and Decisions

The full tables, preparation text, metadata, main-volume controls and stock-volume
badges were parsed from the inspected public pages. Both pages explicitly say
these user-contributed media are not curated or tested and lack a valid reference.
They are evidence for their reported recipes, not independent journal validation
or growth evidence. No DOI, authorship, stock percent basis or final volume was
invented. Bibliography includes title, page author/creator, publication year,
source type, discovery mode, access date and capture hash.

| Source | Capture SHA256 | Page Metadata |
| --- | --- | --- |
| [P7](https://mediadive.dsmz.de/medium/P7) | `ce4a93ee29dbf3008a4bfcedd4962718c0bd6feb95b38b2d5dc5951ed2a29dcd` | Lorenz; published/modified 2023-11-02 |
| [P10](https://mediadive.dsmz.de/medium/P10) | `f57ebb12ab9b45cdb3a746764fcd9e0a228e1dab2346b2ade67db95b477456ad` | Alvarez Maqueda Rafael Alejandro Uriel, Cleto Gutierrez Miriam Rebeka; published 2024-08-05, modified 2024-08-29 |

Accessed 2026-10-07. P7 was rechecked through the web reader. P10 was retrieved
again using curl after the web reader failed; the new HTTP-success capture is
byte-identical to the previously inspected capture. The frozen source inventory
and earlier P7/P10 handoff are unchanged historical artifacts.

### P7

`CultureMech:010437`,
`data/normalized_yaml/bacterial/n27_rhodospirillaceae_medium_modified.yaml`:

- Preserve eight direct and seven SL-6 solute g/L values, with explicit evidence
  for the dataset-reported rate, not a measured final-medium concentration.
- Correct ethanol and three stock additions from per-liter rates to the stated
  batch volumes: 0.5, 5, 0.4 and 1 ml become 0.0005, 0.005, 0.0004 and 0.001 L.
  Unit L denotes batch input, not L/L. No dilution calculation uses the main
  1000 ml UI control as a proven final volume.
- Remove the unsupported 1 g/L iron-citrate conversion from an unspecified
  0.1% basis. Preserve the literal stock strength and solvent with evidence.
- Remove the unsupported 0.1 g/L B12 final-stock concentration. Preserve the
  10 mg mass in notes and represent the explicitly stated 100 ml water input as
  0.1 L. The schema has no mass-only concentration unit.
- Restore four water nodes: 1 L main distilled-water input, 1 L SL-6
  distilled-water input, 0.1 L B12 water input and unquantified iron-stock water.
  H2O does not establish distilled-water purity for the last two stocks.
- Replace the stale main-volume description and correct the SL-6 dose notes.
  Preserve pH, state, preparation, mappings, identifiers and prior history.

The extra listed liquid inputs total 6.9 ml; this does not establish 1006.9 ml
final medium. The main-water input and dataset's rates remain distinct claims.
SL-6's separate badge declares 1000 ml final stock, but its preparation has no
makeup instruction. No stock constituent is flattened into the main ingredients.

### P10

`CultureMech:010430`,
`data/normalized_yaml/bacterial/bekisolidmedium_hydrogenovibrio_crunogenus_quimiolitotrofo.yaml`:

- Preserve seven direct dataset-reported g/L rates and seven stock rates.
- Support copper sulfate pentahydrate from preparation substep 3.6 and the
  stock's 1000 ml final-volume badge. Its table has a blank mass-unit cell;
  the explicit preparation mass, not the blank cell, supports 0.05 g/L stock.
- Remove the `VARIABLE` trace-dose assertion. The HTML says `trace` without
  a unit or quantity; neither zero, a fixed dose nor a variable range is known.
  Keep the trace stock and its composition; do not calculate final-medium doses.
- Restore the explicit 1 L distilled-water preparation input, not a final-volume
  makeup amount. Update root and stock notes to preserve that distinction.
- Document the unresolved salts/proportions of the phosphate-buffer mixture.
  Do not infer chemical identity or molarity from the reported 4 g/L rate.

## Audit and Guards

The revised [frozen plan](plan.json) covers all 36 existing concentration claims,
five new water nodes and ten context edits: 51 report rows across exactly two
per-record reports. Twenty-nine existing rates are unchanged with added evidence.
Seven existing quantity slots are corrected: four dose-basis conversions and
three removals. Four new batch-volume slots and one unquantified solvent node
are separate categories.

Independent inversion of the applied records verifies 39 new evidence entries, two
bibliography entries and two appended curation events. Every edit has a scoped
PURL and exact snippet in YAML; one root evidence entry groups multiple stock
claims using separate excerpts and locators. Evidence counts are not counts of
independent scientific confirmations or taxa-media associations.

The first preview incorrectly labeled two H2O inputs as distilled water.
Manual adversarial inspection caught this before application. That rejected
preview is preserved as `rejected-preview-water-label.json`, is not applied,
and is not an additional reviewed-record report. The revised plan uses `Water`
for those nodes; the independent audit explicitly checks both labels.

The mutator defaults to preview and refuses source-hash, full-table, metadata,
volume-basis, formulation, identity, frozen-plan or concurrent-target drift.
Both records are checked before writes. Serialization is round-trip checked and
closed-schema validated. Reapplication must be a no-op. The common guarded
transaction now accepts explicit reviewer hooks; existing P2/P8 behavior and
frozen output must remain identical.

No generated merge, raw record, schema, ontology mapping, variant, new ID or
growth association is edited. Source-local solution anchors are not treated as
global solution accessions.

## Verification

Baseline/post-edit full strict scans pass all 15,910 normalized records. Both
targets pass baseline/post open-schema validation and preview closed-schema
validation. Revised guard tests pass 71 cases with two applied-record checks
deselected; the post-apply focused suite passes **823 tests**, including all
28 P7/P10 tests, with zero errors, failures or skips. Apply/readback/no-op,
independent whole-record inversion, ID validation and P2/P3/P6/P8 source readbacks
pass. These checks use isolated Python 3.11, not maintained Python 3.13 or CI.
The full suite was not rerun. Black and Ruff pass for the changed Python files.
The separate [snippet readback](snippet-readback.json) uses a standard-library
HTML parser independent of the mutator and checks all 39 new evidence snippets
against the hash-pinned captures. Table cells are whitespace-normalized and
joined; an empty unit cell retains an empty separator. This text check does not
substitute for the scoped scientific decisions above.

Product validation fails because `oaklib` is missing. Both reference checks fail
because `linkml-reference-validator` cannot be spawned. Manual source/table
verification is recorded above, not reported as an automated reference pass.
The [actual-group retention check](merge-retention.json) passes both singleton
groups, including ingredients, stocks, preparation, physical state, pH, evidence,
references, notes and curation history. Water membership changes are included.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. [Freshness](merge-freshness.json) fails with 6,320 tracked
and 6,492 fresh records: 3,719 only tracked, 3,891 only fresh, 1,645 changed and
956 unchanged. Regeneration was temporary; no generated merges were published.
`git diff --check` passes. The driver completed with all jobs terminal; its
orchestration exit code does not override the individual failing gates.

The [cumulative semantic audit](../20261007-diff-audit-after-public-input-basis.json)
verifies 4,855 edited records, 28,167 new evidence entries, 4,889 new references,
4,861 curation events and 1,173 quantity/unit corrections. The
[exact-path coverage inventory](../20261007-followup-coverage-after-public-input-basis.json)
verifies 8,108 follow-up reports, leaving 7,802 normalized records outside those
reports. Report presence does not prove all scientific claims are resolved.

## Remaining Scope

The source ambiguities above remain explicit, not numerically resolved. P1,
P4, P5 and P9 still need public-medium follow-up. The remaining normalized corpus,
unresolved findings in earlier reports, importer defects, formulation-aware
merge/evidence retention, validation dependencies and publication workflow remain
part of the full objective.
