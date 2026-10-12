# Adversarial Review

## Findings Addressed In This Batch

1. M258 contained a false formulation, not merely a unit typo. A historical
   diff proves that alpha-methylbutyric acid was replaced by three LB
   constituents. The exact JCM266 and TOGO M258 sources support restoration
   of the acid in its fatty-acid stock. The unrelated LB nodes are removed,
   and the former supplier paragraph remains explicitly superseded.
2. M260's trace minerals were assigned to the wrong receiving preparation.
   The exact local seawater table places the 10 ml trace dose inside MJ(-N)
   seawater, whose own receiving-medium dose is 100 ml. The nested structure
   now preserves both doses without multiplying by assumed final volumes.
3. Both records conflated preparation water inputs with medium concentrations.
   All old quantity fields and source rows are accounted for. Milligram
   amounts remain milligrams in source-backed notes; no g/L rate is inferred
   from water additions. Rumen product description is not an extra dose.

The independent audit reconstructs the expected graph directly from source
rows rather than invoking the mutator. Seventy-two focused tests challenge
wrong amounts/forms, loss of the restored acid, reintroduced LB constituents,
invented acid grounding, erased history/provenance, duplicated evidence,
missing old claims, source-table ambiguity, assumed percentage basis,
centrifuge rpm substituted for g-force, stock flattening and concurrent edits.
The guarded fixture also verifies preview-only behavior, readback and no-op
reruns. All 72 pass; the wider 740-test selection passes too.

## Remaining Findings

- High priority: the same historical operation displaced acid/albumin names
  in other records. The read-only inventory identifies 120 remaining root-LB
  candidates after excluding M258 and already-restored M2366. They need their
  own exact sources, not a bulk restoration of historical numeric values.
- J266 is the immediate source-inspected follow-up. Its true 1 g yeast extract
  and erroneous 5 g/L LB yeast extract share a label. A name-only map is unsafe;
  use exact node paths and supplier provenance to distinguish them.
- Global merge/freshness failures and prior bibliography-title gaps remain
  outside the two applied repairs. Existing chemical groundings are not all
  recertified. Full-record completion and publication remain unproven.

This is a local adversarial self-review with mutation tests, not an independent
human or external PR approval. No external issue, PR, or review was submitted.
