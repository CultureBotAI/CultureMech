# Remaining Ingredient Work

The all-record goal remains active. This batch applied four DSMZ/KOMODO 403/751
repairs, not all remaining ingredient or concentration issues.

Subsequent [PDF validation work](../20261008-recipe-pdf-validation/README.md)
fixed the extraction issue recorded below, without changing any recipe. The
[latest handoff](../20261008-recipe-pdf-validation/next-work.md) preserves these
queues and adds the source-backed DSMZ 1829 concentration decisions.

Current follow-up coverage is 11,784 of 15,910 exact normalized paths, leaving
4,126 outside these reports. Covered records can still have unresolved claims.
The cumulative diff audit records 5,167 edited records and 32,948 added evidence
entries. No taxa-media association was added in this batch.

## Unedited Queues

`next-lb-identity-context.json` retains 107 unchanged identity candidates: 76
acid-name and 31 albumin-name substitutions. SHA256:
`f014ac7ab997b344c4bf6abd829309c67e546b2b43cec7b34820e964533de431`.
The separate M142-dependent queue has 71 unchanged records. These queues are
disjoint, but not additive to the uncovered-path count.

## Next BSK Records

`next-bsk-context.json` pins three unchanged full YAML baselines and five fresh
source captures. SHA256:
`afef4e855d33495a1e7f54c7e6b809fe345c26533ad19f00a626328bc60136c3`.
All three complete YAMLs, the three API responses, JCM173 original HTML and the
DSMZ1829 original PDF text were read. The DSMZ page image was visually inspected.
This is preparation only: none of these records has been edited in this batch.

| Key | ID | Path | Current SHA256 |
| --- | --- | --- | --- |
| M2410 | CultureMech:008994 | data/normalized_yaml/bacterial/bsk_ii_medium.yaml | 9d8d0f75c0a761ff625bceb21236fd2170684352a71b0273020b2790142eec9f |
| D1829 | CultureMech:001256 | data/normalized_yaml/bacterial/bskii_medium_borrelia.yaml | fdddb16b72057f486570d5ee924f81555f24ceb74584c72b279dc7ed7808f8a6 |
| J173 | CultureMech:002533 | data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml | 5d38808a5ae93d9f894f3de4a65672d85ce8a54ef1a971c4ff1df3856c646ce7 |

### DSMZ 1829

The [original PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1829.pdf)
explicitly specifies final volume 100 ml and water to make up to that volume.
This resolves a consequential omission in the API's unquantified water row.
Do not remove supported mass concentrations simply because the API alone lacks
the final-volume statement. Recheck the original row and denominator together.

- API solution 6374 has twelve rows, including 0.85 g albumin fraction V.
  Remove only the false LB nodes 8-10; genuine yeast extract at index 6 remains.
- Existing mass rates can be verified from the source batch masses divided by
  0.1 L. Albumin would be 8.5 g/L with the verified denominator. Record all
  conversion inputs in evidence, not merely the API's calculated `g_l` values.
- Rabbit serum is an 8.56 ml batch input, not the existing 8.56 g/L. Its dose
  and any normalized addition rate must be clearly distinguished.
- MEM alpha Modification is a named product powder, 0.89 g per 100 ml, not the
  CMRL product used in the other BSK formulations. Do not invent its composition.
- NaOH is explicitly 1 M, without a fixed dose; final pH is 7.3. No filter pore
  size is specified. Water is makeup, not a separate 100 ml fixed addition.
- The printed 2023 copyright is not automatically a publication year.

### JCM 173

The [original recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=173)
corroborates the MediaDive J173 batch amounts, including the unusual **2.5 mg**
Neopeptone entry. Do not silently change it to grams by analogy.

- Main API solution 3829 has no recipe rows; A (3830) has ten rows and B (3831)
  has three. The single global procedure was imported into B's API steps and
  must not be interpreted as instructions to filter/autoclave every component.
- A uses 4.95 g CMRL with glutamate and 25 g fraction V albumin with 500 ml water.
  B uses 2.5 mg Neopeptone and 7 g gelatin with 100 ml water. These water inputs
  do not independently establish final stock or medium volumes.
- Preserve genuine yeast extract at old index 10, distinct from the false
  supplier-tagged yeast at index 2. False LB nodes are 1-3.
- Restore the 40 ml heat-inactivated sterile rabbit-serum addition, currently
  present only in procedure prose. Preserve 56 C/45 minute serum context and the
  original's explicit 0.22 micrometer filter, repairing the API's mojibake only
  with original-source evidence. NaOH is 1 N, not 1 M and not a fixed dose.
- Reconcile pH and sterilization scopes from the complete original procedure;
  do not simply copy the DSMZ403 or M2410 preparation graph.

### TOGO M2410

The [TOGO API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2410)
has twelve ingredient rows and eleven comment entries, one empty. It gives no
`src_url`. [Barbour 1984, PMID 6393604](https://pubmed.ncbi.nlm.nih.gov/6393604/)
is a literature lead with verified title/author/year, not yet verified as the
exact source formulation. Browser checks blocked full-text inspection through
PMC and eScholarship. Do not cite those unread full texts as formulation evidence.

- Restore 50 g bovine serum albumin fraction V in place of false LB nodes 4-6.
  Preserve genuine yeastolate and Neopeptone, each distinct from the false nodes.
- CMRL is 100 ml of 10X product **without glutamine**, added to 900 ml water.
  It is not the JCM173 powder. Existing root g/L values need scope review.
- The comments add a 200 ml 7% gelatin preparation and, later, unheated rabbit
  serum to final 6%. Both are currently omitted from structured ingredients.
  Percentage bases remain unspecified; do not infer stock strength or serum dose.
- Retain the 1 N NaOH titration and pH temperature context. The filter is 0.2
  micrometers, not the schema FILTER_STERILIZE enum's 0.22 micrometers. Preserve
  the stated storage and handling contexts without importing JCM173's heated serum.

An ignored-inclusive search of the concentration-curation report tree found
canonical reports for D1829 and J173, but none for the exact M2410 path. Recheck
this before generating output; use supplements for the existing canonical reports.

## Validation And Publication

The PDF reference-extraction issue is reproduced and documented locally, not
fixed. Do not patch caches or weaken snippets to make the gate pass. Global
merge/freshness failures remain separate from target merge-retention checks.
Keep full-corpus scans serial with tests that might mutate the live corpus.

Other remaining work includes M247/M272/M273/M274 reducing-stage reviews, the
M273/M274 FeSO4 source conflict and J151/M142 bibliography gaps. Do not import
one formulation's quantities into another because their names are similar.

Publication is unfinished. The prior issue #150 progress draft remains unposted
after an external-disclosure rejection, with no new authorization. Local issue
drafts are not GitHub submissions. Do not bypass the rejection through another
channel, and do not mark the all-record goal complete from these batch receipts.
