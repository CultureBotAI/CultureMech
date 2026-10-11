# Next: JCM261 / TOGO M253 Variant

Triage only. No recipe or relationship edits for this next cohort have been
applied. Do not count the capture as review completion.

## Verified Inputs

`next-j261-context.json` SHA256:
`da25a5f492f0fcc0bf1fdeca5f4cb0c80a261b7387c2c9acb83efdcc7b31b53c`.

It pins the current full YAML and hashes for J261/M253 and their J151/M142
dependencies. The three newly fetched sources returned HTTP 200:

- MediaDive J261: `https://mediadive.dsmz.de/rest/medium/J261`.
  SHA256 `976a7183a60a978dcab0be755793652e5a85b547875573c55098508079902558`.
- TOGO M253:
  `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M253`.
  SHA256 `038e5565979fd1fc8325fa66627d090643ac5fae4c50afe7f529dd27ca115b4b`.
- JCM261: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=261`.
  SHA256 `2f64b31105f997668cbc06f195426434ae928ac75f0f79d322b2b9ee16be5e7d`.

J151/M142/JCM151 source captures are inherited with original metadata from the
prior nine-source capture, not represented as newly fetched. Browser access to
the three new URLs failed; direct HTTP retrieval succeeded and was inspected.

## Evidence Changes The Next Action

JCM261 is a deliberate variant, not an exact source duplicate of JCM151.
The official instruction and MediaDive `data.solutions[0].steps[0].step`
explicitly specify final yeast extract 2.0 g/L, final peptone 2.0 g/L,
Na2S2O3 pentahydrate 1.0 g/L, sulfur omission and pH 7.0. These final rates
do not need an inferred final-volume denominator.

The local J261 has 26 ingredients copied from J151, including sulfur and
unmodified yeast/peptone rates, and lacks the thiosulfate addition. Its
preparation text already states the variant correctly. `parent_media.path`
points to the bacterial J151 path, whereas the current exact tracked parent
is under archaea. Both parent/child relationships currently say
`SOURCE_DUPLICATE`, based on the copied flattened composition.

M253 has eight direct ingredients and two empty stock references. Its source
API has ten main rows and no inline stock definitions:

| Source row | Item | Source amount |
| --- | --- | --- |
| 0 | Resazurin | 1 mg per batch |
| 1 | Na2S nonahydrate | 0.5 g per batch |
| 2 | Yeast extract (BD-Difco) | 2 g in table; final 2 g/L in variant instruction |
| 3 | Na2S2O3 pentahydrate | 1 g/L |
| 4 | Bacto peptone (BD-Difco) | 2 g in table; final 2 g/L in variant instruction |
| 5 | Citric acid | 5 mg per batch |
| 6 | Salt base solution | 1 L, explicitly references M142 |
| 7 | Trace minerals | 10 ml, explicitly references M142 |
| 8 | H2SO4 | No fixed dose |
| 9 | N2 | No fixed dose |

M253 `comments[0]` copies J151 preparation, including sulfur addition and
pH 6.5, but `comments[2]` explicitly overrides it with sulfur omission and
pH 7.0. `comments[1]` is empty. Preserve the conflict/override distinction;
do not execute the inherited sulfur step or silently certify both pH values.

## Repair Requirements

1. Re-read current hashes and source captures before editing. J151/M142 now
   have separately scoped stocks from the applied six-record repair.
2. Replace copied J261 ingredients with a supported base-medium reference
   plus explicit variant modifications, or another established representation
   that retains base evidence without double counting. Inspect prior
   base-reference repairs and merge retention behavior before choosing.
   A base reference plus ordinary additive yeast/peptone rows is insufficient:
   these final rates override the parent's amounts, not add to them. A fully
   source-mapped formulation may represent that distinction more faithfully.
3. Preserve annotations/history for retained and removed copied nodes in the
   audited change history; do not lose the explicit sulfur-omission decision.
4. Correct the source-duplicate relationship and exact parent path in both
   directions with source snippets. `DERIVED_FROM` may fit the combined
   concentration/substitution/pH changes better than a single narrower enum;
   confirm against repository conventions. No new IDs are needed.
5. For M253, the three explicit final rates can be evidenced directly from
   its variant paragraph and the original JCM261 source. The remaining
   batch masses do not become final g/L by association. Restore the two
   stock boundaries using the explicitly referenced M142 stock sections.
6. Model sulfide's separate preparation without inventing a percent basis or
   dose, and preserve the gas/acid quantity uncertainty.
7. Preview, independently audit all old/new claims and source-row scope,
   guard apply, validate, verify no-op, and update cumulative hash-chain
   accounting. Existing J261 canonical report should link to a follow-up;
   M253 would add one canonical curation report, not a duplicate.

The ignored/hidden-inclusive report search found J261's current curation
report in `20261007-mediadive-media-2000-2500`; both records also have
historical full-corpus audit reports. No new canonical M253 curation report
was present in that search. The next repair must not treat report presence
as proof that these variant corrections are already applied.

After the variant repair, consider the larger dependency inventory in
`m142-dependent-stock-candidates.json`: 103 tracked records, 107 named stock
reference nodes, 99 records outside follow-up coverage. Each receiving source
must verify its own stock identity, dose, units and preparation stage; the
shared M142 reference alone does not prove formulation identity. This inventory
can organize a larger batch without converting candidate matches into evidence.
