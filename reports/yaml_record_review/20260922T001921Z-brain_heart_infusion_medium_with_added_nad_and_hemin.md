# YAML Record Review: brain heart infusion medium (with added NAD and hemin)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml
- Started UTC: 2026-09-22T00:19:21Z
- Finished UTC: 2026-09-22T00:21:04Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009491` |
| Name | `brain_heart_infusion_medium_with_added_nad_and_hemin` |
| Original name | brain heart infusion medium (with added NAD and hemin) |
| Source grounding | `TOGO:M2969` |
| Merge fingerprint | `be5722aee9dad2c6be640ba3087d1f220737d226c04a2e280eca99a2c34f4a15` |

This is a generated one-source merge of the normalized bacterial TOGO import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` | Pass |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml --out /private/tmp/brain_heart_infusion_medium_with_added_nad_and_hemin.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

The stable CultureMech ID and generated filename agree with the normalized owner and the TOGO grounding. A gitignore-independent exact search covering `data`, `reports`, and the repository root found one maintained owner under `data/normalized_yaml/bacterial/`, one generated merge under `data/merge_yaml/merged/`, expected normalized indexes, legacy import reports, and old curation-candidate rows for `CultureMech:009491`, `TOGO:M2969`, the merge fingerprint, and the record slug.

TOGO M2969 identifies the medium as `brain heart infusion medium (with added NAD and hemin)`. Its component list contains 1 L `brain heart infusion medium (Difco)`, plus separate `hemin (ICN)` and `NAD (Sigma)` growth-factor entries. That source supports the record identity and its BHI/NAD/hemin outline, but not the record's replacement of 1 L BHI with a fully enumerated BD 237500 commercial BHI formula.

## Evidence

Supported:

- `media_term.term.id: TOGO:M2969` and `media_term.term.label` match the TOGO M2969 API payload.
- The physical state is plausibly liquid because the TOGO component is 1 L BHI medium, not agar.
- The source supports undefined complex medium classification: the base BHI component carries TOGO/GMO undefined and complex component annotations.
- TOGO supports retaining `hemin (ICN)` and `NAD (Sigma)` as added growth factors.

Unsupported or over-scoped:

- The TOGO seed source does not enumerate calf brain, beef heart, proteose peptone, glucose, sodium chloride, or disodium phosphate rows. Those rows were inferred from an external commercial BHI composition note and all point to an uncurated Microbe Notes URL, even though M2969 only said `brain heart infusion medium (Difco)`, 1 L.
- The commercial decomposition is internally narrower and more specific than its source: the TOGO item names Difco BHI, while the generated rows claim `Difco/BD Brain Heart Infusion`, catalog `237500`, and a 2026-03-28 Microbe Notes lookup.
- The hemin and NAD entries have no ontology grounding and no concentrations. TOGO gives source brands and GMO IDs, but no masses or final concentrations; a reproducible record needs the primary recipe that TOGO summarized or an explicit decision to keep those additions unknown.
- The TOGO comment says the formulation was used for NTHi strains, but the record has only the generic `Microbial cultivation` application and no organism scope, strain scope, or primary citation for the non-typeable *Haemophilus influenzae* context.

## Completeness

Consequential gaps:

- The maintained owner should preserve the 1 L BHI commercial base or replace it with a cited Difco/BD product formula from an inspected authoritative source. The current split rows lose the fact that the seed recipe used a prepared BHI medium as one component.
- Hemin and NAD need exact units, supplier context, and term grounding. The current `VARIABLE` concentrations make the recipe non-reproducible.
- The NTHi source context behind TOGO M2969 is missing. TOGO exposes the culture sentence but not a `src_url`; no DOI, PMID, PMC ID, or paper title is recorded locally.
- `target_organisms`, source-citation objects, and a curation-quality flag for unresolved additive concentrations are absent.

Empty optional slots that are acceptable as empty:

- The source did not expose strain IDs, oxygen conditions, incubation temperature, or sterilization instructions, so those condition and preparation fields should stay empty until the primary publication is curated.

Bounded searches:

- A gitignore-independent exact search for `TOGO:M2969`, `CultureMech:009491`, `brain_heart_infusion_medium_with_added_nad_and_hemin`, and the merge fingerprint covered `data`, `reports`, and the repository root. It found no duplicate maintained owner for this ID.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*brain_heart_infusion_medium_with_added_nad_and_hemin.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The record replaces TOGO's 1 L Difco BHI base with a BD 237500 constituent list that M2969 does not provide. | The TOGO API lists one `brain heart infusion medium (Difco)` item at 1 L. The YAML instead stores six inferred BHI subingredients with `Difco/BD Brain Heart Infusion` supplier catalog rows and a Microbe Notes product URL. | `data/normalized_yaml/bacterial/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` |
| major | The added hemin and NAD growth factors are not reproducible. | TOGO lists `hemin (ICN)` and `NAD (Sigma)`, but the generated YAML has no concentrations or term IDs for either additive. | `data/normalized_yaml/bacterial/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` |
| major | The record lacks the primary NTHi evidence and organism scope behind the TOGO excerpt. | The TOGO API comment describes cultivation of NTHi strains on supplemented BHI, but the YAML records neither non-typeable *Haemophilus influenzae* nor any DOI, PMID, or PMC source for that culture condition. | `data/normalized_yaml/bacterial/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml`, replace the unsupported six-row BHI decomposition with a 1 L `brain heart infusion medium (Difco)` base component, unless a curator inspects an authoritative Difco source that supports expanding the base.
2. Search the primary NTHi publication behind TOGO M2969, then curate exact hemin and NAD concentrations with units, term IDs, and source evidence if the publication provides them.
3. Add a primary citation and attach it to the narrow NTHi cultivation claim; include the relevant organism or strains in `target_organisms` if the evidence supports them.
4. If the primary source cannot resolve additive concentrations, keep the `VARIABLE` amounts but add an explicit quality flag or discussion note documenting that TOGO M2969 omits them.
5. Regenerate `data/merge_yaml/merged/brain_heart_infusion_medium_with_added_nad_and_hemin.yaml` from the maintained owner after curation.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch TOGO M2969 and manually confirm that the curated BHI/NAD/hemin ingredients still represent the source entry without inventing unsupported Difco or Sigma details.
- Repeat a gitignore-independent exact search for `TOGO:M2969` and `CultureMech:009491` to confirm only the normalized owner and generated artifacts changed.

## Additional Notes

The gitignore-independent exact search also found `data/curation/organism_candidates.json` and `data/curation/organism_review.csv` rows pointing at the old path `bacterial/TOGO_M2969_brain_heart_infusion_medium_with_added_NAD_and_hemin.yaml`. Those are stale raw curation-candidate references rather than a second live YAML owner.
