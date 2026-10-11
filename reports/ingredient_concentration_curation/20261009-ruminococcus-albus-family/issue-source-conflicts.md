# Medium436 Source Conflicts And Remaining Gaps

Local review issue only. No GitHub issue was created.

1. DSMZ436 lists batch masses but not an explicit defensible final-volume
   denominator. Its mineral stock percentages have no stated w/v, w/w or v/v
   basis. Keep these literal statements; provider `g_l` is separate evidence,
   not a retrospective interpretation of the original. Water additions and
   stock input volumes do not prove final volume.
2. The visually inspected DSMZ PDF prints `CaCl2 x 7 H2O`; JCM675 specifies
   dihydrate. TOGO M2636 has a seven-water component name and a hexahydrate
   ontology label in the same source row. Preserve source-specific labels and
   the disagreement, without inferred molecular weights or interchangeability.
3. KOMODO3017 names `Fatty acid mixture (medium 436)` but its own Instructions
   URL points to DSMZ3017. The applied repair withdraws the unverified equivalence,
   restores four named ingredients and leaves all four provider amounts null.
   An empty imported formula must not be filled from a different source.
4. KOMODO3037 remains inaccessible (HTTP 403). Earlier catalog mappings are
   not recipe evidence. Its unchanged empty formulation is unresolved, not
   verified complete; do not bypass access controls or infer stock quantities.
5. TOGO M2636's old solution4674 link identifies a different formulation:
   dibasic rather than monobasic phosphate, different ammonium/magnesium/calcium
   amounts and a different calcium hydrate. The receiving record now has its
   own source-backed inline composition, without changing solution4674. Its six previously
   supported quantities remain unchanged. Its false placeholder and prefixed
   reference title still need a separate provenance-preserving repair.
6. J675 is an already curated comparison, reverified against byte-identical
   sources with 42 reference checks. Do not count its earlier 40 evidence
   entries again. No new curation event is warranted by that comparison alone.

Evidence is pinned in the preceding batch's `next-436-context-approved.json`,
`next-436-inspection.json`, `next-436-J675-comparison.json` and
`next-436-row-decisions.json`, and in this batch's claim ledgers. Upstream
ambiguities remain open even when representation and schema checks pass.
