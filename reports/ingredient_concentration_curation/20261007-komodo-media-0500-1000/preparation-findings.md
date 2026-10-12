# Source and preparation findings

This batch selects offsets 500 through 999 of the frozen KOMODO inventory:
500 exact tracked normalized paths, from accession `92_6685` through `220_25300`.
There are 122 base accessions and 378 variant accessions. Base-recipe evidence
is not propagated to those variants, including records previously annotated
as source duplicates. Automated claim tables cover every selected path; this
does not claim manual scientific verification of every statement in all 500.

## Inspected Proposals

All 27 preliminary candidate records were read in full alongside their complete
captured source responses and exact mapping rows. Their before-records, source
data and metadata are preserved in [candidate context](inspected-candidate-context.json).
The initial preview proposed 167 evidence-only ingredient endorsements. Three
source-pinned [withholdings](withholdings.json) remove 26 endorsements:

- **111, Beijerinckia:** the table's 950 mL basis does not include the separately
  prepared glucose in another 50 mL of water. The current flat record cannot
  simultaneously represent the glucose stock, basal stage and complete medium.
  The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf)
  confirms this two-stage preparation. No replacement concentration is inferred.
- **125, Methylobacterium:** the preparation requires a methanol addition or
  methane-air incubation, while neither alternative is represented as a selected
  formulation in the local record. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf)
  confirms the alternatives. Resolve the branch and its amount/atmosphere scope.
- **187, M 40 Y:** local/source metadata give pH 5.4, but source preparation says
  to adjust to 5.6. The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium187.pdf)
  inspected here lists amounts but no pH statement. No unsupported pre/post-
  sterilization interpretation or replacement pH is asserted.

The remaining 24 proposed records have 141 amount endorsements plus separate
identity-mapping evidence. All are evidence-only: no concentration value or unit
is changed. Accepted snippets support the provider-declared main-recipe `g_l`
value, not an independently measured final volume, stock dose or assay dilution.
Full-record inversion independently checks that unrelated data remain unchanged.

## Unresolved Ingredient Details

- 93 retains unsupported Tween 80 and ethanol liquid amounts encoded as mass
  rates. The matching solid ingredient entries do not validate those liquids.
- 114 and 115 retain unqualified percent-basis sodium chloride and conditional
  agar as unsupported. Historical `kg_microbe_match` values pointing to 101 are
  not used as recipe identity evidence.
- 122 retains unmodeled iron/resazurin stocks, a separately added cellobiose
  stock and optional cellulose. Amount evidence does not establish stock
  strengths/doses or endorse the historical aerobic note.
- 147, 172, 183 and 190 contain source-specific branded or soluble ingredients;
  their attributes are not silently discarded to support unqualified rows.
- 157 and 172 describe separate additions/sterilization without complete stock
  dose and final-volume information. The direct provider amounts do not supply
  those missing inputs.
- 160 and 167 describe alternative cellobiose/filter-paper or agar/liquid
  preparations. Conditional rows and missing filter-paper quantities are not
  promoted into one combined formulation.
- 173 has buffer and seawater volumes imported as mass rates. Neither is
  endorsed; the buffer's molarity does not authorize its current `G_PER_L` value.
- 181 retains an unsupported valeric-acid volume encoded as mass.
- 188's cellulose row lacks a provider concentration and has preparation context
  involving a filter strip. It remains unsupported, not inferred from water.
- 192's hemin preparation uses a separately specified NaOH solution; its stock
  boundary is unresolved and that ingredient receives no new amount endorsement.
- 219 retains an unsupported glycerol volume encoded as mass. Its phosphate
  hydrate label and secondary anhydrous ontology link require separate identity
  review; amount evidence explicitly does not validate secondary ontology IDs.

No growth association, variant relationship, historical event or secondary
ontology identifier is changed in this batch. Source-duplicate entries are not
independent scientific confirmations.

## Unavailable Sources

[Source captures](source-captures.json) pin 123 distinct mapped endpoints:
114 accessible responses and nine HTTP 404 responses. The unavailable DSMZ
accessions are 124a, 131, 164, 168, 184, 197, 199, 200 and 208; they affect eleven
selected record paths. Each receives an unchanged unsupported result.

The initial sandbox fetch failed DNS resolution; an authorized network retry
established actual HTTP 404 responses. A separate serial request preserved each
404 body, endpoint, access time and hash without inventing a recipe. The
ignored-inclusive local source filename search and direct original-PDF attempts
for 124a and 131 did not yield amount evidence. This is a bounded access finding,
not a claim that all historical versions or archive copies are unavailable.

## Validation Scope

The existing independent audit and actual-group retention checker now accept
`--folder` so both frozen batches can use the same checks. Their defaults still
target the first batch. The frozen plans, source hashes and earlier reports are
not rewritten. Terminal gate results belong in `validation.json` and the batch
README; preview or schema validity alone does not establish scientific completion.
