# Seventh Medium Pass: Source-Scope Findings

All 43 preliminary candidates' complete main ingredient tables, preparation
steps, proposed claims, and local metadata were inspected. Of 239 preliminary
evidence-only claims, 47 were withheld across nine records. Six records are
withheld completely; three retain unrelated supported rows. The 192 retained
claims concern existing provider-declared main-recipe rates, not independently
measured final volume, post-titration total concentrations, or verified secondary
chemical mappings. This is not verification of all ingredients in all 319 records.

[withholdings.json](withholdings.json) pins each decision to an exact record ID,
API response hash, JSON locator, and literal excerpt. These decisions only remove
support. [preflight.json](preflight.json) independently verifies unchanged
quantities and provenance-only changes, including the partially withheld records.

## Withheld Claims

| Accession | Claims withheld | Source issue |
| --- | ---: | --- |
| J1105 | 5, whole record | The API uses only the 10 ml carbonate dose as denominator, omitting the explicitly prepared 1 L base. |
| J1163 | 1, partial | The nickel ammonium double-sulfate identity requires original-source verification; no alternative formula is established. |
| J1168 | 2, whole record | Antibiotics are separately dissolved in water and methanol; stock solvent volumes are unspecified. |
| J1201 | 9, whole record | Glucose and carbonate are supplied from separately prepared stocks without complete solvent-volume accounting. |
| J1239 | 6, whole record | Separately autoclaved yeast extract and sucrose have unspecified solvent volumes; sulfur is also added separately to vessels. |
| J1249 | 9, whole record | The later 20 ml acetic-acid addition is omitted from the ingredient table and its 1001 ml denominator. |
| J1262 | 1, partial | The carbonate table input is followed by unquantified carbonate titration; total carbonate is not established. |
| J1264 | 13, whole record | The 1000 ml denominator omits the table's 0.2 ml lactate addition; carbonate titration also remains unquantified. |
| J1323 | 1, partial | The reported MnCl4 x 6 H2O formula requires original-source verification; no replacement stoichiometry is established. |

Withholding is not correction. Listed liquid-volume sums expose accounting
conflicts but do not prove measured final volume. No unknown percentage basis,
density, chemical identity, titrant dose, or stock strength is inferred.
J1163 retains six unrelated rows, J1262 eight, and J1323 nine.

## Preparation Controls

- J1044/J1045/J1047/J1052/J1111/J1210 include later liquid additions in the
  provider denominator. Their unambiguous base rows remain eligible; this does
  not endorse the legacy stock amounts expressed as mass concentrations.
- J1128 includes 956 ml water plus 20, 4, and 20 ml additions; J1179 includes
  935 ml water plus 50, 10, and 5 ml; J1268 includes 645 ml water plus 100,
  100, 100, 20, and 35 ml. No stock percentage is converted by this pass.
- J1154 includes 990 ml water plus 10 ml methanol. Its later methanol addition
  is not omitted from the provider volume. Methanol's legacy mass unit is still
  unsupported and unchanged; evidence for six base/agar rows does not support it.
- J1185 and J1263 use unquantified carbonate for pH adjustment. Existing base
  rows retain provider-recipe scope, not measured post-titration concentrations.
  No numeric carbonate dose is added. J1262's separate carbonate input is
  withheld because that same ingredient also receives an unknown titration dose.
- J1050/J1141/J1217/J1222/J1236 remain liquid recipes despite optional agar
  instructions. J1102/J1208 strain-specific substitutions remain separate from
  the base claims. Indeterminate manganese-sulfate hydration is not converted
  into a fixed hydrate or molarity.
- J1063 specifies carbonate as powder, not an unquantified stock solution.
  J1321's separately steamed sulfur does not establish an additional solvent
  dose; the sulfur row itself remains unsupported by this evidence-only pass.

## Variant Follow-Ups

These existing annotations are not newly supported, corrected, or propagated
by the base-row evidence. The plan freezes their before/after context.

- J1044 (`ml_15_medium.yaml`) describes yeast extract increasing from 5 to
  20 g/L relative to `ml_medium.yaml`, whereas its API table supplies 20 ml
  of a 10% yeast-extract stock. Reconcile both exact recipes and percentage
  basis before asserting a mass-concentration comparison.
- J1047 (`JCM_J1047_MARINITOGA_MEDIUM.yaml`) compares glucose and reducing
  agents to J997 using 14 and 10 g/L. Those numbers originate from ml stock
  doses in J1047 (1 M glucose and 5% reducing-agent stocks). The J997 source
  also has unresolved solvent accounting from the sixth pass. Reassess both
  formulations and reciprocal annotations, not only this parent's text.
- J1052 (`573c_medium.yaml`) compares metal-salt amounts to
  `alicyclobacillus_cellulosilyticus_medium.yaml`. Its three 1 ml stock doses
  are encoded as 1 g/L in legacy ingredient fields. The percentages and both
  formulations require review before a concentration-variant claim is supported.
- J1154 (`JCM_J1154_K_MEDIUM.yaml`) compares methanol as 10 versus 1 g/L
  with `medium_k.yaml`. J1154 specifies a volume dose, not a mass; no density
  is given by this review. Inspect both recipes and correct the units and
  reciprocal relationship evidence together.
- J1217 (`modified_reinforced_clostridial_medium.yaml`) labels its pH-8 child
  as `SOURCE_DUPLICATE` despite its own source pH 6.0-6.5. Ingredient-set
  similarity alone cannot establish exact formulation identity. The relationship
  remains a separate unresolved review item.

## Original Sources And Access Gaps

The original JCM 1105 and 1249 conflicts and capture hashes are preserved in
the [acquisition handoff](../20261007-medium-source-fetch-3000-3319-preparation-leads.md).
Their complete source tables and preparation were inspected before withholding.
The JCM 1154 page was also inspected during preparation review; its methanol
and water amounts agree with the API, without supporting a mass conversion.

Official HTML endpoints were fetched again on 2026-10-07 for J1044, J1163,
and J1323. Each returned a medium-number-specific 844-byte document containing
`Nothing found.` rather than a recipe. This is an access/content gap, not proof
that the historical recipe never existed. Captures in the ignored local cache:

| Source | Capture filename | SHA256 |
| --- | --- | --- |
| [J1044](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1044) | `JCM_GRMD1044-scope.html` | `863752af0b79a8cd64ba67f71f92fdf303024db1d4b704bddde2b288ba8dd534` |
| [J1163](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1163) | `JCM_GRMD1163-scope.html` | `a413fd077adc5a3ac9e043f59ac4c36da6b67d555e62191918d50811c7eb5317` |
| [J1323](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1323) | `JCM_GRMD1323-scope.html` | `e4d7ffa595190f41a4ae2cec27fff9641431ae2587f52bfdd048581bcc473506` |

The local source-capture filename search included ignored and hidden files.
Targeted web searches yielded no usable original recipe for these questions;
search snippets were not used as amount evidence. All 319 API captures were
acquired and verified separately. Twenty contain no recipe table and remain
unresolved. The ten public-medium targets P1-P10 remain outside this cohort,
not removed from the all-record objective.
