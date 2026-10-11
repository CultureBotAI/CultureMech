# Draft: LB Expansion Replaced Non-LB Ingredient Identities

Local issue draft only. Not submitted to GitHub; outbound publication approval
is still outstanding.

## Severity And Evidence

High-priority formulation corruption. Historical commit
`7e8bd7c6026306323b6d86bc0238fa35b8fa1d17` replaced non-LB ingredients with
Tryptone 10 g/L, Yeast extract 5 g/L and Sodium chloride 10 g/L. The independent
historical scan examined all 758 changed normalized YAMLs without parse errors,
finding 145 LB expansions: 80 acid-name and 42 albumin-name replacements, plus
23 LB-named replacements. The last group is not automatically validated.

For M258, the source says `alpha-Methylbutyric acid` (Greek alpha in the original)
at 0.5 g in the fatty-acid stock, not LB ingredients. Exact source text and
field-scoped evidence are preserved in the applied plan and YAML. Historical
before/after nodes and current exact paths/IDs are in
`historical-lb-inventory.json`.

M258 is repaired in this batch. M2366 had already restored its albumin in a
prior stock-boundary repair. The remaining 120 candidates have frozen current
baselines in `next-lb-identity-context.json`: 79 acid-name and 41 albumin-name
cases. Ninety already have follow-up reports, so report presence is not a
reliable resolution criterion.

## Likely Failure Mechanism

The current sibling `culturebotai-claw/scripts/expand_commercial_product.py`
uses lowercased substring matching in both discovery and replacement:
`any(pattern in term for pattern in product_patterns)`. A short `lb` alias
matches inside both `methylbutyric` and `albumin`.

Inspected sibling script SHA256:
`b025762b4e734715c691dda7e95c59cdea1ff10bd5452049500ba151be80e417`.
The historical alias configuration and invocation have not been recovered;
this mechanism is reproduced conditionally, not proven as that invocation.
The sibling tool was not executed or edited.

## Resolution Requirements

- Match product identity with guarded exact names or explicit bounded aliases,
  not unrestricted substrings. Test acid, albumin, lactalbumin and legitimate
  LB formulations; preserve distinctions such as Miller versus Lennox.
- Reconstruct each affected formulation from its exact source. Support every
  correction with a persistent URL/DOI and exact snippet in the record.
- Do not restore historical g/L values blindly: flattened stocks, missing water,
  omitted doses and stock-specific pH can independently corrupt those values.
- Preserve genuine yeast extract/peptone/salt nodes even when an erroneous
  expanded node has the same preferred term. Identify removals by exact path
  and product provenance; preserve append-only history.
- Run schema, strict, reference, quantity/identity mutation tests, guarded
  application/readback/no-op and generated-output retention checks. Reconcile
  exact per-record reports and queues without counting structural coverage as
  complete evidence verification.
