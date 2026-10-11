# Next TOGO Pair: Source Triage Only

No YAML edits or completed unique reviews are claimed here. Both full current
records were inspected; source retrieval completed on 2026-10-08. The
[context](20261008-togo-next-pair-context.json) pins the record hashes, complete
source responses, URLs, HTTP status and retrieval time. Its SHA256 is
`e851cc1e0af57fa8107ca34f122eab815d78f8621a0145e01b8e9d94c1e78dbd`.

## TOGO M1038 / JCM985

Path: `data/normalized_yaml/archaea/TOGO_M1038_Methanomethylovorans_Uponensis_Medium.yaml`.
ID: `CultureMech:007553`. Existing follow-up inventory: 17 claims.

The [TOGO API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1038)
preserves three preparation paragraphs; the original JCM985 page returns
`Nothing found.` Relevant next decisions:

- Water is 960 ml input, not the imported 960 g/L.
- Six solutions in `components[1].items[0:6]` are added after cooling in batch
  volumes: 20, 10, 10, 1, 1, 1 ml. All are currently mislabeled G_PER_L.
- The last sulfide stock is different: `comments[1].comment` explicitly says
  `Finally, add per liter the following solution from an anaerobic stock`.
  `components[2].items[0]` supplies 8 ml, supporting a candidate **8 ML_PER_L**,
  not a generic 0.008 L batch dose. Preserve this preparation boundary.
- Resazurin is **1 mg per source batch**, not the imported 1 g/L. The batch's
  final volume is not explicit; do not simply change to 1 MG_PER_L. Propose an
  evidence-backed 1 mg batch note and withdrawal of the unsupported g/L slot.
- `%` stock strengths have no explicit w/v versus w/w basis. Do not turn the
  8%, 3%, and 5% labels into asserted percentage enum concentrations yet.
- Gas mixture is explicitly N2/CO2 80:20 v/v, but this does not establish an
  absolute gas amount. Existing VARIABLE placeholders are not measured doses.
- Review the M190, M180 and M431 stock references before expanding composition.
  Neither their contents nor final medium volume is verified by this triage.

## TOGO M1039 / JCM986

Path: `data/normalized_yaml/archaea/TOGO_M1039_Methanococcoides_Medium.yaml`.
ID: `CultureMech:007554`. Existing follow-up inventory: four claims.

Both the [TOGO API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1039)
and the accessible [JCM986 page](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=986)
explicitly support the existing trimethylamine hydrochloride **3 g/L**; it needs
ingredient-level evidence. TOGO's second row supplies **1 L** base medium, not
the imported 1 g/L. Its reference is TOGO M257, while original JCM text uses
JCM265. The local M257 record's original-source metadata maps to JCM265;
verify the external accession mapping and exact base recipe before expansion.

Original JCM wording: `Use Medium No. 265 supplemented with 3.0 g/L`.
The remaining formula and pH are in the captured paragraph with HTML subscripts;
extract adjacent text without inventing spaces inside chemical formulae.
The source also gives the 80:20 v/v gas mixture, not absolute gas quantities.

## Next Action

Build a guarded preview for all direct ingredients, gas placeholders and stocks
in both records. Treat source-mass notes, stock doses, percentage-basis gaps and
final-medium quantities separately. Run baseline validation, preserve mappings
and history, attach a PURL and exact snippet for each edit, then apply and verify.
This handoff does not increase the reported 11,747 unique follow-up paths.
