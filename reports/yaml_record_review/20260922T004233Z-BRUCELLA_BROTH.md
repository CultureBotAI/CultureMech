# YAML Record Review: Brucella Broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BRUCELLA_BROTH.yaml
- Started UTC: 2026-09-22T00:42:33Z
- Finished UTC: 2026-09-22T00:42:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009933 |
| Label | brucella_broth |
| Original label | Brucella Broth |
| Category | bacterial |
| Source accession | TOGO:M540 |
| Original source | JCM_M538 / GRMD 538 |
| Generated path | data/merge_yaml/merged/BRUCELLA_BROTH.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml |
| Merge fingerprint | 773cc09417493598852ca397d293777b7b84204bb5aefd1f56f0705860190173 |

The reviewed target is a generated merge under `data/merge_yaml/merged`, derived
from `TOGO_M540_Brucella_Broth`. Future formulation and growth-evidence fixes
belong in `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` or in
the maintained duplicate metadata that should reconcile it with the direct JCM
J538 import.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BRUCELLA_BROTH.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BRUCELLA_BROTH.yaml --out /private/tmp/BRUCELLA_BROTH.strict.tsv --workers 1 --quiet` | Passed; TSV contained only the header |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BRUCELLA_BROTH.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BRUCELLA_BROTH.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/BRUCELLA_BROTH.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and
`just validate-references` were not rerun because the project uv environment tries
to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The record's TOGO identity is internally coherent. The live TOGO M540 payload
identifies the medium as `Brucella Broth`, records `original_media_id:
JCM_M538`, names the JCM GRMD 538 URL, reports pH 7.0, and lists Brucella
Broth's one-liter formula with distilled water, pancreatic digest of casein,
peptic digest of animal tissue, yeast extract, NaCl, glucose, and NaHSO3.

The original JCM GRMD 538 URL currently returns `Nothing found`, so the JCM 538
identity is no longer directly verifiable from the current JCM site. The
repository also contains an active direct-JCM MediaDive owner,
`data/normalized_yaml/bacterial/brucella_broth.yaml`, with
`CultureMech:002886`, `mediadive.medium:J538`, pH 7.0, and the same six dry
ingredient rows. That record is the same Brucella Broth source without TOGO's
explicit distilled-water row and should be reconciled with the M540 owner rather
than remaining a separate generated medium.

The CHEBI mappings for water, sodium chloride, glucose, and sodium
hydrogensulfite are appropriate. Yeast extract, pancreatic digest of casein, and
peptic digest of animal tissue are undefined digest or extract materials and are
properly unmapped.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| TOGO M540 denotes Brucella Broth from JCM 538 | The TOGO API reports M540 with name `Brucella Broth`, `JCM_M538`, and the GRMD 538 URL |
| Basal recipe includes 10 g/L pancreatic digest of casein, 10 g/L peptic digest of animal tissue, 2 g/L yeast extract, 5 g/L NaCl, 1 g/L glucose, and 0.1 g/L NaHSO3 | TOGO M540 lists those six rows; the direct MediaDive/JCM J538 owner has the same six dry rows |
| pH should be 7.0 | TOGO M540 reports `ph: 7.0`, and the direct MediaDive/JCM J538 owner already carries `ph_value: 7.0` |
| PMID 10609610 is a relevant Brucella Broth growth paper | The full text used *Helicobacter pylori* OMU89-362, inoculated it into BB/FBS, and measured OD620 after 37 C microaerobic shaking |
| The growth stimulation in BB/FBS reached a maximum at 3.5 mM H2O2 | PMID 10609610 Figure 1 and Table 1 support maximal stimulation at 3.5 mM H2O2 in Brucella Broth with 10% FBS |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| `Distilled water`, `1 G_PER_L` | TOGO M540 says 1 L, so this should be a liter or milliliter solvent quantity, not one gram per liter. |
| No `ph_value` in the TOGO owner or generated merge | TOGO M540 says pH 7.0, and the duplicate direct-JCM owner already preserved it. |
| No structured TOGO/JCM formulation reference | The only structured reference is `PMID:10609610`, which supports the *H. pylori* variant experiment but not the base JCM formula. TOGO M540 and the direct JCM 538 provenance remain free text in `notes`. |
| One generated record for TOGO M540 and another for MediaDive/JCM J538 | TOGO explicitly wraps JCM_M538, and both local owners carry the same Brucella Broth formula under different source accessions and CultureMech IDs. |
| `max_od600: 0.724` with `max_od_wavelength_nm: 620` under a condition described as BLBB/FBS pretreated with 3.5 mM H2O2 and catalase | PMID 10609610 Table 3 reports OD620 0.724 for BLBB/FBS after H2O2 then phosphate buffer then distilled water, not for the row that used catalase. The catalase plus distilled-water row was 0.839, while BB/FBS plus 3.5 mM H2O2 was 0.650 in Tables 1 and 2. |
| The FBS/H2O2 variant does not model bisulfite removal | The metric is attached to bisulfite-less Brucella Broth, whose formula removes the 0.1 g/L sodium bisulfite present in the parent JCM medium. The variant modifications add FBS and H2O2 but never remove NaHSO3. |

## Completeness

The basal TOGO formulation is not complete: the owner needs pH 7.0, a corrected
distilled-water unit, structured TOGO/JCM references, and a representation of
the TOGO comment that commercial Brucella Broth is also available. A direct
JCM/MediaDive owner for J538 already records pH 7.0 and the commercial-availability
comment but lacks TOGO's one-liter solvent row, so neither source copy is a full
reconciled representation of the TOGO M540 payload.

The PMID 10609610 growth evidence is partly supported but over-compressed. The
paper compares BB/FBS, BHIB/FBS, BLBB/FBS, bisulfite add-back, H2O2, and catalase
treatments. The current `brucella_broth_fbs_h2o2_helicobacter_pylori` variant
captures only FBS and H2O2 addition, while its numeric metric is from a BLBB/FBS
pretreatment condition with no NaHSO3 and no catalase. That condition cannot be
reconstructed from the variant's listed modifications.

A gitignore-independent `rg --no-ignore --hidden --pcre2` search for
`CultureMech:009933`, `TOGO:M540`, `JCM_M538`, `GRMD=538`, the
`TOGO_M540_Brucella_Broth` owner slug, and merge fingerprint `773cc0...` covered
hidden and ignored files under `data/normalized_yaml`, `data/merge_yaml/merged`,
ID registries, generated indexes, archived validation reports, growth-review
reports, media reports, and existing YAML review reports. It found one TOGO M540
normalized owner, this generated merge, expected index/report references, and the
direct-JCM `brucella_broth.yaml` sibling. I found no pre-existing
`reports/yaml_record_review/*BRUCELLA_BROTH.md` report.

The missing genome or BioSample identifier for *H. pylori* OMU89-362 is already
called out in `reports/media_growth_review_corpus_scope.md` and remains a bounded
strain-level growth-evidence gap. Empty stock-solution and solidification fields
are expected because this is a liquid complex broth with no stock additions.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | Distilled water is imported with the wrong unit: TOGO M540 has 1 L, but the maintained owner and generated merge store `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` and the TOGO import repair path for liter solvent rows |
| Major | The TOGO M540 owner is missing pH 7.0, structured formulation references, and the source comment about commercial Brucella Broth, so the generated merge is less complete than the inspected TOGO payload. | `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` |
| Major | JCM 538 is represented twice as active Brucella Broth owners: TOGO M540 under `CultureMech:009933` and direct MediaDive/JCM J538 under `CultureMech:002886`. They are not linked as source duplicates and still produce separate generated records because each retained different pieces of the source. | Duplicate metadata and normalized owners for `TOGO_M540_Brucella_Broth.yaml` and `brucella_broth.yaml` |
| Major | The PMID 10609610 growth metric misstates the experimental condition behind OD620 0.724. The recorded value comes from the Table 3 BLBB/FBS row pretreated with H2O2 and no catalase, not a catalase-treated row or the BB/FBS plus H2O2 condition modeled in `brucella_broth_fbs_h2o2_helicobacter_pylori`. | `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` |

No blocker or minor findings found.

## Recommended Edits

1. Correct the TOGO M540 distilled-water row to a liter or `1000 ML_PER_L`
   solvent quantity in `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml`.
2. Add TOGO M540/JCM 538 structured references, `ph_value: 7.0`, and a scoped
   note or preparation/comment field for the commercial Brucella Broth comment
   to the TOGO owner.
3. Reconcile `TOGO_M540_Brucella_Broth.yaml` with
   `data/normalized_yaml/bacterial/brucella_broth.yaml` as source-duplicate views
   of the same JCM 538 medium, preserving the TOGO solvent row and the direct-JCM
   pH/comment data.
4. Revisit the PMID 10609610 variant. Either record a BB/FBS plus 3.5 mM H2O2
   metric with OD620 0.650 from Tables 1 and 2, or explicitly model the
   bisulfite-less Brucella Broth experiment that produced OD620 0.724 by removing
   NaHSO3 and using the correct no-catalase Table 3 treatment.
5. Continue the genome/BioSample search for *H. pylori* OMU89-362 and attach the
   exact strain genome only if one is found.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml`.
- Rerun the duplicate/source-duplicate merge workflow and confirm exact
  `TOGO:M540` and exact `mediadive.medium:J538` no longer emit two independent
  Brucella Broth records.
- Rerun `just verify-merges` and inspect the regenerated
  `data/merge_yaml/merged/BRUCELLA_BROTH.yaml` and
  `data/merge_yaml/merged/brucella_broth__a969823c.yaml` diff.
- Manually compare TOGO M540 and the PMID 10609610 PDF to the updated normalized
  owner to confirm the basal recipe, pH, variant modifications, strain, and OD620
  measurement condition all have nearest-source support.

## Additional Notes

- The current JCM GRMD 538 page returned `Nothing found`; ignored-file-inclusive
  local search plus TOGO M540 were enough to identify the direct JCM duplicate,
  but not to re-verify a live JCM 538 page.
- The PubMed abstract confirms the broad BB/FBS/H2O2 result but not the OD620
  0.724 value. The numeric mismatch was only visible after fetching the J-STAGE
  full-text PDF and inspecting the table on page 1012.
