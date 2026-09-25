# YAML Record Review: cellulolytic_natronoarchaea_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml
- Started UTC: 2026-09-22T06:36:20Z
- Finished UTC: 2026-09-22T06:37:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007796 |
| Name | cellulolytic_natronoarchaea_medium |
| Original name | Cellulolytic Natronoarchaea Medium |
| Category | bacterial |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml |
| Generated record | data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml |
| Merge fingerprint | d9bc2cec79f86be3b77dcce0c035d12c665749b866d50f906d1231d27cf68361 |
| Merged from | TOGO_M1264_Cellulolytic_Natronoarchaea_Medium |

The record is generated from one TOGO import of JCM medium 1180 through TOGO
medium M1264. The live TOGO API reports `original_media_id: JCM_M1180`, source
URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1180`, and name
`Cellulolytic Natronoarchaea Medium`; the live JCM page for `GRMD=1180` is the
same CELLULOLYTIC NATRONOARCHAEA MEDIUM formula.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml` | Passed |
| strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml --out /private/tmp/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors |
| reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| embedded curation history | `just validate-history data/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.yaml` | Not checked: `just validate-history` validates standalone `history/` records against `HistoryRecord`, not `MediaRecipe.curation_history` blocks |

`just`-based validators were not used because the local project environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools.
The narrow validators above ran offline with Python 3.11.

## Identity and Grounding

The source accession identity is correct: TOGO M1264 and JCM `GRMD=1180` both
name the Cellulolytic Natronoarchaea medium.

The record is classified under `category: bacterial` even though the medium
name denotes natronoarchaea. That category is source-inconsistent and has also
placed the maintained owner under `data/normalized_yaml/bacterial/`.

The base salts are grounded to appropriate CHEBI terms. The six stock additions
have no grounded final ingredient or stock compositions because solution
migration converted them to empty `Unknown solution` objects.

## Evidence

The live JCM 1180 table supports the five base salts at 128 g NaCl, 95 g
Na2CO3, 15 g NaHCO3, 2.5 g KCl, and 1.75 g K2HPO4 per liter after bringing
the recipe to a final volume of 1.0 L.

The source supports six after-cooling stock additions: 1.25 ml of 10 percent
NH4Cl, 1 ml of 1 M MgSO4, 1 ml of the trace-element solution from Medium 1079
(TOGO M1148), 5 ml of the trace vitamins from Medium 197 (TOGO M190), 0.2 ml
of 10 percent yeast extract, and 20 ml of 10 percent cellobiose. The generated
record copies the ml numbers into `G_PER_L` concentration values and leaves the
stock contents empty.

JCM 1180 explicitly says to add the components to distilled water, bring the
volume to 1 L, and after cooling add the autoclaved or filter-sterilized
solutions. The generated record does not retain an ordered preparation step for
that post-cooling boundary.

## Completeness

A gitignore-independent search over `data`, `.`, YAML, JSON, and archived
reports found one maintained TOGO owner, one separate maintained
`data/normalized_yaml/bacterial/cellulolytic_natronoarchaea_medium.yaml`, and a
second generated `data/merge_yaml/merged/cellulolytic_natronoarchaea_medium__b67e3bdc.yaml`
for the same JCM `GRMD=1180` source. The MediaDive sibling has already
expanded M1148 and M190 stock components into the parent medium and inflated
the base-salt concentrations, so the two imports cannot currently fingerprint
together.

Empty optional organism and growth slots are acceptable for this source:
JCM 1180 gives the formulation and one preparation sentence but no growth
measurement.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The six post-cooling stock additions have milliliter additions stored as `G_PER_L`: `0.2`, `1.25`, `1`, `20`, `1`, and `5`. This loses the stock-vs-final concentration boundary. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml; TOGO importer |
| Major | All six solution entries are empty `Unknown solution` placeholders. The two referenced solutions should remain references to M1148 and M190, and the four inline 10 percent or 1 M stocks need explicit stock metadata or final diluted amounts. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml; solution migration logic |
| Major | The same JCM 1180 medium exists as a second maintained/generated record with a different CultureMech ID and a different fingerprint, so source-equivalent MediaDive and TOGO imports are not reconciled. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml; data/normalized_yaml/bacterial/cellulolytic_natronoarchaea_medium.yaml; merge reconciliation |
| Major | The medium is filed as `category: bacterial` and lives in `data/normalized_yaml/bacterial/` despite denoting a natronoarchaeal medium. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml |
| Minor | The imported `Distilled water` line stores `1 L` as `1 G_PER_L`; it should be represented as a final-volume preparation fact or a liter volume, not as one gram per liter of water. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml |
| Minor | The first TOGO import history note says `Source: JCM, ID: M1264`; `M1264` is the TOGO medium ID, while the original JCM ID is `JCM_M1180` / `GRMD=1180`. | data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.yaml`,
   preserve the six after-cooling additions as milliliter stock additions and
   keep M1148 and M190 as referenced stock media.
2. Give the four inline stocks explicit solution identities or final diluted
   ingredient amounts: 10 percent NH4Cl, 1 M MgSO4, 10 percent yeast extract,
   and 10 percent cellobiose.
3. Add a preparation step that states the base salts are brought to 1.0 L and
   the stock solutions are added after cooling.
4. Move or reclassify this medium under the archaeal category.
5. Reconcile the TOGO and MediaDive maintained records for JCM 1180 so the
   merge emits one generated Cellulolytic Natronoarchaea record.
6. Add a clarifying history event distinguishing TOGO M1264 from JCM 1180 if
   earlier append-only history cannot be edited.

## Follow-up Checks

1. Rerun merge generation and verify that the JCM `GRMD=1180` formula emits one
   generated record.
2. Rerun LinkML, strict, term, and reference validation for the regenerated
   record.
3. Compare the regenerated record against live JCM 1180 and TOGO M1264 to
   confirm that the 1.25 ml, 1 ml, 1 ml, 5 ml, 0.2 ml, and 20 ml stock
   additions are not represented as grams per liter.
4. Verify that the MediaDive sibling no longer expands M1148 and M190 stock
   contents into the parent JCM 1180 formula.

## Additional Notes

The live M1148 and M190 TOGO API records were inspected only to confirm that
TOGO's `reference_media_id` values point at separate stock media. Their full
recipes are not required inside the M1264 medium.
