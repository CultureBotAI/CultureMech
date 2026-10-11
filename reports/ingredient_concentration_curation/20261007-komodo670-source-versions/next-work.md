# Remaining Curation Handoff

The four DSM 9463/9466/9467/9468 records in the preceding
[seven-record handoff](../20261007-dsmz546-659-670-stocks/next-variant-handoff.json)
now have this batch's explicit successor. Their historical snapshots must not be
treated as current. The other three handoff records are still the 673 candidates:

- `data/normalized_yaml/archaea/KOMODO_673_THERMOCOCCUS_PROFUNDUS_medium.yaml`
- `data/normalized_yaml/archaea/thermococcus_profundus_medium.yaml`
- `data/normalized_yaml/bacterial/mediadive_5645_Main_sol_673.yaml`

Recheck live hashes before editing. The already captured original 673 PDF gives
explicit yeast, peptone and NaCl changes relative to 266. The original 266 PDF's
table and preparation disagree on sulfur input. Preserve that conflict; do not
select a number merely because another importer or related YAML repeats it.
The yeast stock stage and inherited sulfide stock also need explicit dose/basis
review. The [pinned PDF captures](../20261007-dsmz546-659-670-stocks/next-variant-source-captures.json)
are leads and source evidence, not a claim that the three records were repaired.

The next uncovered KOMODO cohort is offset 2500, after the existing
`20261007-komodo-media-2000-2500` plan. Use the current coverage snapshot and exact
tracked inventory, not filenames alone, to resume. Broader remaining prefixes
include TOGO, KOMODO, MEDIADB, UTEX, NBRC and JCM; the objective still covers all
records, not only these handoff candidates.

Before publication, repair or explicitly resolve the merge-retention failures,
reference-validation failures and global freshness/name/fingerprint gates.
Regenerate derived artifacts through maintained tools, not by editing generated
merged YAML. Git publication and cleanup remain unperformed.
