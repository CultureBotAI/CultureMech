# YAML Record Review: ANAEROBIC TRYPTIC SOY BROTH MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml
- Started UTC: 2026-09-21T12:21:00Z
- Finished UTC: 2026-09-21T12:21:40Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015369`
- Label: `ANAEROBIC TRYPTIC SOY BROTH MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:869`, source `DSMZ`, original DSMZ PDF `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium869.pdf`
- Generated status: generated merge record with fingerprint `5ed6566986682e5271b86e6424efe23403f60bbe162235c6ab351e09526b5a59`
- Merge lineage: one source, `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml`; KOMODO/TSB normalization rules own the duplicate-source split with KOMODO medium `869`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml --out /private/tmp/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes DSMZ/MediaDive medium 869. The inspected MediaDive payload reports `id: 869`, `ANAEROBIC TRYPTIC SOY BROTH MEDIUM`, pH 5.5, source `DSMZ`, and the DSMZ Medium 869 PDF link; the inspected PDF has the same medium number and title.

The source identity is not fully canonical in generated output. A separate KOMODO `869` owner, `data/normalized_yaml/bacterial/clostridium_ck_medium.yaml`, also points to DSMZ 869 but was transformed into inferred Trypticase soy broth constituents with a Wikipedia-backed commercial-product note. The DSMZ record does not decompose the 5.5 g Trypticase soy broth powder this way, so the KOMODO record should be reconciled to source-faithful DSMZ 869 or held as a distinct derived estimate instead of silently splitting the DSMZ 869 source.

The available ontology grounding is acceptable at this level: `D-Glucose` is correctly grounded to `CHEBI:17634`, resazurin is grounded, and unresolved `Trypticase soy broth` is a complex commercial powder.

## Evidence

Supported:

- DSMZ 869 and MediaDive support 5.50 g Trypticase soy broth, 0.50 ml 0.1 percent resazurin, 2.00 g D-glucose, and 1000 ml distilled water.
- MediaDive correctly converts 0.50 ml of 0.1 percent resazurin to `0.0005 G_PER_L`.
- DSMZ 869 supports pH 5.5, N2 sparging, anoxic Hungate-type tubes or serum vials, autoclaving the base medium, and adding glucose from a separately sterilized anoxic stock solution.
- DSMZ 869 explicitly notes a DSM 12992-specific variant that adjusts the complete medium to pH 6.5; the separate `medium_869_modified_for_dsm_12992` owner therefore represents a legitimate variant identity rather than a duplicate of the base medium.

Unsupported or over-scoped:

- The source 1000 ml distilled-water row is missing.
- The glucose row is chemically and quantitatively correct but loses the fact that glucose is added from a separately sterilized anoxic stock.
- The DSMZ `BD BBL` qualifier on Trypticase soy broth is lost.
- The source preparation is collapsed into one `AUTOCLAVE` step that also includes the post-autoclave glucose stock addition.
- No structured reference ties the DSMZ PDF or MediaDive payload to the imported formulation.

## Completeness

Consequential gaps:

- Water is absent, so the final-volume basis is implicit rather than auditable.
- The glucose stock addition is not explicit.
- The DSMZ source brand qualifier for the TSB powder is not represented.
- No structured reference entry captures the DSMZ PDF or MediaDive source beyond the prose `notes` field.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. DSMZ Medium 869 is a recipe source, not primary growth evidence.
- The DSM 12992 pH 6.5 variant is absent from this base record but exists as a separate KOMODO-derived owner.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'mediadive.medium:869' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found this specialized DSMZ 869 owner, this generated merge, the DSM 12992 variant, and the KOMODO `clostridium_ck_medium` owner.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | major | KOMODO medium 869 is a second DSMZ 869 import but is generated separately as `clostridium_ck_medium` after expanding Trypticase soy broth into inferred constituents, so the source identity is split across conflicting source records. | `data/normalized_yaml/bacterial/clostridium_ck_medium.yaml`, `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml`, and KOMODO/TSB normalization rules |
| F2 | major | The 1000 ml water row is missing from the MediaDive DSMZ 869 owner and generated merge. | `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml` and the MediaDive importer |
| F3 | major | The separately sterilized anoxic glucose stock addition is collapsed into a normal top-level dry ingredient and the preparation step marks the whole paragraph as `AUTOCLAVE`. | `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml` and the MediaDive step importer |
| F4 | minor | The DSMZ `BD BBL` qualifier for Trypticase soy broth is missing. | `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml` |
| F5 | minor | DSMZ and MediaDive sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml` |

## Recommended Edits

1. Restore the 1000 ml distilled-water row.
2. Preserve the glucose row as 2 g final D-glucose while representing that it comes from a separately sterilized anoxic stock.
3. Split preparation into base-medium dissolution, N2 sparging, pH 5.5 adjustment, anoxic dispensing, autoclaving, and post-autoclave glucose stock addition.
4. Add the `BD BBL` qualifier to the Trypticase soy broth source label or notes.
5. Add structured references for MediaDive 869 and DSMZ Medium 869.
6. Reconcile KOMODO medium 869 with this source-faithful DSMZ record, or explicitly mark the constituent-expanded KOMODO record as a derived estimate rather than a second canonical DSMZ 869 formulation.
7. Regenerate `data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml` and any affected KOMODO-derived merge.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on `data/normalized_yaml/specialized/anaerobic_tryptic_soy_broth_medium.yaml`.
- Re-run the same focused validators on regenerated `data/merge_yaml/merged/ANAEROBIC_TRYPTIC_SOY_BROTH_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove normalized edits are reflected in generated merges.
- Search ignored and tracked data for `mediadive.medium:869`, `komodo.medium:869`, and `komodo.medium:869_12992` to confirm the base DSMZ 869 import and DSM 12992 variant are reconciled as intended.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The inspected generated merge and normalized owner are identical through the source-owned fields; the generated record only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`.
