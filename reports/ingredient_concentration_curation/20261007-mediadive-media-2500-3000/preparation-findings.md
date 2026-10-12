# Sixth Medium Pass: Preparation Findings

The complete main ingredient tables, preparation steps, and proposed amounts
were read for all 68 preliminary candidates. Of 358 mechanically proposed
claims, 135 were withheld across 18 whole records. The remaining 223 claims
in 50 records concern existing provider-declared main-recipe concentrations.
Neither source agreement nor schema validity establishes measured final volume,
retained dissolved amount, ontology identity, or growth on a variant.

[withholdings.json](withholdings.json) pins every veto to its exact record ID,
source response SHA256, JSON locator, and literal source excerpt. A veto can
only remove support. [preflight.json](preflight.json) verifies that no rejected
quantity changes and that the retained changes append provenance only.

## Withheld Records

| Source accession | Unresolved source issue |
| --- | --- |
| J526 | Filter-sterilized ferrous sulfate addition; solvent volume is not established. |
| J542 | Conditional precipitate removal means input loading need not equal retained dissolved amount. |
| J557 | Separately filter-sterilized carbonate; stock solvent accounting is not established. |
| J559 | Sulfide is added as a 5% stock; the percentage basis and complete-volume accounting require review. |
| J611 | A 900 ml base receives 100 ml carbonate stock that the API table omits. |
| J626 | Glucose and sulfide are supplied from separate concentrated stocks. |
| J634 | Cysteine and sulfide are supplied from separate 5% stocks. |
| J646 | Post-autoclave sulfide is specified as a final molarity, not a known stock dose and solvent volume. |
| J698 | API denominator is 1002 ml despite table liquids totaling 1002.5 ml; an autotrophic variant also changes ingredients. |
| J711 | Glucose and carbonate additions appear in preparation text but not the table. |
| J719 | Separate cysteine and sulfide stocks require dose and volume reconciliation. |
| J725 | API denominator is 1019 ml while listed liquids total 1018.6 ml; per-liter stock instructions also need staging review. |
| J744 | An earlier 10 ml sulfide addition is omitted from the table, which lists a distinct later dose; trace-stock identity also needs review. |
| J767 | API denominator is 1001 ml despite 1000 ml water plus 1.4 ml DMSO. |
| J811 | A sterile sulfide addition has no established solvent-volume accounting. |
| J888 | Potato extraction and sieving do not specify recovered-volume makeup. |
| J896 | API arithmetic uses 40 ml serum instead of the original recipe's explicit 584 ml complete-medium volume. |
| J997 | Glucose, cysteine, and sulfide are added from stocks whose solvent accounting is unresolved. |

Listed liquid-volume sums identify inconsistencies; they are not asserted as
measured final volumes. Withholding does not correct the legacy formulations.
In particular, no speculative mass/volume conversion replaces a percentage.

## Controls And Variants

- J653 includes 900 ml water plus 100 ml ammonium bicarbonate stock. The
  unambiguous base rows remain eligible; the stock itself is not newly verified.
- J654 includes 900 ml water and a 100 ml lactate solution. Its stock volume
  is represented, unlike J611. No unspecified percentage basis is converted.
- J766 includes 1000 ml water plus 20 ml bicarbonate stock in the provider
  denominator; eligible base rows remain scoped to that reported recipe basis.
- J975 explicitly makes its base to 970 ml before a 30 ml carbonate addition.
  The original page confirms this distinction. Evidence for six eligible base
  rows does not endorse the still-unsupported stock representation.
- J890 and J891 include their acid and ethanol volumes in the provider basis.
  No density or conversion to mass concentration is inferred.
- J595 retains its cellulose base; cellobiose substitution is not propagated.
- J615's strain-specific pH instruction is not applied to all formulations.
- J660 and J809 retain liquid base scope rather than acquiring semisolid/agar
  variant amounts. J735's conditional tryptophan is not made universal.
- J734, J870, and J961 retain liquid scope despite optional solid instructions.
  Indeterminate hydration labels are not changed into fixed hydrates or molarity.

## Original Sources

The separately captured official JCM pages for
[J611](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=611),
[J896](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896), and
[J975](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=975)
were inspected. Their capture hashes are recorded in the historical
[acquisition handoff](../20261007-medium-source-fetch-2500-3000-preparation-leads.md).
This is not a claim to have inspected all 500 original recipes; 81 of the API
responses contain no recipe table. Original-source follow-up remains necessary.

The priority [J896 repair handoff](jcm896-repair-handoff.md) preserves the
specific original-source basis. It is not an applied correction or permission
to rewrite the frozen cohort plan or its historical result.
