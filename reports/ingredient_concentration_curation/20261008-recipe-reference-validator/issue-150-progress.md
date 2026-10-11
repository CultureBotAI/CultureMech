Local, **uncommitted** follow-up on concentration curation and its audit trail:

The cumulative source-specific audit now passes after fixing two stale-history
tests. Their follow-up list stopped before later applied stock/variant repairs.
The tests now share the cumulative auditor's registry and independently validate
each repair before checking historical claims. Recomputing a hash cannot approve
a forged ingredient or rewritten history; those negative tests fail as intended.

Current cumulative accounting is 5,134 edited records, 1,404 quantity corrections,
585 stock-node relocations and 419 unsupported quantity slots withdrawn with
source-backed context retained. The 31,168 evidence entries also cover batch,
preparation and relationship claims; they are **not** a count of verified
final-medium concentrations or completion of this issue.

This latest pass corrects only two evidence excerpts, adding no concentration
values. The official-source reference-validator repair is documented in #571:
all 206 excerpts and 19 titles in the seven-record cohort now pass. The remaining
91 M142-dependent records are still unapplied. Original JCM670 has been inspected
for M689: four stock additions are explicitly per liter, whereas the import
stores them as g/L. That repair is still pending, including its stock definitions
and the separate treatment of batch masses versus final concentrations.

The full all-record review, remaining source/data conflicts, publication gates,
and requested PR/merge workflow remain open. This update does not close #150.
