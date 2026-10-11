# Remaining JCM Source Cohort: Unapplied Preparation Leads

This is acquisition and triage, not completed scientific review or applied
curation. The [319-target acquisition](20261007-medium-source-fetch-3000-3319.json)
covers frozen inventory offsets `[3000:3319]`, JCM J1010 through J1329 in
inventory order. All source and baseline hashes verify; 20 responses have no
recipe table. The full inventory and all-record objective remain unchanged.

The temporary mechanical preview is
`/tmp/ingredient-media-20261007/media-3000-3319-preview.json`.
It proposes 239 evidence-only claims across 43 records, with zero operational
or schema failures, before source-scope decisions. No canonical cohort reports
or YAML edits were produced for these 319 targets.

All 43 candidates' main preparation texts were inspected. Complete ingredient
tables were additionally read for J1105, J1128, J1154, J1168, J1179, J1249, and
J1268. Other amount tables, local record contexts, stock boundaries, and
original-source checks remain to be reviewed before freezing a canonical plan.

## Original-Source Conflicts

### J1105: Base Volume Missing From API Arithmetic

Target `data/normalized_yaml/bacterial/virgibacillus_merv_medium.yaml`,
ID `CultureMech:002283`; baseline SHA256
`349e8317e227697953c3b6feafc3cba1aabc29c827f35c792803896cb2e311e7`.
API capture SHA256:
`559db99d6d1e32f140e35701576a9d39128fcc0856b1f965910a9e9a6fe77f56`.

The [original JCM recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1105)
says to **"bring volume to 1.0 L"**, then add 10 ml carbonate solution after
autoclaving. The API instead uses a 10 ml denominator, making its NaCl rate
10,000 g/L. All five mechanically eligible claims must be withheld. Unlike
J896's explicit final makeup, this source has a base followed by another liquid
addition: establish the preparation boundary before asserting final-medium rates.
Do not silently treat 1 L as final volume, infer a percentage basis, or change
the source's unusual citrate trihydrate to a more familiar hydrate.

Original capture: `/tmp/ingredient-media-20261007/JCM_GRMD1105-scope.html`.
SHA256: `2c7d8a4ae523578495afb0f7de58f4185a15a9cd5a489e938f46602d714356f8`.

### J1249: Acid Addition Omitted From The API Table

Target `data/normalized_yaml/bacterial/tyg_acetate_medium.yaml`,
ID `CultureMech:002415`; baseline SHA256
`2aae2454f5433283dd108798254d82e0310f4593d001226e4a95665889fca002`.
API capture SHA256:
`c701815bf576113ff1375cd0a207048e6ead386f3dc3ea65dd56f930309cd26d`.

The [original JCM recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1249)
states **"After autoclaving, aseptically add 20 ml acetic acid (filter-sterilized)."**
That addition appears in the API preparation but not its table or 1001 ml
denominator. All nine mechanically eligible claims need withholding until the
complete formulation and volume basis are represented. Listed water plus liquid
additions is not proof of measured final volume; no acid density, purity, or
percentage basis is inferred. Preserve the source's indeterminate manganese
sulfate hydration rather than assigning a fixed molecular form.

Original capture: `/tmp/ingredient-media-20261007/JCM_GRMD1249-scope.html`.
SHA256: `f5a37b17568398cf06d393bf582451d1282660999dc89292a196f5a6e4e1b35e`.

Both original HTML documents were inspected on 2026-10-07, including all table
rows and preparation text; unknown authors/publication years remain unknown.

## Further Leads And Controls

- J1168 dissolves antibiotics separately in water and methanol without specifying
  solvent volumes. Do not endorse base concentrations without scope review.
- J1201 adds glucose and carbonate stocks after sterilization; review solvent
  accounting and the clarified-rumen-fluid preparation.
- J1239 separately prepares yeast extract and sucrose. Inspect their stock stage
  and source quantities before adding support.
- J1185 and J1262/J1263/J1264 adjust pH with an unspecified carbonate stock dose.
  Distinguish nonquantified titration from a fixed formulation amount.
- J1102 and J1208 include strain-specific substrate/reducing-agent variants.
  Do not propagate those changes into every base recipe.
- J1044/J1045/J1047/J1052/J1111/J1210 interleave separately prepared additions;
  inspect their complete tables and liquid-volume accounting.
- J1128 lists 956 ml water plus 20, 4, and 20 ml stock additions. J1179 lists
  935 ml water plus 50, 10, and 5 ml additions. J1268 lists 645 ml water plus
  100, 100, 100, 20, and 35 ml stocks. These are possible represented-dose
  controls, not automatic omissions; their stock identities and strengths remain
  separate unsupported claims.
- J1154 includes 990 ml water plus 10 ml methanol and agar. It should not be
  treated as an omitted-methanol example merely because addition occurs later.
- Preserve liquid/solid distinctions in J1050/J1141/J1217/J1222/J1236.

Freeze source-pinned withholding decisions and independently preflight the
canonical plan only after completing those reviews. The temporary preview is
not safe to apply as-is.

## Ten Public-Medium Records Remain In Scope

The initial 329-target request [stopped after three payload failures](20261007-medium-source-fetch-3000-3329-partial.json).
P1-P3 lacked the required `solutions` key; P4-P10 were not attempted. A separate
public P1 response was inspected: it contains medium identity/pH metadata only,
not a recipe or ingredient amounts. Its successful HTTP envelope is not
concentration evidence. Both public catalog URLs were inaccessible through the
web tool; that does not prove the pages or recipes are absent.

The valid 319 JCM captures were subsequently revalidated as a complete subset,
without erasing the failed 329-target acquisition or trimming the inventory.
The P1 record's journal DOI and old catalog reference are leads, not newly
verified concentration evidence. Route all ten public records to an appropriate
source-specific review rather than filling in an empty `solutions` list to
make the generic fetcher appear successful.
