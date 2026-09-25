# YAML Record Review: Brucella Blood Agar With Hemin Menadione

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml
- Started UTC: 2026-09-22T00:37:57Z
- Finished UTC: 2026-09-22T00:39:41Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:010102 |
| Label | brucella_blood_agar_with_hemin_menadione |
| Original label | Brucella Blood Agar With Hemin Menadione |
| Category | bacterial |
| Source accession | TOGO:M696 |
| Generated path | data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml |
| Merge fingerprint | bc6bad7e07d15bdf9b323a1ed4ddbd8bdc6fe7789c73c7c5ff4d5d1ef81b67c3 |

The reviewed target is a generated merge under `data/merge_yaml/merged`, derived from
`TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione`. Future corrections belong in
the normalized owner above or in the import/merge logic that emits this generated
copy; `data/merge_yaml/merged` itself should not be edited by hand.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml --out /private/tmp/Brucella_Blood_Agar_With_Hemin_Menadione.strict.tsv --workers 1 --quiet` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and
`just validate-references` were not rerun because the project uv environment tries
to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The generated target's stable ID, TOGO accession, label, category, medium type,
and solid-agar physical state agree with TOGO M696 and JCM Medium 677. The TOGO
API identifies M696 as `Brucella Blood Agar With Hemin Menadione`, sourced from
`JCM_M677` at the JCM GRMD 677 URL, and reports the expected distilled water,
horse blood, Brucella agar, hemin solution, and menadione solution rows.

JCM GRMD 677 is also the exact source: the page title is
`BRUCELLA BLOOD AGAR WITH HEMIN MENADIONE`, and its table lists 43.0 g Brucella
agar (BD-BBL), 50.0 ml horse blood, 10.0 ml hemin solution from Medium No. 469,
10.0 ml menadione solution from Medium No. 469, and 1.0 L distilled water.
The linked JCM GRMD 469 page supplies the hemin and menadione stock recipes, so
the generated cross references denote real stock-solution additions rather than
literal gram-per-liter powder components.

The water CHEBI mapping to `CHEBI:15377` is appropriate. The Brucella agar and
horse blood ingredients are complex biological/commercial materials that are
properly left without CHEBI terms in the maintained owner.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| The record denotes TOGO M696 / JCM Medium 677 | TOGO M696 reports `original_media_id` `JCM_M677` and the JCM GRMD 677 source URL; JCM GRMD 677 has the same medium title |
| `physical_state: SOLID_AGAR` | JCM 677 is an agar medium and includes 43.0 g Brucella agar (BD-BBL) |
| `medium_type: COMPLEX` and `composition_type: UNDEFINED` | Brucella agar (BD-BBL) and horse blood are undefined complex materials |
| Brucella agar (BD-BBL), 43.0 g/L | JCM 677 lists Brucella agar (BD-BBL) at 43.0 g in a one-liter formulation |

Unsupported or stale in the generated merge:

| Generated claim | Problem |
| --- | --- |
| `Distilled water`, `1 G_PER_L` | TOGO says 1 L and JCM says 1.0 L. The maintained owner correctly stores this as `1000 ML_PER_L`. |
| `Horse blood`, `50 G_PER_L` | TOGO says 50 ml and JCM says 50.0 ml. The maintained owner correctly stores this as `50.0 ML_PER_L`. |
| `Hemin solution (see Medium [M470])`, `10 G_PER_L`, empty composition, `name: Unknown solution` | TOGO says 10 ml and JCM 677 says 10.0 ml of the hemin solution from JCM 469. JCM 469 defines the hemin stock as 50 mg hemin dissolved first in 1 ml 1 N NaOH and adjusted to 100 ml. |
| `Menadione solution (see Medium [M470])`, `10 G_PER_L`, empty composition, `name: Unknown solution` | TOGO says 10 ml and JCM 677 says 10.0 ml of the menadione solution from JCM 469. JCM 469 defines the menadione stock as 5 mg menadione dissolved first in 1 ml ethanol and adjusted to 100 ml. |
| No structured preparation or sterilization fields | JCM says to autoclave media at 121 C for 15 min unless otherwise stated. The normalized owner already records this default autoclave step. |
| No structured `references` list | The source URLs are only prose in `notes`; the maintained owner already has structured TOGO M696, JCM 677, and JCM 469 references. |

## Completeness

The generated merge is materially behind its normalized owner. The maintained
`data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml`
record already has the correct water and horse-blood volume units, JCM 469
hemin and menadione stock compositions, JCM-backed preparation steps, autoclave
metadata, structured references, and quality flags from the 2026-09-10
`RESOLVED_OFFICIAL_SIMPLE_SCORE20` event.

A gitignore-independent `rg --no-ignore --hidden --pcre2` search for
`CultureMech:010102`, `TOGO:M696`, `JCM_M677`, `GRMD=677`, the owner slug, and
merge fingerprint `bc6bad...` covered ignored and hidden files across the
repository. It found the expected generated record, maintained TOGO owner,
generated indexes, archived validation reports, and proposal reports. It also
found `data/normalized_yaml/bacterial/brucella_blood_agar_with_hemin_menadione.yaml`,
a distinct MediaDive/JCM 677 import with `CultureMech:003022`, the same medium
formulation, and its own September JCM-backed repair. I found no pre-existing
`reports/yaml_record_review/*Brucella_Blood_Agar_With_Hemin_Menadione.md`
report.

Empty optional target-organism, pH, and temperature slots are not defects for
this source-only formulation record: TOGO and JCM 677 provide a recipe, not a
strain-specific growth or incubation claim.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | The generated merge is stale relative to its normalized owner. The owner was repaired on 2026-09-10, but the generated file still has the pre-repair import with gram-per-liter units for liter/milliliter quantities, empty `Unknown solution` stubs for hemin and menadione, and no structured JCM 469 stock compositions, preparation steps, sterilization, references, or quality flags. | `data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml` and the merge regeneration workflow |
| Major | Four source volume rows are represented with mass units in the generated target: water is `1 G_PER_L`, horse blood is `50 G_PER_L`, and both hemin/menadione stock additions are `10 G_PER_L`. TOGO and JCM support one liter or milliliter additions, and the maintained owner already stores `1000 ML_PER_L`, `50.0 ML_PER_L`, and `10.0 ML_PER_L` values. | `data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml` and the TOGO import/merge path that preserved stale units in the generated copy |
| Major | The generated hemin and menadione additions lost their referenced JCM Medium 469 compositions and were downgraded to empty `name: Unknown solution` records. JCM 469 supports hemin at 0.5 g/L with 1 N NaOH and menadione at 0.05 g/L with ethanol in the stock solutions. | `data/normalized_yaml/bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml` and the merge regeneration workflow |

No blocker or minor findings found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml`
   from the repaired owner rather than hand-editing the generated merge. The
   regenerated output should carry forward `1000 ML_PER_L` distilled water,
   `50.0 ML_PER_L` horse blood, two `10.0 ML_PER_L` solution additions, JCM 469
   stock compositions, preparation steps, autoclave metadata, structured
   references, and the 2026-09-10 curation event.
2. Verify that any TOGO merge path that consumes referenced `reference_media_id`
   solution rows no longer emits empty `Unknown solution` stubs or mass units for
   volume rows when a maintained normalized owner already resolved the stock.

## Follow-up Checks

- Rerun the merge generator and inspect the diff for
  `data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml` only.
  The diff should be a derived refresh from the normalized owner, not a manual
  edit to the merge output.
- Rerun `just verify-merges` to prove the generated merge matches normalized
  source recipes.
- Rerun `just validate-schema data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml`.
- Rerun `just validate-strict data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml`.
- Rerun `just validate-references data/merge_yaml/merged/Brucella_Blood_Agar_With_Hemin_Menadione.yaml` once the generated file has structured references.
- Manually compare TOGO M696, JCM 677, and JCM 469 against the regenerated merge
  to confirm all five recipe rows and both stock formulas survived regeneration.

## Additional Notes

- TOGO's API names the hemin and menadione cross reference as `M470`, while the
  live JCM page links both stocks to `GRMD=469`; this appears to be the TOGO
  accession for the JCM 469 page rather than a substantive evidence conflict.
- The duplicate MediaDive/JCM import at
  `data/normalized_yaml/bacterial/brucella_blood_agar_with_hemin_menadione.yaml`
  is outside this generated target but now carries the same JCM 677/JCM 469
  formulation repair. Its `kg_microbe_match: mediadive.medium:12` was not
  reviewed for this TOGO M696 report.
