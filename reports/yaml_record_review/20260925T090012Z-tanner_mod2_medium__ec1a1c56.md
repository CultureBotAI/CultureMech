# YAML Record Review: tanner_mod2_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tanner_mod2_medium__ec1a1c56.yaml`
- Started UTC: 2026-09-25T08:59:29Z
- Finished UTC: 2026-09-25T09:00:12Z
- Verdict: needs curation

## Target

Generated merged record `CultureMech:002404` for `tanner_mod2_medium`, with
`mediadive.medium:J1238`, fingerprint
`ec1a1c5658ec8bfd450151c4a83fea069ad35c7e85143c906b40022f9627da76`, and one
merged source, `tanner_mod2_medium`.

## Validation

- LinkML schema: passed.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM/MediaDive medium J1238, `TANNER MOD2
MEDIUM`. A source-equivalent TOGO M1332 record exists locally as
`data/merge_yaml/merged/TANNER_MOD2_MEDIUM.yaml`; it points to the same JCM 1238
page but did not merge with the MediaDive record because both imports flatten
solution additions differently.

## Evidence

JCM 1238 prints the base recipe as NaCl, NH4Cl, KCl, KH2PO4, MgSO4 x 7 H2O,
CaCl2 x 2 H2O, MOPS, yeast extract, 10 ml SL-9 mineral solution, L-cysteine
HCl x H2O, resazurin, and 990 ml water. The source then instructs curators to
adjust pH 7.0, autoclave under N2, and add sterile anaerobic stocks per liter:
30 ml 1 M fructose, 10 ml trace vitamins, 1 ml vitamin B12 solution, and 1 ml
0.01% Coenzyme M solution.

JCM 1238 also prints the full one-liter SL-9 stock recipe, including 20 mg
amounts for CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, Na2SeO4, and
Na2WO4 x 2 H2O; 1 mg ZnSO4 x 7 H2O; and gram-scale nitrilotriacetic acid,
MnSO4 x n H2O, Fe(NH4)2(SO4)2 x 6 H2O, and CoCl2 x 6 H2O.

MediaDive J1238 preserves that nested structure as `Main sol. J1238`,
`SL-9 mineral solution`, `Trace vitamins`, and `Vitamin B12 solution 0.05 g/L`.

## Completeness

The generated flat record is incomplete as a final medium. It copies the SL-9,
trace-vitamin, and B12 stock recipe concentrations into top-level ingredients
instead of representing that only 10 ml, 10 ml, and 1 ml of those stocks are
used per liter. It also converts the 30 ml fructose and 1 ml Coenzyme M stock
additions directly to `30 G_PER_L` and `1 G_PER_L`.

The generated `Vitamin B12` row merges the trace-vitamin stock value `0.0001`
with the separate B12 stock value `0.05`, yielding `0.050100000000000006 G_PER_L`
and losing both source contexts.

## Findings

- SL-9 mineral solution ingredients are present at full stock strength instead
  of their 10 ml/l final contribution.
- Trace-vitamin and vitamin B12 stock ingredients are flattened at stock
  strength instead of their 10 ml/l and 1 ml/l final contributions.
- `Fructose` and `Coenzyme M` use the source milliliter addition volumes as
  `G_PER_L` final concentrations.
- The generated `Vitamin B12` row sums two separate stock contexts into one
  biologically meaningless decimal value.
- The source-equivalent TOGO M1332 merge remains separate and carries its own
  ml-to-`G_PER_L` solution rows.
- `Na2SeO4` still has a legacy `mediaingredientmech_term` link instead of the
  CHEBI-keyed `mediaingredientmech_chebi_term` shape used on neighboring rows.

## Recommended Edits

- Preserve the JCM/MediaDive stock additions as structured solution additions or
  apply dilution factors before flattening into final concentrations.
- Keep SL-9, Trace vitamins, and Vitamin B12 solution as separate stock
  contexts; do not merge their water or Vitamin B12 rows into the final main
  ingredient list.
- Convert the 30 ml 1 M fructose and 1 ml 0.01% Coenzyme M additions from their
  stock concentrations rather than treating `30` and `1` as grams per liter.
- Repair TOGO M1332 with the same solution-handling fix and then merge it with
  the MediaDive/JCM J1238 source for one Tanner MOD2 record.
- Replace the lingering `mediaingredientmech_term` on `Na2SeO4` with the
  CHEBI-keyed sodium selenate link.

## Follow-up Checks

- Re-fetch JCM 1238 after the fix and confirm that only milliliter stock
  additions are flattened.
- Confirm the generated record no longer has `Vitamin B12` at
  `0.050100000000000006 G_PER_L`.
- Confirm `TANNER_MOD2_MEDIUM.yaml` no longer duplicates the same JCM 1238
  recipe after the TOGO source is repaired.

## Additional Notes

None found
