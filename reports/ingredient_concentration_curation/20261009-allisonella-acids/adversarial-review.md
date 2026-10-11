# Allisonella Adversarial Review

This is a local review of the two-record batch, not a GitHub review or an
all-record completion statement. The independent audit derives expected nodes
from source tables rather than calling the mutator to obtain expected values.

## Findings Addressed

1. Flattened fatty-acid stock entries were presented as medium g/L. Restore
   all seven liquid stock inputs, including missing DL-2-methylbutyric acid,
   and separate the 3.10 ml stock dose. Every new input is mutation-tested.
2. Resazurin stock strength and receiving dose were conflated. Keep 0.1% w/v
   and 0.50 ml separate; tests reject swapping strength units or dosing basis.
3. False LB constituents must not cause removal of genuine same-named recipe
   inputs. Only the three supplier-tagged LB nodes are removed. Tests retain
   genuine yeast extract, Trypticase and NaCl.
4. DSMZ and KOMODO quantities, chemical forms and null values are not
   interchangeable. Preserve each source projection, do not invent density,
   and archive copied chemical annotations without transferring them to
   less-specific KOMODO labels. Tests reject reintroducing those annotations.
5. A PDF heading and dose row share the fatty-acid label. The extractor requires
   a unique quantity row ending in a source unit; regression tests reject
   duplicate quantity rows and avoid treating the heading as a dose.
6. Archiving an entire replaced list element through a field-only accessor
   fails. The complete original KOMODO ingredient list is instead archived
   once through its named field, preserving all displaced annotations.
7. Matching copied signatures do not establish exact duplicate identity.
   Both reciprocal links are evidence-backed `DERIVED_FROM`, with exact
   path/ID/name checks and no new organism-growth assertion.
8. A plausible number with a fabricated snippet or omitted source node could
   pass schema validation. Tests corrupt all 43 source/input quantities and
   challenge omission, extra nodes, grounding, snippets, duplicate evidence,
   history, claims, lineage, metadata and family relationships.

The dedicated suite passes 80 tests. The broader focused suite passes 526.
Apply/readback/no-op and independent applied audit all pass. Baseline and
post-edit record schema/strict/reference checks pass. Later broad results are
reported in the batch validation receipt; do not infer a clean global merge
gate from this cohort's passing checks.

## Still Open

See [source limitations](issue-source-limits.md). The scope does not recertify
every retained chemical grounding. Nor does it resolve the wider acid queue's
[21 stale exact family references](../20261009-middlebrook-linked/issue-stale-family-paths.md),
the separate M142 queue, outside-report coverage, stale generated merges or
publication. These remain explicit work rather than silent exclusions.
