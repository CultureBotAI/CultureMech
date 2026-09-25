# YAML Record Review: ATALASSOTOGA_AZC2201_MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml
- Started UTC: 2026-09-21T16:24:25Z
- Finished UTC: 2026-09-21T16:26:27Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007801` |
| Label | `atalassotoga_azc2201_medium` |
| Original label | `Atalassotoga AZC2201 Medium` |
| Category | `bacterial` |
| Source identity | `TOGO:M1269`; original JCM `JCM_M1184` |
| Source URL | `https://togomedium.org/medium/M1269`; `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1184` |
| Generated status | Generated on 2026-08-06 from `data/normalized_yaml/bacterial/TOGO_M1269_Atalassotoga_AZC2201_Medium.yaml` |
| Merge fingerprint | `897e1ed821d6eba4242e68bc418092126cd2efd3c950d22db8631c1f5c0af838` |

`data/merge_yaml/merged/` is derived output. Future fixes belong in
`data/normalized_yaml/bacterial/TOGO_M1269_Atalassotoga_AZC2201_Medium.yaml` or
the Togo importer, then this generated file should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml` | Pass. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml --out /private/tmp/ATALASSOTOGA_AZC2201_MEDIUM.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. The only emitted message was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused validator for embedded `MediaRecipe.curation_history` is documented for one merged recipe. `just validate-history` targets standalone records under `history/`. |

Direct `just` validation was not used because this checkout currently reaches a
project `uv` build of `llvmlite==0.46.0` under Python 3.13 before target-specific
validation and fails in `setuptools` with `TypeError: Popen.__init__() got an
unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- The generated ID, label, and `media_term` identify Togo Medium M1269,
  `Atalassotoga AZC2201 Medium`, with JCM GRMD 1184 recorded as the original
  source.
- The Togo SPARQLIST API for `M1269` resolves and returns the same name,
  `original_media_id` of `JCM_M1184`, and `src_url` pointing at JCM
  `GRMD=1184`.
- The cited JCM `GRMD=1184` page currently returns a small "Nothing found"
  response, so direct JCM primary-source verification is unresolved.
- The Togo source and generated record agree on the 10 named simple base
  ingredients and the seven post-autoclave solution additions, but the import
  corrupts units for water, resazurin, and every solution addition.

## Evidence

| Claim in generated record | Review |
|---|---|
| Distilled water at 1 `G_PER_L` | Wrong unit. The Togo API lists 1 litre of distilled water in main solution 1. |
| MgSO4.7H2O, NaCl, CaCl2.2H2O, KH2PO4, K2HPO4, MgCl2.6H2O, KCl, `(NH4)2SO4`, and L-Cysteine.HCl.H2O at their direct g/L amounts | Supported by Togo main solution 1. |
| Resazurin at 1 `G_PER_L` | 1000-fold too high. Togo lists 1 mg, not 1 g, in main solution 1. |
| FeCl2, trace element, Fe-Ni-WO-Se, yeast extract, fructose, Na2S2O3, and vitamin solution descriptors at `G_PER_L` values | Wrong unit. Togo lists these additions after autoclaving as 1, 1, 1, 10, 20, 10, and 1 ml per litre, respectively. |
| No preparation steps | Incomplete. Togo carries pH 4.0 adjustment, boiling and cooling under nitrogen, dispensing under nitrogen, autoclaving, and post-cooling aseptic anaerobic addition of the seven solutions. |

## Completeness

- A corrected `find data/normalized_yaml/bacterial \( -name
  'TOGO_M1269_Atalassotoga_AZC2201_Medium.yaml' -o -name
  'atalassotoga_azc2201_medium.yaml' \) -print` search covers ignored files and
  finds both the Togo M1269 owner and a same-source JCM owner at
  `data/normalized_yaml/bacterial/atalassotoga_azc2201_medium.yaml`.
- An ignored-file-inclusive exact search for `CultureMech:007801`,
  `TOGO:M1269`, `M1269`, `JCM_M1184`, `GRMD=1184`, and `Atalassotoga AZC2201`
  across `data`, `reports`, `history`, and `.claude` found this Togo owner, the
  separate JCM owner, generated/index records, import QC reports, and archived
  validation rows.
- `find reports/yaml_record_review -maxdepth 1 \( -name
  '*ATALASSOTOGA_AZC2201_MEDIUM.md' -o -name
  '*atalassotoga_azc2201_medium*.md' \) -print` searched the ignored report
  directory and found no prior review for this pair of generated Atalassotoga
  stems before this report was written.
- The source-specific preparation comment is absent, leaving pH, anaerobic
  handling, dispensing, sterilization, and post-autoclave supplement timing
  unrepresented in the Togo record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Seven post-autoclave solution additions use mass-concentration units for source millilitre additions. | Togo lists FeCl2, trace element, Fe-Ni-WO-Se, yeast extract, fructose, Na2S2O3, and vitamin additions in ml per litre; the generated record stores the same numeric values as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1269_Atalassotoga_AZC2201_Medium.yaml` or the Togo importer. |
| major | Resazurin is 1000-fold too concentrated. | Togo lists 1 mg of Resazurin; the generated record says 1 `G_PER_L`. | Same Togo owner or importer. |
| major | The Togo preparation comment was dropped. | The API carries pH 4.0 adjustment, boil/cool under nitrogen, anaerobic dispensing, autoclaving, and post-cooling anaerobic supplement addition instructions; the record has no `preparation_steps`. | Same Togo owner or importer. |
| major | Distilled water is represented as a mass concentration. | Togo lists 1 L distilled water for main solution 1; the record says 1 `G_PER_L`. | Same Togo owner or importer. |
| major | The same JCM source exists as two generated CultureMech records with incompatible modeling. | `data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml` is Togo M1269 copied from JCM M1184, while `data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml` is a separate JCM GRMD 1184 import. | Merge/deduplication rules plus both maintained owners. |

## Recommended Edits

1. Convert all seven Togo post-autoclave solution additions from `G_PER_L` to
   `ML_PER_L`, preserving their source-stated 1, 1, 1, 10, 20, 10, and 1 ml
   values.
2. Change Resazurin from `1 G_PER_L` to the 1 mg/L source amount.
3. Represent distilled water as the 1 litre make-up volume instead of
   `1 G_PER_L`.
4. Import the Togo preparation comment into ordered steps for pH adjustment,
   nitrogen handling, anaerobic distribution, autoclaving, and post-cooling
   addition of the filter-sterilized or autoclaved solutions.
5. Decide whether the Togo M1269 and direct JCM 1184 owners should be merged or
   explicitly linked as source duplicates before regenerating both Atalassotoga
   generated records.

## Follow-up Checks

- Rerun open-schema, strict, term, and reference validation on the Togo
  Atalassotoga owner after correction.
- Rerun the concentration plausibility audit and confirm it no longer flags
  Resazurin at 1 g/L.
- Verify the regenerated merge has seven `ML_PER_L` solution additions and no
  `Unknown solution` placeholders for solution names whose source already gives
  labels.
- Re-run duplicate-stem review for the Togo and direct JCM Atalassotoga owners
  after curation.

## Additional Notes

- The JCM source page cited by Togo returned an 844-byte HTML page stating that
  no medium was found for GRMD 1184 at review time. The Togo API payload was
  therefore the inspected source for ingredient and preparation claims in this
  report.
