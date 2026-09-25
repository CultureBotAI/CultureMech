# YAML Record Review: calroanaerobacter_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
- Started UTC: 2026-09-22T02:55:22Z
- Finished UTC: 2026-09-22T02:58:27Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007626`, `calroanaerobacter_medium`, `Calroanaerobacter Medium`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M1107_Calroanaerobacter_Medium` on fingerprint `d36ff3c24c505257841a9b33010c2e352399e887c0014ba9b5b0c03dfceeb889`.
- Authoritative owner: `data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml`.
- Claimed source identity: TOGO Medium `M1107`, imported from JCM Medium 1042.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M1107` identifies this recipe as `Calroanaerobacter Medium` and as an import from JCM Medium 1042.
- The cited live JCM 1042 page now returns `Nothing found`, so JCM itself was not available for a live cross-check.
- The TOGO `M1107` API payload supports the direct final-medium rows for 5 g sodium pyruvate, 3.46 g PIPES, 2 g yeast extract, 2 g tryptone, 5 ml Trace vitamins, 1 L artificial seawater, pH 7.0, and an N2 headspace.
- The TOGO `M1107` API payload supports the artificial-seawater formula that is currently flattened into top-level `ingredients`.
- The TOGO `M190` payload confirms the referenced Trace vitamins formula, and the TOGO `M142` payload confirms the referenced Trace minerals formula used inside the artificial seawater stock.
- Nitrogen is source-compatible only as a headspace gas during vessel dispensing, not as a standalone variable-concentration final ingredient.
- Yeast extract and tryptone are intentionally ungrounded as undefined biological mixtures.

## Evidence

- TOGO `M1107` lists 5 ml Trace vitamins from `M190`, 1 L Artificial seawater, and the Calroanaerobacter basal additions as distinct top-level items.
- TOGO `M1107` lists the artificial-seawater subcomponent as a separate 1 L recipe with distilled water, MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, KH2PO4, MgCl2 x 6 H2O, KCl, NaHCO3, ammonium sulfate, NaBr, SrCl2 x 6 H2O, ammonium ferric citrate, and 5 ml Trace minerals from `M142`.
- The generated record instead has `Artificial seawater (see below)` as an empty top-level `1 G_PER_L` ingredient and also flattens every printed artificial-seawater internal ingredient into the same top-level list.
- The 5 ml Trace vitamins and 5 ml Trace minerals additions are both represented as empty `Unknown solution` objects with `G_PER_L` concentrations.
- TOGO `M1107` carries pH `7.0` and a preparation comment to adjust pH, dispense under N2, seal with butyl rubber stoppers, and autoclave.
- A separate direct JCM / MediaDive J1042 owner exists for the same JCM medium and preserves the pH and preparation steps, but it independently flattens TOGO M190/M142 stock rows into final ingredients.

## Completeness

- The direct Calroanaerobacter basal ingredients are present.
- The pH 7.0 value and preparation text are absent.
- The 1 L/L artificial-seawater addition is not modeled as a stock addition with internal composition.
- The 5 ml/L Trace vitamins stock addition is present only as an empty `Unknown solution`.
- The 5 ml/L Trace minerals stock addition under artificial seawater is present only as an empty `Unknown solution`.
- Nitrogen gas is present only as a variable ingredient, not as the dispensing headspace.
- Empty `target_organisms` and `source_references` are not inherently defects for this TOGO import; the source verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: the generated record flattens Artificial seawater into final `ingredients`; TOGO calls for 1 L of that subcomponent in the Calroanaerobacter final medium.
- Major: the artificial-seawater addition is represented as `1 G_PER_L` instead of a 1 L stock/base addition.
- Major: the generated record leaves the 5 ml Trace vitamins addition as an empty `Unknown solution` with concentration `5 G_PER_L`.
- Major: the generated record leaves the artificial seawater's 5 ml Trace minerals addition as an empty `Unknown solution` with concentration `5 G_PER_L`.
- Major: the generated record omits the TOGO pH 7.0 state and all preparation instructions.
- Minor: N2 is modeled as a variable final-medium ingredient instead of a headspace preparation detail.
- Minor: the direct JCM / MediaDive J1042 import is split from the TOGO M1107 import rather than reconciled as a duplicate or variant relationship.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml`, not the generated merge.
- Model Artificial seawater as a structured 1 L/L base solution and move its internal salts into that subcomponent.
- Model the TOGO M190 Trace vitamins addition as a 5 ml/L stock and populate its composition from TOGO M190 / JCM 197.
- Model the TOGO M142 Trace minerals addition under Artificial seawater as a 5 ml/L stock and populate its composition from TOGO M142 / JCM 151.
- Restore the TOGO pH 7.0 state and the pH/N2/sealed-autoclave preparation text.
- Move N2 out of final `ingredients` and into the preparation/headspace representation.
- Reconcile this TOGO M1107 owner with `data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml` after both imports are curated.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized TOGO owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml`.
- Compare the regenerated TOGO record against TOGO M1107, M190, and M142, with special attention to pH, N2 handling, 1 L Artificial seawater, 5 ml Trace vitamins, 5 ml Trace minerals, and absence of artificial-seawater salts from final `ingredients`.
- Re-run duplicate detection between the TOGO M1107 and direct JCM / MediaDive J1042 owners after both are curated.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname '*calroanaerobacter*' -o -iname '*caloranaerobacter*' -o -iname '*DSMMZ*' \) -print` ignored `.gitignore` rules and found only the two generated Calroanaerobacter records plus their two active normalized owners.
- A gitignore-independent structured-data search for `TOGO:M1107`, `TOGO_M1107_Calroanaerobacter`, `mediadive.medium:J1042`, `JCM_M1042`, the JCM 1042 URL, and Calroanaerobacter labels found the active TOGO owner, the direct JCM / MediaDive owner, both generated records, registry/catalog rows, current content-review rows, and current deep-research priority rows for both Calroanaerobacter owners.
