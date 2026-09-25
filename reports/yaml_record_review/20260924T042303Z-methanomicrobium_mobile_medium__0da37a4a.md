# YAML Record Review: METHANOMICROBIUM MOBILE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml
- Started UTC: 2026-09-24T04:21:42Z
- Finished UTC: 2026-09-24T04:23:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001807 |
| Name | methanomicrobium_mobile_medium |
| Original name | METHANOMICROBIUM MOBILE MEDIUM |
| Category | archaea |
| Media term | mediadive.medium:666b |
| Source | DSMZ Medium 666b through MediaDive |
| Generated path reviewed | data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml |
| Canonical owner | data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml |

The reviewed file is a generated merge of one MediaDive/DSMZ owner. It
captures the DSMZ 666b identity, but it omits one required complex addition and
substitutes the wrong reducing-agent salt for the source cysteine row.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml --out /private/tmp/methanomicrobium_mobile_medium__0da37a4a.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanomicrobium_mobile_medium__0da37a4a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The DSMZ 666b identity is correct.** MediaDive REST and the live MediaDive
  medium page identify `666b` as `METHANOMICROBIUM MOBILE MEDIUM`.
- **Most small molecules are grounded specifically.** K2HPO4, KH2PO4, NaCl,
  ammonium sulfate, CaCl2 x 2 H2O, MgSO4 x 7 H2O, indigo carmine, NaHCO3, DTT,
  and the unsupported Na2S x 9 H2O row all have exact or acceptable CHEBI
  groundings.
- **The source cysteine row is missing.** MediaDive lists 0.3 g/L L-Cysteine
  HCl x H2O; the YAML stores 0.3 g/L Na2S x 9 H2O instead.
- **Clarified rumen fluid is missing from composition.** MediaDive lists a 400
  ml addition of solution 2618 in the main liter; the YAML only imports the
  rumen-fluid preparation text as a standalone step.

## Evidence

### Supported by inspected sources

- MediaDive medium `666b` supports K2HPO4, KH2PO4, NaCl, ammonium sulfate,
  CaCl2 x 2 H2O, MgSO4 x 7 H2O, 5 mg indigocarmine, 6.4 g NaHCO3, 5 g yeast
  extract, 0.3 g DL-Dithiothreitol, 0.3 g L-Cysteine HCl x H2O, 600 ml
  distilled water, and 400 ml Clarified rumen fluid per 1 L main solution.
- MediaDive supports pH 6.8; boiling and cooling under H2/CO2 80/20; adding
  bicarbonate before the autoclave; dispensing under H2/CO2 80/20 into
  Hungate-type tubes or serum vials; post-autoclave cysteine and DTT additions
  from anoxic stocks; final pH 6.7-6.8; and 2 bar H2/CO2 80/20 overpressure
  after inoculation.
- MediaDive solution 2618 supports the rumen-fluid preparation retained in
  step 3.

### Unsupported or over-scoped in the YAML

- Na2S x 9 H2O is unsupported by MediaDive 666b and appears where L-Cysteine
  HCl x H2O should be.
- The 400 ml Clarified rumen fluid addition is absent.
- The 600 ml distilled-water row is absent.
- DTT is present as a direct top-level ingredient, but the source explicitly
  adds both DTT and cysteine after autoclaving from sterile anoxic stock
  solutions.
- The rumen-fluid recipe is present as a generic `AUTOCLAVE` step, but no
  solution or ingredient links that preparation to the 400 ml main-solution
  addition.

## Completeness

- **One main-solution addition is missing.** Clarified rumen fluid is part of
  the 1 L DSMZ recipe and has a MediaDive solution ID, but it is absent from
  the generated record.
- **One reducing agent is wrong.** L-Cysteine HCl x H2O was replaced by Na2S x
  9 H2O.
- **Water is missing.** MediaDive lists 600 ml distilled water in the main
  solution.
- **Stock-addition scope is missing.** Cysteine and DTT should remain
  post-autoclave additions from sterile anoxic stocks, rather than plain
  premix ingredients.
- **Bounded local search.** A gitignore-independent search for
  `mediadive.medium:666b`, `DSMZ Medium 666b`, `METHANOMICROBIUM MOBILE`, and
  `methanomicrobium_mobile_medium` under `data/normalized_yaml` and
  `data/merge_yaml/merged` found this DSMZ owner, its generated record, the
  separate TOGO M258 owner, the separate JCM J266/KOMODO merged record, and a
  parent-media reference from Methanofollis medium.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | L-Cysteine HCl x H2O was replaced by unsupported Na2S x 9 H2O. | MediaDive 666b lists 0.3 g L-Cysteine HCl x H2O and no Na2S row; the YAML lists 0.3 g/L Na2S x 9 H2O. | `data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml` |
| Major | The 400 ml Clarified rumen fluid addition is missing. | MediaDive 666b adds 400 ml of solution 2618 to the main 1 L solution; the YAML has only the solution's preparation prose. | `data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml` and the MediaDive importer |
| Major | Source solution topology and water were lost. | MediaDive has a 600 ml distilled-water row and scopes DTT plus cysteine as post-autoclave anoxic stock additions. | `data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml` and import unit handling |
| Minor | The source URL is underspecified. | The YAML note says only `Source: DSMZ`; MediaDive REST identifies medium `666b`, but no DSMZ or MediaDive URL is preserved in `notes`. | `data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml` |

## Recommended Edits

1. Replace Na2S x 9 H2O with the source 0.3 g/L L-Cysteine HCl x H2O row.
2. Restore 400 ml Clarified rumen fluid as a solution addition and keep the
   rumen-fluid preparation text scoped to that solution.
3. Restore 600 ml distilled water in the main solution.
4. Mark L-Cysteine HCl x H2O and DTT as post-autoclave sterile anoxic stock
   additions, matching the MediaDive 666b procedure.
5. Preserve a resolvable MediaDive or DSMZ source URL in the maintained owner's
   notes.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/methanomicrobium_mobile_medium.yaml` and the
  regenerated merged record.
- Manually compare the regenerated YAML against MediaDive medium 666b and
  solution 2618 to confirm the main-solution volume is 600 ml water plus 400 ml
  Clarified rumen fluid.
- Confirm Na2S x 9 H2O no longer appears unless a distinct inspected source
  supports it.

## Additional Notes

- `data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml`
  covers TOGO M258, and `data/merge_yaml/merged/METHANOMICROBIUM_MOBILE_MEDIUM.yaml`
  covers JCM J266 plus KOMODO 161. They share the same short name but are
  separate generated records with their own owner files.
