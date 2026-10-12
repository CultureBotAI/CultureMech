# JCM Preparation-Scope Findings

The preliminary 500-record preview proposed 643 claims in 129 records.
Manual inspection of those candidates' source amounts and complete main
preparation text withheld **151 claims in 24 records** before writing YAML.
The applied plan retains 492 evidence-only claims in 107 records. No quantity
was corrected or filled by this pass, and withholding is not a scientific repair.

[withholdings.json](withholdings.json) records each decision's stable ID,
medium accession, field scope, exact short quote, structured source locator,
URL, response SHA256, and reason. Those decisions are frozen into
[plan.json](plan.json). The reviewer only permits them to block support.
They cannot supply values, bypass other guards, or be overridden at apply time.
Other batches do not automatically inherit these source-specific decisions.

## Explicit Conflicts

| Medium | Finding | Applied decision |
| --- | --- | --- |
| J19 | Ascorbate/cysteine additions occur after sterilization and are absent from the table. | Withhold both proposed base claims; reconstruct the supplemented recipe. |
| J30 | Potato extraction is followed by sieving; no recovered volume or final makeup is established. | Withhold glucose/agar claims as well as the already unsupported potato input. |
| J112 | A single row combines cellobiose and cellulose alternatives. | Withhold only that row; eight unambiguous base rows receive evidence. |
| J146 | Rabbit serum and thiamine pyrophosphate are added to dispensed tubes, not represented by the base table. | Withhold all 13 proposed claims. |
| J182 | A 900 ml base receives 100 ml bicarbonate stock missing from the table. | Withhold all six proposed claims; do not infer the stock's percent basis. |
| J264 | An erythromycin/ethanol stock is added after autoclaving but omitted from the table. | Withhold all three proposed claims. |
| J295 | A 950 ml base receives 50 ml cellobiose stock missing from the table. | Withhold all eight proposed claims. |
| J333 | Potato mass precedes extraction and filtration; final makeup applies to the recovered medium. | Withhold potato alone; sucrose and agar retain support. |
| J389 | Two separately prepared additions each use 10 ml water; their relationship to the table's 1000 ml is unspecified. | Withhold all 11 claims; neither 1000 nor 1020 ml is silently selected. |
| J461 | API arithmetic uses 1025 ml extraction inputs, but preparation makes the filtrate to 1 L before nutrients. | Withhold both proposed claims; restore preparation stages before numeric correction. |

The official JCM pages corroborate the preparation distinctions in
[J182](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=182),
[J264](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=264),
[J295](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=295),
[J333](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=333),
[J389](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=389), and
[J461](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461).
The J19 and J146 official endpoints return `Nothing found`; their withholding
findings are pinned to inspected MediaDive preparation text, not fabricated
original-page verification. J182 also has a current branded-peptone difference
from the dataset; that attributed row was already unsupported.

## Additional Stock Gaps

J90, J98, J121, J180, J196, J267, J283, J287, J299, J318, J375, J459,
J489, and J500 separately prepare and add solutions without establishing how
their solvent relates to the table volume. All proposed claims in these 14
records are withheld pending stock-dose and complete-medium volume review.
The source tables still support reported input masses, but this pass does not
reinterpret those masses as verified final concentrations or guess stock doses.

## Controls And Limits

- J14 explicitly makes a 950 ml base before adding 50 ml blood. Its total
  volume basis is not treated like the omitted-stock cases.
- J333 explicitly makes the recovered medium to 1 L after sucrose/agar addition;
  that does not establish potato yield or retained potato solids.
- JCM 299 really lists 12 g L-cystine, and JCM 321 lists 0.5 g NaCl. Neither is
  replaced by a more familiar amount. J299 still has the stock-volume gap above.
- The JCM 2 original endpoint is empty. The inspected DSMZ-hosted J2 PDF
  agrees with the MediaDive amounts and explicitly gives 1000 ml; it is another
  presentation by the same provider, not independent scientific confirmation.
- Source type, discovery mode, retrieval date, dataset-provider identity and
  original JCM accession remain explicit. Individual authors and publication
  years are not invented from website or PDF copyright dates.
- [original-source-checks.json](original-source-checks.json) pins 13 inspected
  HTML responses and two visually inspected provider PDFs. This is not a claim
  that all 500 original recipes were retrieved or scientifically resolved.

## Earlier-Batch Follow-Up Leads

The original DSMZ 618 and 956 PDFs were subsequently retrieved and visually
inspected in full. DSMZ 618 adds Tween 80 after sterilization at a final
percentage; DSMZ 956 specifies alternative methanol/methylamine additions after
sterilization. [The source-pinned handoff](earlier-preparation-handoff.json)
identifies seven earlier supported base/agar claims requiring preparation-scope
reassessment, as well as three unsupported legacy percent-to-g/L encodings.
No replacement denominator or percent basis is supplied by those PDFs.
Those records were not changed by this batch, and old plans/reports were not
rewritten. DSMZ 955 is a contrasting
optional-agar case, not evidence of the same liquid-stock dilution problem.

These leads and the 24 withholdings remain part of the all-record goal.
Passing hash/snippet checks cannot resolve scientific preparation scope.
