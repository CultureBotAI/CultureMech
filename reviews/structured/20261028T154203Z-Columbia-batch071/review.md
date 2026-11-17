# Scientific review of Columbia

- Review: 20261028T154203Z-Columbia-batch071
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T15:21:27.720238Z
- Finished UTC: 2026-10-28T15:42:03.340045Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

All fourteen Columbia broth rates match the exact FEBA section and can be retained. Curation is needed for supplied-material mappings, one canonical-label difference and claim-level source traceability. Preparation and growth conditions remain unsupported by the scoped source.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch071 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015503 | data/merge_yaml/merged/Columbia.yaml | generated | Columbia |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015503 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:015503 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:015503 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:015503 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact source and material identity

identity: concern. Targets: CultureMech:015503.

The full Columbia section in the version-pinned FEBA media file matches all fourteen local amounts and the broth description. Its complex digests and extracts support COMPLEX/UNDEFINED, and broth supports LIQUID. The generic CultureBotHT repository API returned 404, so the historical import file and exact historical upstream version were not recovered. Specialized is an importer fallback category, not proof of an organism association.

### Preparation and growth evidence limits

evidence: unknown. Targets: CultureMech:015503.

The scoped FEBA section supplies rates but no preparation protocol, pH, incubation conditions, strain identity or experimental growth result. These remain unknown; no typical protocol or organism is inferred from the medium name. The neighboring FEBA sections are excluded.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:015503.

Both October reports perform zero external source checks; their unchanged amount tables are derivative summaries. The current importer shallow-copies upstream fields and records a generic repository URL; its present behavior cannot authenticate the original source retrieval. Current conservative merging preserves scientific fields and rejects incompatible formulations. Inspected writer behavior is described separately by exact file and function; it does not prove historical execution.

### Every concentration and source-only amount/stage

quantity: supported. Targets: CultureMech:015503.

All 28 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{
  "schema": "private explicit quantity decisions v1",
  "target_id": "CultureMech:015503",
  "selected_concentration_field_count": 28,
  "selected_concentration_fields_covered": 28,
  "decisions": [
    {
      "decision_id": "q1",
      "subject": "Proteose Peptone",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[0].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 5 g/L for Proteose Peptone. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4594-4594",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Proteose Peptone\t5\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q2",
      "subject": "Pancreatic digest of casein",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "10",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[1].concentration",
          "original": {
            "value": "10",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 10 g/L for Pancreatic digest of casein. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4595-4595",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Pancreatic digest of casein\t10\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q3",
      "subject": "Yeast Extract",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[2].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 5 g/L for Yeast Extract. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4596-4596",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Yeast Extract\t5\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q4",
      "subject": "Beef Heart Infusion ",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "3",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[3].concentration",
          "original": {
            "value": "3",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 3 g/L for Beef Heart Infusion. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4597-4597",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Beef Heart Infusion \t3\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q5",
      "subject": "D-Glucose",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "2.5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[4].concentration",
          "original": {
            "value": "2.5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 2.5 g/L for D-Glucose. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4598-4598",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "D-Glucose\t2.5\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q6",
      "subject": "Sodium Chloride",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[5].concentration",
          "original": {
            "value": "5",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 5 g/L for Sodium Chloride. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4599-4599",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Sodium Chloride\t5\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q7",
      "subject": "Sodium carbonate",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.6",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[6].concentration",
          "original": {
            "value": "0.6",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.6 g/L for Sodium carbonate. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4600-4600",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Sodium carbonate\t0.6\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q8",
      "subject": "Iron(II) Sulfate",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[7].concentration",
          "original": {
            "value": "0.02",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.02 g/L for Iron(II) Sulfate. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4601-4601",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Iron(II) Sulfate\t0.02\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q9",
      "subject": "Magnesium sulfate",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[8].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.1 g/L for Magnesium sulfate. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4602-4602",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Magnesium sulfate\t0.1\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q10",
      "subject": "L-Cysteine HCL",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[9].concentration",
          "original": {
            "value": "0.1",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.1 g/L for L-Cysteine HCL. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4603-4603",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "L-Cysteine HCL\t0.1\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q11",
      "subject": "Tris(hydroxymethyl)aminomethane",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "0.83",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[10].concentration",
          "original": {
            "value": "0.83",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.83 g/L for Tris(hydroxymethyl)aminomethane. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4604-4604",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Tris(hydroxymethyl)aminomethane\t0.83\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q12",
      "subject": "Tris hydrochloride",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "2.86",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[11].concentration",
          "original": {
            "value": "2.86",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 2.86 g/L for Tris hydrochloride. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4605-4605",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Tris hydrochloride\t2.86\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q13",
      "subject": "Hemin",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "0.005",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[12].concentration",
          "original": {
            "value": "0.005",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.005 g/L for Hemin. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4606-4606",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Hemin\t0.005\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    },
    {
      "decision_id": "q14",
      "subject": "Menadione",
      "local_fields": [
        {
          "record_path": "data/merge_yaml/merged/Columbia.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.001",
            "unit": "G_PER_L"
          }
        },
        {
          "record_path": "data/normalized_yaml/specialized/columbia.yaml",
          "field_path": "ingredients[13].concentration",
          "original": {
            "value": "0.001",
            "unit": "G_PER_L"
          }
        }
      ],
      "decision": "evidence_only",
      "stage": "Explicit FEBA Columbia broth rate",
      "interpretation": "The exact version-pinned Columbia section explicitly states 0.001 g/L for Menadione. Both current layers retain this amount and unit. Newly captured source support can be attached without changing the value; there is no existing claim-scoped source evidence to mark verified. No stock dilution or final-batch arithmetic is needed.",
      "sources": [
        {
          "locator": "extracted-text lines 4607-4607",
          "source_key": "febaMedia",
          "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
          "source_raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "source_text_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
          "accessed_at": "2026-10-28T15:22:09.157085Z",
          "exact_source_quote": "Menadione\t0.001\tg/L",
          "quote_representation": "captured extracted text"
        }
      ]
    }
  ],
  "local_field_census_reference": "REVIEW_WORK/batch071/record04/grounding-inventory.json",
  "source_only_gaps_are_explicit": true,
  "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."
}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:015503.

data/merge_yaml/merged/Columbia.yaml: primary 14/14, secondary 0/14; data/normalized_yaml/specialized/columbia.yaml: primary 14/14, secondary 0/14. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:015503.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:015503.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Tris hydrochloride and heart infusion are mapped to different material identities

major / open / confirmed; issue key: culturemech-015503-material-form-grounding.

Both layers map Tris hydrochloride to CHEBI:9754, whose current formula C4H11NO3 describes tris base rather than its hydrochloride. They map Beef Heart Infusion to UBERON:0000948, the anatomical heart organ rather than an infusion product. The distinct source labels and correct rates should remain. The source also does not specify hydration for Iron(II) Sulfate, so its anhydrous assertion CHEBI:75832 is not independently established here; no hydrate replacement or molar calculation is justified.

### f2: Proteose peptone label differs from the current canonical label

minor / open / confirmed; issue key: culturemech-015503-proteose-canonical-label.

MICRO:0000180 resolves to proteose peptone, while both term labels capitalize Proteose. The identity is supported; this is literal label correspondence only, not an ingredient replacement.

### f3: Matching FEBA rates lack claim-scoped source evidence

minor / open / confirmed; issue key: culturemech-015503-claim-level-source-provenance.

Both layers retain the FEBA note and generic CultureBotHT source link but no exact versioned formulation citation or claim-level excerpts. The current FEBA section authenticates its explicit rates; the 404 repository response and derivative October reports cannot authenticate the historical import execution or access time.

## Recommended Actions And Acceptance Checks

### action1

Resolve each exact supplied material against an appropriate ontology or retain the precise source label with mapping explicitly unresolved. Do not map a commercial infusion to an anatomical organ or merge tris hydrochloride with tris base. Preserve all supported rates; document the iron hydration limit without guessing a replacement.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Refresh only the canonical term label to the exact current authority label while retaining preferred_term and the supported ingredient identity.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Attach the exact FEBA version and matching excerpts at the supported claims. Preserve all historical events unchanged; append any newly verified source context with the actual curation date and record the unrecovered historical upstream version.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/Columbia.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/specialized/columbia.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch071/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch071/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch071/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch071/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17634 = D-glucose; definition ['A glucose with &lt;small&gt;D&lt;/small&gt;-configuration.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi28869 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28869; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:28869 = menadione; definition ['A member of the class of 1,4-naphthoquinones that is 1,4-naphthoquinone which is substituted at position 2 by a methyl group. It is used as a nutritional supplement and for the treatment of hypoprothrombinemia.']; formula ['C11H8O2']; mass ['172.183']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:50385 = hemin; definition ['It is used as a prescription medication to relieve repeated attacks of acute intermittent porphyria related to the menstrual cycle in affected women.']; formula ['C34H32ClFeN4O4']; mass ['651.952']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75832 = iron(2+) sulfate (anhydrous); definition ['A compound of iron and sulfate in which the ratio of iron(2+) to sulfate ions is 1:1. Various hydrates occur naturally - most commonly the heptahydrate, which loses water to form the tetrahydrate at 57°C and the monohydrate at 65°C.']; formula ['Fe.O4S']; mass ['151.908']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91247 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91247 = L-cysteine hydrochloride; definition ['A hydrochloride obtained by combining &lt;small&gt;L&lt;/small&gt;-cysteine with one molar equivalent of hydrogen chloride.']; formula ['C3H7NO2S.HCl']; mass ['157.622']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:9754 = tris; definition ['A primary amino compound that is &lt;em&gt;tert&lt;/em&gt;-butylamine in which one hydrogen attached to each methyl group is replaced by a hydroxy group. A compound widely used as a biological buffer substance in the pH range 7—9; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 8.3 at 20 °C; p&lt;em&gt;K&lt;/em&gt;&lt;small&gt;&lt;sub&gt;a&lt;/sub&gt;&lt;/small&gt; = 7.82 at 37 °C.']; formula ['C4H11NO3']; mass ['121.136']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact FOODON:03315426 = yeast extract; definition ['SIREN DB annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact MICRO:0000180 = proteose peptone; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact MICRO:0000182 = tryptone; definition []; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact UBERON:0000948 = heart; definition ['Taxon notes:" the ascidian tube-like heart lacks chambers....The ascidian heart is formed after metamorphosis as a simple tube-like structure with a single-layered myoepithelium that is continuous with a single-layered pericar- dial wall. It lacks chambers and endocardium.... The innovation of the chambered heart was a key event in vertebrate evolution, because the chambered heart generates one-way blood flow with high pressure, a critical requirement for the efficient blood supply of large-body vertebrates... all extant vertebrates have hearts with two or more chambers (Moorman and Christoffels 2003)" DOI:10.1101/gad.1485706', 'A myogenic muscular circulatory organ found in the vertebrate cardiovascular system composed of chambers of cardiac muscle. It is the primary circulatory organ.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| trisHClSearch | https://www.ebi.ac.uk/ols4/api/search?q=tris%20hydrochloride&amp;ontology=chebi&amp;exact=true; raw source; exact captured text/DOM/JSON locators in quantity inventory | context_only | Bounded current OLS exact search for tris hydrochloride returned no matches. No replacement identifier is inferred from this search; this is discovery evidence only. |
| febaMedia | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Only the complete version-pinned FEBA Columbia section (heading and fourteen explicit g/L rows) was read scientifically; neighboring medium sections are excluded. This dataset does not provide preparation, pH or experimental growth evidence for this record. |
| culturebotHT | https://api.github.com/repos/CultureBotAI/CultureBotHT; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 404, error &lt;HTTPError 404: 'Not Found'&gt;. This response does not authenticate a recipe. |
| grounding | REVIEW_WORK/batch071/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/columbia.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Columbia.md; entire report; historical-authentication.json | supports | Entire historical report read, including unchanged and unresolved fields; reports for a different maintained owner or generated branch are comparison-only, and dependency reports transfer only the explicitly assessed stock scope. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch071/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer26 | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses equal duplicate values without summing them and retains the first conflicting value with a flag. This behavior is distinct from historical summed-amount artifacts and does not authenticate source-specific stock or product structure. |
| writer27 | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients; merge_ingredient_group | context_only | Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group retains the first concentration, flags differing values and selects the first CHEBI. It cannot establish source stages or justify collapsing independent supplemental and product-contained components. |
| writer28 | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium; infer_category; import_file | context_only | Current CultureBotHTImporter.transform_medium shallow-copies input data, maps medium types, uses infer_category only when category is missing, appends a generic repository source URL and an actual timestamped import event, and flags missing primary terms. It does not independently verify ingredient identity or source quantities. import_file serializes the transformed record; historical execution is not established by this read. |
| writer29 | scripts/migrate_solutions_from_ingredients.py; _is_solution; _resolve_solution; _migrate_media_file | context_only | Current _is_solution uses name patterns, _resolve_solution keeps concentrations while creating empty reference stubs or matching a name-indexed solution, and _migrate_media_file appends those solutions and history. It does not reconstruct nested source batches or authenticate copied unit/basis. |
| writer30 | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS duplicate notes. This bounded repair is not a general solution for product decomposition, stock flattening or differing source formulations. |
| writer31 | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _extract_assembled_solutions; _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph | context_only | Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions distinguish primary sections, nested stocks and assembled solutions. _parse_unit maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices still require a verified source basis. _extract_preparation_steps retains comments. _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied object. These present behaviors neither authenticate historical execution nor prove that all source metadata survived the old import. |
| writer32 | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Current formulation_content retains exact scientific quantities, preparation and other scientific fields; merge_formulation_evidence rejects incompatible projections and unions evidence at matching scopes. A source-equivalence claim is not established by shared ingredient identities. |
| writer33 | src/culturemech/merge/matcher.py; group_formulations; group_recipes | context_only | Current group_formulations calls group_recipes with fail_on_invalid=True and FormulationFingerprinter. Expected standalone or unfingerprintable records are excluded; malformed or unexpected inputs raise. Valid records are grouped by full scientific content. This guard does not retrieve or authenticate source recipes. |
| writer34 | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group routes a single maintained owner with merge metadata; multiple owners pass through conservative merge_formulation_evidence. Regenerating from an unrepaired owner retains its defects. Current conservative behavior is credited and does not establish how the old generated record was produced. |
| quantity-inventory | REVIEW_WORK/batch071/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The historical CultureBotHT file/version was not recovered; the current repository API returned 404. This is a bounded retrieval result, not proof that every archive is absent.
- No preparation, pH, experimental growth or final-batch volume is inferred from the FEBA section. Neighboring medium sections are not scientifically assessed.
- Iron sulfate hydration and replacement mappings for tris hydrochloride and heart infusion remain unresolved; the bounded exact OLS search returned no tris-hydrochloride hit.
- Current MIM exact-identifier rows are linkage context, not proof of supplied-form equivalence or historical mapping validity.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T154203Z-Columbia-batch071
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of Columbia
started_at: '2026-10-28T15:21:27.720238Z'
finished_at: '2026-10-28T15:42:03.340045Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: All fourteen Columbia broth rates match the exact FEBA section and can be
  retained. Curation is needed for supplied-material mappings, one canonical-label
  difference and claim-level source traceability. Preparation and growth conditions
  remain unsupported by the scoped source.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/Columbia.yaml
    sha256: 16f71938f3579a7f38271ac139c023fe6b617f1a74e2aa6942305eca2b3d600b
    role: target
  - path: data/normalized_yaml/specialized/columbia.yaml
    sha256: efcf51fb4d1309b5e1ac7f4f2de45b13932a1398a52ef5134eb5d7cb82cee31c
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Columbia.md
    sha256: 2cc2da9e63c93d88fa4ca5cbefe777563a59db6c3ab128ab251558ead433088a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/columbia.md
    sha256: 022d897e734ac2576d7adc148c5556b89e2b8a0ce2c582e8d2d444a88b803d53
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch071 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015503
targets:
- target_id: CultureMech:015503
  path: data/merge_yaml/merged/Columbia.yaml
  label: Columbia
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:015503
  command: just validate-schema data/merge_yaml/merged/Columbia.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:015503
  command: just validate-strict data/merge_yaml/merged/Columbia.yaml --workers 1 --out
    REVIEW_WORK/batch071/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:015503
  command: just validate-terms data/merge_yaml/merged/Columbia.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:015503
  command: just validate-references data/merge_yaml/merged/Columbia.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/Columbia.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T15:33:14.240802Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 16f71938f3579a7f38271ac139c023fe6b617f1a74e2aa6942305eca2b3d600b
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/specialized/columbia.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T15:33:14.240951Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: efcf51fb4d1309b5e1ac7f4f2de45b13932a1398a52ef5134eb5d7cb82cee31c
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch071/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:28.921198Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 5876df53acd3a1bf39c204af0ff6847b441669af368046ca7beac0b1d9efbd2d
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch071/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:29.866120Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: d35bce8aa56844fd3b04505135c3fe8d7afc5a4149aeb2164871ec4127b80039
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch071/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:31.366198Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 6173215acdb8e187d2ff1592113dedf0c42921a28ab8b5c728dd5f9160d0c712
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch071/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T15:21:32.480931Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: af223476bebbcd65d557b2e19de0740d7bbd4ac7d3e0e07b7ec5e39ccc52c029
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:20.264304Z'
  support: supports
  summary: OLS current exact CHEBI:17634 = D-glucose; definition ['A glucose with
    <small>D</small>-configuration.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.976452Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi28869
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28869
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.938208Z'
  support: supports
  summary: OLS current exact CHEBI:28869 = menadione; definition ['A member of the
    class of 1,4-naphthoquinones that is 1,4-naphthoquinone which is substituted at
    position 2 by a methyl group. It is used as a nutritional supplement and for the
    treatment of hypoprothrombinemia.']; formula ['C11H8O2']; mass ['172.183']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 7d5bbd9644ae17adf1a4cf5660c04a06c2db3430709c2a0d2da9a026611d9444
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.782396Z'
  support: supports
  summary: OLS current exact CHEBI:29377 = sodium carbonate; definition []; formula
    ['CO3.2Na']; mass ['105.988']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:18.205445Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi50385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.779399Z'
  support: supports
  summary: OLS current exact CHEBI:50385 = hemin; definition ['It is used as a prescription
    medication to relieve repeated attacks of acute intermittent porphyria related
    to the menstrual cycle in affected women.']; formula ['C34H32ClFeN4O4']; mass
    ['651.952']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: b989203634707b89526a8664c8fa65cb4976c4cdd791427218cf01b37d17356e
- evidence_id: chebi75832
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.735857Z'
  support: supports
  summary: OLS current exact CHEBI:75832 = iron(2+) sulfate (anhydrous); definition
    ['A compound of iron and sulfate in which the ratio of iron(2+) to sulfate ions
    is 1:1. Various hydrates occur naturally - most commonly the heptahydrate, which
    loses water to form the tetrahydrate at 57°C and the monohydrate at 65°C.']; formula
    ['Fe.O4S']; mass ['151.908']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9119cb3893b1a8171f719ef3e8fe6e5775a4fd59575baec8cd6da953801d089
- evidence_id: chebi91247
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.714816Z'
  support: supports
  summary: OLS current exact CHEBI:91247 = L-cysteine hydrochloride; definition ['A
    hydrochloride obtained by combining <small>L</small>-cysteine with one molar equivalent
    of hydrogen chloride.']; formula ['C3H7NO2S.HCl']; mass ['157.622']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 8ff9a3639e1afba34c0d40072292486ff792c7b63a496d189a1cfeb2e6574890
- evidence_id: chebi9754
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.592733Z'
  support: supports
  summary: OLS current exact CHEBI:9754 = tris; definition ['A primary amino compound
    that is <em>tert</em>-butylamine in which one hydrogen attached to each methyl
    group is replaced by a hydroxy group. A compound widely used as a biological buffer
    substance in the pH range 7—9; p<em>K</em><small><sub>a</sub></small> = 8.3 at
    20 °C; p<em>K</em><small><sub>a</sub></small> = 7.82 at 37 °C.']; formula ['C4H11NO3'];
    mass ['121.136']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: foodon03315426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.355227Z'
  support: supports
  summary: OLS current exact FOODON:03315426 = yeast extract; definition ['SIREN DB
    annotation:\n* not heat-treated FOODON:03440003\n* part of algae or fungus FOODON:03420247'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000180
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000180
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.189089Z'
  support: supports
  summary: OLS current exact MICRO:0000180 = proteose peptone; definition []; formula
    None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b3a39a531c5ab5508a297228d13ba81c99899b041d5292a9d668eded939bfe73
- evidence_id: micro0000182
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.134614Z'
  support: supports
  summary: OLS current exact MICRO:0000182 = tryptone; definition []; formula None;
    mass None; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: uberon0000948
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000948
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T15:24:19.124776Z'
  support: supports
  summary: OLS current exact UBERON:0000948 = heart; definition ['Taxon notes:" the
    ascidian tube-like heart lacks chambers....The ascidian heart is formed after
    metamorphosis as a simple tube-like structure with a single-layered myoepithelium
    that is continuous with a single-layered pericar- dial wall. It lacks chambers
    and endocardium.... The innovation of the chambered heart was a key event in vertebrate
    evolution, because the chambered heart generates one-way blood flow with high
    pressure, a critical requirement for the efficient blood supply of large-body
    vertebrates... all extant vertebrates have hearts with two or more chambers (Moorman
    and Christoffels 2003)" DOI:10.1101/gad.1485706', 'A myogenic muscular circulatory
    organ found in the vertebrate cardiovascular system composed of chambers of cardiac
    muscle. It is the primary circulatory organ.']; formula None; mass None; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c658bbcacd89befa47e3bd4859f176db247b3ce67483b6590c91d0865d41aed4
- evidence_id: trisHClSearch
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?q=tris%20hydrochloride&ontology=chebi&exact=true
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T15:24:18.204980Z'
  support: context_only
  summary: Bounded current OLS exact search for tris hydrochloride returned no matches.
    No replacement identifier is inferred from this search; this is discovery evidence
    only.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: One OLS4 search API request, q=tris hydrochloride, ontology=chebi,
    exact=true, using the retained current response. Zero results for this exact query
    only; synonyms, alternate spellings, other services and the whole ontology were
    not exhaustively searched.
- evidence_id: febaMedia
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T15:22:09.157085Z'
  support: supports
  summary: Only the complete version-pinned FEBA Columbia section (heading and fourteen
    explicit g/L rows) was read scientifically; neighboring medium sections are excluded.
    This dataset does not provide preparation, pH or experimental growth evidence
    for this record.
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: culturebotHT
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T15:22:09.157157Z'
  support: unknown
  summary: 'Actual retrieval HTTP 404, error <HTTPError 404: ''Not Found''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch071/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T15:33:14.246843Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 893dfbcf816e6dd27c317cdb3c57159684867f7382f545181400827cfc5b1fe3
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/columbia.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T15:33:14.247152Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 022d897e734ac2576d7adc148c5556b89e2b8a0ce2c582e8d2d444a88b803d53
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Columbia.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T15:33:14.247173Z'
  support: supports
  summary: Entire historical report read, including unchanged and unresolved fields;
    reports for a different maintained owner or generated branch are comparison-only,
    and dependency reports transfer only the explicitly assessed stock scope. This
    narrative or zero-source-check report is a derivative lead, not new primary-source
    authentication.
  snapshot_sha256: 2cc2da9e63c93d88fa4ca5cbefe777563a59db6c3ab128ab251558ead433088a
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch071/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T15:33:14.247194Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 2845b1ead1984bcde144190d0b2a9d63a103b88ef587de746ffd80a3feb361ed
- evidence_id: writer26
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T15:33:14.247250Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses equal duplicate values without
    summing them and retains the first conflicting value with a flag. This behavior
    is distinct from historical summed-amount artifacts and does not authenticate
    source-specific stock or product structure.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer27
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients; merge_ingredient_group
  accessed_at: '2026-10-28T15:33:14.247274Z'
  support: context_only
  summary: Current merge_duplicate_ingredients groups normalized names; merge_ingredient_group
    retains the first concentration, flags differing values and selects the first
    CHEBI. It cannot establish source stages or justify collapsing independent supplemental
    and product-contained components.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer28
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium; infer_category; import_file
  accessed_at: '2026-10-28T15:33:14.247298Z'
  support: context_only
  summary: Current CultureBotHTImporter.transform_medium shallow-copies input data,
    maps medium types, uses infer_category only when category is missing, appends
    a generic repository source URL and an actual timestamped import event, and flags
    missing primary terms. It does not independently verify ingredient identity or
    source quantities. import_file serializes the transformed record; historical execution
    is not established by this read.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer29
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _is_solution; _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T15:33:14.247327Z'
  support: context_only
  summary: Current _is_solution uses name patterns, _resolve_solution keeps concentrations
    while creating empty reference stubs or matching a name-indexed solution, and
    _migrate_media_file appends those solutions and history. It does not reconstruct
    nested source batches or authenticate copied unit/basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer30
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T15:33:14.247350Z'
  support: context_only
  summary: Current repair_ingredient and repair_record act on parsed IDENTICAL_PARTS
    duplicate notes. This bounded repair is not a general solution for product decomposition,
    stock flattening or differing source formulations.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer31
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _extract_assembled_solutions;
    _parse_unit; _extract_preparation_steps; _convert_to_culturemech; _extract_ph
  accessed_at: '2026-10-28T15:33:14.247391Z'
  support: context_only
  summary: Current _extract_primary_components, _solution_from_item and _extract_assembled_solutions
    distinguish primary sections, nested stocks and assembled solutions. _parse_unit
    maps bare g/mg/ml to per-litre enum labels, while L remains L; those enum choices
    still require a verified source basis. _extract_preparation_steps retains comments.
    _convert_to_culturemech sets COMPLEX by default, and _extract_ph reads its supplied
    object. These present behaviors neither authenticate historical execution nor
    prove that all source metadata survived the old import.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer32
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content; merge_formulation_evidence
  accessed_at: '2026-10-28T15:33:14.247414Z'
  support: context_only
  summary: Current formulation_content retains exact scientific quantities, preparation
    and other scientific fields; merge_formulation_evidence rejects incompatible projections
    and unions evidence at matching scopes. A source-equivalence claim is not established
    by shared ingredient identities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer33
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations; group_recipes
  accessed_at: '2026-10-28T15:33:14.247435Z'
  support: context_only
  summary: Current group_formulations calls group_recipes with fail_on_invalid=True
    and FormulationFingerprinter. Expected standalone or unfingerprintable records
    are excluded; malformed or unexpected inputs raise. Valid records are grouped
    by full scientific content. This guard does not retrieve or authenticate source
    recipes.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer34
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T15:33:14.247456Z'
  support: context_only
  summary: Current merge_group routes a single maintained owner with merge metadata;
    multiple owners pass through conservative merge_formulation_evidence. Regenerating
    from an unrepaired owner retains its defects. Current conservative behavior is
    credited and does not establish how the old generated record was produced.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch071/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T15:42:03.340045Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 497e33a0994aa6fdcf4d8bf0bf5acb99ff6e6e745f32718983e7f51dc5feb5e1
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and material identity
  outcome: concern
  summary: The full Columbia section in the version-pinned FEBA media file matches
    all fourteen local amounts and the broth description. Its complex digests and
    extracts support COMPLEX/UNDEFINED, and broth supports LIQUID. The generic CultureBotHT
    repository API returned 404, so the historical import file and exact historical
    upstream version were not recovered. Specialized is an importer fallback category,
    not proof of an organism association.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - local0
  - local1
  - febaMedia
  - culturebotHT
- assessment_id: a2
  area: evidence
  topic: Preparation and growth evidence limits
  outcome: unknown
  summary: The scoped FEBA section supplies rates but no preparation protocol, pH,
    incubation conditions, strain identity or experimental growth result. These remain
    unknown; no typical protocol or organism is inferred from the medium name. The
    neighboring FEBA sections are excluded.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - febaMedia
- assessment_id: a3
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: Both October reports perform zero external source checks; their unchanged
    amount tables are derivative summaries. The current importer shallow-copies upstream
    fields and records a generic repository URL; its present behavior cannot authenticate
    the original source retrieval. Current conservative merging preserves scientific
    fields and rejects incompatible formulations. Inspected writer behavior is described
    separately by exact file and function; it does not prove historical execution.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - history-auth
  - writer26
  - writer27
  - writer28
  - writer29
  - writer30
  - writer31
  - writer32
  - writer33
  - writer34
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: supported
  summary: All 28 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - quantity-inventory
  details: "{\n  \"schema\": \"private explicit quantity decisions v1\",\n  \"target_id\"\
    : \"CultureMech:015503\",\n  \"selected_concentration_field_count\": 28,\n  \"\
    selected_concentration_fields_covered\": 28,\n  \"decisions\": [\n    {\n    \
    \  \"decision_id\": \"q1\",\n      \"subject\": \"Proteose Peptone\",\n      \"\
    local_fields\": [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[0].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 5 g/L for Proteose\
    \ Peptone. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4594-4594\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Proteose Peptone\\t5\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q2\",\n      \"subject\": \"Pancreatic digest of casein\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"10\",\n            \"unit\": \"G_PER_L\"\n     \
    \     }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[1].concentration\",\n          \"original\"\
    : {\n            \"value\": \"10\",\n            \"unit\": \"G_PER_L\"\n     \
    \     }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 10 g/L for Pancreatic\
    \ digest of casein. Both current layers retain this amount and unit. Newly captured\
    \ source support can be attached without changing the value; there is no existing\
    \ claim-scoped source evidence to mark verified. No stock dilution or final-batch\
    \ arithmetic is needed.\",\n      \"sources\": [\n        {\n          \"locator\"\
    : \"extracted-text lines 4595-4595\",\n          \"source_key\": \"febaMedia\"\
    ,\n          \"reference\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Pancreatic digest of casein\\t10\\tg/L\",\n          \"quote_representation\"\
    : \"captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q3\",\n      \"subject\": \"Yeast Extract\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[2].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 5 g/L for Yeast Extract.\
    \ Both current layers retain this amount and unit. Newly captured source support\
    \ can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4596-4596\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Yeast Extract\\t5\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q4\",\n      \"subject\": \"Beef Heart Infusion \",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"3\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[3].concentration\",\n          \"original\"\
    : {\n            \"value\": \"3\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 3 g/L for Beef Heart\
    \ Infusion. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4597-4597\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Beef Heart Infusion \\t3\\tg/L\",\n          \"quote_representation\": \"\
    captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q5\",\n      \"subject\": \"D-Glucose\",\n      \"local_fields\": [\n    \
    \    {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\",\n\
    \          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"2.5\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[4].concentration\",\n          \"original\"\
    : {\n            \"value\": \"2.5\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 2.5 g/L for D-Glucose.\
    \ Both current layers retain this amount and unit. Newly captured source support\
    \ can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4598-4598\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"D-Glucose\\t2.5\\tg/L\",\n          \"quote_representation\": \"captured extracted\
    \ text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q6\",\n\
    \      \"subject\": \"Sodium Chloride\",\n      \"local_fields\": [\n        {\n\
    \          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\",\n      \
    \    \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[5].concentration\",\n          \"original\"\
    : {\n            \"value\": \"5\",\n            \"unit\": \"G_PER_L\"\n      \
    \    }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 5 g/L for Sodium Chloride.\
    \ Both current layers retain this amount and unit. Newly captured source support\
    \ can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4599-4599\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Sodium Chloride\\t5\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q7\",\n      \"subject\": \"Sodium carbonate\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.6\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[6].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.6\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 0.6 g/L for Sodium\
    \ carbonate. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4600-4600\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Sodium carbonate\\t0.6\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q8\",\n      \"subject\": \"Iron(II) Sulfate\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[7].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.02\",\n            \"unit\": \"G_PER_L\"\n   \
    \       }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n     \
    \ \"stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\"\
    : \"The exact version-pinned Columbia section explicitly states 0.02 g/L for Iron(II)\
    \ Sulfate. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4601-4601\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Iron(II) Sulfate\\t0.02\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q9\",\n      \"subject\": \"Magnesium sulfate\",\n      \"local_fields\":\
    \ [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[8].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 0.1 g/L for Magnesium\
    \ sulfate. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4602-4602\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Magnesium sulfate\\t0.1\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q10\",\n      \"subject\": \"L-Cysteine HCL\",\n      \"local_fields\": [\n\
    \        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[9].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.1\",\n            \"unit\": \"G_PER_L\"\n    \
    \      }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n      \"\
    stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\": \"\
    The exact version-pinned Columbia section explicitly states 0.1 g/L for L-Cysteine\
    \ HCL. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4603-4603\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"L-Cysteine HCL\\t0.1\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\":\
    \ \"q11\",\n      \"subject\": \"Tris(hydroxymethyl)aminomethane\",\n      \"\
    local_fields\": [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.83\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[10].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.83\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n \
    \     \"stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\"\
    : \"The exact version-pinned Columbia section explicitly states 0.83 g/L for Tris(hydroxymethyl)aminomethane.\
    \ Both current layers retain this amount and unit. Newly captured source support\
    \ can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4604-4604\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Tris(hydroxymethyl)aminomethane\\t0.83\\tg/L\",\n          \"quote_representation\"\
    : \"captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q12\",\n      \"subject\": \"Tris hydrochloride\",\n      \"local_fields\"\
    : [\n        {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"2.86\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[11].concentration\",\n          \"\
    original\": {\n            \"value\": \"2.86\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n \
    \     \"stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\"\
    : \"The exact version-pinned Columbia section explicitly states 2.86 g/L for Tris\
    \ hydrochloride. Both current layers retain this amount and unit. Newly captured\
    \ source support can be attached without changing the value; there is no existing\
    \ claim-scoped source evidence to mark verified. No stock dilution or final-batch\
    \ arithmetic is needed.\",\n      \"sources\": [\n        {\n          \"locator\"\
    : \"extracted-text lines 4605-4605\",\n          \"source_key\": \"febaMedia\"\
    ,\n          \"reference\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Tris hydrochloride\\t2.86\\tg/L\",\n          \"quote_representation\": \"\
    captured extracted text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\"\
    : \"q13\",\n      \"subject\": \"Hemin\",\n      \"local_fields\": [\n       \
    \ {\n          \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\",\n  \
    \        \"field_path\": \"ingredients[12].concentration\",\n          \"original\"\
    : {\n            \"value\": \"0.005\",\n            \"unit\": \"G_PER_L\"\n  \
    \        }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[12].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.005\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n \
    \     \"stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\"\
    : \"The exact version-pinned Columbia section explicitly states 0.005 g/L for\
    \ Hemin. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4606-4606\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Hemin\\t0.005\\tg/L\",\n          \"quote_representation\": \"captured extracted\
    \ text\"\n        }\n      ]\n    },\n    {\n      \"decision_id\": \"q14\",\n\
    \      \"subject\": \"Menadione\",\n      \"local_fields\": [\n        {\n   \
    \       \"record_path\": \"data/merge_yaml/merged/Columbia.yaml\",\n         \
    \ \"field_path\": \"ingredients[13].concentration\",\n          \"original\":\
    \ {\n            \"value\": \"0.001\",\n            \"unit\": \"G_PER_L\"\n  \
    \        }\n        },\n        {\n          \"record_path\": \"data/normalized_yaml/specialized/columbia.yaml\"\
    ,\n          \"field_path\": \"ingredients[13].concentration\",\n          \"\
    original\": {\n            \"value\": \"0.001\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"decision\": \"evidence_only\",\n \
    \     \"stage\": \"Explicit FEBA Columbia broth rate\",\n      \"interpretation\"\
    : \"The exact version-pinned Columbia section explicitly states 0.001 g/L for\
    \ Menadione. Both current layers retain this amount and unit. Newly captured source\
    \ support can be attached without changing the value; there is no existing claim-scoped\
    \ source evidence to mark verified. No stock dilution or final-batch arithmetic\
    \ is needed.\",\n      \"sources\": [\n        {\n          \"locator\": \"extracted-text\
    \ lines 4607-4607\",\n          \"source_key\": \"febaMedia\",\n          \"reference\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n          \"source_raw_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"source_text_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n          \"accessed_at\": \"2026-10-28T15:22:09.157085Z\",\n          \"exact_source_quote\"\
    : \"Menadione\\t0.001\\tg/L\",\n          \"quote_representation\": \"captured\
    \ extracted text\"\n        }\n      ]\n    }\n  ],\n  \"local_field_census_reference\"\
    : \"REVIEW_WORK/batch071/record04/grounding-inventory.json\",\n  \"source_only_gaps_are_explicit\"\
    : true,\n  \"note\": \"Batch amounts, provider normalization, stock composition,\
    \ working dose and preparation controls are separate. No source edits or automatic\
    \ curation performed.\"\n}"
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/Columbia.yaml: primary 14/14, secondary 0/14; data/normalized_yaml/specialized/columbia.yaml:
    primary 14/14, secondary 0/14. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - grounding
- assessment_id: a6
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - local0
- assessment_id: a7
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:015503
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-015503-material-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Tris hydrochloride and heart infusion are mapped to different material identities
  description: Both layers map Tris hydrochloride to CHEBI:9754, whose current formula
    C4H11NO3 describes tris base rather than its hydrochloride. They map Beef Heart
    Infusion to UBERON:0000948, the anatomical heart organ rather than an infusion
    product. The distinct source labels and correct rates should remain. The source
    also does not specify hydration for Iron(II) Sulfate, so its anhydrous assertion
    CHEBI:75832 is not independently established here; no hydrate replacement or molar
    calculation is justified.
  target_ids:
  - CultureMech:015503
  field_paths:
  - ingredients[11].term
  - ingredients[3].term
  - ingredients[7].term
  evidence_ids:
  - febaMedia
  - chebi9754
  - uberon0000948
  - chebi75832
  - grounding
  rule_id: review-yaml-record/exact-supplied-material
  native_severity: P2
  normalization_reason: 'Custom P2 material-identity concern normalized to major:
    two current identifiers denote different materials from the explicit source labels.
    The iron hydration issue is separately an unverified specificity limit, not a
    demonstrated alternate hydrate.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-015503-proteose-canonical-label
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Proteose peptone label differs from the current canonical label
  description: MICRO:0000180 resolves to proteose peptone, while both term labels
    capitalize Proteose. The identity is supported; this is literal label correspondence
    only, not an ingredient replacement.
  target_ids:
  - CultureMech:015503
  field_paths:
  - ingredients[0].term.label
  evidence_ids:
  - micro0000180
  - grounding
  rule_id: review-yaml-record/id-label-correspondence
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-015503-claim-level-source-provenance
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Matching FEBA rates lack claim-scoped source evidence
  description: Both layers retain the FEBA note and generic CultureBotHT source link
    but no exact versioned formulation citation or claim-level excerpts. The current
    FEBA section authenticates its explicit rates; the 404 repository response and
    derivative October reports cannot authenticate the historical import execution
    or access time.
  target_ids:
  - CultureMech:015503
  field_paths:
  - sources
  - evidence
  - ingredients[*].concentration.evidence
  - curation_history
  evidence_ids:
  - febaMedia
  - culturebotHT
  - history-auth
  rule_id: review-yaml-record/claim-provenance
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Resolve each exact supplied material against an appropriate ontology
    or retain the precise source label with mapping explicitly unresolved. Do not
    map a commercial infusion to an anatomical organ or merge tris hydrochloride with
    tris base. Preserve all supported rates; document the iron hydration limit without
    guessing a replacement.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015503
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Refresh only the canonical term label to the exact current authority
    label while retaining preferred_term and the supported ingredient identity.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015503
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Attach the exact FEBA version and matching excerpts at the supported
    claims. Preserve all historical events unchanged; append any newly verified source
    context with the actual curation date and record the unrecovered historical upstream
    version.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015503
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/columbia.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- The historical CultureBotHT file/version was not recovered; the current repository
  API returned 404. This is a bounded retrieval result, not proof that every archive
  is absent.
- No preparation, pH, experimental growth or final-batch volume is inferred from the
  FEBA section. Neighboring medium sections are not scientifically assessed.
- Iron sulfate hydration and replacement mappings for tris hydrochloride and heart
  infusion remain unresolved; the bounded exact OLS search returned no tris-hydrochloride
  hit.
- Current MIM exact-identifier rows are linkage context, not proof of supplied-form
  equivalence or historical mapping validity.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
