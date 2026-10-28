# Source and formulation review: 2asw (CultureMech:000038)

- Review: 20261021T073836Z-culturemech-000038-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:20:53Z
- Finished UTC: 2026-10-21T07:38:36Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

CCAP 2ASW is identifiable, but eleven stock concentrations are flattened into direct medium ingredients and the stock doses, soil extract and preparation are omitted. UTEX642 is assigned a different strain taxon, legacy diatom media lack verified parent-formulation identity and structured growth scope, and the sodium-response variant conflicts with its supplement. Later bounded owner citations are sound within their stated limits but absent from the generated target. Full Tsuji methods and Liang TableS2 remain unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 78; batch 008 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seven task batches contain 70 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 72 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000038 | data/merge_yaml/merged/2ASW.yaml | generated | 2asw |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000038 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000038 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/078/strict.tsv |
| validate-terms | passed | True | CultureMech:000038 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br><br><br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 0.00/2.20G [00:00&lt;?, ?B/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 1.12M/2.20G [00:00&lt;03:29, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 2.19M/2.20G [00:00&lt;03:32, 11.1MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 4.44M/2.20G [00:00&lt;02:22, 16.5MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 5.50M/2.20G [00:00&lt;02:43, 14.4MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 6.50M/2.20G [00:00&lt;03:03, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 7.88M/2.20G [00:00&lt;02:56, 13.4MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 9.00M/2.20G [00:00&lt;03:06, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 10.0M/2.20G [00:00&lt;03:19, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 14.1M/2.20G [00:00&lt;01:50, 21.4MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 22.7M/2.20G [00:01&lt;00:59, 39.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 33.9M/2.20G [00:01&lt;00:37, 61.6MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 42.4M/2.20G [00:01&lt;00:33, 69.5MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 49.7M/2.20G [00:01&lt;00:32, 71.0MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 53.5M/2.20G [00:01&lt;00:37, 61.1MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 55.0M/2.20G [00:01&lt;00:48, 47.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 56.6M/2.20G [00:01&lt;00:59, 38.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 57.9M/2.20G [00:01&lt;01:16, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 59.0M/2.20G [00:01&lt;01:33, 24.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 60.1M/2.20G [00:01&lt;01:58, 19.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 61.1M/2.20G [00:02&lt;02:17, 16.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 62.6M/2.20G [00:02&lt;02:19, 16.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 64.4M/2.20G [00:02&lt;02:15, 17.0MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 65.6M/2.20G [00:02&lt;02:28, 15.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 67.0M/2.20G [00:02&lt;02:32, 15.0MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 68.1M/2.20G [00:02&lt;02:46, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 69.4M/2.20G [00:02&lt;02:50, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 70.5M/2.20G [00:02&lt;02:57, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 71.8M/2.20G [00:02&lt;02:59, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 72.8M/2.20G [00:03&lt;03:18, 11.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 73.7M/2.20G [00:03&lt;03:29, 10.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 75.2M/2.20G [00:03&lt;03:06, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 76.2M/2.20G [00:03&lt;03:18, 11.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 77.1M/2.20G [00:03&lt;03:36, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 78.1M/2.20G [00:03&lt;03:42, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 79.1M/2.20G [00:03&lt;03:46, 10.1MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 79.9M/2.20G [00:03&lt;03:57, 9.59MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 80.7M/2.20G [00:03&lt;04:09, 9.15MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 81.9M/2.20G [00:03&lt;03:48, 9.99MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 83.2M/2.20G [00:04&lt;03:28, 10.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 84.4M/2.20G [00:04&lt;03:21, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 85.3M/2.20G [00:04&lt;03:29, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 86.3M/2.20G [00:04&lt;03:34, 10.6MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 87.8M/2.20G [00:04&lt;03:12, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 89.6M/2.20G [00:04&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 91.0M/2.20G [00:04&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 92.4M/2.20G [00:04&lt;02:43, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 94.0M/2.20G [00:04&lt;02:33, 14.7MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 95.1M/2.20G [00:05&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 96.2M/2.20G [00:05&lt;03:02, 12.4MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 97.4M/2.20G [00:05&lt;03:09, 11.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 98.6M/2.20G [00:05&lt;03:05, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 99.9M/2.20G [00:05&lt;03:00, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 102M/2.20G [00:05&lt;02:46, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 103M/2.20G [00:05&lt;02:34, 14.6MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 104M/2.20G [00:05&lt;02:42, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 106M/2.20G [00:05&lt;02:42, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 107M/2.20G [00:05&lt;02:51, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 109M/2.20G [00:06&lt;02:45, 13.6MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 110M/2.20G [00:06&lt;02:55, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 110M/2.20G [00:06&lt;03:24, 11.0MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 111M/2.20G [00:06&lt;03:51, 9.71MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 112M/2.20G [00:06&lt;03:51, 9.71MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 113M/2.20G [00:06&lt;03:47, 9.87MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 114M/2.20G [00:06&lt;03:49, 9.80MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 115M/2.20G [00:06&lt;03:34, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:06&lt;04:09, 9.00MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:07&lt;04:44, 7.90MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 118M/2.20G [00:07&lt;03:17, 11.4MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;03:53, 9.59MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;04:52, 7.67MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;05:42, 6.53MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:07&lt;06:13, 5.99MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:07&lt;06:20, 5.88MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 121M/2.20G [00:07&lt;06:03, 6.16MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 122M/2.20G [00:07&lt;05:28, 6.81MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 123M/2.20G [00:07&lt;04:49, 7.73MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 124M/2.20G [00:08&lt;04:12, 8.85MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 125M/2.20G [00:08&lt;03:41, 10.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 127M/2.20G [00:08&lt;03:02, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 129M/2.20G [00:08&lt;02:26, 15.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 131M/2.20G [00:08&lt;02:21, 15.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 132M/2.20G [00:08&lt;02:37, 14.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 133M/2.20G [00:08&lt;02:41, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 134M/2.20G [00:08&lt;02:47, 13.3MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 136M/2.20G [00:08&lt;02:44, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 137M/2.20G [00:09&lt;02:56, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 138M/2.20G [00:09&lt;03:10, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 140M/2.20G [00:09&lt;02:49, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 140M/2.20G [00:09&lt;03:08, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 141M/2.20G [00:09&lt;03:14, 11.4MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 142M/2.20G [00:09&lt;03:35, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 143M/2.20G [00:09&lt;03:30, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 145M/2.20G [00:09&lt;03:05, 11.9MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:09&lt;03:05, 12.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 147M/2.20G [00:09&lt;03:00, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:10&lt;03:02, 12.1MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:10&lt;03:08, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 151M/2.20G [00:10&lt;03:06, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 152M/2.20G [00:10&lt;02:54, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 154M/2.20G [00:10&lt;02:48, 13.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 155M/2.20G [00:10&lt;02:50, 13.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 156M/2.20G [00:10&lt;02:55, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 158M/2.20G [00:10&lt;02:42, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 158M/2.20G [00:10&lt;03:00, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 159M/2.20G [00:11&lt;03:23, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 160M/2.20G [00:11&lt;03:32, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 161M/2.20G [00:11&lt;03:36, 10.2MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 162M/2.20G [00:11&lt;03:22, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 163M/2.20G [00:11&lt;03:22, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 164M/2.20G [00:11&lt;03:26, 10.6MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 166M/2.20G [00:11&lt;03:13, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 167M/2.20G [00:11&lt;02:57, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 168M/2.20G [00:11&lt;02:54, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 169M/2.20G [00:11&lt;03:05, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 171M/2.20G [00:12&lt;02:47, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 172M/2.20G [00:12&lt;02:42, 13.4MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 174M/2.20G [00:12&lt;02:37, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 175M/2.20G [00:12&lt;02:36, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 177M/2.20G [00:12&lt;02:37, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 178M/2.20G [00:12&lt;02:31, 14.4MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 179M/2.20G [00:12&lt;02:59, 12.1MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 180M/2.20G [00:12&lt;02:51, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 182M/2.20G [00:12&lt;02:48, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 182M/2.20G [00:12&lt;03:04, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 184M/2.20G [00:13&lt;02:54, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 185M/2.20G [00:13&lt;02:38, 13.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 186M/2.20G [00:13&lt;02:50, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 188M/2.20G [00:13&lt;02:40, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 189M/2.20G [00:13&lt;02:43, 13.2MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 190M/2.20G [00:13&lt;02:49, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 192M/2.20G [00:13&lt;02:49, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 193M/2.20G [00:13&lt;02:37, 13.7MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 194M/2.20G [00:13&lt;02:55, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 195M/2.20G [00:14&lt;02:47, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 197M/2.20G [00:14&lt;02:24, 14.9MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 200M/2.20G [00:14&lt;01:50, 19.4MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 204M/2.20G [00:14&lt;01:26, 24.7MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 208M/2.20G [00:14&lt;01:15, 28.5MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 211M/2.20G [00:14&lt;01:07, 31.6MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;▉         &#124; 216M/2.20G [00:14&lt;01:01, 35.0MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;▉         &#124; 221M/2.20G [00:14&lt;00:52, 40.3MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;█         &#124; 227M/2.20G [00:14&lt;00:46, 46.1MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;█         &#124; 233M/2.20G [00:14&lt;00:42, 49.7MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█         &#124; 241M/2.20G [00:15&lt;00:35, 59.6MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█         &#124; 252M/2.20G [00:15&lt;00:28, 73.7MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█▏        &#124; 259M/2.20G [00:15&lt;00:28, 74.7MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 263M/2.20G [00:15&lt;00:32, 64.8MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 274M/2.20G [00:15&lt;00:26, 77.5MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 282M/2.20G [00:15&lt;00:26, 79.4MB/s]<br>Downloading ncbitaxon.db.gz:  13%&#124;█▎        &#124; 292M/2.20G [00:15&lt;00:23, 88.3MB/s]<br>Downloading ncbitaxon.db.gz:  13%&#124;█▎        &#124; 302M/2.20G [00:15&lt;00:22, 92.0MB/s]<br>Downloading ncbitaxon.db.gz:  14%&#124;█▍        &#124; 312M/2.20G [00:15&lt;00:21, 96.7MB/s]<br>Downloading ncbitaxon.db.gz:  14%&#124;█▍        &#124; 322M/2.20G [00:15&lt;00:20, 98.6MB/s]<br>Downloading ncbitaxon.db.gz:  15%&#124;█▍        &#124; 332M/2.20G [00:16&lt;00:20, 100MB/s]<br>Downloading ncbitaxon.db.gz:  15%&#124;█▌        &#124; 341M/2.20G [00:16&lt;00:22, 90.5MB/s]<br>Downloading ncbitaxon.db.gz:  16%&#124;█▌        &#124; 354M/2.20G [00:16&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  16%&#124;█▌        &#124; 363M/2.20G [00:16&lt;00:19, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 373M/2.20G [00:16&lt;00:19, 102MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 383M/2.20G [00:16&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 392M/2.20G [00:16&lt;00:19, 100MB/s]<br>Downloading ncbitaxon.db.gz:  18%&#124;█▊        &#124; 402M/2.20G [00:16&lt;00:19, 100MB/s]<br>Downloading ncbitaxon.db.gz:  18%&#124;█▊        &#124; 410M/2.20G [00:16&lt;00:20, 95.3MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▊        &#124; 421M/2.20G [00:17&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▉        &#124; 430M/2.20G [00:17&lt;00:19, 98.4MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▉        &#124; 439M/2.20G [00:17&lt;00:19, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  20%&#124;█▉        &#124; 449M/2.20G [00:17&lt;00:19, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  20%&#124;██        &#124; 458M/2.20G [00:17&lt;00:19, 96.5MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██        &#124; 467M/2.20G [00:17&lt;00:19, 96.4MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██        &#124; 473M/2.20G [00:17&lt;00:21, 85.9MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██▏       &#124; 481M/2.20G [00:17&lt;00:22, 82.7MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██▏       &#124; 481M/2.20G [00:17&lt;00:38, 47.9MB/s]<br>Downloading ncbitaxon.db.gz:  22%&#124;██▏       &#124; 488M/2.20G [00:17&lt;00:34, 54.4MB/s]<br>Downloading ncbitaxon.db.gz:  22%&#124;██▏       &#124; 500M/2.20G [00:18&lt;00:25, 72.3MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 508M/2.20G [00:18&lt;00:26, 70.3MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 518M/2.20G [00:18&lt;00:22, 81.2MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 528M/2.20G [00:18&lt;00:20, 86.6MB/s]<br>Downloading ncbitaxon.db.gz:  24%&#124;██▍       &#124; 538M/2.20G [00:18&lt;00:19, 90.6MB/s]<br>Downloading ncbitaxon.db.gz:  24%&#124;██▍       &#124; 546M/2.20G [00:18&lt;00:20, 87.5MB/s]<br>Downloading ncbitaxon.db.gz:  25%&#124;██▍       &#124; 556M/2.20G [00:18&lt;00:19, 90.9MB/s]<br>Downloading ncbitaxon.db.gz:  25%&#124;██▌       &#124; 568M/2.20G [00:18&lt;00:17, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▌       &#124; 577M/2.20G [00:18&lt;00:17, 98.1MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▌       &#124; 586M/2.20G [00:19&lt;00:17, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▋       &#124; 595M/2.20G [00:19&lt;00:18, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  27%&#124;██▋       &#124; 607M/2.20G [00:19&lt;00:16, 104MB/s]<br>Downloading ncbitaxon.db.gz:  27%&#124;██▋       &#124; 615M/2.20G [00:19&lt;00:18, 95.5MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 625M/2.20G [00:19&lt;00:17, 98.0MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 634M/2.20G [00:19&lt;00:17, 97.3MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 642M/2.20G [00:19&lt;00:17, 94.8MB/s]<br>Downloading ncbitaxon.db.gz:  29%&#124;██▉       &#124; 652M/2.20G [00:19&lt;00:18, 89.8MB/s]<br>Downloading ncbitaxon.db.gz:  29%&#124;██▉       &#124; 664M/2.20G [00:19&lt;00:16, 100MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;██▉       &#124; 675M/2.20G [00:19&lt;00:15, 105MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;███       &#124; 678M/2.20G [00:20&lt;00:20, 80.2MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;███       &#124; 680M/2.20G [00:20&lt;00:25, 64.3MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███       &#124; 690M/2.20G [00:20&lt;00:22, 74.4MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███       &#124; 699M/2.20G [00:20&lt;00:20, 80.2MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███▏      &#124; 708M/2.20G [00:20&lt;00:19, 84.5MB/s]<br>Downloading ncbitaxon.db.gz:  32%&#124;███▏      &#124; 715M/2.20G [00:20&lt;00:20, 79.6MB/s]<br>Downloading ncbitaxon.db.gz:  32%&#124;███▏      &#124; 726M/2.20G [00:20&lt;00:17, 89.8MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 735M/2.20G [00:20&lt;00:17, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 745M/2.20G [00:20&lt;00:17, 92.4MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 755M/2.20G [00:21&lt;00:16, 94.4MB/s]<br>Downloading ncbitaxon.db.gz:  34%&#124;███▍      &#124; 764M/2.20G [00:21&lt;00:16, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  34%&#124;███▍      &#124; 774M/2.20G [00:21&lt;00:16, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▍      &#124; 782M/2.20G [00:21&lt;00:16, 93.1MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▌      &#124; 794M/2.20G [00:21&lt;00:15, 100MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▌      &#124; 800M/2.20G [00:21&lt;00:16, 89.9MB/s]<br>Downloading ncbitaxon.db.gz:  36%&#124;███▌      &#124; 813M/2.20G [00:21&lt;00:14, 103MB/s]<br>Downloading ncbitaxon.db.gz:  36%&#124;███▋      &#124; 823M/2.20G [00:21&lt;00:14, 102MB/s]<br>Downloading ncbitaxon.db.gz:  37%&#124;███▋      &#124; 830M/2.20G [00:21&lt;00:16, 93.0MB/s]<br>Downloading ncbitaxon.db.gz:  37%&#124;███▋      &#124; 841M/2.20G [00:21&lt;00:14, 99.7MB/s]<br>Downloading ncbitaxon.db.gz:  38%&#124;███▊      &#124; 849M/2.20G [00:22&lt;00:16, 90.4MB/s]<br>Downloading ncbitaxon.db.gz:  38%&#124;███▊      &#124; 861M/2.20G [00:22&lt;00:14, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▊      &#124; 871M/2.20G [00:22&lt;00:14, 103MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▉      &#124; 881M/2.20G [00:22&lt;00:14, 102MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▉      &#124; 891M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  40%&#124;███▉      &#124; 901M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  40%&#124;████      &#124; 910M/2.20G [00:22&lt;00:14, 99.4MB/s]<br>Downloading ncbitaxon.db.gz:  41%&#124;████      &#124; 919M/2.20G [00:22&lt;00:14, 93.5MB/s]<br>Downloading ncbitaxon.db.gz:  41%&#124;████▏     &#124; 932M/2.20G [00:22&lt;00:13, 104MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 941M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 950M/2.20G [00:23&lt;00:13, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 959M/2.20G [00:23&lt;00:14, 96.7MB/s]<br>Downloading ncbitaxon.db.gz:  43%&#124;████▎     &#124; 968M/2.20G [00:23&lt;00:13, 98.0MB/s]<br>Downloading ncbitaxon.db.gz:  43%&#124;████▎     &#124; 978M/2.20G [00:23&lt;00:13, 99.1MB/s]<br>Downloading ncbitaxon.db.gz:  44%&#124;████▍     &#124; 988M/2.20G [00:23&lt;00:13, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  44%&#124;████▍     &#124; 996M/2.20G [00:23&lt;00:14, 92.6MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▍     &#124; 0.98G/2.20G [00:23&lt;00:15, 85.3MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▍     &#124; 0.99G/2.20G [00:23&lt;00:15, 86.7MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▌     &#124; 1.00G/2.20G [00:23&lt;00:14, 88.2MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▌     &#124; 1.01G/2.20G [00:24&lt;00:13, 93.7MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▌     &#124; 1.02G/2.20G [00:24&lt;00:14, 88.6MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▋     &#124; 1.02G/2.20G [00:24&lt;00:15, 81.7MB/s]<br>Downloading ncbitaxon.db.gz:  47%&#124;████▋     &#124; 1.04G/2.20G [00:24&lt;00:13, 90.7MB/s]<br>Downloading ncbitaxon.db.gz:  47%&#124;████▋     &#124; 1.04G/2.20G [00:24&lt;00:14, 85.3MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.05G/2.20G [00:24&lt;00:13, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.06G/2.20G [00:24&lt;00:14, 85.4MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.07G/2.20G [00:24&lt;00:14, 86.0MB/s]<br>Downloading ncbitaxon.db.gz:  49%&#124;████▉     &#124; 1.08G/2.20G [00:24&lt;00:14, 84.2MB/s]<br>Downloading ncbitaxon.db.gz:  49%&#124;████▉     &#124; 1.09G/2.20G [00:24&lt;00:13, 92.2MB/s]<br>Downloading ncbitaxon.db.gz:  50%&#124;████▉     &#124; 1.10G/2.20G [00:25&lt;00:12, 97.1MB/s]<br>Downloading ncbitaxon.db.gz:  50%&#124;█████     &#124; 1.11G/2.20G [00:25&lt;00:12, 97.0MB/s]<br>Downloading ncbitaxon.db.gz:  51%&#124;█████     &#124; 1.12G/2.20G [00:25&lt;00:11, 100MB/s]<br>Downloading ncbitaxon.db.gz:  51%&#124;█████     &#124; 1.12G/2.20G [00:25&lt;00:12, 92.4MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.14G/2.20G [00:25&lt;00:11, 102MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.15G/2.20G [00:25&lt;00:11, 101MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.15G/2.20G [00:25&lt;00:12, 91.1MB/s]<br>Downloading ncbitaxon.db.gz:  53%&#124;█████▎    &#124; 1.16G/2.20G [00:25&lt;00:11, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  53%&#124;█████▎    &#124; 1.17G/2.20G [00:25&lt;00:11, 101MB/s]<br>Downloading ncbitaxon.db.gz:  54%&#124;█████▎    &#124; 1.18G/2.20G [00:26&lt;00:11, 97.2MB/s]<br>Downloading ncbitaxon.db.gz:  54%&#124;█████▍    &#124; 1.19G/2.20G [00:26&lt;00:12, 89.6MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▍    &#124; 1.20G/2.20G [00:26&lt;00:10, 102MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▍    &#124; 1.21G/2.20G [00:26&lt;00:11, 96.9MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▌    &#124; 1.22G/2.20G [00:26&lt;00:12, 87.5MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▌    &#124; 1.23G/2.20G [00:26&lt;00:10, 95.6MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▌    &#124; 1.24G/2.20G [00:26&lt;00:11, 91.4MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▋    &#124; 1.24G/2.20G [00:26&lt;00:11, 90.5MB/s]<br>Downloading ncbitaxon.db.gz:  57%&#124;█████▋    &#124; 1.26G/2.20G [00:26&lt;00:10, 101MB/s]<br>Downloading ncbitaxon.db.gz:  57%&#124;█████▋    &#124; 1.26G/2.20G [00:26&lt;00:10, 95.7MB/s]<br>Downloading ncbitaxon.db.gz:  58%&#124;█████▊    &#124; 1.28G/2.20G [00:27&lt;00:09, 102MB/s]<br>Downloading ncbitaxon.db.gz:  58%&#124;█████▊    &#124; 1.29G/2.20G [00:27&lt;00:09, 104MB/s]<br>Downloading ncbitaxon.db.gz:  59%&#124;█████▉    &#124; 1.30G/2.20G [00:27&lt;00:09, 106MB/s]<br>Downloading ncbitaxon.db.gz:  59%&#124;█████▉    &#124; 1.31G/2.20G [00:27&lt;00:09, 105MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;█████▉    &#124; 1.31G/2.20G [00:27&lt;00:10, 92.7MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;██████    &#124; 1.32G/2.20G [00:27&lt;00:09, 95.9MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;██████    &#124; 1.33G/2.20G [00:27&lt;00:09, 94.8MB/s]<br>Downloading ncbitaxon.db.gz:  61%&#124;██████    &#124; 1.34G/2.20G [00:27&lt;00:09, 97.7MB/s]<br>Downloading ncbitaxon.db.gz:  61%&#124;██████▏   &#124; 1.35G/2.20G [00:27&lt;00:09, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  62%&#124;██████▏   &#124; 1.36G/2.20G [00:27&lt;00:09, 99.2MB/s]<br>Downloading ncbitaxon.db.gz:  62%&#124;██████▏   &#124; 1.37G/2.20G [00:28&lt;00:08, 101MB/s]<br>Downloading ncbitaxon.db.gz:  63%&#124;██████▎   &#124; 1.38G/2.20G [00:28&lt;00:08, 106MB/s]<br>Downloading ncbitaxon.db.gz:  63%&#124;██████▎   &#124; 1.39G/2.20G [00:28&lt;00:08, 105MB/s]<br>Downloading ncbitaxon.db.gz:  64%&#124;██████▎   &#124; 1.40G/2.20G [00:28&lt;00:09, 95.9MB/s]<br>Downloading ncbitaxon.db.gz:  64%&#124;██████▍   &#124; 1.41G/2.20G [00:28&lt;00:07, 109MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▍   &#124; 1.42G/2.20G [00:28&lt;00:07, 108MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▍   &#124; 1.43G/2.20G [00:28&lt;00:07, 105MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▌   &#124; 1.44G/2.20G [00:28&lt;00:08, 102MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▌   &#124; 1.44G/2.20G [00:28&lt;00:10, 75.0MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▌   &#124; 1.46G/2.20G [00:29&lt;00:09, 86.5MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▋   &#124; 1.46G/2.20G [00:29&lt;00:09, 85.0MB/s]<br>Downloading ncbitaxon.db.gz:  67%&#124;██████▋   &#124; 1.47G/2.20G [00:29&lt;00:09, 82.2MB/s]<br>Downloading ncbitaxon.db.gz:  67%&#124;██████▋   &#124; 1.48G/2.20G [00:29&lt;00:08, 94.1MB/s]<br>Downloading ncbitaxon.db.gz:  68%&#124;██████▊   &#124; 1.49G/2.20G [00:29&lt;00:08, 95.2MB/s]<br>Downloading ncbitaxon.db.gz:  68%&#124;██████▊   &#124; 1.50G/2.20G [00:29&lt;00:08, 93.4MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▊   &#124; 1.51G/2.20G [00:29&lt;00:07, 96.2MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.52G/2.20G [00:29&lt;00:08, 88.3MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:29&lt;00:08, 90.6MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:29&lt;00:10, 69.0MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:30&lt;00:14, 49.3MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.53G/2.20G [00:30&lt;00:14, 49.6MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.54G/2.20G [00:30&lt;00:15, 46.0MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.54G/2.20G [00:30&lt;00:15, 44.7MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;███████   &#124; 1.55G/2.20G [00:30&lt;00:12, 57.0MB/s]<br>Downloading ncbitaxon.db.gz:  71%&#124;███████   &#124; 1.56G/2.20G [00:30&lt;00:09, 71.1MB/s]<br>Downloading ncbitaxon.db.gz:  71%&#124;███████   &#124; 1.57G/2.20G [00:30&lt;00:08, 80.4MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.58G/2.20G [00:30&lt;00:08, 78.6MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.59G/2.20G [00:30&lt;00:07, 86.2MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.60G/2.20G [00:31&lt;00:06, 93.3MB/s]<br>Downloading ncbitaxon.db.gz:  73%&#124;███████▎  &#124; 1.60G/2.20G [00:31&lt;00:07, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  73%&#124;███████▎  &#124; 1.61G/2.20G [00:31&lt;00:06, 90.3MB/s]<br>Downloading ncbitaxon.db.gz:  74%&#124;███████▍  &#124; 1.63G/2.20G [00:31&lt;00:06, 94.0MB/s]<br>Downloading ncbitaxon.db.gz:  74%&#124;███████▍  &#124; 1.64G/2.20G [00:31&lt;00:06, 98.1MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▍  &#124; 1.64G/2.20G [00:31&lt;00:06, 88.9MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▌  &#124; 1.65G/2.20G [00:31&lt;00:06, 94.0MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▌  &#124; 1.66G/2.20G [00:31&lt;00:06, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  76%&#124;███████▌  &#124; 1.67G/2.20G [00:31&lt;00:05, 97.5MB/s]<br>Downloading ncbitaxon.db.gz:  76%&#124;███████▋  &#124; 1.68G/2.20G [00:31&lt;00:05, 96.2MB/s]<br>Downloading ncbitaxon.db.gz:  77%&#124;███████▋  &#124; 1.69G/2.20G [00:32&lt;00:06, 91.3MB/s]<br>Downloading ncbitaxon.db.gz:  77%&#124;███████▋  &#124; 1.70G/2.20G [00:32&lt;00:05, 94.5MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.71G/2.20G [00:32&lt;00:05, 97.5MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.72G/2.20G [00:32&lt;00:05, 97.8MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.73G/2.20G [00:32&lt;00:05, 93.9MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.74G/2.20G [00:32&lt;00:05, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.74G/2.20G [00:32&lt;00:05, 87.4MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.75G/2.20G [00:32&lt;00:05, 90.4MB/s]<br>Downloading ncbitaxon.db.gz:  80%&#124;███████▉  &#124; 1.76G/2.20G [00:32&lt;00:05, 94.2MB/s]<br>Downloading ncbitaxon.db.gz:  80%&#124;████████  &#124; 1.77G/2.20G [00:33&lt;00:04, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  81%&#124;████████  &#124; 1.78G/2.20G [00:33&lt;00:04, 95.6MB/s]<br>Downloading ncbitaxon.db.gz:  81%&#124;████████  &#124; 1.79G/2.20G [00:33&lt;00:04, 98.6MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.80G/2.20G [00:33&lt;00:04, 94.1MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.81G/2.20G [00:33&lt;00:04, 98.2MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.82G/2.20G [00:33&lt;00:04, 94.7MB/s]<br>Downloading ncbitaxon.db.gz:  83%&#124;████████▎ &#124; 1.83G/2.20G [00:33&lt;00:04, 100MB/s]<br>Downloading ncbitaxon.db.gz:  83%&#124;████████▎ &#124; 1.84G/2.20G [00:33&lt;00:03, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  84%&#124;████████▎ &#124; 1.85G/2.20G [00:33&lt;00:03, 99.8MB/s]<br>Downloading ncbitaxon.db.gz:  84%&#124;████████▍ &#124; 1.85G/2.20G [00:33&lt;00:03, 100MB/s]<br>Downloading ncbitaxon.db.gz:  85%&#124;████████▍ &#124; 1.86G/2.20G [00:34&lt;00:03, 102MB/s]<br>Downloading ncbitaxon.db.gz:  85%&#124;████████▌ &#124; 1.87G/2.20G [00:34&lt;00:03, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▌ &#124; 1.88G/2.20G [00:34&lt;00:03, 102MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▌ &#124; 1.89G/2.20G [00:34&lt;00:03, 99.6MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▋ &#124; 1.90G/2.20G [00:34&lt;00:03, 93.5MB/s]<br>Downloading ncbitaxon.db.gz:  87%&#124;████████▋ &#124; 1.91G/2.20G [00:34&lt;00:03, 91.4MB/s]<br>Downloading ncbitaxon.db.gz:  87%&#124;████████▋ &#124; 1.92G/2.20G [00:34&lt;00:02, 102MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.93G/2.20G [00:34&lt;00:03, 92.0MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.94G/2.20G [00:34&lt;00:02, 99.2MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.95G/2.20G [00:34&lt;00:02, 92.9MB/s]<br>Downloading ncbitaxon.db.gz:  89%&#124;████████▉ &#124; 1.96G/2.20G [00:35&lt;00:02, 97.0MB/s]<br>Downloading ncbitaxon.db.gz:  89%&#124;████████▉ &#124; 1.97G/2.20G [00:35&lt;00:02, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  90%&#124;████████▉ &#124; 1.98G/2.20G [00:35&lt;00:02, 96.5MB/s]<br>Downloading ncbitaxon.db.gz:  90%&#124;█████████ &#124; 1.98G/2.20G [00:35&lt;00:02, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████ &#124; 1.99G/2.20G [00:35&lt;00:02, 95.0MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████ &#124; 2.00G/2.20G [00:35&lt;00:02, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████▏&#124; 2.01G/2.20G [00:35&lt;00:02, 93.6MB/s]<br>Downloading ncbitaxon.db.gz:  92%&#124;█████████▏&#124; 2.02G/2.20G [00:35&lt;00:02, 91.0MB/s]<br>Downloading ncbitaxon.db.gz:  92%&#124;█████████▏&#124; 2.03G/2.20G [00:35&lt;00:01, 93.2MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.04G/2.20G [00:36&lt;00:01, 94.5MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.05G/2.20G [00:36&lt;00:01, 95.2MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.06G/2.20G [00:36&lt;00:01, 97.9MB/s]<br>Downloading ncbitaxon.db.gz:  94%&#124;█████████▍&#124; 2.07G/2.20G [00:36&lt;00:01, 94.2MB/s]<br>Downloading ncbitaxon.db.gz:  94%&#124;█████████▍&#124; 2.07G/2.20G [00:36&lt;00:01, 87.4MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▍&#124; 2.08G/2.20G [00:36&lt;00:01, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▍&#124; 2.09G/2.20G [00:36&lt;00:01, 97.9MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▌&#124; 2.10G/2.20G [00:36&lt;00:01, 94.4MB/s]<br>Downloading ncbitaxon.db.gz:  96%&#124;█████████▌&#124; 2.11G/2.20G [00:36&lt;00:01, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  96%&#124;█████████▌&#124; 2.12G/2.20G [00:36&lt;00:00, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  97%&#124;█████████▋&#124; 2.13G/2.20G [00:37&lt;00:00, 96.0MB/s]<br>Downloading ncbitaxon.db.gz:  97%&#124;█████████▋&#124; 2.14G/2.20G [00:37&lt;00:00, 97.3MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.15G/2.20G [00:37&lt;00:00, 100MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.16G/2.20G [00:37&lt;00:00, 94.3MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.17G/2.20G [00:37&lt;00:00, 102MB/s]<br>Downloading ncbitaxon.db.gz:  99%&#124;█████████▉&#124; 2.18G/2.20G [00:37&lt;00:00, 91.8MB/s]<br>Downloading ncbitaxon.db.gz:  99%&#124;█████████▉&#124; 2.19G/2.20G [00:37&lt;00:00, 99.7MB/s]<br>Downloading ncbitaxon.db.gz: 100%&#124;█████████▉&#124; 2.20G/2.20G [00:37&lt;00:00, 98.0MB/s] |
| validate-references | passed | True | CultureMech:000038 | Validating evidence references (MediaRecipe)...<br>Reference checks: 3; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000038 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| validate-terms-initial-network-attempt | failed | False | CultureMech:000038 | Original sandbox attempt could not resolve a public dependency/reference host. Preserved as a failed historical attempt with its actual exit code; the same documented check later completed successfully with network access. |
| validate-references-initial-network-attempt | failed | False | CultureMech:000038 | Original sandbox attempt could not resolve a public dependency/reference host. Preserved as a failed historical attempt with its actual exit code; the same documented check later completed successfully with network access. |
| Verify complete Tsuji methods | unavailable | True | CultureMech:000038 | Subscription preview and public supplement available; exact paper strain attribution, preacclimation sequence and potential main-text explanation of selenite conflict remain unverified. |
| Verify Liang complete study formulation | unavailable | True | CultureMech:000038 | Full article body available; external author-hosted TableS2 failed DNS and full study composition remains unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000038.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:000038.

13 primary CHEBI identities resolve with matching labels; 0 of 0 current secondary keys have live pinned-index rows. Unresolved keys: [].

13 direct ingredient instances; CHEBI-primary instance linkage 13/13 (100.00%), verified secondary coverage 0/13 (0.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### Exact CCAP parent and study-medium boundaries

identity: concern. Targets: CultureMech:000038.

CCAP2ASW accession and current revision are supported. F/2ASW in Matsui and the defined modified F/2ASW in Tsuji are study formulations whose derivation from this CCAP parent is not established. Similar ASW names do not prove recipe ancestry. New owner variants retain explicit incomplete-formula limits.

### All13 ingredient concentrations and three stock additions

quantity: concern. Targets: CultureMech:000038.

correct: first3 values are extra-salts stock g/L and next8 are vitamin-stock g/L. Their nominal added contributions require7.50mL/L and2.50mL/L respectively. Last2 values are direct tricine/NaCl additions. The nitrate note acknowledges stock basis but does not provide a structured stock or dose. Soil extract25mL/L is omitted. Retain source stock compositions and dose hierarchy instead of merely overwriting with derived final contributions.

[{"field": "ingredients[0].concentration", "material": "NaNO3", "record_value_g_l": "15.00", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.112500", "calculation": "15.00 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[1].concentration", "material": "Na2HPO4", "record_value_g_l": "0.60", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.004500", "calculation": "0.60 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[2].concentration", "material": "K2HPO4", "record_value_g_l": "0.50", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.003750", "calculation": "0.50 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[3].concentration", "material": "Biotin", "record_value_g_l": "0.0002", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "5.0E-7", "calculation": "0.0002 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[4].concentration", "material": "Calcium pantothenate", "record_value_g_l": "0.02", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[5].concentration", "material": "Cyanocobalamin", "record_value_g_l": "0.004", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.0000100", "calculation": "0.004 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[6].concentration", "material": "Folic acid", "record_value_g_l": "0.0004", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00000100", "calculation": "0.0004 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[7].concentration", "material": "Inositol", "record_value_g_l": "1.0", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00250", "calculation": "1.0 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[8].concentration", "material": "Nicotinic acid", "record_value_g_l": "0.02", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[9].concentration", "material": "Thiamine HCl", "record_value_g_l": "0.1", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00025", "calculation": "0.1 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[10].concentration", "material": "Thymine", "record_value_g_l": "0.6", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00150", "calculation": "0.6 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[11].concentration", "material": "Tricine", "record_value_g_l": "0.50", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre": "0.50", "calculation": "No stock dilution: source directly states medium addition per litre.", "decision": "verified direct addition; not total seawater content"}, {"field": "ingredients[12].concentration", "material": "NaCl", "record_value_g_l": "35.00", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre": "35.00", "calculation": "No stock dilution: source directly states medium addition per litre.", "decision": "verified direct addition; not total seawater content"}]

### Water alternatives, pH and sterilization

completeness: concern. Targets: CultureMech:000038.

add: make to1L with filtered natural seawater; alternative deionised water to1L plus33.6g Instant Ocean sea salts. Preserve this water-base alternative alongside listed35g NaCl without assuming the sea salts replace that addition. Source pH7.6–7.8 uses1M NaOH or1M HCl before autoclaving15psi15min. These are absent from both local layers. Reagent strength is not final concentration; added titrant volumes and total seawater ion content are unknown.

### Canonical labels and source specificity

grounding: concern. Targets: CultureMech:000038.

All13 primary labels/IDs resolve and are not obsolete; no secondary keys are asserted. Primary linkage13/13(100%) and secondary0/13(0%) measure linkage only. Eleven exact preferred-name MIM rows agree. Inositol maps to myo-inositol although the source is nonspecific; Tricine maps to a broader class than pinned MIM. Neither discrepancy proves a different supplied chemical.

### D.salina CCAP19/18 parent maintenance and identifiers

evidence: supported. Targets: CultureMech:000038.

Collection evidence supports the named strain in2ASW, axenic serial subculture at20–35C. Taxid3046 is species rank, while collection strain and genome metadata provide strain context. BioProject/assembly/WGS/BioSample identity support is distinct from cultivation evidence.

### Two Matsui diatom strain claims and harvest context

grounding: concern. Targets: CultureMech:000038.

The paper supports UTEX642 and CCMP1335 in study F/2ASW with the stated20C, continuous light, CO2/air and harvest OD730 ranges. OD is a midlog sampling criterion, not terminal yield. CCMP1335 matches taxid296543 and independent genome identifiers. UTEX642 is CCAP1052/1A/Pt2, while asserted556484 is CCAP1055/1/Pt1 clone8.6; narrative caution cannot repair that strain mismatch.

### Sodium-response strain and variant claims

evidence: unknown. Targets: CultureMech:000038.

The abstract supports species-level sodium/CO2 observations; TableS1 supports NaCl manipulation and0.1mM nonahydrate metasilicate. Its0.001micromolar selenite equals1nM, conflicting with the record10nM. Exact paper strain/preacclimation await full methods. UTEX verifies collection LB2658 naming, but authority/alias differences leave its taxon unresolved; no wrong taxon is asserted because the record has no term.

### Structured growth scope and export consequences

scope: concern. Targets: CultureMech:000038.

The three non-Dunaliella descriptors describe study media in prose but lack scoped_to_variant. Current code would emit parent edges for the two grounded diatoms. Correct formulation relationships first, then scope or relocate growth. Current code suppresses scoped parent growth; it does not establish complete variant-growth export.

### Two owner-only study variants and taxonomic qualifications

evidence: supported. Targets: CultureMech:000038.

Liang1.5M NaCl and Hiibel33.6g/L sea-salt substitution have exact narrow support; neither supplies a complete inherited parent recipe. All18 Dunaliella names/strains match Table1 and owner notes; genus-only rows and disputed UTEX LB200 remain qualified. D.bardawil is a taxonomic synonym of D.salina, not independent strain verification. Centrate results and other-medium cohorts are not promoted to2ASW growth.

### Later owner references and variants missing from generated target

completeness: concern. Targets: CultureMech:000038.

Two bounded study variants, three paper references and the October14 citation event are absent from the generated record. Shared legacy recipe/strain errors remain in both layers and must be corrected before regeneration.

### Citation identity, evidence placement, history and stale export notes

provenance: concern. Targets: CultureMech:000038.

Five paper identities/authors/years and all asserted project/genome identifiers were checked. Four legacy history entries per layer lack timezones; retain uncertainty and append-only history. Most legacy claims lack exact excerpts, and CCMP1335 genome support is attached only to a growth DOI. Owner references[6] and[7] incorrectly describe current KGX as ignoring variant scope.

### Generic conditions, classifications and applications

scope: concern. Targets: CultureMech:000038.

Algae/COMPLEX/UNDEFINED/LIQUID agrees with the seawater/soil-extract recipe; isolate describes separate named cultures, not universal axenicity. Light50–100,12:12/16:8 and15–30C are importer defaults, not verified parent conditions. They must not replace collection20–35C or distinct experimental conditions. Marine is descriptive;35g NaCl is not total salinity. Process quality flags do not certify formulation accuracy.

## Findings

### f1: Stock compositions are flattened into the medium recipe

blocker / open / confirmed; issue key: CM000038-stock-hierarchy.

Eleven stock g/L values appear as direct ingredients; stock doses7.50/2.50mL per final litre and soil-extract25mL/L are absent. This cannot represent the source formulation.

### f2: Source base alternatives and preparation are missing

major / open / confirmed; issue key: CM000038-source-preparation.

Neither layer represents filtered seawater/deionised-water plus Instant Ocean alternatives, final litre, pH7.6–7.8 with1M titrant or15psi15min autoclaving.

### f3: UTEX642 is assigned the taxon of a distinct collection strain

blocker / open / confirmed; issue key: CM000038-utex642-wrong-strain-taxon.

Primary collection sources identify UTEX642 with CCAP1052/1A/Pt2; NCBITaxon556484 names CCAP1055/1/Pt1 clone8.6. The PARTIAL prose caution does not make this asserted strain taxon correct.

### f4: Diatom study media lack established CCAP parent ancestry

major / open / confirmed; issue key: CM000038-diatom-parent-identity.

Legacy variants treat F/2ASW and modified F/2ASW as descendants of this CCAP extra-salts/vitamin/soil-extract recipe. The inspected publications do not establish that relationship.

### f5: Recorded selenite is ten times the supplementary formulation

major / open / confirmed; issue key: CM000038-selenite-source-conflict.

The record10nM sodium selenite conflicts with TableS1 0.001micromolar=1nM.0.1mM metasilicate is supported, with nonahydrate form in the source.

### f6: Variant-only growth lacks structured scope

major / open / confirmed; issue key: CM000038-variant-growth-scope.

Three study-medium organism descriptors qualify scope only in prose. The grounded diatoms would become parent growth edges under current export code.

### f7: Parent culture conditions are unsupported importer defaults

major / open / confirmed; issue key: CM000038-generic-culture-defaults.

The light intensity/cycle and temperature strings are unconditional importer values. Source maintenance and study conditions are different and strain-specific.

### f8: Generated target omits bounded owner study additions

major / open / confirmed; issue key: CM000038-generated-study-staleness.

Two study variants, three references and later citation history are missing from the target despite their bounded support in the owner.

### f9: Legacy claims lack narrow excerpts and identity sources

minor / open / confirmed; issue key: CM000038-claim-evidence-placement.

Legacy ingredients, variants and organism observations mostly have source pointers/explanations without exact excerpts. CCMP1335 assembly/BioSample/WGS support requires the independent NCBI source.

### f10: Two mappings need source-specific granularity review

minor / open / confirmed; issue key: CM000038-grounding-specificity.

CCAP Inositol does not specify myo stereochemistry; the pinned index uses generic inositol. Tricine target class is broader than the pinned molecular term. Canonical labels resolve and a wrong supplied chemical is not established.

### f11: Owner notes misstate current variant export behavior

minor / open / confirmed; issue key: CM000038-stale-export-notes.

Two later owner citation notes say current KGX ignores scoped_to_variant; current code suppresses scoped parent growth.

### f12: Four legacy history entries lack timezone context

minor / open / confirmed; issue key: CM000038-history-timezone-gap.

Each layer retains one date-only and three naive timestamps. Their timezone cannot be reconstructed from the text.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct verified stock composition and dose hierarchy in the maintained owner, including SE1 and its source preparation; preserve original stock concentrations and separate any derived contributions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add source-scoped alternatives, preparation and exact evidence, preserving seawater composition and titrant-volume uncertainty.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the supported strain identity or an explicitly qualified broader species mapping; retain UTEX642 paper evidence without transferring it to a different strain.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Verify exact recipe identity and ancestry; retain distinct study-media records or qualified relationships where full parent equivalence is unsupported.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reconcile exact main-text/supplement protocol before changing the owner; preserve the observed discrepancy and inaccessible-methods limit, and cite the resolved quantity/form.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

After resolving organism and formulation identity, scope each descriptor to its verified variant or linked medium; verify that no unsupported parent growth edge is emitted.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a7

Remove or explicitly qualify generic defaults and retain only source-supported strain/formulation-scoped conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a8

After shared legacy errors and stale owner notes are curated, regenerate and verify narrow excerpts, study limits and taxonomic qualifications survive.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a9

Attach short exact field-scoped excerpts and metadata while keeping growth, sequence identity, stock arithmetic and unresolved methods distinct.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a10

Reconcile ontology granularity using source material identity and the packaged resolver; document unresolved inositol specificity rather than guessing another isomer.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a11

Correct current-versus-historical wording on a future authorized owner edit and distinguish parent-edge suppression from actual variant-edge support.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a12

Preserve append-only events and record any recoverable timestamp context in a new provenance event; do not invent a timezone or silently rewrite history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2ASW.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/algae/2asw.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2ASW.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2ASW.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch008/078/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch008/078/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2ASW.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br><br><br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 0.00/2.20G [00:00&lt;?, ?B/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 1.12M/2.20G [00:00&lt;03:29, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 2.19M/2.20G [00:00&lt;03:32, 11.1MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 4.44M/2.20G [00:00&lt;02:22, 16.5MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 5.50M/2.20G [00:00&lt;02:43, 14.4MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 6.50M/2.20G [00:00&lt;03:03, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 7.88M/2.20G [00:00&lt;02:56, 13.4MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 9.00M/2.20G [00:00&lt;03:06, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 10.0M/2.20G [00:00&lt;03:19, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 14.1M/2.20G [00:00&lt;01:50, 21.4MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 22.7M/2.20G [00:01&lt;00:59, 39.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 33.9M/2.20G [00:01&lt;00:37, 61.6MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 42.4M/2.20G [00:01&lt;00:33, 69.5MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 49.7M/2.20G [00:01&lt;00:32, 71.0MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 53.5M/2.20G [00:01&lt;00:37, 61.1MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 55.0M/2.20G [00:01&lt;00:48, 47.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 56.6M/2.20G [00:01&lt;00:59, 38.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 57.9M/2.20G [00:01&lt;01:16, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 59.0M/2.20G [00:01&lt;01:33, 24.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 60.1M/2.20G [00:01&lt;01:58, 19.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 61.1M/2.20G [00:02&lt;02:17, 16.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 62.6M/2.20G [00:02&lt;02:19, 16.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 64.4M/2.20G [00:02&lt;02:15, 17.0MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 65.6M/2.20G [00:02&lt;02:28, 15.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 67.0M/2.20G [00:02&lt;02:32, 15.0MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 68.1M/2.20G [00:02&lt;02:46, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 69.4M/2.20G [00:02&lt;02:50, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 70.5M/2.20G [00:02&lt;02:57, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 71.8M/2.20G [00:02&lt;02:59, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 72.8M/2.20G [00:03&lt;03:18, 11.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 73.7M/2.20G [00:03&lt;03:29, 10.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 75.2M/2.20G [00:03&lt;03:06, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 76.2M/2.20G [00:03&lt;03:18, 11.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 77.1M/2.20G [00:03&lt;03:36, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 78.1M/2.20G [00:03&lt;03:42, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 79.1M/2.20G [00:03&lt;03:46, 10.1MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 79.9M/2.20G [00:03&lt;03:57, 9.59MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 80.7M/2.20G [00:03&lt;04:09, 9.15MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 81.9M/2.20G [00:03&lt;03:48, 9.99MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 83.2M/2.20G [00:04&lt;03:28, 10.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▎         &#124; 84.4M/2.20G [00:04&lt;03:21, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 85.3M/2.20G [00:04&lt;03:29, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 86.3M/2.20G [00:04&lt;03:34, 10.6MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 87.8M/2.20G [00:04&lt;03:12, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 89.6M/2.20G [00:04&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 91.0M/2.20G [00:04&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 92.4M/2.20G [00:04&lt;02:43, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 94.0M/2.20G [00:04&lt;02:33, 14.7MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 95.1M/2.20G [00:05&lt;02:44, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 96.2M/2.20G [00:05&lt;03:02, 12.4MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 97.4M/2.20G [00:05&lt;03:09, 11.9MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 98.6M/2.20G [00:05&lt;03:05, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 99.9M/2.20G [00:05&lt;03:00, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 102M/2.20G [00:05&lt;02:46, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 103M/2.20G [00:05&lt;02:34, 14.6MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 104M/2.20G [00:05&lt;02:42, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 106M/2.20G [00:05&lt;02:42, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 107M/2.20G [00:05&lt;02:51, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 109M/2.20G [00:06&lt;02:45, 13.6MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 110M/2.20G [00:06&lt;02:55, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 110M/2.20G [00:06&lt;03:24, 11.0MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 111M/2.20G [00:06&lt;03:51, 9.71MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 112M/2.20G [00:06&lt;03:51, 9.71MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 113M/2.20G [00:06&lt;03:47, 9.87MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 114M/2.20G [00:06&lt;03:49, 9.80MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 115M/2.20G [00:06&lt;03:34, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:06&lt;04:09, 9.00MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:07&lt;04:44, 7.90MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 118M/2.20G [00:07&lt;03:17, 11.4MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;03:53, 9.59MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;04:52, 7.67MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 119M/2.20G [00:07&lt;05:42, 6.53MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:07&lt;06:13, 5.99MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:07&lt;06:20, 5.88MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 121M/2.20G [00:07&lt;06:03, 6.16MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 122M/2.20G [00:07&lt;05:28, 6.81MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 123M/2.20G [00:07&lt;04:49, 7.73MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 124M/2.20G [00:08&lt;04:12, 8.85MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 125M/2.20G [00:08&lt;03:41, 10.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 127M/2.20G [00:08&lt;03:02, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 129M/2.20G [00:08&lt;02:26, 15.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 131M/2.20G [00:08&lt;02:21, 15.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 132M/2.20G [00:08&lt;02:37, 14.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 133M/2.20G [00:08&lt;02:41, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 134M/2.20G [00:08&lt;02:47, 13.3MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 136M/2.20G [00:08&lt;02:44, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 137M/2.20G [00:09&lt;02:56, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 138M/2.20G [00:09&lt;03:10, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 140M/2.20G [00:09&lt;02:49, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 140M/2.20G [00:09&lt;03:08, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 141M/2.20G [00:09&lt;03:14, 11.4MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 142M/2.20G [00:09&lt;03:35, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 143M/2.20G [00:09&lt;03:30, 10.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 145M/2.20G [00:09&lt;03:05, 11.9MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:09&lt;03:05, 12.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 147M/2.20G [00:09&lt;03:00, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:10&lt;03:02, 12.1MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:10&lt;03:08, 11.7MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 151M/2.20G [00:10&lt;03:06, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 152M/2.20G [00:10&lt;02:54, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 154M/2.20G [00:10&lt;02:48, 13.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 155M/2.20G [00:10&lt;02:50, 13.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 156M/2.20G [00:10&lt;02:55, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 158M/2.20G [00:10&lt;02:42, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 158M/2.20G [00:10&lt;03:00, 12.2MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 159M/2.20G [00:11&lt;03:23, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 160M/2.20G [00:11&lt;03:32, 10.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 161M/2.20G [00:11&lt;03:36, 10.2MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 162M/2.20G [00:11&lt;03:22, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 163M/2.20G [00:11&lt;03:22, 10.8MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 164M/2.20G [00:11&lt;03:26, 10.6MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 166M/2.20G [00:11&lt;03:13, 11.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 167M/2.20G [00:11&lt;02:57, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 168M/2.20G [00:11&lt;02:54, 12.6MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 169M/2.20G [00:11&lt;03:05, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 171M/2.20G [00:12&lt;02:47, 13.1MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 172M/2.20G [00:12&lt;02:42, 13.4MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 174M/2.20G [00:12&lt;02:37, 13.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 175M/2.20G [00:12&lt;02:36, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 177M/2.20G [00:12&lt;02:37, 13.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 178M/2.20G [00:12&lt;02:31, 14.4MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 179M/2.20G [00:12&lt;02:59, 12.1MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 180M/2.20G [00:12&lt;02:51, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 182M/2.20G [00:12&lt;02:48, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 182M/2.20G [00:12&lt;03:04, 11.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 184M/2.20G [00:13&lt;02:54, 12.5MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 185M/2.20G [00:13&lt;02:38, 13.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 186M/2.20G [00:13&lt;02:50, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 188M/2.20G [00:13&lt;02:40, 13.5MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 189M/2.20G [00:13&lt;02:43, 13.2MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 190M/2.20G [00:13&lt;02:49, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   8%&#124;▊         &#124; 192M/2.20G [00:13&lt;02:49, 12.8MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 193M/2.20G [00:13&lt;02:37, 13.7MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 194M/2.20G [00:13&lt;02:55, 12.3MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 195M/2.20G [00:14&lt;02:47, 12.9MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▊         &#124; 197M/2.20G [00:14&lt;02:24, 14.9MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 200M/2.20G [00:14&lt;01:50, 19.4MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 204M/2.20G [00:14&lt;01:26, 24.7MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 208M/2.20G [00:14&lt;01:15, 28.5MB/s]<br>Downloading ncbitaxon.db.gz:   9%&#124;▉         &#124; 211M/2.20G [00:14&lt;01:07, 31.6MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;▉         &#124; 216M/2.20G [00:14&lt;01:01, 35.0MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;▉         &#124; 221M/2.20G [00:14&lt;00:52, 40.3MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;█         &#124; 227M/2.20G [00:14&lt;00:46, 46.1MB/s]<br>Downloading ncbitaxon.db.gz:  10%&#124;█         &#124; 233M/2.20G [00:14&lt;00:42, 49.7MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█         &#124; 241M/2.20G [00:15&lt;00:35, 59.6MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█         &#124; 252M/2.20G [00:15&lt;00:28, 73.7MB/s]<br>Downloading ncbitaxon.db.gz:  11%&#124;█▏        &#124; 259M/2.20G [00:15&lt;00:28, 74.7MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 263M/2.20G [00:15&lt;00:32, 64.8MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 274M/2.20G [00:15&lt;00:26, 77.5MB/s]<br>Downloading ncbitaxon.db.gz:  12%&#124;█▏        &#124; 282M/2.20G [00:15&lt;00:26, 79.4MB/s]<br>Downloading ncbitaxon.db.gz:  13%&#124;█▎        &#124; 292M/2.20G [00:15&lt;00:23, 88.3MB/s]<br>Downloading ncbitaxon.db.gz:  13%&#124;█▎        &#124; 302M/2.20G [00:15&lt;00:22, 92.0MB/s]<br>Downloading ncbitaxon.db.gz:  14%&#124;█▍        &#124; 312M/2.20G [00:15&lt;00:21, 96.7MB/s]<br>Downloading ncbitaxon.db.gz:  14%&#124;█▍        &#124; 322M/2.20G [00:15&lt;00:20, 98.6MB/s]<br>Downloading ncbitaxon.db.gz:  15%&#124;█▍        &#124; 332M/2.20G [00:16&lt;00:20, 100MB/s]<br>Downloading ncbitaxon.db.gz:  15%&#124;█▌        &#124; 341M/2.20G [00:16&lt;00:22, 90.5MB/s]<br>Downloading ncbitaxon.db.gz:  16%&#124;█▌        &#124; 354M/2.20G [00:16&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  16%&#124;█▌        &#124; 363M/2.20G [00:16&lt;00:19, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 373M/2.20G [00:16&lt;00:19, 102MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 383M/2.20G [00:16&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  17%&#124;█▋        &#124; 392M/2.20G [00:16&lt;00:19, 100MB/s]<br>Downloading ncbitaxon.db.gz:  18%&#124;█▊        &#124; 402M/2.20G [00:16&lt;00:19, 100MB/s]<br>Downloading ncbitaxon.db.gz:  18%&#124;█▊        &#124; 410M/2.20G [00:16&lt;00:20, 95.3MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▊        &#124; 421M/2.20G [00:17&lt;00:19, 101MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▉        &#124; 430M/2.20G [00:17&lt;00:19, 98.4MB/s]<br>Downloading ncbitaxon.db.gz:  19%&#124;█▉        &#124; 439M/2.20G [00:17&lt;00:19, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  20%&#124;█▉        &#124; 449M/2.20G [00:17&lt;00:19, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  20%&#124;██        &#124; 458M/2.20G [00:17&lt;00:19, 96.5MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██        &#124; 467M/2.20G [00:17&lt;00:19, 96.4MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██        &#124; 473M/2.20G [00:17&lt;00:21, 85.9MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██▏       &#124; 481M/2.20G [00:17&lt;00:22, 82.7MB/s]<br>Downloading ncbitaxon.db.gz:  21%&#124;██▏       &#124; 481M/2.20G [00:17&lt;00:38, 47.9MB/s]<br>Downloading ncbitaxon.db.gz:  22%&#124;██▏       &#124; 488M/2.20G [00:17&lt;00:34, 54.4MB/s]<br>Downloading ncbitaxon.db.gz:  22%&#124;██▏       &#124; 500M/2.20G [00:18&lt;00:25, 72.3MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 508M/2.20G [00:18&lt;00:26, 70.3MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 518M/2.20G [00:18&lt;00:22, 81.2MB/s]<br>Downloading ncbitaxon.db.gz:  23%&#124;██▎       &#124; 528M/2.20G [00:18&lt;00:20, 86.6MB/s]<br>Downloading ncbitaxon.db.gz:  24%&#124;██▍       &#124; 538M/2.20G [00:18&lt;00:19, 90.6MB/s]<br>Downloading ncbitaxon.db.gz:  24%&#124;██▍       &#124; 546M/2.20G [00:18&lt;00:20, 87.5MB/s]<br>Downloading ncbitaxon.db.gz:  25%&#124;██▍       &#124; 556M/2.20G [00:18&lt;00:19, 90.9MB/s]<br>Downloading ncbitaxon.db.gz:  25%&#124;██▌       &#124; 568M/2.20G [00:18&lt;00:17, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▌       &#124; 577M/2.20G [00:18&lt;00:17, 98.1MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▌       &#124; 586M/2.20G [00:19&lt;00:17, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  26%&#124;██▋       &#124; 595M/2.20G [00:19&lt;00:18, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  27%&#124;██▋       &#124; 607M/2.20G [00:19&lt;00:16, 104MB/s]<br>Downloading ncbitaxon.db.gz:  27%&#124;██▋       &#124; 615M/2.20G [00:19&lt;00:18, 95.5MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 625M/2.20G [00:19&lt;00:17, 98.0MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 634M/2.20G [00:19&lt;00:17, 97.3MB/s]<br>Downloading ncbitaxon.db.gz:  28%&#124;██▊       &#124; 642M/2.20G [00:19&lt;00:17, 94.8MB/s]<br>Downloading ncbitaxon.db.gz:  29%&#124;██▉       &#124; 652M/2.20G [00:19&lt;00:18, 89.8MB/s]<br>Downloading ncbitaxon.db.gz:  29%&#124;██▉       &#124; 664M/2.20G [00:19&lt;00:16, 100MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;██▉       &#124; 675M/2.20G [00:19&lt;00:15, 105MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;███       &#124; 678M/2.20G [00:20&lt;00:20, 80.2MB/s]<br>Downloading ncbitaxon.db.gz:  30%&#124;███       &#124; 680M/2.20G [00:20&lt;00:25, 64.3MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███       &#124; 690M/2.20G [00:20&lt;00:22, 74.4MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███       &#124; 699M/2.20G [00:20&lt;00:20, 80.2MB/s]<br>Downloading ncbitaxon.db.gz:  31%&#124;███▏      &#124; 708M/2.20G [00:20&lt;00:19, 84.5MB/s]<br>Downloading ncbitaxon.db.gz:  32%&#124;███▏      &#124; 715M/2.20G [00:20&lt;00:20, 79.6MB/s]<br>Downloading ncbitaxon.db.gz:  32%&#124;███▏      &#124; 726M/2.20G [00:20&lt;00:17, 89.8MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 735M/2.20G [00:20&lt;00:17, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 745M/2.20G [00:20&lt;00:17, 92.4MB/s]<br>Downloading ncbitaxon.db.gz:  33%&#124;███▎      &#124; 755M/2.20G [00:21&lt;00:16, 94.4MB/s]<br>Downloading ncbitaxon.db.gz:  34%&#124;███▍      &#124; 764M/2.20G [00:21&lt;00:16, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  34%&#124;███▍      &#124; 774M/2.20G [00:21&lt;00:16, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▍      &#124; 782M/2.20G [00:21&lt;00:16, 93.1MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▌      &#124; 794M/2.20G [00:21&lt;00:15, 100MB/s]<br>Downloading ncbitaxon.db.gz:  35%&#124;███▌      &#124; 800M/2.20G [00:21&lt;00:16, 89.9MB/s]<br>Downloading ncbitaxon.db.gz:  36%&#124;███▌      &#124; 813M/2.20G [00:21&lt;00:14, 103MB/s]<br>Downloading ncbitaxon.db.gz:  36%&#124;███▋      &#124; 823M/2.20G [00:21&lt;00:14, 102MB/s]<br>Downloading ncbitaxon.db.gz:  37%&#124;███▋      &#124; 830M/2.20G [00:21&lt;00:16, 93.0MB/s]<br>Downloading ncbitaxon.db.gz:  37%&#124;███▋      &#124; 841M/2.20G [00:21&lt;00:14, 99.7MB/s]<br>Downloading ncbitaxon.db.gz:  38%&#124;███▊      &#124; 849M/2.20G [00:22&lt;00:16, 90.4MB/s]<br>Downloading ncbitaxon.db.gz:  38%&#124;███▊      &#124; 861M/2.20G [00:22&lt;00:14, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▊      &#124; 871M/2.20G [00:22&lt;00:14, 103MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▉      &#124; 881M/2.20G [00:22&lt;00:14, 102MB/s]<br>Downloading ncbitaxon.db.gz:  39%&#124;███▉      &#124; 891M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  40%&#124;███▉      &#124; 901M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  40%&#124;████      &#124; 910M/2.20G [00:22&lt;00:14, 99.4MB/s]<br>Downloading ncbitaxon.db.gz:  41%&#124;████      &#124; 919M/2.20G [00:22&lt;00:14, 93.5MB/s]<br>Downloading ncbitaxon.db.gz:  41%&#124;████▏     &#124; 932M/2.20G [00:22&lt;00:13, 104MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 941M/2.20G [00:22&lt;00:13, 102MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 950M/2.20G [00:23&lt;00:13, 99.5MB/s]<br>Downloading ncbitaxon.db.gz:  42%&#124;████▏     &#124; 959M/2.20G [00:23&lt;00:14, 96.7MB/s]<br>Downloading ncbitaxon.db.gz:  43%&#124;████▎     &#124; 968M/2.20G [00:23&lt;00:13, 98.0MB/s]<br>Downloading ncbitaxon.db.gz:  43%&#124;████▎     &#124; 978M/2.20G [00:23&lt;00:13, 99.1MB/s]<br>Downloading ncbitaxon.db.gz:  44%&#124;████▍     &#124; 988M/2.20G [00:23&lt;00:13, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  44%&#124;████▍     &#124; 996M/2.20G [00:23&lt;00:14, 92.6MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▍     &#124; 0.98G/2.20G [00:23&lt;00:15, 85.3MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▍     &#124; 0.99G/2.20G [00:23&lt;00:15, 86.7MB/s]<br>Downloading ncbitaxon.db.gz:  45%&#124;████▌     &#124; 1.00G/2.20G [00:23&lt;00:14, 88.2MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▌     &#124; 1.01G/2.20G [00:24&lt;00:13, 93.7MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▌     &#124; 1.02G/2.20G [00:24&lt;00:14, 88.6MB/s]<br>Downloading ncbitaxon.db.gz:  46%&#124;████▋     &#124; 1.02G/2.20G [00:24&lt;00:15, 81.7MB/s]<br>Downloading ncbitaxon.db.gz:  47%&#124;████▋     &#124; 1.04G/2.20G [00:24&lt;00:13, 90.7MB/s]<br>Downloading ncbitaxon.db.gz:  47%&#124;████▋     &#124; 1.04G/2.20G [00:24&lt;00:14, 85.3MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.05G/2.20G [00:24&lt;00:13, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.06G/2.20G [00:24&lt;00:14, 85.4MB/s]<br>Downloading ncbitaxon.db.gz:  48%&#124;████▊     &#124; 1.07G/2.20G [00:24&lt;00:14, 86.0MB/s]<br>Downloading ncbitaxon.db.gz:  49%&#124;████▉     &#124; 1.08G/2.20G [00:24&lt;00:14, 84.2MB/s]<br>Downloading ncbitaxon.db.gz:  49%&#124;████▉     &#124; 1.09G/2.20G [00:24&lt;00:13, 92.2MB/s]<br>Downloading ncbitaxon.db.gz:  50%&#124;████▉     &#124; 1.10G/2.20G [00:25&lt;00:12, 97.1MB/s]<br>Downloading ncbitaxon.db.gz:  50%&#124;█████     &#124; 1.11G/2.20G [00:25&lt;00:12, 97.0MB/s]<br>Downloading ncbitaxon.db.gz:  51%&#124;█████     &#124; 1.12G/2.20G [00:25&lt;00:11, 100MB/s]<br>Downloading ncbitaxon.db.gz:  51%&#124;█████     &#124; 1.12G/2.20G [00:25&lt;00:12, 92.4MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.14G/2.20G [00:25&lt;00:11, 102MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.15G/2.20G [00:25&lt;00:11, 101MB/s]<br>Downloading ncbitaxon.db.gz:  52%&#124;█████▏    &#124; 1.15G/2.20G [00:25&lt;00:12, 91.1MB/s]<br>Downloading ncbitaxon.db.gz:  53%&#124;█████▎    &#124; 1.16G/2.20G [00:25&lt;00:11, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  53%&#124;█████▎    &#124; 1.17G/2.20G [00:25&lt;00:11, 101MB/s]<br>Downloading ncbitaxon.db.gz:  54%&#124;█████▎    &#124; 1.18G/2.20G [00:26&lt;00:11, 97.2MB/s]<br>Downloading ncbitaxon.db.gz:  54%&#124;█████▍    &#124; 1.19G/2.20G [00:26&lt;00:12, 89.6MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▍    &#124; 1.20G/2.20G [00:26&lt;00:10, 102MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▍    &#124; 1.21G/2.20G [00:26&lt;00:11, 96.9MB/s]<br>Downloading ncbitaxon.db.gz:  55%&#124;█████▌    &#124; 1.22G/2.20G [00:26&lt;00:12, 87.5MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▌    &#124; 1.23G/2.20G [00:26&lt;00:10, 95.6MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▌    &#124; 1.24G/2.20G [00:26&lt;00:11, 91.4MB/s]<br>Downloading ncbitaxon.db.gz:  56%&#124;█████▋    &#124; 1.24G/2.20G [00:26&lt;00:11, 90.5MB/s]<br>Downloading ncbitaxon.db.gz:  57%&#124;█████▋    &#124; 1.26G/2.20G [00:26&lt;00:10, 101MB/s]<br>Downloading ncbitaxon.db.gz:  57%&#124;█████▋    &#124; 1.26G/2.20G [00:26&lt;00:10, 95.7MB/s]<br>Downloading ncbitaxon.db.gz:  58%&#124;█████▊    &#124; 1.28G/2.20G [00:27&lt;00:09, 102MB/s]<br>Downloading ncbitaxon.db.gz:  58%&#124;█████▊    &#124; 1.29G/2.20G [00:27&lt;00:09, 104MB/s]<br>Downloading ncbitaxon.db.gz:  59%&#124;█████▉    &#124; 1.30G/2.20G [00:27&lt;00:09, 106MB/s]<br>Downloading ncbitaxon.db.gz:  59%&#124;█████▉    &#124; 1.31G/2.20G [00:27&lt;00:09, 105MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;█████▉    &#124; 1.31G/2.20G [00:27&lt;00:10, 92.7MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;██████    &#124; 1.32G/2.20G [00:27&lt;00:09, 95.9MB/s]<br>Downloading ncbitaxon.db.gz:  60%&#124;██████    &#124; 1.33G/2.20G [00:27&lt;00:09, 94.8MB/s]<br>Downloading ncbitaxon.db.gz:  61%&#124;██████    &#124; 1.34G/2.20G [00:27&lt;00:09, 97.7MB/s]<br>Downloading ncbitaxon.db.gz:  61%&#124;██████▏   &#124; 1.35G/2.20G [00:27&lt;00:09, 97.6MB/s]<br>Downloading ncbitaxon.db.gz:  62%&#124;██████▏   &#124; 1.36G/2.20G [00:27&lt;00:09, 99.2MB/s]<br>Downloading ncbitaxon.db.gz:  62%&#124;██████▏   &#124; 1.37G/2.20G [00:28&lt;00:08, 101MB/s]<br>Downloading ncbitaxon.db.gz:  63%&#124;██████▎   &#124; 1.38G/2.20G [00:28&lt;00:08, 106MB/s]<br>Downloading ncbitaxon.db.gz:  63%&#124;██████▎   &#124; 1.39G/2.20G [00:28&lt;00:08, 105MB/s]<br>Downloading ncbitaxon.db.gz:  64%&#124;██████▎   &#124; 1.40G/2.20G [00:28&lt;00:09, 95.9MB/s]<br>Downloading ncbitaxon.db.gz:  64%&#124;██████▍   &#124; 1.41G/2.20G [00:28&lt;00:07, 109MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▍   &#124; 1.42G/2.20G [00:28&lt;00:07, 108MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▍   &#124; 1.43G/2.20G [00:28&lt;00:07, 105MB/s]<br>Downloading ncbitaxon.db.gz:  65%&#124;██████▌   &#124; 1.44G/2.20G [00:28&lt;00:08, 102MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▌   &#124; 1.44G/2.20G [00:28&lt;00:10, 75.0MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▌   &#124; 1.46G/2.20G [00:29&lt;00:09, 86.5MB/s]<br>Downloading ncbitaxon.db.gz:  66%&#124;██████▋   &#124; 1.46G/2.20G [00:29&lt;00:09, 85.0MB/s]<br>Downloading ncbitaxon.db.gz:  67%&#124;██████▋   &#124; 1.47G/2.20G [00:29&lt;00:09, 82.2MB/s]<br>Downloading ncbitaxon.db.gz:  67%&#124;██████▋   &#124; 1.48G/2.20G [00:29&lt;00:08, 94.1MB/s]<br>Downloading ncbitaxon.db.gz:  68%&#124;██████▊   &#124; 1.49G/2.20G [00:29&lt;00:08, 95.2MB/s]<br>Downloading ncbitaxon.db.gz:  68%&#124;██████▊   &#124; 1.50G/2.20G [00:29&lt;00:08, 93.4MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▊   &#124; 1.51G/2.20G [00:29&lt;00:07, 96.2MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.52G/2.20G [00:29&lt;00:08, 88.3MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:29&lt;00:08, 90.6MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:29&lt;00:10, 69.0MB/s]<br>Downloading ncbitaxon.db.gz:  69%&#124;██████▉   &#124; 1.53G/2.20G [00:30&lt;00:14, 49.3MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.53G/2.20G [00:30&lt;00:14, 49.6MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.54G/2.20G [00:30&lt;00:15, 46.0MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;██████▉   &#124; 1.54G/2.20G [00:30&lt;00:15, 44.7MB/s]<br>Downloading ncbitaxon.db.gz:  70%&#124;███████   &#124; 1.55G/2.20G [00:30&lt;00:12, 57.0MB/s]<br>Downloading ncbitaxon.db.gz:  71%&#124;███████   &#124; 1.56G/2.20G [00:30&lt;00:09, 71.1MB/s]<br>Downloading ncbitaxon.db.gz:  71%&#124;███████   &#124; 1.57G/2.20G [00:30&lt;00:08, 80.4MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.58G/2.20G [00:30&lt;00:08, 78.6MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.59G/2.20G [00:30&lt;00:07, 86.2MB/s]<br>Downloading ncbitaxon.db.gz:  72%&#124;███████▏  &#124; 1.60G/2.20G [00:31&lt;00:06, 93.3MB/s]<br>Downloading ncbitaxon.db.gz:  73%&#124;███████▎  &#124; 1.60G/2.20G [00:31&lt;00:07, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  73%&#124;███████▎  &#124; 1.61G/2.20G [00:31&lt;00:06, 90.3MB/s]<br>Downloading ncbitaxon.db.gz:  74%&#124;███████▍  &#124; 1.63G/2.20G [00:31&lt;00:06, 94.0MB/s]<br>Downloading ncbitaxon.db.gz:  74%&#124;███████▍  &#124; 1.64G/2.20G [00:31&lt;00:06, 98.1MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▍  &#124; 1.64G/2.20G [00:31&lt;00:06, 88.9MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▌  &#124; 1.65G/2.20G [00:31&lt;00:06, 94.0MB/s]<br>Downloading ncbitaxon.db.gz:  75%&#124;███████▌  &#124; 1.66G/2.20G [00:31&lt;00:06, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  76%&#124;███████▌  &#124; 1.67G/2.20G [00:31&lt;00:05, 97.5MB/s]<br>Downloading ncbitaxon.db.gz:  76%&#124;███████▋  &#124; 1.68G/2.20G [00:31&lt;00:05, 96.2MB/s]<br>Downloading ncbitaxon.db.gz:  77%&#124;███████▋  &#124; 1.69G/2.20G [00:32&lt;00:06, 91.3MB/s]<br>Downloading ncbitaxon.db.gz:  77%&#124;███████▋  &#124; 1.70G/2.20G [00:32&lt;00:05, 94.5MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.71G/2.20G [00:32&lt;00:05, 97.5MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.72G/2.20G [00:32&lt;00:05, 97.8MB/s]<br>Downloading ncbitaxon.db.gz:  78%&#124;███████▊  &#124; 1.73G/2.20G [00:32&lt;00:05, 93.9MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.74G/2.20G [00:32&lt;00:05, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.74G/2.20G [00:32&lt;00:05, 87.4MB/s]<br>Downloading ncbitaxon.db.gz:  79%&#124;███████▉  &#124; 1.75G/2.20G [00:32&lt;00:05, 90.4MB/s]<br>Downloading ncbitaxon.db.gz:  80%&#124;███████▉  &#124; 1.76G/2.20G [00:32&lt;00:05, 94.2MB/s]<br>Downloading ncbitaxon.db.gz:  80%&#124;████████  &#124; 1.77G/2.20G [00:33&lt;00:04, 96.3MB/s]<br>Downloading ncbitaxon.db.gz:  81%&#124;████████  &#124; 1.78G/2.20G [00:33&lt;00:04, 95.6MB/s]<br>Downloading ncbitaxon.db.gz:  81%&#124;████████  &#124; 1.79G/2.20G [00:33&lt;00:04, 98.6MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.80G/2.20G [00:33&lt;00:04, 94.1MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.81G/2.20G [00:33&lt;00:04, 98.2MB/s]<br>Downloading ncbitaxon.db.gz:  82%&#124;████████▏ &#124; 1.82G/2.20G [00:33&lt;00:04, 94.7MB/s]<br>Downloading ncbitaxon.db.gz:  83%&#124;████████▎ &#124; 1.83G/2.20G [00:33&lt;00:04, 100MB/s]<br>Downloading ncbitaxon.db.gz:  83%&#124;████████▎ &#124; 1.84G/2.20G [00:33&lt;00:03, 98.9MB/s]<br>Downloading ncbitaxon.db.gz:  84%&#124;████████▎ &#124; 1.85G/2.20G [00:33&lt;00:03, 99.8MB/s]<br>Downloading ncbitaxon.db.gz:  84%&#124;████████▍ &#124; 1.85G/2.20G [00:33&lt;00:03, 100MB/s]<br>Downloading ncbitaxon.db.gz:  85%&#124;████████▍ &#124; 1.86G/2.20G [00:34&lt;00:03, 102MB/s]<br>Downloading ncbitaxon.db.gz:  85%&#124;████████▌ &#124; 1.87G/2.20G [00:34&lt;00:03, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▌ &#124; 1.88G/2.20G [00:34&lt;00:03, 102MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▌ &#124; 1.89G/2.20G [00:34&lt;00:03, 99.6MB/s]<br>Downloading ncbitaxon.db.gz:  86%&#124;████████▋ &#124; 1.90G/2.20G [00:34&lt;00:03, 93.5MB/s]<br>Downloading ncbitaxon.db.gz:  87%&#124;████████▋ &#124; 1.91G/2.20G [00:34&lt;00:03, 91.4MB/s]<br>Downloading ncbitaxon.db.gz:  87%&#124;████████▋ &#124; 1.92G/2.20G [00:34&lt;00:02, 102MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.93G/2.20G [00:34&lt;00:03, 92.0MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.94G/2.20G [00:34&lt;00:02, 99.2MB/s]<br>Downloading ncbitaxon.db.gz:  88%&#124;████████▊ &#124; 1.95G/2.20G [00:34&lt;00:02, 92.9MB/s]<br>Downloading ncbitaxon.db.gz:  89%&#124;████████▉ &#124; 1.96G/2.20G [00:35&lt;00:02, 97.0MB/s]<br>Downloading ncbitaxon.db.gz:  89%&#124;████████▉ &#124; 1.97G/2.20G [00:35&lt;00:02, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  90%&#124;████████▉ &#124; 1.98G/2.20G [00:35&lt;00:02, 96.5MB/s]<br>Downloading ncbitaxon.db.gz:  90%&#124;█████████ &#124; 1.98G/2.20G [00:35&lt;00:02, 90.1MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████ &#124; 1.99G/2.20G [00:35&lt;00:02, 95.0MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████ &#124; 2.00G/2.20G [00:35&lt;00:02, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  91%&#124;█████████▏&#124; 2.01G/2.20G [00:35&lt;00:02, 93.6MB/s]<br>Downloading ncbitaxon.db.gz:  92%&#124;█████████▏&#124; 2.02G/2.20G [00:35&lt;00:02, 91.0MB/s]<br>Downloading ncbitaxon.db.gz:  92%&#124;█████████▏&#124; 2.03G/2.20G [00:35&lt;00:01, 93.2MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.04G/2.20G [00:36&lt;00:01, 94.5MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.05G/2.20G [00:36&lt;00:01, 95.2MB/s]<br>Downloading ncbitaxon.db.gz:  93%&#124;█████████▎&#124; 2.06G/2.20G [00:36&lt;00:01, 97.9MB/s]<br>Downloading ncbitaxon.db.gz:  94%&#124;█████████▍&#124; 2.07G/2.20G [00:36&lt;00:01, 94.2MB/s]<br>Downloading ncbitaxon.db.gz:  94%&#124;█████████▍&#124; 2.07G/2.20G [00:36&lt;00:01, 87.4MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▍&#124; 2.08G/2.20G [00:36&lt;00:01, 96.6MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▍&#124; 2.09G/2.20G [00:36&lt;00:01, 97.9MB/s]<br>Downloading ncbitaxon.db.gz:  95%&#124;█████████▌&#124; 2.10G/2.20G [00:36&lt;00:01, 94.4MB/s]<br>Downloading ncbitaxon.db.gz:  96%&#124;█████████▌&#124; 2.11G/2.20G [00:36&lt;00:01, 91.7MB/s]<br>Downloading ncbitaxon.db.gz:  96%&#124;█████████▌&#124; 2.12G/2.20G [00:36&lt;00:00, 94.9MB/s]<br>Downloading ncbitaxon.db.gz:  97%&#124;█████████▋&#124; 2.13G/2.20G [00:37&lt;00:00, 96.0MB/s]<br>Downloading ncbitaxon.db.gz:  97%&#124;█████████▋&#124; 2.14G/2.20G [00:37&lt;00:00, 97.3MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.15G/2.20G [00:37&lt;00:00, 100MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.16G/2.20G [00:37&lt;00:00, 94.3MB/s]<br>Downloading ncbitaxon.db.gz:  98%&#124;█████████▊&#124; 2.17G/2.20G [00:37&lt;00:00, 102MB/s]<br>Downloading ncbitaxon.db.gz:  99%&#124;█████████▉&#124; 2.18G/2.20G [00:37&lt;00:00, 91.8MB/s]<br>Downloading ncbitaxon.db.gz:  99%&#124;█████████▉&#124; 2.19G/2.20G [00:37&lt;00:00, 99.7MB/s]<br>Downloading ncbitaxon.db.gz: 100%&#124;█████████▉&#124; 2.20G/2.20G [00:37&lt;00:00, 98.0MB/s] |
| validate-references | just validate-references data/merge_yaml/merged/2ASW.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 3; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/algae/2asw.yaml:1:id: CultureMech:000038<br>./data/merge_yaml/merged/2ASW.yaml:1:id: CultureMech:000038<br> |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17268 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17268 resolves to myo-inositol and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17439 resolves to cyanocob(III)alamin and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17821 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17821; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17821 resolves to thymine and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:27470 resolves to folic acid and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:34683 resolves to disodium hydrogenphosphate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi46760 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46760; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:46760 resolves to tricine and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:63005 resolves to sodium nitrate and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {} |
| ccap2asw | https://www.ccap.ac.uk/wp-content/uploads/MR_2ASW.pdf; Page1: Stocks per litre; Medium per litre; preparation; footnote | supports | Current revision002, approved/reviewed29May2026, read in full. Extra salts and vitamins are stocks per litre; tricine0.50g and NaCl35g are medium additions per final litre. Stock doses are7.50,2.50 and25.00mL for salts, vitamins and SE1 respectively. The source specifies water-base alternatives, pH adjustment and autoclaving. Current PDF hash matches the October identity-correction event; equivalence to the earlier import is not asserted. |
| ccapSE1Marine | https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf; Page1: Preparing the soil; Medium | supports | Full marine SE1 recipe read. Dried prepared soil with twice its volume of deionised water is autoclaved twice, cooled and settled2–3weeks; supernatant is decanted and sterilized again. The source states15psi/126C/20min for each of the first two cycles and15psi/121C/15min for the last; retain these literal conditions for curator verification without silently reconciling pressure/temperature. No elemental composition can be inferred. |
| ccap1918 | https://www.ccap.ac.uk/catalogue/strain-19-18; Culture media, purity and growth conditions; strain identity | supports | CCAP19/18 is Dunaliella salina; current page links2ASW, axenic serial subculture and20–35C maintenance. This supports a named collection strain, not a universal temperature or growth rate. |
| matsui2018cdn | https://oup.silverchair-cdn.com/article-minimal/6116611; Materials and Methods: Cells and Culture Conditions; RT-qPCR; transformation and screening | supports | Full public publisher text inspected. Cells and Culture Conditions names UTEX642 and CCMP1335 in artificial seawater plus half-strength Guillard f solution,20C, continuous30–75 micromol photons m-2 s-1,1%CO2 or ambient0.04%CO2. RT-qPCR gives midlog harvest OD730 ranges0.2–0.3 and0.1–0.15 respectively. Plate transformation/selection has protocol-specific additions; the paper does not establish the CCAP2ASW base formula. |
| tsuji2021publisher | https://link.springer.com/article/10.1007/s10126-021-10037-4; Abstract; access restriction | context_only | Accessible publisher abstract supports Chaetoceros gracilis sodium/CO2 experiments and growth at0.23mM Na+ under5%CO2 but not0.04%CO2. The page is a subscription preview; exact strain attribution and preacclimation procedure in the main methods could not be reverified. |
| tsuji2021supplement | https://media.springernature.com/original/springer-static/esm/art:10.1007%2Fs10126-021-10037-4/MediaObjects/10126_2021_10037_MOESM1_ESM.pdf; Page1 TableS1: Trace elements (micromolar), basal components (mM), footnotes a/b | supports | Complete public TableS1 inspected, including headers and footnotes. Na2SeO3 is0.001micromolar; Na2SiO3·9H2O is0.1mM. NaCl treatments are0,10,20,50,200,423mM with0.23mM residual basal sodium. The defined basal/trace/vitamin formulation does not establish ancestry from the CCAP soil-extract recipe. |
| spectrum2023xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10269666/fullTextXML; Materials and Methods: Algal strains and cultivation conditions | supports | Full JATS source inspected. Methods identify D.salina CCAP19/18 cultivated in study2ASW containing1.5M NaCl,26C,8000lx and16/8 light/dark. FACHB-847 uses a separately cited Dunaliella medium. The owner correctly limits its variant to the explicit concentration and culture context; external TableS2 was unavailable. |
| frontiers2015 | https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2015.00020/full; Strains and media; Table1; Preliminary centrate screening; Gomord bibliography entry | supports | Publisher methods/Table1 and relevant results inspected. Eighteen Dunaliella strains are maintained on modified2ASW with33.6g/L sea salts replacing NaCl; maintenance is room temperature with18/6 light/dark. Centrate screening is a separate treatment. UTEX LB200 identification is disputed in results. Other genera use other media. The Gomord bibliography entry is a plant-glycosylation review; its missing recipe details are not inherited. |
| genome2017xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5658486/fullTextXML; Article title; Accession number(s) | supports | Full genome article supports CCAP19/18 identity, PRJNA32771, SAMN02746051, NSFN00000000 and first version NSFN01000000. It is identity evidence, not a2ASW formula or growth demonstration. |
| matsui2018metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1104%2Fpp.18.00453&amp;format=json&amp;resultType=core; DOI query: resultList.result; title/authors/year/PMID | supports | [{"doi": "10.1104/pp.18.00453", "id": "30076224", "pmcid": null, "title": "Plasma Membrane-Type Aquaporins from Marine Diatoms Function as CO&lt;sub&gt;2&lt;/sub&gt;/NH&lt;sub&gt;3&lt;/sub&gt; Channels and Provide Photoprotection.", "authorString": "Matsui H, Hopkinson BM, Nakajima K, Matsuda Y.", "pubYear": "2018"}] |
| tsuji2021metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2Fs10126-021-10037-4&amp;format=json&amp;resultType=core; DOI query: resultList.result; title/authors/year/PMID | supports | [{"doi": "10.1007/s10126-021-10037-4", "id": "34109463", "pmcid": null, "title": "Characterization of a CO&amp;lt;sub&amp;gt;2&amp;lt;/sub&amp;gt;-Concentrating Mechanism with Low Sodium Dependency in the Centric Diatom Chaetoceros gracilis.", "authorString": "Tsuji Y, Kusi-Appiah G, Kozai N, Fukuda Y, Yamano T, Fukuzawa H.", "pubYear": "2021"}] |
| spectrum2023metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fspectrum.00069-23&amp;format=json&amp;resultType=core; DOI query: resultList.result; title/authors/year/PMID | supports | [{"doi": "10.1128/spectrum.00069-23", "id": "37022233", "pmcid": "PMC10269666", "title": "Roles of Two Phytoene Synthases and Orange Protein in Carotenoid Metabolism of the \u03b2-Carotene-Accumulating &lt;i&gt;Dunaliella salina&lt;/i&gt;.", "authorString": "Liang MH, Xie SR, Dai JL, Chen HH, Jiang JG.", "pubYear": "2023"}] |
| genome2017metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FgenomeA.01105-17&amp;format=json&amp;resultType=core; DOI query: resultList.result; title/authors/year/PMID | supports | [{"doi": "10.1128/genomea.01105-17", "id": "29074648", "pmcid": "PMC5658486", "title": "Draft Nuclear Genome Sequence of the Halophilic and Beta-Carotene-Accumulating Green Alga &lt;i&gt;Dunaliella salina&lt;/i&gt; Strain CCAP19/18.", "authorString": "Polle JEW, Barry K, Cushman J, Schmutz J, Tran D, Hathwaik LT, Yim WC, Jenkins J, McKie-Krisberg Z, Prochnik S, Lindquist E, Dockter RB, Adam C, Molina H, Bunkenborg J, Jin E, Buchheim M, Magnuson J.", "pubYear": "2017"}] |
| frontiers2015metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffenrg.2015.00020&amp;format=json&amp;resultType=core; DOI query hitCount | context_only | The bounded DOI query returned no EuropePMC hit. Publisher identity was verified directly; no PMID is invented and no global absence is claimed. |
| taxonomyRetry | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3046,556484,296543,3044,3047,13790,257627,147822,289300,3026963,3026961,5748,3098&amp;retmode=xml; Direct Taxon elements: identifiers, canonical names, ranks and synonyms | supports | [{"tax_id": "3046", "scientific_name": "Dunaliella salina", "rank": "species", "synonyms": ["Dunaliella bardawil"]}, {"tax_id": "556484", "scientific_name": "Phaeodactylum tricornutum CCAP 1055/1", "rank": "strain", "synonyms": []}, {"tax_id": "296543", "scientific_name": "Thalassiosira pseudonana CCMP1335", "rank": "strain", "synonyms": ["Thalassiosira pseudonana strain CCMP1335"]}, {"tax_id": "3044", "scientific_name": "Dunaliella", "rank": "genus", "synonyms": []}, {"tax_id": "3047", "scientific_name": "Dunaliella tertiolecta", "rank": "species", "synonyms": []}, {"tax_id": "13790", "scientific_name": "Dunaliella bioculata", "rank": "species", "synonyms": []}, {"tax_id": "257627", "scientific_name": "Dunaliella primolecta", "rank": "species", "synonyms": []}, {"tax_id": "147822", "scientific_name": "Dunaliella peircei", "rank": "species", "synonyms": []}, {"tax_id": "289300", "scientific_name": "Dunaliella maritima", "rank": "species", "synonyms": []}, {"tax_id": "3026963", "scientific_name": "Dunaliella terricola", "rank": "species", "synonyms": []}, {"tax_id": "3026961", "scientific_name": "Dunaliella granulata", "rank": "species", "synonyms": []}, {"tax_id": "5748", "scientific_name": "Nannochloropsis", "rank": "genus", "synonyms": []}, {"tax_id": "3098", "scientific_name": "Neochloris", "rank": "genus", "synonyms": []}] |
| bioproject32771 | https://www.ncbi.nlm.nih.gov/bioproject/32771; Project title; organism and links | supports | Project identity agrees with Dunaliella salina CCAP19/18. It supplies sequencing provenance, not source recipe or cultivation evidence. |
| genomeDsalina | https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_002284615.2/dataset_report; reports[0].organism; assembly_info; wgs_info | supports | GCA_002284615.2 is current and identifies D.salina CCAP19/18, taxid3046, PRJNA32771, SAMN02746051 and WGS NSFN00000000.2. The record base WGS accession is valid. |
| genomeTpseudonana | https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000149405.2/dataset_report; reports[0].organism; assembly_info; wgs_info | supports | GCF_000149405.2 is current, paired with GCA_000149405.2, and identifies CCMP1335/taxid296543, SAMN02744045 and WGS AAFD00000000.2. These claims require NCBI identity evidence rather than only a growth-paper citation. |
| ccap-1052-1a | https://www.ccap.ac.uk/catalogue/strain-1052-1a; Equivalent Strains; Notes; Original Designation | supports | Explicit equivalent-strain field lists UTEX642; notes identify Pt2. |
| ccap-1055-1 | https://www.ccap.ac.uk/catalogue/strain-1055-1; Equivalent Strains; Notes; Original Designation | supports | This strain is Pt1 clone8.6/PtGen from CCMP632, distinct from the UTEX642 equivalence on CCAP1052/1A. |
| utex-0642 | https://utex.org/products/utex-lb-0642; UTEX Number; Origin; Relatives | supports | UTEX confirms accession642 and its relation to CCAP1052/1A. Relatives is not treated as an exact equivalence for every entry. |
| ncbi-taxonomy-556484 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=556484; TaxId; ScientificName; Rank; ParentTaxId | supports | NCBI556484 names Phaeodactylum tricornutum CCAP1055/1 at strain rank, parent2850. It does not identify UTEX642. |
| chaetoceros-utex-lb-2658 | https://utex.org/products/utex-lb-2658; UTEX Number; Strain; Also Known As; Description of Location | supports | UTEX names LB2658 as Chaetoceros gracilis Schütt and also lists C.gracile/C.muelleri; this verifies collection naming only, not the strain used in an inaccessible paper methods section. |
| chaetoceros-ncbi-taxonomy-240364-265525 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=240364,265525; Direct taxa; scientific names; synonyms; authority names | supports | NCBI bare-name C.gracilis corresponds to C.neogracilis240364 with Pantocsek authority; C.muelleri is separate species265525. The authority/alias differences do not justify assigning either to UTEX2658 without additional evidence. |
| chebi24848 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24848; Exact OLS term or direct parent/child response | supports | Generic inositol is a cyclohexanehexol class; CCAP does not state a stereoisomer. |
| chebi39063 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39063; Exact OLS term or direct parent/child response | supports | The pinned Tricine row resolves to N-tris(hydroxymethyl)methylglycine. |
| chebi46760children | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_46760/children; Exact OLS term or direct parent/child response | supports | Tricine CHEBI46760 has CHEBI39063 and its zwitterion as children; this is a granularity distinction. |
| chebi39063parents | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_39063/parents; Exact OLS term or direct parent/child response | supports | CHEBI39063 has the broader tricine CHEBI46760 parent. |
| arithmetic | Complete target, owner and current CCAP source tables; All13 amounts; stock-dose arithmetic; pinned mapping rows; every history timestamp | supports | {"quantity_trace": [{"field": "ingredients[0].concentration", "material": "NaNO3", "record_value_g_l": "15.00", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.112500", "calculation": "15.00 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[1].concentration", "material": "Na2HPO4", "record_value_g_l": "0.60", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.004500", "calculation": "0.60 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[2].concentration", "material": "K2HPO4", "record_value_g_l": "0.50", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre": "0.003750", "calculation": "0.50 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[3].concentration", "material": "Biotin", "record_value_g_l": "0.0002", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "5.0E-7", "calculation": "0.0002 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[4].concentration", "material": "Calcium pantothenate", "record_value_g_l": "0.02", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[5].concentration", "material": "Cyanocobalamin", "record_value_g_l": "0.004", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.0000100", "calculation": "0.004 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[6].concentration", "material": "Folic acid", "record_value_g_l": "0.0004", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00000100", "calculation": "0.0004 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[7].concentration", "material": "Inositol", "record_value_g_l": "1.0", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00250", "calculation": "1.0 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[8].concentration", "material": "Nicotinic acid", "record_value_g_l": "0.02", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[9].concentration", "material": "Thiamine HCl", "record_value_g_l": "0.1", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00025", "calculation": "0.1 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[10].concentration", "material": "Thymine", "record_value_g_l": "0.6", "actual_source_basis": "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre": "0.00150", "calculation": "0.6 g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation: stock composition"}, {"field": "ingredients[11].concentration", "material": "Tricine", "record_value_g_l": "0.50", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre": "0.50", "calculation": "No stock dilution: source directly states medium addition per litre.", "decision": "verified direct addition; not total seawater content"}, {"field": "ingredients[12].concentration", "material": "NaCl", "record_value_g_l": "35.00", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre": "35.00", "calculation": "No stock dilution: source directly states medium addition per litre.", "decision": "verified direct addition; not total seawater content"}], "mim_comparison": [{"field": "ingredients[0].term", "record_id": "CHEBI:63005", "pinned_preferred_row": {"label": "NaNO3", "match_type": "preferred_term", "identifier": "CHEBI:63005", "preferred_term": "NaNO3", "ontology_id": "CHEBI:63005", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[1].term", "record_id": "CHEBI:34683", "pinned_preferred_row": {"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[2].term", "record_id": "CHEBI:131527", "pinned_preferred_row": {"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[3].term", "record_id": "CHEBI:15956", "pinned_preferred_row": {"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[4].term", "record_id": "CHEBI:31345", "pinned_preferred_row": {"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[5].term", "record_id": "CHEBI:17439", "pinned_preferred_row": {"label": "Cyanocobalamin", "match_type": "preferred_term", "identifier": "CHEBI:17439", "preferred_term": "Cyanocobalamin", "ontology_id": "CHEBI:17439", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[6].term", "record_id": "CHEBI:27470", "pinned_preferred_row": {"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[7].term", "record_id": "CHEBI:17268", "pinned_preferred_row": {"label": "Inositol", "match_type": "preferred_term", "identifier": "CHEBI:24848", "preferred_term": "Inositol", "ontology_id": "CHEBI:24848", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": false}, {"field": "ingredients[8].term", "record_id": "CHEBI:15940", "pinned_preferred_row": {"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[9].term", "record_id": "CHEBI:49105", "pinned_preferred_row": {"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[10].term", "record_id": "CHEBI:17821", "pinned_preferred_row": {"label": "Thymine", "match_type": "preferred_term", "identifier": "CHEBI:17821", "preferred_term": "Thymine", "ontology_id": "CHEBI:17821", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[11].term", "record_id": "CHEBI:46760", "pinned_preferred_row": {"label": "Tricine", "match_type": "preferred_term", "identifier": "CHEBI:39063", "preferred_term": "Tricine", "ontology_id": "CHEBI:39063", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": false}, {"field": "ingredients[12].term", "record_id": "CHEBI:26710", "pinned_preferred_row": {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}], "history": [{"layer": "target", "index": 0, "timestamp": "2026-01-28", "timezone_present": false}, {"layer": "target", "index": 1, "timestamp": "2026-02-03T11:23:39.554565", "timezone_present": false}, {"layer": "target", "index": 2, "timestamp": "2026-02-03T11:26:43.440568", "timezone_present": false}, {"layer": "target", "index": 3, "timestamp": "2026-03-13T06:18:52.992431Z", "timezone_present": true}, {"layer": "target", "index": 4, "timestamp": "2026-03-17T19:45:03.950098+00:00", "timezone_present": true}, {"layer": "target", "index": 5, "timestamp": "2026-04-04T12:54:55.050840", "timezone_present": false}, {"layer": "target", "index": 6, "timestamp": "2026-05-09T13:35:00-07:00", "timezone_present": true}, {"layer": "target", "index": 7, "timestamp": "2026-06-10T07:37:33.980020+00:00", "timezone_present": true}, {"layer": "target", "index": 8, "timestamp": "2026-08-06T00:58:02.481264+00:00", "timezone_present": true}, {"layer": "target", "index": 9, "timestamp": "2026-09-13T00:00:00-07:00", "timezone_present": true}, {"layer": "target", "index": 10, "timestamp": "2026-10-05T19:29:05+00:00", "timezone_present": true}, {"layer": "target", "index": 11, "timestamp": "2026-10-05T19:43:18.434134+00:00", "timezone_present": true}, {"layer": "owner", "index": 0, "timestamp": "2026-01-28", "timezone_present": false}, {"layer": "owner", "index": 1, "timestamp": "2026-02-03T11:23:39.554565", "timezone_present": false}, {"layer": "owner", "index": 2, "timestamp": "2026-02-03T11:26:43.440568", "timezone_present": false}, {"layer": "owner", "index": 3, "timestamp": "2026-03-13T06:18:52.992431Z", "timezone_present": true}, {"layer": "owner", "index": 4, "timestamp": "2026-03-17T19:45:03.950098+00:00", "timezone_present": true}, {"layer": "owner", "index": 5, "timestamp": "2026-04-04T12:54:55.050840", "timezone_present": false}, {"layer": "owner", "index": 6, "timestamp": "2026-05-09T13:35:00-07:00", "timezone_present": true}, {"layer": "owner", "index": 7, "timestamp": "2026-06-10T07:37:33.980020+00:00", "timezone_present": true}, {"layer": "owner", "index": 8, "timestamp": "2026-08-06T00:58:02.481264+00:00", "timezone_present": true}, {"layer": "owner", "index": 9, "timestamp": "2026-09-13T00:00:00-07:00", "timezone_present": true}, {"layer": "owner", "index": 10, "timestamp": "2026-10-05T19:29:05+00:00", "timezone_present": true}, {"layer": "owner", "index": 11, "timestamp": "2026-10-14T02:43:29.178060+00:00", "timezone_present": true}]} |
| importer | src/culturemech/import/ccap_importer.py; Unconditional light/temperature assignments around lines179–184 | supports | Exact current light intensity, light cycle and temperature strings are unconditional importer defaults, not source-scoped cultivation observations. |
| exporter | src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge; transform | supports | Current code omits truthy scoped_to_variant descriptors and otherwise emits a parent growth edge when a taxon is present. The two grounded diatom descriptors lack scope; the ungrounded Chaetoceros descriptor emits no taxon edge. Code was inspected, not exported. Existing tests/test_kgx_variant_growth_scope.py was read and not executed. |
| prior-report | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/2asw.md; Entire historical report | context_only | The prior report explicitly source-checked0/15 claims and is not current scientific validation; current source comparisons are independent. |
| validate-terms-initial-network-attempt | just validate-terms data/merge_yaml/merged/2ASW.yaml; Original attempt; later successful retry retained separately | context_only | Validating ontology terms (MediaRecipe)...<br><br>Traceback (most recent call last):<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py", line 204, in _new_conn<br>    sock = connection.create_connection(<br>        (self._dns_host, self.port),<br>    ...&lt;2 lines&gt;...<br>        socket_options=self.socket_options,<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/util/connection.py", line 60, in create_connection<br>    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):<br>               ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>  File "/Users/marcin/.local/share/uv/python/cpython-3.13.2-macos-aarch64-none/lib/python3.13/socket.py", line 977, in getaddrinfo<br>    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):<br>               ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>socket.gaierror: [Errno 8] nodename nor servname provided, or not known<br><br>The above exception was the direct cause of the following exception:<br><br>Traceback (most recent call last):<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py", line 787, in urlopen<br>    response = self._make_request(<br>        conn,<br>    ...&lt;10 lines&gt;...<br>        **response_kw,<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py", line 488, in _make_request<br>    raise new_e<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py", line 464, in _make_request<br>    self._validate_conn(conn)<br>    ~~~~~~~~~~~~~~~~~~~^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn<br>    conn.connect()<br>    ~~~~~~~~~~~~^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py", line 759, in connect<br>    self.sock = sock = self._new_conn()<br>                       ~~~~~~~~~~~~~~^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py", line 211, in _new_conn<br>    raise NameResolutionError(self.host, self, e) from e<br>urllib3.exceptions.NameResolutionError: HTTPSConnection(host='semanticsql.berkeleybop.io', port=443): Failed to resolve 'semanticsql.berkeleybop.io' ([Errno 8] nodename nor servname provided, or not known)<br><br>The above exception was the direct cause of the following exception:<br><br>Traceback (most recent call last):<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/adapters.py", line 644, in send<br>    resp = conn.urlopen(<br>        method=request.method,<br>    ...&lt;9 lines&gt;...<br>        chunked=chunked,<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py", line 841, in urlopen<br>    retries = retries.increment(<br>        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/util/retry.py", line 535, in increment<br>    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]<br>    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='semanticsql.berkeleybop.io', port=443): Max retries exceeded with url: /ncbitaxon.db.gz (Caused by NameResolutionError("HTTPSConnection(host='semanticsql.berkeleybop.io', port=443): Failed to resolve 'semanticsql.berkeleybop.io' ([Errno 8] nodename nor servname provided, or not known)"))<br><br>During handling of the above exception, another exception occurred:<br><br>Traceback (most recent call last):<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/utils/download.py", line 202, in download<br>    with requests.get(url, **kwargs) as response, path.open("wb") as file:  # noqa:S113<br>         ~~~~~~~~~~~~^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/api.py", line 73, in get<br>    return request("get", url, params=params, **kwargs)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/api.py", line 59, in request<br>    return session.request(method=method, url=url, **kwargs)<br>           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/sessions.py", line 589, in request<br>    resp = self.send(prep, **send_kwargs)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/sessions.py", line 703, in send<br>    r = adapter.send(request, **kwargs)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/adapters.py", line 677, in send<br>    raise ConnectionError(e, request=request)<br>requests.exceptions.ConnectionError: HTTPSConnectionPool(host='semanticsql.berkeleybop.io', port=443): Max retries exceeded with url: /ncbitaxon.db.gz (Caused by NameResolutionError("HTTPSConnection(host='semanticsql.berkeleybop.io', port=443): Failed to resolve 'semanticsql.berkeleybop.io' ([Errno 8] nodename nor servname provided, or not known)"))<br><br>The above exception was the direct cause of the following exception:<br><br>Traceback (most recent call last):<br>  File "/private/tmp/culturemech-review-env/bin/linkml-term-validator", line 10, in &lt;module&gt;<br>    sys.exit(main())<br>             ~~~~^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/cli.py", line 431, in main<br>    app()<br>    ~~~^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py", line 336, in __call__<br>    raise e<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py", line 319, in __call__<br>    return get_command(self)(*args, **kwargs)<br>           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py", line 1631, in __call__<br>    return self.main(*args, **kwargs)<br>           ~~~~~~~~~^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/core.py", line 814, in main<br>    return _main(<br>        self,<br>    ...&lt;6 lines&gt;...<br>        **extra,<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/core.py", line 190, in _main<br>    rv = self.invoke(ctx)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py", line 2032, in invoke<br>    return _process_result(sub_ctx.command.invoke(sub_ctx))<br>                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py", line 1415, in invoke<br>    return ctx.invoke(self.callback, **ctx.params)<br>           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py", line 910, in invoke<br>    return callback(*args, **kwargs)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py", line 706, in wrapper<br>    return callback(**use_params)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/cli.py", line 278, in validate_data<br>    report = validator.validate_source(loader, target_class=target_class)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml/validator/validator.py", line 68, in validate_source<br>    return ValidationReport(results=list(self.iter_results_from_source(loader, target_class)))<br>                                    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml/validator/validator.py", line 105, in iter_results_from_source<br>    for result in plugin.process(instance, context):<br>                  ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py", line 192, in process<br>    yield from self._process_recursive(<br>    ...&lt;4 lines&gt;...<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py", line 257, in _process_recursive<br>    yield from self._process_recursive(<br>    ...&lt;4 lines&gt;...<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py", line 238, in _process_recursive<br>    yield from self._validate_binding(<br>    ...&lt;6 lines&gt;...<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py", line 335, in _validate_binding<br>    yield from self._validate_term_exists(<br>    ...&lt;6 lines&gt;...<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py", line 565, in _validate_term_exists<br>    ontology_label = self.get_ontology_label(field_value)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/base.py", line 251, in get_ontology_label<br>    adapter = self._get_adapter(prefix)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/base.py", line 219, in _get_adapter<br>    adapter = get_adapter(adapter_string)<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/selector.py", line 155, in get_adapter<br>    return res.implementation_class(res, **kwargs)<br>           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^<br>  File "&lt;string&gt;", line 27, in __init__<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/implementations/sqldb/sql_implementation.py", line 350, in __post_init__<br>    db_path = FILE_CACHE.ensure_gunzip(<br>        url=url, autoclean=False, download_kwargs=SEMSQL_SQLITE_DOWNLOAD_KWARGS<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/utilities/caching.py", line 277, in ensure_gunzip<br>    self._module.ensure_gunzip(<br>    ~~~~~~~~~~~~~~~~~~~~~~~~~~^<br>        url=url,<br>        ^^^^^^^^<br>    ...&lt;3 lines&gt;...<br>        download_kwargs=download_kwargs,<br>        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>    )<br>    ^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/impl.py", line 455, in ensure_gunzip<br>    path = self.ensure(<br>        *subkeys,<br>    ...&lt;3 lines&gt;...<br>        download_kwargs=download_kwargs,<br>    )<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/impl.py", line 284, in ensure<br>    utils.download(<br>    ~~~~~~~~~~~~~~^<br>        url=url,<br>        ^^^^^^^^<br>    ...&lt;3 lines&gt;...<br>        **(download_kwargs or {}),<br>        ^^^^^^^^^^^^^^^^^^^^^^^^^^<br>    )<br>    ^<br>  File "/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/utils/download.py", line 220, in download<br>    raise DownloadError(backend, url, path, e) from e<br>pystow.utils.download.DownloadError: Failed with requests to download https://semanticsql.berkeleybop.io/ncbitaxon.db.gz to /private/tmp/culturemech-review-pystow/oaklib/ncbitaxon.db.gz<br>error: recipe &#96;validate-terms&#96; failed with exit code 1 |
| validate-references-initial-network-attempt | just validate-references data/merge_yaml/merged/2ASW.yaml; Original attempt; later successful retry retained separately | context_only | Validating evidence references (MediaRecipe)...<br><br>[ERROR] reference_validation: HTTPSConnectionPool(host='www.ccap.ac.uk', port=443): Max retries exceeded with url: /catalogue/strain-19-18 (Caused by NameResolutionError("HTTPSConnection(host='www.ccap.ac.uk', port=443): Failed to resolve 'www.ccap.ac.uk' ([Errno 8] nodename nor servname provided, or not known)"))<br>error: recipe &#96;validate-references&#96; failed with exit code 2 |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Full Tsuji main methods and external Liang TableS2 were inaccessible. The exact paper strain/preacclimation and full Liang formulation remain unverified; no paid access or contact was attempted.
- Current CCAP PDF is the inspected revision; historical import-version identity was not reconstructed. No stock composition is inferred for soil extract or seawater, and no total NaCl or elemental salinity conversion is asserted.
- Exact UTEX642 taxon and UTEX2658 taxonomic assignment remain unresolved. Existing species/genus mappings do not independently verify physical strain identity. No growth/export or corpus regeneration was run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073836Z-culturemech-000038-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2asw (CultureMech:000038)'
started_at: '2026-10-21T07:20:53Z'
finished_at: '2026-10-21T07:38:36Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: CCAP 2ASW is identifiable, but eleven stock concentrations are flattened
  into direct medium ingredients and the stock doses, soil extract and preparation
  are omitted. UTEX642 is assigned a different strain taxon, legacy diatom media lack
  verified parent-formulation identity and structured growth scope, and the sodium-response
  variant conflicts with its supplement. Later bounded owner citations are sound within
  their stated limits but absent from the generated target. Full Tsuji methods and
  Liang TableS2 remain unavailable.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/2ASW.yaml
    sha256: dfc2dfbb23fd114d1660f5040284e9f235d087abdc26a229ef3ec00e863dded8
    role: target
  - path: data/normalized_yaml/algae/2asw.yaml
    sha256: 0ba654a5395797550d80a1b3f3e48930862a2188d4568d58c6cda673c47f1ee7
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/2asw.md
    sha256: 42fbf4a6e62a5dbeb8a6df3ff07300f8202644bf055dbec54d55ac6db3a7a8e3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/ccap_raw_yaml.py
    sha256: f2c119c4f67bd245c9fbd2b7480c1c6454a64b79922599cb583203628f476a8c
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/ccap_fetcher.py
    sha256: 09e297722639216f5211096bcac559fae674a03a46e0d324f8360996836368e8
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
  - path: tests/test_kgx_variant_growth_scope.py
    sha256: b38521f30c683539dbfe880a747ad73e12ce1c20a60132dc8409f1e7573e196f
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 78; batch 008 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seven task batches contain
    70 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 72 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000038
targets:
- target_id: CultureMech:000038
  path: data/merge_yaml/merged/2ASW.yaml
  label: 2asw
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2ASW.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/078/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/078/strict.tsv"
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed



    Downloading ncbitaxon.db.gz:   0%|          | 0.00/2.20G [00:00<?, ?B/s]

    Downloading ncbitaxon.db.gz:   0%|          | 1.12M/2.20G [00:00<03:29, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 2.19M/2.20G [00:00<03:32, 11.1MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 4.44M/2.20G [00:00<02:22, 16.5MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 5.50M/2.20G [00:00<02:43, 14.4MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 6.50M/2.20G [00:00<03:03, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 7.88M/2.20G [00:00<02:56, 13.4MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 9.00M/2.20G [00:00<03:06, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 10.0M/2.20G [00:00<03:19, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   1%|          | 14.1M/2.20G [00:00<01:50, 21.4MB/s]

    Downloading ncbitaxon.db.gz:   1%|          | 22.7M/2.20G [00:01<00:59, 39.2MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 33.9M/2.20G [00:01<00:37, 61.6MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 42.4M/2.20G [00:01<00:33, 69.5MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 49.7M/2.20G [00:01<00:32, 71.0MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 53.5M/2.20G [00:01<00:37, 61.1MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 55.0M/2.20G [00:01<00:48, 47.4MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 56.6M/2.20G [00:01<00:59, 38.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 57.9M/2.20G [00:01<01:16, 30.2MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 59.0M/2.20G [00:01<01:33, 24.7MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 60.1M/2.20G [00:01<01:58, 19.4MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 61.1M/2.20G [00:02<02:17, 16.7MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 62.6M/2.20G [00:02<02:19, 16.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 64.4M/2.20G [00:02<02:15, 17.0MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 65.6M/2.20G [00:02<02:28, 15.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 67.0M/2.20G [00:02<02:32, 15.0MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 68.1M/2.20G [00:02<02:46, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 69.4M/2.20G [00:02<02:50, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 70.5M/2.20G [00:02<02:57, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 71.8M/2.20G [00:02<02:59, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 72.8M/2.20G [00:03<03:18, 11.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 73.7M/2.20G [00:03<03:29, 10.9MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 75.2M/2.20G [00:03<03:06, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 76.2M/2.20G [00:03<03:18, 11.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 77.1M/2.20G [00:03<03:36, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 78.1M/2.20G [00:03<03:42, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 79.1M/2.20G [00:03<03:46, 10.1MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 79.9M/2.20G [00:03<03:57, 9.59MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 80.7M/2.20G [00:03<04:09, 9.15MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 81.9M/2.20G [00:03<03:48, 9.99MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 83.2M/2.20G [00:04<03:28, 10.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 84.4M/2.20G [00:04<03:21, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 85.3M/2.20G [00:04<03:29, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 86.3M/2.20G [00:04<03:34, 10.6MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 87.8M/2.20G [00:04<03:12, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 89.6M/2.20G [00:04<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 91.0M/2.20G [00:04<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 92.4M/2.20G [00:04<02:43, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 94.0M/2.20G [00:04<02:33, 14.7MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 95.1M/2.20G [00:05<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 96.2M/2.20G [00:05<03:02, 12.4MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 97.4M/2.20G [00:05<03:09, 11.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 98.6M/2.20G [00:05<03:05, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 99.9M/2.20G [00:05<03:00, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 102M/2.20G [00:05<02:46, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 103M/2.20G [00:05<02:34, 14.6MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 104M/2.20G [00:05<02:42, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 106M/2.20G [00:05<02:42, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 107M/2.20G [00:05<02:51, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 109M/2.20G [00:06<02:45, 13.6MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 110M/2.20G [00:06<02:55, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 110M/2.20G [00:06<03:24, 11.0MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 111M/2.20G [00:06<03:51, 9.71MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 112M/2.20G [00:06<03:51, 9.71MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 113M/2.20G [00:06<03:47, 9.87MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 114M/2.20G [00:06<03:49, 9.80MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 115M/2.20G [00:06<03:34, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 116M/2.20G [00:06<04:09, 9.00MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 116M/2.20G [00:07<04:44, 7.90MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 118M/2.20G [00:07<03:17, 11.4MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<03:53, 9.59MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<04:52, 7.67MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<05:42, 6.53MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 120M/2.20G [00:07<06:13, 5.99MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 120M/2.20G [00:07<06:20, 5.88MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 121M/2.20G [00:07<06:03, 6.16MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 122M/2.20G [00:07<05:28, 6.81MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 123M/2.20G [00:07<04:49, 7.73MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 124M/2.20G [00:08<04:12, 8.85MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 125M/2.20G [00:08<03:41, 10.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 127M/2.20G [00:08<03:02, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 129M/2.20G [00:08<02:26, 15.2MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 131M/2.20G [00:08<02:21, 15.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 132M/2.20G [00:08<02:37, 14.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 133M/2.20G [00:08<02:41, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 134M/2.20G [00:08<02:47, 13.3MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 136M/2.20G [00:08<02:44, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 137M/2.20G [00:09<02:56, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 138M/2.20G [00:09<03:10, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 140M/2.20G [00:09<02:49, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 140M/2.20G [00:09<03:08, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 141M/2.20G [00:09<03:14, 11.4MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 142M/2.20G [00:09<03:35, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 143M/2.20G [00:09<03:30, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 145M/2.20G [00:09<03:05, 11.9MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 146M/2.20G [00:09<03:05, 12.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 147M/2.20G [00:09<03:00, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 148M/2.20G [00:10<03:02, 12.1MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 149M/2.20G [00:10<03:08, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 151M/2.20G [00:10<03:06, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 152M/2.20G [00:10<02:54, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 154M/2.20G [00:10<02:48, 13.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 155M/2.20G [00:10<02:50, 13.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 156M/2.20G [00:10<02:55, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 158M/2.20G [00:10<02:42, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 158M/2.20G [00:10<03:00, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 159M/2.20G [00:11<03:23, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 160M/2.20G [00:11<03:32, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 161M/2.20G [00:11<03:36, 10.2MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 162M/2.20G [00:11<03:22, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 163M/2.20G [00:11<03:22, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 164M/2.20G [00:11<03:26, 10.6MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 166M/2.20G [00:11<03:13, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 167M/2.20G [00:11<02:57, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 168M/2.20G [00:11<02:54, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 169M/2.20G [00:11<03:05, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 171M/2.20G [00:12<02:47, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 172M/2.20G [00:12<02:42, 13.4MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 174M/2.20G [00:12<02:37, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 175M/2.20G [00:12<02:36, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 177M/2.20G [00:12<02:37, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 178M/2.20G [00:12<02:31, 14.4MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 179M/2.20G [00:12<02:59, 12.1MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 180M/2.20G [00:12<02:51, 12.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 182M/2.20G [00:12<02:48, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 182M/2.20G [00:12<03:04, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 184M/2.20G [00:13<02:54, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 185M/2.20G [00:13<02:38, 13.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 186M/2.20G [00:13<02:50, 12.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 188M/2.20G [00:13<02:40, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 189M/2.20G [00:13<02:43, 13.2MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 190M/2.20G [00:13<02:49, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 192M/2.20G [00:13<02:49, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 193M/2.20G [00:13<02:37, 13.7MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 194M/2.20G [00:13<02:55, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 195M/2.20G [00:14<02:47, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 197M/2.20G [00:14<02:24, 14.9MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 200M/2.20G [00:14<01:50, 19.4MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 204M/2.20G [00:14<01:26, 24.7MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 208M/2.20G [00:14<01:15, 28.5MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 211M/2.20G [00:14<01:07, 31.6MB/s]

    Downloading ncbitaxon.db.gz:  10%|▉         | 216M/2.20G [00:14<01:01, 35.0MB/s]

    Downloading ncbitaxon.db.gz:  10%|▉         | 221M/2.20G [00:14<00:52, 40.3MB/s]

    Downloading ncbitaxon.db.gz:  10%|█         | 227M/2.20G [00:14<00:46, 46.1MB/s]

    Downloading ncbitaxon.db.gz:  10%|█         | 233M/2.20G [00:14<00:42, 49.7MB/s]

    Downloading ncbitaxon.db.gz:  11%|█         | 241M/2.20G [00:15<00:35, 59.6MB/s]

    Downloading ncbitaxon.db.gz:  11%|█         | 252M/2.20G [00:15<00:28, 73.7MB/s]

    Downloading ncbitaxon.db.gz:  11%|█▏        | 259M/2.20G [00:15<00:28, 74.7MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 263M/2.20G [00:15<00:32, 64.8MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 274M/2.20G [00:15<00:26, 77.5MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 282M/2.20G [00:15<00:26, 79.4MB/s]

    Downloading ncbitaxon.db.gz:  13%|█▎        | 292M/2.20G [00:15<00:23, 88.3MB/s]

    Downloading ncbitaxon.db.gz:  13%|█▎        | 302M/2.20G [00:15<00:22, 92.0MB/s]

    Downloading ncbitaxon.db.gz:  14%|█▍        | 312M/2.20G [00:15<00:21, 96.7MB/s]

    Downloading ncbitaxon.db.gz:  14%|█▍        | 322M/2.20G [00:15<00:20, 98.6MB/s]

    Downloading ncbitaxon.db.gz:  15%|█▍        | 332M/2.20G [00:16<00:20, 100MB/s]

    Downloading ncbitaxon.db.gz:  15%|█▌        | 341M/2.20G [00:16<00:22, 90.5MB/s]

    Downloading ncbitaxon.db.gz:  16%|█▌        | 354M/2.20G [00:16<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  16%|█▌        | 363M/2.20G [00:16<00:19, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 373M/2.20G [00:16<00:19, 102MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 383M/2.20G [00:16<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 392M/2.20G [00:16<00:19, 100MB/s]

    Downloading ncbitaxon.db.gz:  18%|█▊        | 402M/2.20G [00:16<00:19, 100MB/s]

    Downloading ncbitaxon.db.gz:  18%|█▊        | 410M/2.20G [00:16<00:20, 95.3MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▊        | 421M/2.20G [00:17<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▉        | 430M/2.20G [00:17<00:19, 98.4MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▉        | 439M/2.20G [00:17<00:19, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  20%|█▉        | 449M/2.20G [00:17<00:19, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  20%|██        | 458M/2.20G [00:17<00:19, 96.5MB/s]

    Downloading ncbitaxon.db.gz:  21%|██        | 467M/2.20G [00:17<00:19, 96.4MB/s]

    Downloading ncbitaxon.db.gz:  21%|██        | 473M/2.20G [00:17<00:21, 85.9MB/s]

    Downloading ncbitaxon.db.gz:  21%|██▏       | 481M/2.20G [00:17<00:22, 82.7MB/s]

    Downloading ncbitaxon.db.gz:  21%|██▏       | 481M/2.20G [00:17<00:38, 47.9MB/s]

    Downloading ncbitaxon.db.gz:  22%|██▏       | 488M/2.20G [00:17<00:34, 54.4MB/s]

    Downloading ncbitaxon.db.gz:  22%|██▏       | 500M/2.20G [00:18<00:25, 72.3MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 508M/2.20G [00:18<00:26, 70.3MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 518M/2.20G [00:18<00:22, 81.2MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 528M/2.20G [00:18<00:20, 86.6MB/s]

    Downloading ncbitaxon.db.gz:  24%|██▍       | 538M/2.20G [00:18<00:19, 90.6MB/s]

    Downloading ncbitaxon.db.gz:  24%|██▍       | 546M/2.20G [00:18<00:20, 87.5MB/s]

    Downloading ncbitaxon.db.gz:  25%|██▍       | 556M/2.20G [00:18<00:19, 90.9MB/s]

    Downloading ncbitaxon.db.gz:  25%|██▌       | 568M/2.20G [00:18<00:17, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▌       | 577M/2.20G [00:18<00:17, 98.1MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▌       | 586M/2.20G [00:19<00:17, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▋       | 595M/2.20G [00:19<00:18, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  27%|██▋       | 607M/2.20G [00:19<00:16, 104MB/s]

    Downloading ncbitaxon.db.gz:  27%|██▋       | 615M/2.20G [00:19<00:18, 95.5MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 625M/2.20G [00:19<00:17, 98.0MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 634M/2.20G [00:19<00:17, 97.3MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 642M/2.20G [00:19<00:17, 94.8MB/s]

    Downloading ncbitaxon.db.gz:  29%|██▉       | 652M/2.20G [00:19<00:18, 89.8MB/s]

    Downloading ncbitaxon.db.gz:  29%|██▉       | 664M/2.20G [00:19<00:16, 100MB/s]

    Downloading ncbitaxon.db.gz:  30%|██▉       | 675M/2.20G [00:19<00:15, 105MB/s]

    Downloading ncbitaxon.db.gz:  30%|███       | 678M/2.20G [00:20<00:20, 80.2MB/s]

    Downloading ncbitaxon.db.gz:  30%|███       | 680M/2.20G [00:20<00:25, 64.3MB/s]

    Downloading ncbitaxon.db.gz:  31%|███       | 690M/2.20G [00:20<00:22, 74.4MB/s]

    Downloading ncbitaxon.db.gz:  31%|███       | 699M/2.20G [00:20<00:20, 80.2MB/s]

    Downloading ncbitaxon.db.gz:  31%|███▏      | 708M/2.20G [00:20<00:19, 84.5MB/s]

    Downloading ncbitaxon.db.gz:  32%|███▏      | 715M/2.20G [00:20<00:20, 79.6MB/s]

    Downloading ncbitaxon.db.gz:  32%|███▏      | 726M/2.20G [00:20<00:17, 89.8MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 735M/2.20G [00:20<00:17, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 745M/2.20G [00:20<00:17, 92.4MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 755M/2.20G [00:21<00:16, 94.4MB/s]

    Downloading ncbitaxon.db.gz:  34%|███▍      | 764M/2.20G [00:21<00:16, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  34%|███▍      | 774M/2.20G [00:21<00:16, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▍      | 782M/2.20G [00:21<00:16, 93.1MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▌      | 794M/2.20G [00:21<00:15, 100MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▌      | 800M/2.20G [00:21<00:16, 89.9MB/s]

    Downloading ncbitaxon.db.gz:  36%|███▌      | 813M/2.20G [00:21<00:14, 103MB/s]

    Downloading ncbitaxon.db.gz:  36%|███▋      | 823M/2.20G [00:21<00:14, 102MB/s]

    Downloading ncbitaxon.db.gz:  37%|███▋      | 830M/2.20G [00:21<00:16, 93.0MB/s]

    Downloading ncbitaxon.db.gz:  37%|███▋      | 841M/2.20G [00:21<00:14, 99.7MB/s]

    Downloading ncbitaxon.db.gz:  38%|███▊      | 849M/2.20G [00:22<00:16, 90.4MB/s]

    Downloading ncbitaxon.db.gz:  38%|███▊      | 861M/2.20G [00:22<00:14, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▊      | 871M/2.20G [00:22<00:14, 103MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▉      | 881M/2.20G [00:22<00:14, 102MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▉      | 891M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  40%|███▉      | 901M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  40%|████      | 910M/2.20G [00:22<00:14, 99.4MB/s]

    Downloading ncbitaxon.db.gz:  41%|████      | 919M/2.20G [00:22<00:14, 93.5MB/s]

    Downloading ncbitaxon.db.gz:  41%|████▏     | 932M/2.20G [00:22<00:13, 104MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 941M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 950M/2.20G [00:23<00:13, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 959M/2.20G [00:23<00:14, 96.7MB/s]

    Downloading ncbitaxon.db.gz:  43%|████▎     | 968M/2.20G [00:23<00:13, 98.0MB/s]

    Downloading ncbitaxon.db.gz:  43%|████▎     | 978M/2.20G [00:23<00:13, 99.1MB/s]

    Downloading ncbitaxon.db.gz:  44%|████▍     | 988M/2.20G [00:23<00:13, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  44%|████▍     | 996M/2.20G [00:23<00:14, 92.6MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▍     | 0.98G/2.20G [00:23<00:15, 85.3MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▍     | 0.99G/2.20G [00:23<00:15, 86.7MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▌     | 1.00G/2.20G [00:23<00:14, 88.2MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▌     | 1.01G/2.20G [00:24<00:13, 93.7MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▌     | 1.02G/2.20G [00:24<00:14, 88.6MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▋     | 1.02G/2.20G [00:24<00:15, 81.7MB/s]

    Downloading ncbitaxon.db.gz:  47%|████▋     | 1.04G/2.20G [00:24<00:13, 90.7MB/s]

    Downloading ncbitaxon.db.gz:  47%|████▋     | 1.04G/2.20G [00:24<00:14, 85.3MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.05G/2.20G [00:24<00:13, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.06G/2.20G [00:24<00:14, 85.4MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.07G/2.20G [00:24<00:14, 86.0MB/s]

    Downloading ncbitaxon.db.gz:  49%|████▉     | 1.08G/2.20G [00:24<00:14, 84.2MB/s]

    Downloading ncbitaxon.db.gz:  49%|████▉     | 1.09G/2.20G [00:24<00:13, 92.2MB/s]

    Downloading ncbitaxon.db.gz:  50%|████▉     | 1.10G/2.20G [00:25<00:12, 97.1MB/s]

    Downloading ncbitaxon.db.gz:  50%|█████     | 1.11G/2.20G [00:25<00:12, 97.0MB/s]

    Downloading ncbitaxon.db.gz:  51%|█████     | 1.12G/2.20G [00:25<00:11, 100MB/s]

    Downloading ncbitaxon.db.gz:  51%|█████     | 1.12G/2.20G [00:25<00:12, 92.4MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.14G/2.20G [00:25<00:11, 102MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.15G/2.20G [00:25<00:11, 101MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.15G/2.20G [00:25<00:12, 91.1MB/s]

    Downloading ncbitaxon.db.gz:  53%|█████▎    | 1.16G/2.20G [00:25<00:11, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  53%|█████▎    | 1.17G/2.20G [00:25<00:11, 101MB/s]

    Downloading ncbitaxon.db.gz:  54%|█████▎    | 1.18G/2.20G [00:26<00:11, 97.2MB/s]

    Downloading ncbitaxon.db.gz:  54%|█████▍    | 1.19G/2.20G [00:26<00:12, 89.6MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▍    | 1.20G/2.20G [00:26<00:10, 102MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▍    | 1.21G/2.20G [00:26<00:11, 96.9MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▌    | 1.22G/2.20G [00:26<00:12, 87.5MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▌    | 1.23G/2.20G [00:26<00:10, 95.6MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▌    | 1.24G/2.20G [00:26<00:11, 91.4MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▋    | 1.24G/2.20G [00:26<00:11, 90.5MB/s]

    Downloading ncbitaxon.db.gz:  57%|█████▋    | 1.26G/2.20G [00:26<00:10, 101MB/s]

    Downloading ncbitaxon.db.gz:  57%|█████▋    | 1.26G/2.20G [00:26<00:10, 95.7MB/s]

    Downloading ncbitaxon.db.gz:  58%|█████▊    | 1.28G/2.20G [00:27<00:09, 102MB/s]

    Downloading ncbitaxon.db.gz:  58%|█████▊    | 1.29G/2.20G [00:27<00:09, 104MB/s]

    Downloading ncbitaxon.db.gz:  59%|█████▉    | 1.30G/2.20G [00:27<00:09, 106MB/s]

    Downloading ncbitaxon.db.gz:  59%|█████▉    | 1.31G/2.20G [00:27<00:09, 105MB/s]

    Downloading ncbitaxon.db.gz:  60%|█████▉    | 1.31G/2.20G [00:27<00:10, 92.7MB/s]

    Downloading ncbitaxon.db.gz:  60%|██████    | 1.32G/2.20G [00:27<00:09, 95.9MB/s]

    Downloading ncbitaxon.db.gz:  60%|██████    | 1.33G/2.20G [00:27<00:09, 94.8MB/s]

    Downloading ncbitaxon.db.gz:  61%|██████    | 1.34G/2.20G [00:27<00:09, 97.7MB/s]

    Downloading ncbitaxon.db.gz:  61%|██████▏   | 1.35G/2.20G [00:27<00:09, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  62%|██████▏   | 1.36G/2.20G [00:27<00:09, 99.2MB/s]

    Downloading ncbitaxon.db.gz:  62%|██████▏   | 1.37G/2.20G [00:28<00:08, 101MB/s]

    Downloading ncbitaxon.db.gz:  63%|██████▎   | 1.38G/2.20G [00:28<00:08, 106MB/s]

    Downloading ncbitaxon.db.gz:  63%|██████▎   | 1.39G/2.20G [00:28<00:08, 105MB/s]

    Downloading ncbitaxon.db.gz:  64%|██████▎   | 1.40G/2.20G [00:28<00:09, 95.9MB/s]

    Downloading ncbitaxon.db.gz:  64%|██████▍   | 1.41G/2.20G [00:28<00:07, 109MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▍   | 1.42G/2.20G [00:28<00:07, 108MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▍   | 1.43G/2.20G [00:28<00:07, 105MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▌   | 1.44G/2.20G [00:28<00:08, 102MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▌   | 1.44G/2.20G [00:28<00:10, 75.0MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▌   | 1.46G/2.20G [00:29<00:09, 86.5MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▋   | 1.46G/2.20G [00:29<00:09, 85.0MB/s]

    Downloading ncbitaxon.db.gz:  67%|██████▋   | 1.47G/2.20G [00:29<00:09, 82.2MB/s]

    Downloading ncbitaxon.db.gz:  67%|██████▋   | 1.48G/2.20G [00:29<00:08, 94.1MB/s]

    Downloading ncbitaxon.db.gz:  68%|██████▊   | 1.49G/2.20G [00:29<00:08, 95.2MB/s]

    Downloading ncbitaxon.db.gz:  68%|██████▊   | 1.50G/2.20G [00:29<00:08, 93.4MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▊   | 1.51G/2.20G [00:29<00:07, 96.2MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.52G/2.20G [00:29<00:08, 88.3MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:29<00:08, 90.6MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:29<00:10, 69.0MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:30<00:14, 49.3MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.53G/2.20G [00:30<00:14, 49.6MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.54G/2.20G [00:30<00:15, 46.0MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.54G/2.20G [00:30<00:15, 44.7MB/s]

    Downloading ncbitaxon.db.gz:  70%|███████   | 1.55G/2.20G [00:30<00:12, 57.0MB/s]

    Downloading ncbitaxon.db.gz:  71%|███████   | 1.56G/2.20G [00:30<00:09, 71.1MB/s]

    Downloading ncbitaxon.db.gz:  71%|███████   | 1.57G/2.20G [00:30<00:08, 80.4MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.58G/2.20G [00:30<00:08, 78.6MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.59G/2.20G [00:30<00:07, 86.2MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.60G/2.20G [00:31<00:06, 93.3MB/s]

    Downloading ncbitaxon.db.gz:  73%|███████▎  | 1.60G/2.20G [00:31<00:07, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  73%|███████▎  | 1.61G/2.20G [00:31<00:06, 90.3MB/s]

    Downloading ncbitaxon.db.gz:  74%|███████▍  | 1.63G/2.20G [00:31<00:06, 94.0MB/s]

    Downloading ncbitaxon.db.gz:  74%|███████▍  | 1.64G/2.20G [00:31<00:06, 98.1MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▍  | 1.64G/2.20G [00:31<00:06, 88.9MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▌  | 1.65G/2.20G [00:31<00:06, 94.0MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▌  | 1.66G/2.20G [00:31<00:06, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  76%|███████▌  | 1.67G/2.20G [00:31<00:05, 97.5MB/s]

    Downloading ncbitaxon.db.gz:  76%|███████▋  | 1.68G/2.20G [00:31<00:05, 96.2MB/s]

    Downloading ncbitaxon.db.gz:  77%|███████▋  | 1.69G/2.20G [00:32<00:06, 91.3MB/s]

    Downloading ncbitaxon.db.gz:  77%|███████▋  | 1.70G/2.20G [00:32<00:05, 94.5MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.71G/2.20G [00:32<00:05, 97.5MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.72G/2.20G [00:32<00:05, 97.8MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.73G/2.20G [00:32<00:05, 93.9MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.74G/2.20G [00:32<00:05, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.74G/2.20G [00:32<00:05, 87.4MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.75G/2.20G [00:32<00:05, 90.4MB/s]

    Downloading ncbitaxon.db.gz:  80%|███████▉  | 1.76G/2.20G [00:32<00:05, 94.2MB/s]

    Downloading ncbitaxon.db.gz:  80%|████████  | 1.77G/2.20G [00:33<00:04, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  81%|████████  | 1.78G/2.20G [00:33<00:04, 95.6MB/s]

    Downloading ncbitaxon.db.gz:  81%|████████  | 1.79G/2.20G [00:33<00:04, 98.6MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.80G/2.20G [00:33<00:04, 94.1MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.81G/2.20G [00:33<00:04, 98.2MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.82G/2.20G [00:33<00:04, 94.7MB/s]

    Downloading ncbitaxon.db.gz:  83%|████████▎ | 1.83G/2.20G [00:33<00:04, 100MB/s]

    Downloading ncbitaxon.db.gz:  83%|████████▎ | 1.84G/2.20G [00:33<00:03, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  84%|████████▎ | 1.85G/2.20G [00:33<00:03, 99.8MB/s]

    Downloading ncbitaxon.db.gz:  84%|████████▍ | 1.85G/2.20G [00:33<00:03, 100MB/s]

    Downloading ncbitaxon.db.gz:  85%|████████▍ | 1.86G/2.20G [00:34<00:03, 102MB/s]

    Downloading ncbitaxon.db.gz:  85%|████████▌ | 1.87G/2.20G [00:34<00:03, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▌ | 1.88G/2.20G [00:34<00:03, 102MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▌ | 1.89G/2.20G [00:34<00:03, 99.6MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▋ | 1.90G/2.20G [00:34<00:03, 93.5MB/s]

    Downloading ncbitaxon.db.gz:  87%|████████▋ | 1.91G/2.20G [00:34<00:03, 91.4MB/s]

    Downloading ncbitaxon.db.gz:  87%|████████▋ | 1.92G/2.20G [00:34<00:02, 102MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.93G/2.20G [00:34<00:03, 92.0MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.94G/2.20G [00:34<00:02, 99.2MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.95G/2.20G [00:34<00:02, 92.9MB/s]

    Downloading ncbitaxon.db.gz:  89%|████████▉ | 1.96G/2.20G [00:35<00:02, 97.0MB/s]

    Downloading ncbitaxon.db.gz:  89%|████████▉ | 1.97G/2.20G [00:35<00:02, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  90%|████████▉ | 1.98G/2.20G [00:35<00:02, 96.5MB/s]

    Downloading ncbitaxon.db.gz:  90%|█████████ | 1.98G/2.20G [00:35<00:02, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████ | 1.99G/2.20G [00:35<00:02, 95.0MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████ | 2.00G/2.20G [00:35<00:02, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████▏| 2.01G/2.20G [00:35<00:02, 93.6MB/s]

    Downloading ncbitaxon.db.gz:  92%|█████████▏| 2.02G/2.20G [00:35<00:02, 91.0MB/s]

    Downloading ncbitaxon.db.gz:  92%|█████████▏| 2.03G/2.20G [00:35<00:01, 93.2MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.04G/2.20G [00:36<00:01, 94.5MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.05G/2.20G [00:36<00:01, 95.2MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.06G/2.20G [00:36<00:01, 97.9MB/s]

    Downloading ncbitaxon.db.gz:  94%|█████████▍| 2.07G/2.20G [00:36<00:01, 94.2MB/s]

    Downloading ncbitaxon.db.gz:  94%|█████████▍| 2.07G/2.20G [00:36<00:01, 87.4MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▍| 2.08G/2.20G [00:36<00:01, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▍| 2.09G/2.20G [00:36<00:01, 97.9MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▌| 2.10G/2.20G [00:36<00:01, 94.4MB/s]

    Downloading ncbitaxon.db.gz:  96%|█████████▌| 2.11G/2.20G [00:36<00:01, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  96%|█████████▌| 2.12G/2.20G [00:36<00:00, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  97%|█████████▋| 2.13G/2.20G [00:37<00:00, 96.0MB/s]

    Downloading ncbitaxon.db.gz:  97%|█████████▋| 2.14G/2.20G [00:37<00:00, 97.3MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.15G/2.20G [00:37<00:00, 100MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.16G/2.20G [00:37<00:00, 94.3MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.17G/2.20G [00:37<00:00, 102MB/s]

    Downloading ncbitaxon.db.gz:  99%|█████████▉| 2.18G/2.20G [00:37<00:00, 91.8MB/s]

    Downloading ncbitaxon.db.gz:  99%|█████████▉| 2.19G/2.20G [00:37<00:00, 99.7MB/s]

    Downloading ncbitaxon.db.gz: 100%|█████████▉| 2.20G/2.20G [00:37<00:00, 98.0MB/s]'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2ASW.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 3; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:000038
- check_id: validate-terms-initial-network-attempt
  name: validate-terms-initial-network-attempt
  command: just validate-terms data/merge_yaml/merged/2ASW.yaml
  exit_code: 1
  required: false
  status: failed
  summary: Original sandbox attempt could not resolve a public dependency/reference
    host. Preserved as a failed historical attempt with its actual exit code; the
    same documented check later completed successfully with network access.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-terms-initial-network-attempt
- check_id: validate-references-initial-network-attempt
  name: validate-references-initial-network-attempt
  command: just validate-references data/merge_yaml/merged/2ASW.yaml
  exit_code: 2
  required: false
  status: failed
  summary: Original sandbox attempt could not resolve a public dependency/reference
    host. Preserved as a failed historical attempt with its actual exit code; the
    same documented check later completed successfully with network access.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-references-initial-network-attempt
- check_id: tsuji-methods
  name: Verify complete Tsuji methods
  required: true
  status: unavailable
  summary: Subscription preview and public supplement available; exact paper strain
    attribution, preacclimation sequence and potential main-text explanation of selenite
    conflict remain unverified.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - tsuji2021publisher
  - tsuji2021supplement
- check_id: liang-table-s2
  name: Verify Liang complete study formulation
  required: true
  status: unavailable
  summary: Full article body available; external author-hosted TableS2 failed DNS
    and full study composition remains unavailable.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - spectrum2023xml
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2ASW.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:38:33Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/algae/2asw.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:38:33Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:24.107546Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2ASW.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch008/078/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:22:25.909365Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-008/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch008/078/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:25:21.012564Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed



    Downloading ncbitaxon.db.gz:   0%|          | 0.00/2.20G [00:00<?, ?B/s]

    Downloading ncbitaxon.db.gz:   0%|          | 1.12M/2.20G [00:00<03:29, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 2.19M/2.20G [00:00<03:32, 11.1MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 4.44M/2.20G [00:00<02:22, 16.5MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 5.50M/2.20G [00:00<02:43, 14.4MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 6.50M/2.20G [00:00<03:03, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 7.88M/2.20G [00:00<02:56, 13.4MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 9.00M/2.20G [00:00<03:06, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   0%|          | 10.0M/2.20G [00:00<03:19, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   1%|          | 14.1M/2.20G [00:00<01:50, 21.4MB/s]

    Downloading ncbitaxon.db.gz:   1%|          | 22.7M/2.20G [00:01<00:59, 39.2MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 33.9M/2.20G [00:01<00:37, 61.6MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 42.4M/2.20G [00:01<00:33, 69.5MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 49.7M/2.20G [00:01<00:32, 71.0MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 53.5M/2.20G [00:01<00:37, 61.1MB/s]

    Downloading ncbitaxon.db.gz:   2%|▏         | 55.0M/2.20G [00:01<00:48, 47.4MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 56.6M/2.20G [00:01<00:59, 38.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 57.9M/2.20G [00:01<01:16, 30.2MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 59.0M/2.20G [00:01<01:33, 24.7MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 60.1M/2.20G [00:01<01:58, 19.4MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 61.1M/2.20G [00:02<02:17, 16.7MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 62.6M/2.20G [00:02<02:19, 16.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 64.4M/2.20G [00:02<02:15, 17.0MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 65.6M/2.20G [00:02<02:28, 15.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 67.0M/2.20G [00:02<02:32, 15.0MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 68.1M/2.20G [00:02<02:46, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 69.4M/2.20G [00:02<02:50, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 70.5M/2.20G [00:02<02:57, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 71.8M/2.20G [00:02<02:59, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 72.8M/2.20G [00:03<03:18, 11.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 73.7M/2.20G [00:03<03:29, 10.9MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 75.2M/2.20G [00:03<03:06, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 76.2M/2.20G [00:03<03:18, 11.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 77.1M/2.20G [00:03<03:36, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   3%|▎         | 78.1M/2.20G [00:03<03:42, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 79.1M/2.20G [00:03<03:46, 10.1MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 79.9M/2.20G [00:03<03:57, 9.59MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 80.7M/2.20G [00:03<04:09, 9.15MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 81.9M/2.20G [00:03<03:48, 9.99MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 83.2M/2.20G [00:04<03:28, 10.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▎         | 84.4M/2.20G [00:04<03:21, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 85.3M/2.20G [00:04<03:29, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 86.3M/2.20G [00:04<03:34, 10.6MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 87.8M/2.20G [00:04<03:12, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 89.6M/2.20G [00:04<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 91.0M/2.20G [00:04<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 92.4M/2.20G [00:04<02:43, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 94.0M/2.20G [00:04<02:33, 14.7MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 95.1M/2.20G [00:05<02:44, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 96.2M/2.20G [00:05<03:02, 12.4MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 97.4M/2.20G [00:05<03:09, 11.9MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 98.6M/2.20G [00:05<03:05, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 99.9M/2.20G [00:05<03:00, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   4%|▍         | 102M/2.20G [00:05<02:46, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 103M/2.20G [00:05<02:34, 14.6MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 104M/2.20G [00:05<02:42, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 106M/2.20G [00:05<02:42, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 107M/2.20G [00:05<02:51, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 109M/2.20G [00:06<02:45, 13.6MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 110M/2.20G [00:06<02:55, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 110M/2.20G [00:06<03:24, 11.0MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 111M/2.20G [00:06<03:51, 9.71MB/s]

    Downloading ncbitaxon.db.gz:   5%|▍         | 112M/2.20G [00:06<03:51, 9.71MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 113M/2.20G [00:06<03:47, 9.87MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 114M/2.20G [00:06<03:49, 9.80MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 115M/2.20G [00:06<03:34, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 116M/2.20G [00:06<04:09, 9.00MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 116M/2.20G [00:07<04:44, 7.90MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 118M/2.20G [00:07<03:17, 11.4MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<03:53, 9.59MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<04:52, 7.67MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 119M/2.20G [00:07<05:42, 6.53MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 120M/2.20G [00:07<06:13, 5.99MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 120M/2.20G [00:07<06:20, 5.88MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 121M/2.20G [00:07<06:03, 6.16MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 122M/2.20G [00:07<05:28, 6.81MB/s]

    Downloading ncbitaxon.db.gz:   5%|▌         | 123M/2.20G [00:07<04:49, 7.73MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 124M/2.20G [00:08<04:12, 8.85MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 125M/2.20G [00:08<03:41, 10.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 127M/2.20G [00:08<03:02, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 129M/2.20G [00:08<02:26, 15.2MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 131M/2.20G [00:08<02:21, 15.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 132M/2.20G [00:08<02:37, 14.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 133M/2.20G [00:08<02:41, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 134M/2.20G [00:08<02:47, 13.3MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 136M/2.20G [00:08<02:44, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 137M/2.20G [00:09<02:56, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 138M/2.20G [00:09<03:10, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 140M/2.20G [00:09<02:49, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   6%|▌         | 140M/2.20G [00:09<03:08, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 141M/2.20G [00:09<03:14, 11.4MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 142M/2.20G [00:09<03:35, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 143M/2.20G [00:09<03:30, 10.5MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 145M/2.20G [00:09<03:05, 11.9MB/s]

    Downloading ncbitaxon.db.gz:   6%|▋         | 146M/2.20G [00:09<03:05, 12.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 147M/2.20G [00:09<03:00, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 148M/2.20G [00:10<03:02, 12.1MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 149M/2.20G [00:10<03:08, 11.7MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 151M/2.20G [00:10<03:06, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 152M/2.20G [00:10<02:54, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 154M/2.20G [00:10<02:48, 13.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 155M/2.20G [00:10<02:50, 13.0MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 156M/2.20G [00:10<02:55, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 158M/2.20G [00:10<02:42, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 158M/2.20G [00:10<03:00, 12.2MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 159M/2.20G [00:11<03:23, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 160M/2.20G [00:11<03:32, 10.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 161M/2.20G [00:11<03:36, 10.2MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 162M/2.20G [00:11<03:22, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 163M/2.20G [00:11<03:22, 10.8MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 164M/2.20G [00:11<03:26, 10.6MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 166M/2.20G [00:11<03:13, 11.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 167M/2.20G [00:11<02:57, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   7%|▋         | 168M/2.20G [00:11<02:54, 12.6MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 169M/2.20G [00:11<03:05, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 171M/2.20G [00:12<02:47, 13.1MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 172M/2.20G [00:12<02:42, 13.4MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 174M/2.20G [00:12<02:37, 13.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 175M/2.20G [00:12<02:36, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 177M/2.20G [00:12<02:37, 13.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 178M/2.20G [00:12<02:31, 14.4MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 179M/2.20G [00:12<02:59, 12.1MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 180M/2.20G [00:12<02:51, 12.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 182M/2.20G [00:12<02:48, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 182M/2.20G [00:12<03:04, 11.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 184M/2.20G [00:13<02:54, 12.5MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 185M/2.20G [00:13<02:38, 13.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 186M/2.20G [00:13<02:50, 12.7MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 188M/2.20G [00:13<02:40, 13.5MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 189M/2.20G [00:13<02:43, 13.2MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 190M/2.20G [00:13<02:49, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   8%|▊         | 192M/2.20G [00:13<02:49, 12.8MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 193M/2.20G [00:13<02:37, 13.7MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 194M/2.20G [00:13<02:55, 12.3MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 195M/2.20G [00:14<02:47, 12.9MB/s]

    Downloading ncbitaxon.db.gz:   9%|▊         | 197M/2.20G [00:14<02:24, 14.9MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 200M/2.20G [00:14<01:50, 19.4MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 204M/2.20G [00:14<01:26, 24.7MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 208M/2.20G [00:14<01:15, 28.5MB/s]

    Downloading ncbitaxon.db.gz:   9%|▉         | 211M/2.20G [00:14<01:07, 31.6MB/s]

    Downloading ncbitaxon.db.gz:  10%|▉         | 216M/2.20G [00:14<01:01, 35.0MB/s]

    Downloading ncbitaxon.db.gz:  10%|▉         | 221M/2.20G [00:14<00:52, 40.3MB/s]

    Downloading ncbitaxon.db.gz:  10%|█         | 227M/2.20G [00:14<00:46, 46.1MB/s]

    Downloading ncbitaxon.db.gz:  10%|█         | 233M/2.20G [00:14<00:42, 49.7MB/s]

    Downloading ncbitaxon.db.gz:  11%|█         | 241M/2.20G [00:15<00:35, 59.6MB/s]

    Downloading ncbitaxon.db.gz:  11%|█         | 252M/2.20G [00:15<00:28, 73.7MB/s]

    Downloading ncbitaxon.db.gz:  11%|█▏        | 259M/2.20G [00:15<00:28, 74.7MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 263M/2.20G [00:15<00:32, 64.8MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 274M/2.20G [00:15<00:26, 77.5MB/s]

    Downloading ncbitaxon.db.gz:  12%|█▏        | 282M/2.20G [00:15<00:26, 79.4MB/s]

    Downloading ncbitaxon.db.gz:  13%|█▎        | 292M/2.20G [00:15<00:23, 88.3MB/s]

    Downloading ncbitaxon.db.gz:  13%|█▎        | 302M/2.20G [00:15<00:22, 92.0MB/s]

    Downloading ncbitaxon.db.gz:  14%|█▍        | 312M/2.20G [00:15<00:21, 96.7MB/s]

    Downloading ncbitaxon.db.gz:  14%|█▍        | 322M/2.20G [00:15<00:20, 98.6MB/s]

    Downloading ncbitaxon.db.gz:  15%|█▍        | 332M/2.20G [00:16<00:20, 100MB/s]

    Downloading ncbitaxon.db.gz:  15%|█▌        | 341M/2.20G [00:16<00:22, 90.5MB/s]

    Downloading ncbitaxon.db.gz:  16%|█▌        | 354M/2.20G [00:16<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  16%|█▌        | 363M/2.20G [00:16<00:19, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 373M/2.20G [00:16<00:19, 102MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 383M/2.20G [00:16<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  17%|█▋        | 392M/2.20G [00:16<00:19, 100MB/s]

    Downloading ncbitaxon.db.gz:  18%|█▊        | 402M/2.20G [00:16<00:19, 100MB/s]

    Downloading ncbitaxon.db.gz:  18%|█▊        | 410M/2.20G [00:16<00:20, 95.3MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▊        | 421M/2.20G [00:17<00:19, 101MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▉        | 430M/2.20G [00:17<00:19, 98.4MB/s]

    Downloading ncbitaxon.db.gz:  19%|█▉        | 439M/2.20G [00:17<00:19, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  20%|█▉        | 449M/2.20G [00:17<00:19, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  20%|██        | 458M/2.20G [00:17<00:19, 96.5MB/s]

    Downloading ncbitaxon.db.gz:  21%|██        | 467M/2.20G [00:17<00:19, 96.4MB/s]

    Downloading ncbitaxon.db.gz:  21%|██        | 473M/2.20G [00:17<00:21, 85.9MB/s]

    Downloading ncbitaxon.db.gz:  21%|██▏       | 481M/2.20G [00:17<00:22, 82.7MB/s]

    Downloading ncbitaxon.db.gz:  21%|██▏       | 481M/2.20G [00:17<00:38, 47.9MB/s]

    Downloading ncbitaxon.db.gz:  22%|██▏       | 488M/2.20G [00:17<00:34, 54.4MB/s]

    Downloading ncbitaxon.db.gz:  22%|██▏       | 500M/2.20G [00:18<00:25, 72.3MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 508M/2.20G [00:18<00:26, 70.3MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 518M/2.20G [00:18<00:22, 81.2MB/s]

    Downloading ncbitaxon.db.gz:  23%|██▎       | 528M/2.20G [00:18<00:20, 86.6MB/s]

    Downloading ncbitaxon.db.gz:  24%|██▍       | 538M/2.20G [00:18<00:19, 90.6MB/s]

    Downloading ncbitaxon.db.gz:  24%|██▍       | 546M/2.20G [00:18<00:20, 87.5MB/s]

    Downloading ncbitaxon.db.gz:  25%|██▍       | 556M/2.20G [00:18<00:19, 90.9MB/s]

    Downloading ncbitaxon.db.gz:  25%|██▌       | 568M/2.20G [00:18<00:17, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▌       | 577M/2.20G [00:18<00:17, 98.1MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▌       | 586M/2.20G [00:19<00:17, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  26%|██▋       | 595M/2.20G [00:19<00:18, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  27%|██▋       | 607M/2.20G [00:19<00:16, 104MB/s]

    Downloading ncbitaxon.db.gz:  27%|██▋       | 615M/2.20G [00:19<00:18, 95.5MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 625M/2.20G [00:19<00:17, 98.0MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 634M/2.20G [00:19<00:17, 97.3MB/s]

    Downloading ncbitaxon.db.gz:  28%|██▊       | 642M/2.20G [00:19<00:17, 94.8MB/s]

    Downloading ncbitaxon.db.gz:  29%|██▉       | 652M/2.20G [00:19<00:18, 89.8MB/s]

    Downloading ncbitaxon.db.gz:  29%|██▉       | 664M/2.20G [00:19<00:16, 100MB/s]

    Downloading ncbitaxon.db.gz:  30%|██▉       | 675M/2.20G [00:19<00:15, 105MB/s]

    Downloading ncbitaxon.db.gz:  30%|███       | 678M/2.20G [00:20<00:20, 80.2MB/s]

    Downloading ncbitaxon.db.gz:  30%|███       | 680M/2.20G [00:20<00:25, 64.3MB/s]

    Downloading ncbitaxon.db.gz:  31%|███       | 690M/2.20G [00:20<00:22, 74.4MB/s]

    Downloading ncbitaxon.db.gz:  31%|███       | 699M/2.20G [00:20<00:20, 80.2MB/s]

    Downloading ncbitaxon.db.gz:  31%|███▏      | 708M/2.20G [00:20<00:19, 84.5MB/s]

    Downloading ncbitaxon.db.gz:  32%|███▏      | 715M/2.20G [00:20<00:20, 79.6MB/s]

    Downloading ncbitaxon.db.gz:  32%|███▏      | 726M/2.20G [00:20<00:17, 89.8MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 735M/2.20G [00:20<00:17, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 745M/2.20G [00:20<00:17, 92.4MB/s]

    Downloading ncbitaxon.db.gz:  33%|███▎      | 755M/2.20G [00:21<00:16, 94.4MB/s]

    Downloading ncbitaxon.db.gz:  34%|███▍      | 764M/2.20G [00:21<00:16, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  34%|███▍      | 774M/2.20G [00:21<00:16, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▍      | 782M/2.20G [00:21<00:16, 93.1MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▌      | 794M/2.20G [00:21<00:15, 100MB/s]

    Downloading ncbitaxon.db.gz:  35%|███▌      | 800M/2.20G [00:21<00:16, 89.9MB/s]

    Downloading ncbitaxon.db.gz:  36%|███▌      | 813M/2.20G [00:21<00:14, 103MB/s]

    Downloading ncbitaxon.db.gz:  36%|███▋      | 823M/2.20G [00:21<00:14, 102MB/s]

    Downloading ncbitaxon.db.gz:  37%|███▋      | 830M/2.20G [00:21<00:16, 93.0MB/s]

    Downloading ncbitaxon.db.gz:  37%|███▋      | 841M/2.20G [00:21<00:14, 99.7MB/s]

    Downloading ncbitaxon.db.gz:  38%|███▊      | 849M/2.20G [00:22<00:16, 90.4MB/s]

    Downloading ncbitaxon.db.gz:  38%|███▊      | 861M/2.20G [00:22<00:14, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▊      | 871M/2.20G [00:22<00:14, 103MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▉      | 881M/2.20G [00:22<00:14, 102MB/s]

    Downloading ncbitaxon.db.gz:  39%|███▉      | 891M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  40%|███▉      | 901M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  40%|████      | 910M/2.20G [00:22<00:14, 99.4MB/s]

    Downloading ncbitaxon.db.gz:  41%|████      | 919M/2.20G [00:22<00:14, 93.5MB/s]

    Downloading ncbitaxon.db.gz:  41%|████▏     | 932M/2.20G [00:22<00:13, 104MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 941M/2.20G [00:22<00:13, 102MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 950M/2.20G [00:23<00:13, 99.5MB/s]

    Downloading ncbitaxon.db.gz:  42%|████▏     | 959M/2.20G [00:23<00:14, 96.7MB/s]

    Downloading ncbitaxon.db.gz:  43%|████▎     | 968M/2.20G [00:23<00:13, 98.0MB/s]

    Downloading ncbitaxon.db.gz:  43%|████▎     | 978M/2.20G [00:23<00:13, 99.1MB/s]

    Downloading ncbitaxon.db.gz:  44%|████▍     | 988M/2.20G [00:23<00:13, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  44%|████▍     | 996M/2.20G [00:23<00:14, 92.6MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▍     | 0.98G/2.20G [00:23<00:15, 85.3MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▍     | 0.99G/2.20G [00:23<00:15, 86.7MB/s]

    Downloading ncbitaxon.db.gz:  45%|████▌     | 1.00G/2.20G [00:23<00:14, 88.2MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▌     | 1.01G/2.20G [00:24<00:13, 93.7MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▌     | 1.02G/2.20G [00:24<00:14, 88.6MB/s]

    Downloading ncbitaxon.db.gz:  46%|████▋     | 1.02G/2.20G [00:24<00:15, 81.7MB/s]

    Downloading ncbitaxon.db.gz:  47%|████▋     | 1.04G/2.20G [00:24<00:13, 90.7MB/s]

    Downloading ncbitaxon.db.gz:  47%|████▋     | 1.04G/2.20G [00:24<00:14, 85.3MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.05G/2.20G [00:24<00:13, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.06G/2.20G [00:24<00:14, 85.4MB/s]

    Downloading ncbitaxon.db.gz:  48%|████▊     | 1.07G/2.20G [00:24<00:14, 86.0MB/s]

    Downloading ncbitaxon.db.gz:  49%|████▉     | 1.08G/2.20G [00:24<00:14, 84.2MB/s]

    Downloading ncbitaxon.db.gz:  49%|████▉     | 1.09G/2.20G [00:24<00:13, 92.2MB/s]

    Downloading ncbitaxon.db.gz:  50%|████▉     | 1.10G/2.20G [00:25<00:12, 97.1MB/s]

    Downloading ncbitaxon.db.gz:  50%|█████     | 1.11G/2.20G [00:25<00:12, 97.0MB/s]

    Downloading ncbitaxon.db.gz:  51%|█████     | 1.12G/2.20G [00:25<00:11, 100MB/s]

    Downloading ncbitaxon.db.gz:  51%|█████     | 1.12G/2.20G [00:25<00:12, 92.4MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.14G/2.20G [00:25<00:11, 102MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.15G/2.20G [00:25<00:11, 101MB/s]

    Downloading ncbitaxon.db.gz:  52%|█████▏    | 1.15G/2.20G [00:25<00:12, 91.1MB/s]

    Downloading ncbitaxon.db.gz:  53%|█████▎    | 1.16G/2.20G [00:25<00:11, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  53%|█████▎    | 1.17G/2.20G [00:25<00:11, 101MB/s]

    Downloading ncbitaxon.db.gz:  54%|█████▎    | 1.18G/2.20G [00:26<00:11, 97.2MB/s]

    Downloading ncbitaxon.db.gz:  54%|█████▍    | 1.19G/2.20G [00:26<00:12, 89.6MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▍    | 1.20G/2.20G [00:26<00:10, 102MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▍    | 1.21G/2.20G [00:26<00:11, 96.9MB/s]

    Downloading ncbitaxon.db.gz:  55%|█████▌    | 1.22G/2.20G [00:26<00:12, 87.5MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▌    | 1.23G/2.20G [00:26<00:10, 95.6MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▌    | 1.24G/2.20G [00:26<00:11, 91.4MB/s]

    Downloading ncbitaxon.db.gz:  56%|█████▋    | 1.24G/2.20G [00:26<00:11, 90.5MB/s]

    Downloading ncbitaxon.db.gz:  57%|█████▋    | 1.26G/2.20G [00:26<00:10, 101MB/s]

    Downloading ncbitaxon.db.gz:  57%|█████▋    | 1.26G/2.20G [00:26<00:10, 95.7MB/s]

    Downloading ncbitaxon.db.gz:  58%|█████▊    | 1.28G/2.20G [00:27<00:09, 102MB/s]

    Downloading ncbitaxon.db.gz:  58%|█████▊    | 1.29G/2.20G [00:27<00:09, 104MB/s]

    Downloading ncbitaxon.db.gz:  59%|█████▉    | 1.30G/2.20G [00:27<00:09, 106MB/s]

    Downloading ncbitaxon.db.gz:  59%|█████▉    | 1.31G/2.20G [00:27<00:09, 105MB/s]

    Downloading ncbitaxon.db.gz:  60%|█████▉    | 1.31G/2.20G [00:27<00:10, 92.7MB/s]

    Downloading ncbitaxon.db.gz:  60%|██████    | 1.32G/2.20G [00:27<00:09, 95.9MB/s]

    Downloading ncbitaxon.db.gz:  60%|██████    | 1.33G/2.20G [00:27<00:09, 94.8MB/s]

    Downloading ncbitaxon.db.gz:  61%|██████    | 1.34G/2.20G [00:27<00:09, 97.7MB/s]

    Downloading ncbitaxon.db.gz:  61%|██████▏   | 1.35G/2.20G [00:27<00:09, 97.6MB/s]

    Downloading ncbitaxon.db.gz:  62%|██████▏   | 1.36G/2.20G [00:27<00:09, 99.2MB/s]

    Downloading ncbitaxon.db.gz:  62%|██████▏   | 1.37G/2.20G [00:28<00:08, 101MB/s]

    Downloading ncbitaxon.db.gz:  63%|██████▎   | 1.38G/2.20G [00:28<00:08, 106MB/s]

    Downloading ncbitaxon.db.gz:  63%|██████▎   | 1.39G/2.20G [00:28<00:08, 105MB/s]

    Downloading ncbitaxon.db.gz:  64%|██████▎   | 1.40G/2.20G [00:28<00:09, 95.9MB/s]

    Downloading ncbitaxon.db.gz:  64%|██████▍   | 1.41G/2.20G [00:28<00:07, 109MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▍   | 1.42G/2.20G [00:28<00:07, 108MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▍   | 1.43G/2.20G [00:28<00:07, 105MB/s]

    Downloading ncbitaxon.db.gz:  65%|██████▌   | 1.44G/2.20G [00:28<00:08, 102MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▌   | 1.44G/2.20G [00:28<00:10, 75.0MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▌   | 1.46G/2.20G [00:29<00:09, 86.5MB/s]

    Downloading ncbitaxon.db.gz:  66%|██████▋   | 1.46G/2.20G [00:29<00:09, 85.0MB/s]

    Downloading ncbitaxon.db.gz:  67%|██████▋   | 1.47G/2.20G [00:29<00:09, 82.2MB/s]

    Downloading ncbitaxon.db.gz:  67%|██████▋   | 1.48G/2.20G [00:29<00:08, 94.1MB/s]

    Downloading ncbitaxon.db.gz:  68%|██████▊   | 1.49G/2.20G [00:29<00:08, 95.2MB/s]

    Downloading ncbitaxon.db.gz:  68%|██████▊   | 1.50G/2.20G [00:29<00:08, 93.4MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▊   | 1.51G/2.20G [00:29<00:07, 96.2MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.52G/2.20G [00:29<00:08, 88.3MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:29<00:08, 90.6MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:29<00:10, 69.0MB/s]

    Downloading ncbitaxon.db.gz:  69%|██████▉   | 1.53G/2.20G [00:30<00:14, 49.3MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.53G/2.20G [00:30<00:14, 49.6MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.54G/2.20G [00:30<00:15, 46.0MB/s]

    Downloading ncbitaxon.db.gz:  70%|██████▉   | 1.54G/2.20G [00:30<00:15, 44.7MB/s]

    Downloading ncbitaxon.db.gz:  70%|███████   | 1.55G/2.20G [00:30<00:12, 57.0MB/s]

    Downloading ncbitaxon.db.gz:  71%|███████   | 1.56G/2.20G [00:30<00:09, 71.1MB/s]

    Downloading ncbitaxon.db.gz:  71%|███████   | 1.57G/2.20G [00:30<00:08, 80.4MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.58G/2.20G [00:30<00:08, 78.6MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.59G/2.20G [00:30<00:07, 86.2MB/s]

    Downloading ncbitaxon.db.gz:  72%|███████▏  | 1.60G/2.20G [00:31<00:06, 93.3MB/s]

    Downloading ncbitaxon.db.gz:  73%|███████▎  | 1.60G/2.20G [00:31<00:07, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  73%|███████▎  | 1.61G/2.20G [00:31<00:06, 90.3MB/s]

    Downloading ncbitaxon.db.gz:  74%|███████▍  | 1.63G/2.20G [00:31<00:06, 94.0MB/s]

    Downloading ncbitaxon.db.gz:  74%|███████▍  | 1.64G/2.20G [00:31<00:06, 98.1MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▍  | 1.64G/2.20G [00:31<00:06, 88.9MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▌  | 1.65G/2.20G [00:31<00:06, 94.0MB/s]

    Downloading ncbitaxon.db.gz:  75%|███████▌  | 1.66G/2.20G [00:31<00:06, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  76%|███████▌  | 1.67G/2.20G [00:31<00:05, 97.5MB/s]

    Downloading ncbitaxon.db.gz:  76%|███████▋  | 1.68G/2.20G [00:31<00:05, 96.2MB/s]

    Downloading ncbitaxon.db.gz:  77%|███████▋  | 1.69G/2.20G [00:32<00:06, 91.3MB/s]

    Downloading ncbitaxon.db.gz:  77%|███████▋  | 1.70G/2.20G [00:32<00:05, 94.5MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.71G/2.20G [00:32<00:05, 97.5MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.72G/2.20G [00:32<00:05, 97.8MB/s]

    Downloading ncbitaxon.db.gz:  78%|███████▊  | 1.73G/2.20G [00:32<00:05, 93.9MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.74G/2.20G [00:32<00:05, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.74G/2.20G [00:32<00:05, 87.4MB/s]

    Downloading ncbitaxon.db.gz:  79%|███████▉  | 1.75G/2.20G [00:32<00:05, 90.4MB/s]

    Downloading ncbitaxon.db.gz:  80%|███████▉  | 1.76G/2.20G [00:32<00:05, 94.2MB/s]

    Downloading ncbitaxon.db.gz:  80%|████████  | 1.77G/2.20G [00:33<00:04, 96.3MB/s]

    Downloading ncbitaxon.db.gz:  81%|████████  | 1.78G/2.20G [00:33<00:04, 95.6MB/s]

    Downloading ncbitaxon.db.gz:  81%|████████  | 1.79G/2.20G [00:33<00:04, 98.6MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.80G/2.20G [00:33<00:04, 94.1MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.81G/2.20G [00:33<00:04, 98.2MB/s]

    Downloading ncbitaxon.db.gz:  82%|████████▏ | 1.82G/2.20G [00:33<00:04, 94.7MB/s]

    Downloading ncbitaxon.db.gz:  83%|████████▎ | 1.83G/2.20G [00:33<00:04, 100MB/s]

    Downloading ncbitaxon.db.gz:  83%|████████▎ | 1.84G/2.20G [00:33<00:03, 98.9MB/s]

    Downloading ncbitaxon.db.gz:  84%|████████▎ | 1.85G/2.20G [00:33<00:03, 99.8MB/s]

    Downloading ncbitaxon.db.gz:  84%|████████▍ | 1.85G/2.20G [00:33<00:03, 100MB/s]

    Downloading ncbitaxon.db.gz:  85%|████████▍ | 1.86G/2.20G [00:34<00:03, 102MB/s]

    Downloading ncbitaxon.db.gz:  85%|████████▌ | 1.87G/2.20G [00:34<00:03, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▌ | 1.88G/2.20G [00:34<00:03, 102MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▌ | 1.89G/2.20G [00:34<00:03, 99.6MB/s]

    Downloading ncbitaxon.db.gz:  86%|████████▋ | 1.90G/2.20G [00:34<00:03, 93.5MB/s]

    Downloading ncbitaxon.db.gz:  87%|████████▋ | 1.91G/2.20G [00:34<00:03, 91.4MB/s]

    Downloading ncbitaxon.db.gz:  87%|████████▋ | 1.92G/2.20G [00:34<00:02, 102MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.93G/2.20G [00:34<00:03, 92.0MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.94G/2.20G [00:34<00:02, 99.2MB/s]

    Downloading ncbitaxon.db.gz:  88%|████████▊ | 1.95G/2.20G [00:34<00:02, 92.9MB/s]

    Downloading ncbitaxon.db.gz:  89%|████████▉ | 1.96G/2.20G [00:35<00:02, 97.0MB/s]

    Downloading ncbitaxon.db.gz:  89%|████████▉ | 1.97G/2.20G [00:35<00:02, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  90%|████████▉ | 1.98G/2.20G [00:35<00:02, 96.5MB/s]

    Downloading ncbitaxon.db.gz:  90%|█████████ | 1.98G/2.20G [00:35<00:02, 90.1MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████ | 1.99G/2.20G [00:35<00:02, 95.0MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████ | 2.00G/2.20G [00:35<00:02, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  91%|█████████▏| 2.01G/2.20G [00:35<00:02, 93.6MB/s]

    Downloading ncbitaxon.db.gz:  92%|█████████▏| 2.02G/2.20G [00:35<00:02, 91.0MB/s]

    Downloading ncbitaxon.db.gz:  92%|█████████▏| 2.03G/2.20G [00:35<00:01, 93.2MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.04G/2.20G [00:36<00:01, 94.5MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.05G/2.20G [00:36<00:01, 95.2MB/s]

    Downloading ncbitaxon.db.gz:  93%|█████████▎| 2.06G/2.20G [00:36<00:01, 97.9MB/s]

    Downloading ncbitaxon.db.gz:  94%|█████████▍| 2.07G/2.20G [00:36<00:01, 94.2MB/s]

    Downloading ncbitaxon.db.gz:  94%|█████████▍| 2.07G/2.20G [00:36<00:01, 87.4MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▍| 2.08G/2.20G [00:36<00:01, 96.6MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▍| 2.09G/2.20G [00:36<00:01, 97.9MB/s]

    Downloading ncbitaxon.db.gz:  95%|█████████▌| 2.10G/2.20G [00:36<00:01, 94.4MB/s]

    Downloading ncbitaxon.db.gz:  96%|█████████▌| 2.11G/2.20G [00:36<00:01, 91.7MB/s]

    Downloading ncbitaxon.db.gz:  96%|█████████▌| 2.12G/2.20G [00:36<00:00, 94.9MB/s]

    Downloading ncbitaxon.db.gz:  97%|█████████▋| 2.13G/2.20G [00:37<00:00, 96.0MB/s]

    Downloading ncbitaxon.db.gz:  97%|█████████▋| 2.14G/2.20G [00:37<00:00, 97.3MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.15G/2.20G [00:37<00:00, 100MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.16G/2.20G [00:37<00:00, 94.3MB/s]

    Downloading ncbitaxon.db.gz:  98%|█████████▊| 2.17G/2.20G [00:37<00:00, 102MB/s]

    Downloading ncbitaxon.db.gz:  99%|█████████▉| 2.18G/2.20G [00:37<00:00, 91.8MB/s]

    Downloading ncbitaxon.db.gz:  99%|█████████▉| 2.19G/2.20G [00:37<00:00, 99.7MB/s]

    Downloading ncbitaxon.db.gz: 100%|█████████▉| 2.20G/2.20G [00:37<00:00, 98.0MB/s]'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2ASW.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:25:26.661716Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 3; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T07:38:33Z'
  support: supports
  summary: './data/normalized_yaml/algae/2asw.yaml:1:id: CultureMech:000038

    ./data/merge_yaml/merged/2ASW.yaml:1:id: CultureMech:000038

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:23.223232Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:23.392016Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi17268
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17268
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:23.488883Z'
  support: supports
  summary: CHEBI:17268 resolves to myo-inositol and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 0b0cce127edf288993722217ac5a9c05a0bb876b8c34a481b3a41a20ed847888
- evidence_id: chebi17439
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:23.574834Z'
  support: supports
  summary: CHEBI:17439 resolves to cyanocob(III)alamin and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi17821
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17821
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.079737Z'
  support: supports
  summary: CHEBI:17821 resolves to thymine and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: fa842c97ef37eb7149260a49f37f93a747804bf52c8534ddc616c9c2e0bdbba4
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-20T07:11:31.325976Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.147433Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.193584Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:48.016999Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate and is not obsolete.
    This verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi46760
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46760
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:24.837633Z'
  support: supports
  summary: CHEBI:46760 resolves to tricine and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 209acf0fe4e8f79f96615834a69b6a113baf59b37f08ecedb1a154b6ada66c27
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:16:25.002266Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride and is not obsolete. This
    verifies the asserted generic chemical identity; no source grade, salt, hydrate
    or stereochemistry beyond the record is inferred.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi63005
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T06:57:48.271252Z'
  support: supports
  summary: CHEBI:63005 resolves to sodium nitrate and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:38:33Z'
  support: supports
  summary: '{}'
- evidence_id: ccap2asw
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_2ASW.pdf
  locator: 'Page1: Stocks per litre; Medium per litre; preparation; footnote'
  accessed_at: '2026-10-21T07:16:20.827259Z'
  support: supports
  summary: Current revision002, approved/reviewed29May2026, read in full. Extra salts
    and vitamins are stocks per litre; tricine0.50g and NaCl35g are medium additions
    per final litre. Stock doses are7.50,2.50 and25.00mL for salts, vitamins and SE1
    respectively. The source specifies water-base alternatives, pH adjustment and
    autoclaving. Current PDF hash matches the October identity-correction event; equivalence
    to the earlier import is not asserted.
  snapshot_sha256: d5d658702a3640ed17c4d9d494f198f7122be90cbc81e64ccdc8afad1c4401cc
- evidence_id: ccapSE1Marine
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf
  locator: 'Page1: Preparing the soil; Medium'
  accessed_at: '2026-10-21T07:18:30.190899Z'
  support: supports
  summary: Full marine SE1 recipe read. Dried prepared soil with twice its volume
    of deionised water is autoclaved twice, cooled and settled2–3weeks; supernatant
    is decanted and sterilized again. The source states15psi/126C/20min for each of
    the first two cycles and15psi/121C/15min for the last; retain these literal conditions
    for curator verification without silently reconciling pressure/temperature. No
    elemental composition can be inferred.
  snapshot_sha256: a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934
- evidence_id: ccap1918
  kind: primary_source
  reference: https://www.ccap.ac.uk/catalogue/strain-19-18
  locator: Culture media, purity and growth conditions; strain identity
  accessed_at: '2026-10-21T07:16:20.671359Z'
  support: supports
  summary: CCAP19/18 is Dunaliella salina; current page links2ASW, axenic serial subculture
    and20–35C maintenance. This supports a named collection strain, not a universal
    temperature or growth rate.
  snapshot_sha256: f964fc991978a3f770d411091795fadcd6f81f6e34b069f935a96aa06e5c7989
- evidence_id: matsui2018cdn
  kind: primary_source
  reference: https://oup.silverchair-cdn.com/article-minimal/6116611
  locator: 'Materials and Methods: Cells and Culture Conditions; RT-qPCR; transformation
    and screening'
  accessed_at: '2026-10-21T07:18:27.884270Z'
  support: supports
  summary: Full public publisher text inspected. Cells and Culture Conditions names
    UTEX642 and CCMP1335 in artificial seawater plus half-strength Guillard f solution,20C,
    continuous30–75 micromol photons m-2 s-1,1%CO2 or ambient0.04%CO2. RT-qPCR gives
    midlog harvest OD730 ranges0.2–0.3 and0.1–0.15 respectively. Plate transformation/selection
    has protocol-specific additions; the paper does not establish the CCAP2ASW base
    formula.
  snapshot_sha256: beecd6db87651dbf5f4119169a755249ba977070ee4a7046d26dff3bab3b5d43
- evidence_id: tsuji2021publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s10126-021-10037-4
  locator: Abstract; access restriction
  accessed_at: '2026-10-21T07:17:08.105561Z'
  support: context_only
  summary: Accessible publisher abstract supports Chaetoceros gracilis sodium/CO2
    experiments and growth at0.23mM Na+ under5%CO2 but not0.04%CO2. The page is a
    subscription preview; exact strain attribution and preacclimation procedure in
    the main methods could not be reverified.
  snapshot_sha256: 427d28efefc7cd2c4fd88ad56f235c2f0921966d6b54bb775930745fbd49deee
- evidence_id: tsuji2021supplement
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art:10.1007%2Fs10126-021-10037-4/MediaObjects/10126_2021_10037_MOESM1_ESM.pdf
  locator: 'Page1 TableS1: Trace elements (micromolar), basal components (mM), footnotes
    a/b'
  accessed_at: '2026-10-21T07:18:31.117378Z'
  support: supports
  summary: Complete public TableS1 inspected, including headers and footnotes. Na2SeO3
    is0.001micromolar; Na2SiO3·9H2O is0.1mM. NaCl treatments are0,10,20,50,200,423mM
    with0.23mM residual basal sodium. The defined basal/trace/vitamin formulation
    does not establish ancestry from the CCAP soil-extract recipe.
  snapshot_sha256: 1cc2581bf2363ea89d31f170ae398b94d1125c647cc1c655a54417e6c73aac98
- evidence_id: spectrum2023xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10269666/fullTextXML
  locator: 'Materials and Methods: Algal strains and cultivation conditions'
  accessed_at: '2026-10-21T07:16:21.002264Z'
  support: supports
  summary: Full JATS source inspected. Methods identify D.salina CCAP19/18 cultivated
    in study2ASW containing1.5M NaCl,26C,8000lx and16/8 light/dark. FACHB-847 uses
    a separately cited Dunaliella medium. The owner correctly limits its variant to
    the explicit concentration and culture context; external TableS2 was unavailable.
  snapshot_sha256: 35398747e184a6699fa12f46288848dcc97932d087fa49e4056ea90f2debf22d
- evidence_id: frontiers2015
  kind: primary_source
  reference: https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2015.00020/full
  locator: Strains and media; Table1; Preliminary centrate screening; Gomord bibliography
    entry
  accessed_at: '2026-10-21T07:16:25.568390Z'
  support: supports
  summary: Publisher methods/Table1 and relevant results inspected. Eighteen Dunaliella
    strains are maintained on modified2ASW with33.6g/L sea salts replacing NaCl; maintenance
    is room temperature with18/6 light/dark. Centrate screening is a separate treatment.
    UTEX LB200 identification is disputed in results. Other genera use other media.
    The Gomord bibliography entry is a plant-glycosylation review; its missing recipe
    details are not inherited.
  snapshot_sha256: 25722daafbecd2fdc5d7b886d76e48e978334900fee717ef14f61401792fa792
- evidence_id: genome2017xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5658486/fullTextXML
  locator: Article title; Accession number(s)
  accessed_at: '2026-10-21T07:16:21.708578Z'
  support: supports
  summary: Full genome article supports CCAP19/18 identity, PRJNA32771, SAMN02746051,
    NSFN00000000 and first version NSFN01000000. It is identity evidence, not a2ASW
    formula or growth demonstration.
  snapshot_sha256: 3c50cdccf710f636997b8456be886fb9344ab3720dab14884190d148b6f1eb59
- evidence_id: matsui2018metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1104%2Fpp.18.00453&format=json&resultType=core
  locator: 'DOI query: resultList.result; title/authors/year/PMID'
  accessed_at: '2026-10-21T07:16:22.186690Z'
  support: supports
  summary: '[{"doi": "10.1104/pp.18.00453", "id": "30076224", "pmcid": null, "title":
    "Plasma Membrane-Type Aquaporins from Marine Diatoms Function as CO<sub>2</sub>/NH<sub>3</sub>
    Channels and Provide Photoprotection.", "authorString": "Matsui H, Hopkinson BM,
    Nakajima K, Matsuda Y.", "pubYear": "2018"}]'
  snapshot_sha256: e479b2a345f3deb010b57022dc85b40bfc22c0ad1999799f6bcf7728d0368f2a
- evidence_id: tsuji2021metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2Fs10126-021-10037-4&format=json&resultType=core
  locator: 'DOI query: resultList.result; title/authors/year/PMID'
  accessed_at: '2026-10-21T07:16:21.810962Z'
  support: supports
  summary: '[{"doi": "10.1007/s10126-021-10037-4", "id": "34109463", "pmcid": null,
    "title": "Characterization of a CO&lt;sub&gt;2&lt;/sub&gt;-Concentrating Mechanism
    with Low Sodium Dependency in the Centric Diatom Chaetoceros gracilis.", "authorString":
    "Tsuji Y, Kusi-Appiah G, Kozai N, Fukuda Y, Yamano T, Fukuzawa H.", "pubYear":
    "2021"}]'
  snapshot_sha256: fd5f281cff4f03b319ae122aefcb005c989585f29a6631871845fa004bbe1ea0
- evidence_id: spectrum2023metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fspectrum.00069-23&format=json&resultType=core
  locator: 'DOI query: resultList.result; title/authors/year/PMID'
  accessed_at: '2026-10-21T07:16:22.667080Z'
  support: supports
  summary: '[{"doi": "10.1128/spectrum.00069-23", "id": "37022233", "pmcid": "PMC10269666",
    "title": "Roles of Two Phytoene Synthases and Orange Protein in Carotenoid Metabolism
    of the \u03b2-Carotene-Accumulating <i>Dunaliella salina</i>.", "authorString":
    "Liang MH, Xie SR, Dai JL, Chen HH, Jiang JG.", "pubYear": "2023"}]'
  snapshot_sha256: 3dc43ab6a9ee6850a6e7437fda40c93f81c75306c8a4d93adf85fed9deab366c
- evidence_id: genome2017metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FgenomeA.01105-17&format=json&resultType=core
  locator: 'DOI query: resultList.result; title/authors/year/PMID'
  accessed_at: '2026-10-21T07:16:22.492832Z'
  support: supports
  summary: '[{"doi": "10.1128/genomea.01105-17", "id": "29074648", "pmcid": "PMC5658486",
    "title": "Draft Nuclear Genome Sequence of the Halophilic and Beta-Carotene-Accumulating
    Green Alga <i>Dunaliella salina</i> Strain CCAP19/18.", "authorString": "Polle
    JEW, Barry K, Cushman J, Schmutz J, Tran D, Hathwaik LT, Yim WC, Jenkins J, McKie-Krisberg
    Z, Prochnik S, Lindquist E, Dockter RB, Adam C, Molina H, Bunkenborg J, Jin E,
    Buchheim M, Magnuson J.", "pubYear": "2017"}]'
  snapshot_sha256: cccc78c24e5f765e4bd20783840ac1df8e1f0fb6527274d1f7ebce7da47ab5dd
- evidence_id: frontiers2015metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffenrg.2015.00020&format=json&resultType=core
  locator: DOI query hitCount
  accessed_at: '2026-10-21T07:16:22.851475Z'
  support: context_only
  summary: The bounded DOI query returned no EuropePMC hit. Publisher identity was
    verified directly; no PMID is invented and no global absence is claimed.
  snapshot_sha256: cefce1c3365a606dcc5581de87119305e768341a13d4069b5bbf7eb8b181da80
- evidence_id: taxonomyRetry
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3046,556484,296543,3044,3047,13790,257627,147822,289300,3026963,3026961,5748,3098&retmode=xml
  locator: 'Direct Taxon elements: identifiers, canonical names, ranks and synonyms'
  accessed_at: '2026-10-21T07:17:10.700088Z'
  support: supports
  summary: '[{"tax_id": "3046", "scientific_name": "Dunaliella salina", "rank": "species",
    "synonyms": ["Dunaliella bardawil"]}, {"tax_id": "556484", "scientific_name":
    "Phaeodactylum tricornutum CCAP 1055/1", "rank": "strain", "synonyms": []}, {"tax_id":
    "296543", "scientific_name": "Thalassiosira pseudonana CCMP1335", "rank": "strain",
    "synonyms": ["Thalassiosira pseudonana strain CCMP1335"]}, {"tax_id": "3044",
    "scientific_name": "Dunaliella", "rank": "genus", "synonyms": []}, {"tax_id":
    "3047", "scientific_name": "Dunaliella tertiolecta", "rank": "species", "synonyms":
    []}, {"tax_id": "13790", "scientific_name": "Dunaliella bioculata", "rank": "species",
    "synonyms": []}, {"tax_id": "257627", "scientific_name": "Dunaliella primolecta",
    "rank": "species", "synonyms": []}, {"tax_id": "147822", "scientific_name": "Dunaliella
    peircei", "rank": "species", "synonyms": []}, {"tax_id": "289300", "scientific_name":
    "Dunaliella maritima", "rank": "species", "synonyms": []}, {"tax_id": "3026963",
    "scientific_name": "Dunaliella terricola", "rank": "species", "synonyms": []},
    {"tax_id": "3026961", "scientific_name": "Dunaliella granulata", "rank": "species",
    "synonyms": []}, {"tax_id": "5748", "scientific_name": "Nannochloropsis", "rank":
    "genus", "synonyms": []}, {"tax_id": "3098", "scientific_name": "Neochloris",
    "rank": "genus", "synonyms": []}]'
  snapshot_sha256: aa7e5c8a8541519fca072335dc8f3768e68563be5bb292cb6e7757d6aafdf352
- evidence_id: bioproject32771
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/32771
  locator: Project title; organism and links
  accessed_at: '2026-10-21T07:16:26.089709Z'
  support: supports
  summary: Project identity agrees with Dunaliella salina CCAP19/18. It supplies sequencing
    provenance, not source recipe or cultivation evidence.
  snapshot_sha256: 8cc1fe294ba00c18ec0b5217945dee5c41cbb994fb781a97c680582510d76c06
- evidence_id: genomeDsalina
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_002284615.2/dataset_report
  locator: reports[0].organism; assembly_info; wgs_info
  accessed_at: '2026-10-21T07:16:19.830020Z'
  support: supports
  summary: GCA_002284615.2 is current and identifies D.salina CCAP19/18, taxid3046,
    PRJNA32771, SAMN02746051 and WGS NSFN00000000.2. The record base WGS accession
    is valid.
  snapshot_sha256: a82bb4b6be21a4da8cb0f5333f0988da1a451e697718a664401b3b97ec9f3999
- evidence_id: genomeTpseudonana
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000149405.2/dataset_report
  locator: reports[0].organism; assembly_info; wgs_info
  accessed_at: '2026-10-21T07:16:19.830963Z'
  support: supports
  summary: GCF_000149405.2 is current, paired with GCA_000149405.2, and identifies
    CCMP1335/taxid296543, SAMN02744045 and WGS AAFD00000000.2. These claims require
    NCBI identity evidence rather than only a growth-paper citation.
  snapshot_sha256: 2118396639a5d9d655df86558ecb863d90ef8121356a741101490569349553bb
- evidence_id: ccap-1052-1a
  kind: primary_source
  reference: https://www.ccap.ac.uk/catalogue/strain-1052-1a
  locator: Equivalent Strains; Notes; Original Designation
  accessed_at: '2026-10-21T07:24:57.270817Z'
  support: supports
  summary: Explicit equivalent-strain field lists UTEX642; notes identify Pt2.
  snapshot_sha256: 676219038bd29964fc8f4d9bf64d96d35921b660b05aa33872cf68ded58791e6
- evidence_id: ccap-1055-1
  kind: primary_source
  reference: https://www.ccap.ac.uk/catalogue/strain-1055-1
  locator: Equivalent Strains; Notes; Original Designation
  accessed_at: '2026-10-21T07:24:57.242973Z'
  support: supports
  summary: This strain is Pt1 clone8.6/PtGen from CCMP632, distinct from the UTEX642
    equivalence on CCAP1052/1A.
  snapshot_sha256: b3242703f6a6d4b8d407a43c13882b204f589db21c8ce3e4bc6076936e5b6244
- evidence_id: utex-0642
  kind: primary_source
  reference: https://utex.org/products/utex-lb-0642
  locator: UTEX Number; Origin; Relatives
  accessed_at: '2026-10-21T07:24:54.750745Z'
  support: supports
  summary: UTEX confirms accession642 and its relation to CCAP1052/1A. Relatives is
    not treated as an exact equivalence for every entry.
  snapshot_sha256: 68e721823bac7daaf0396fc4bac09692f202939f376ab313ad7a8bfa9a851b0a
- evidence_id: ncbi-taxonomy-556484
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=556484
  locator: TaxId; ScientificName; Rank; ParentTaxId
  accessed_at: '2026-10-21T07:24:55.682499Z'
  support: supports
  summary: NCBI556484 names Phaeodactylum tricornutum CCAP1055/1 at strain rank, parent2850.
    It does not identify UTEX642.
  snapshot_sha256: f955bdb9bf10d8a1a1a81520d9158d123315d56df805c733b7a9d453d7468d69
- evidence_id: chaetoceros-utex-lb-2658
  kind: primary_source
  reference: https://utex.org/products/utex-lb-2658
  locator: UTEX Number; Strain; Also Known As; Description of Location
  accessed_at: '2026-10-21T07:29:50.412425Z'
  support: supports
  summary: UTEX names LB2658 as Chaetoceros gracilis Schütt and also lists C.gracile/C.muelleri;
    this verifies collection naming only, not the strain used in an inaccessible paper
    methods section.
  snapshot_sha256: eb59f18f6b0c29b36b07c086602700dc7bb214b5450b148416bba6c6d3d4a9c1
- evidence_id: chaetoceros-ncbi-taxonomy-240364-265525
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=240364,265525
  locator: Direct taxa; scientific names; synonyms; authority names
  accessed_at: '2026-10-21T07:29:51.295226Z'
  support: supports
  summary: NCBI bare-name C.gracilis corresponds to C.neogracilis240364 with Pantocsek
    authority; C.muelleri is separate species265525. The authority/alias differences
    do not justify assigning either to UTEX2658 without additional evidence.
  snapshot_sha256: 86cf5d639d92f2268960599f583b68362a4370f9ed6506a14baefb21daf5878c
- evidence_id: chebi24848
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24848
  locator: Exact OLS term or direct parent/child response
  accessed_at: '2026-10-21T07:23:17.153630Z'
  support: supports
  summary: Generic inositol is a cyclohexanehexol class; CCAP does not state a stereoisomer.
  snapshot_sha256: 3fa2e0500a67481ab6bb14c94ab5bf54099850527cad5e97b5f191ea4325ce8d
- evidence_id: chebi39063
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39063
  locator: Exact OLS term or direct parent/child response
  accessed_at: '2026-10-21T07:23:18.597881Z'
  support: supports
  summary: The pinned Tricine row resolves to N-tris(hydroxymethyl)methylglycine.
  snapshot_sha256: 08db884b1f18600e8f95c6a3c02e90a169313cde5e80d487a89ee30465562d1a
- evidence_id: chebi46760children
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_46760/children
  locator: Exact OLS term or direct parent/child response
  accessed_at: '2026-10-21T07:24:06.405504Z'
  support: supports
  summary: Tricine CHEBI46760 has CHEBI39063 and its zwitterion as children; this
    is a granularity distinction.
  snapshot_sha256: 269c5dc28be14829e05a6bb7f2679f922ff98a861442a32ac3de8759b491886d
- evidence_id: chebi39063parents
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_39063/parents
  locator: Exact OLS term or direct parent/child response
  accessed_at: '2026-10-21T07:24:07.068097Z'
  support: supports
  summary: CHEBI39063 has the broader tricine CHEBI46760 parent.
  snapshot_sha256: d65c8e4fffd677975ad2369420404551f28c3c6aded73114ab5f48cadb1d4e08
- evidence_id: arithmetic
  kind: validation
  reference: Complete target, owner and current CCAP source tables
  locator: All13 amounts; stock-dose arithmetic; pinned mapping rows; every history
    timestamp
  accessed_at: '2026-10-21T07:38:33Z'
  support: supports
  summary: '{"quantity_trace": [{"field": "ingredients[0].concentration", "material":
    "NaNO3", "record_value_g_l": "15.00", "actual_source_basis": "g per litre of extra_salts
    stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre":
    "0.112500", "calculation": "15.00 g/L stock * 0.0075 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[1].concentration",
    "material": "Na2HPO4", "record_value_g_l": "0.60", "actual_source_basis": "g per
    litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre":
    "0.004500", "calculation": "0.60 g/L stock * 0.0075 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[2].concentration",
    "material": "K2HPO4", "record_value_g_l": "0.50", "actual_source_basis": "g per
    litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre":
    "0.003750", "calculation": "0.50 g/L stock * 0.0075 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[3].concentration",
    "material": "Biotin", "record_value_g_l": "0.0002", "actual_source_basis": "g
    per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "5.0E-7", "calculation": "0.0002
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[4].concentration", "material": "Calcium
    pantothenate", "record_value_g_l": "0.02", "actual_source_basis": "g per litre
    of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[5].concentration",
    "material": "Cyanocobalamin", "record_value_g_l": "0.004", "actual_source_basis":
    "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "0.0000100", "calculation": "0.004
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[6].concentration", "material": "Folic
    acid", "record_value_g_l": "0.0004", "actual_source_basis": "g per litre of vitamins
    stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00000100", "calculation": "0.0004 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[7].concentration",
    "material": "Inositol", "record_value_g_l": "1.0", "actual_source_basis": "g per
    litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00250", "calculation": "1.0 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[8].concentration",
    "material": "Nicotinic acid", "record_value_g_l": "0.02", "actual_source_basis":
    "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[9].concentration", "material": "Thiamine
    HCl", "record_value_g_l": "0.1", "actual_source_basis": "g per litre of vitamins
    stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00025", "calculation": "0.1 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[10].concentration",
    "material": "Thymine", "record_value_g_l": "0.6", "actual_source_basis": "g per
    litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00150", "calculation": "0.6 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[11].concentration",
    "material": "Tricine", "record_value_g_l": "0.50", "actual_source_basis": "g added
    per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre":
    "0.50", "calculation": "No stock dilution: source directly states medium addition
    per litre.", "decision": "verified direct addition; not total seawater content"},
    {"field": "ingredients[12].concentration", "material": "NaCl", "record_value_g_l":
    "35.00", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre":
    null, "derived_added_contribution_g_per_final_litre": "35.00", "calculation":
    "No stock dilution: source directly states medium addition per litre.", "decision":
    "verified direct addition; not total seawater content"}], "mim_comparison": [{"field":
    "ingredients[0].term", "record_id": "CHEBI:63005", "pinned_preferred_row": {"label":
    "NaNO3", "match_type": "preferred_term", "identifier": "CHEBI:63005", "preferred_term":
    "NaNO3", "ontology_id": "CHEBI:63005", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, "id_matches": true}, {"field": "ingredients[1].term", "record_id":
    "CHEBI:34683", "pinned_preferred_row": {"label": "Na2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field":
    "ingredients[2].term", "record_id": "CHEBI:131527", "pinned_preferred_row": {"label":
    "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, "id_matches": true}, {"field": "ingredients[3].term", "record_id":
    "CHEBI:15956", "pinned_preferred_row": {"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field":
    "ingredients[4].term", "record_id": "CHEBI:31345", "pinned_preferred_row": {"label":
    "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345",
    "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[5].term",
    "record_id": "CHEBI:17439", "pinned_preferred_row": {"label": "Cyanocobalamin",
    "match_type": "preferred_term", "identifier": "CHEBI:17439", "preferred_term":
    "Cyanocobalamin", "ontology_id": "CHEBI:17439", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, "id_matches": true}, {"field": "ingredients[6].term", "record_id":
    "CHEBI:27470", "pinned_preferred_row": {"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches": true}, {"field":
    "ingredients[7].term", "record_id": "CHEBI:17268", "pinned_preferred_row": {"label":
    "Inositol", "match_type": "preferred_term", "identifier": "CHEBI:24848", "preferred_term":
    "Inositol", "ontology_id": "CHEBI:24848", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, "id_matches": false}, {"field": "ingredients[8].term", "record_id":
    "CHEBI:15940", "pinned_preferred_row": {"label": "Nicotinic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid",
    "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"},
    "id_matches": true}, {"field": "ingredients[9].term", "record_id": "CHEBI:49105",
    "pinned_preferred_row": {"label": "Thiamine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches":
    true}, {"field": "ingredients[10].term", "record_id": "CHEBI:17821", "pinned_preferred_row":
    {"label": "Thymine", "match_type": "preferred_term", "identifier": "CHEBI:17821",
    "preferred_term": "Thymine", "ontology_id": "CHEBI:17821", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, "id_matches": true}, {"field": "ingredients[11].term",
    "record_id": "CHEBI:46760", "pinned_preferred_row": {"label": "Tricine", "match_type":
    "preferred_term", "identifier": "CHEBI:39063", "preferred_term": "Tricine", "ontology_id":
    "CHEBI:39063", "mapping_status": "MAPPED", "ambiguity": "unique"}, "id_matches":
    false}, {"field": "ingredients[12].term", "record_id": "CHEBI:26710", "pinned_preferred_row":
    {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, "id_matches": true}], "history": [{"layer": "target",
    "index": 0, "timestamp": "2026-01-28", "timezone_present": false}, {"layer": "target",
    "index": 1, "timestamp": "2026-02-03T11:23:39.554565", "timezone_present": false},
    {"layer": "target", "index": 2, "timestamp": "2026-02-03T11:26:43.440568", "timezone_present":
    false}, {"layer": "target", "index": 3, "timestamp": "2026-03-13T06:18:52.992431Z",
    "timezone_present": true}, {"layer": "target", "index": 4, "timestamp": "2026-03-17T19:45:03.950098+00:00",
    "timezone_present": true}, {"layer": "target", "index": 5, "timestamp": "2026-04-04T12:54:55.050840",
    "timezone_present": false}, {"layer": "target", "index": 6, "timestamp": "2026-05-09T13:35:00-07:00",
    "timezone_present": true}, {"layer": "target", "index": 7, "timestamp": "2026-06-10T07:37:33.980020+00:00",
    "timezone_present": true}, {"layer": "target", "index": 8, "timestamp": "2026-08-06T00:58:02.481264+00:00",
    "timezone_present": true}, {"layer": "target", "index": 9, "timestamp": "2026-09-13T00:00:00-07:00",
    "timezone_present": true}, {"layer": "target", "index": 10, "timestamp": "2026-10-05T19:29:05+00:00",
    "timezone_present": true}, {"layer": "target", "index": 11, "timestamp": "2026-10-05T19:43:18.434134+00:00",
    "timezone_present": true}, {"layer": "owner", "index": 0, "timestamp": "2026-01-28",
    "timezone_present": false}, {"layer": "owner", "index": 1, "timestamp": "2026-02-03T11:23:39.554565",
    "timezone_present": false}, {"layer": "owner", "index": 2, "timestamp": "2026-02-03T11:26:43.440568",
    "timezone_present": false}, {"layer": "owner", "index": 3, "timestamp": "2026-03-13T06:18:52.992431Z",
    "timezone_present": true}, {"layer": "owner", "index": 4, "timestamp": "2026-03-17T19:45:03.950098+00:00",
    "timezone_present": true}, {"layer": "owner", "index": 5, "timestamp": "2026-04-04T12:54:55.050840",
    "timezone_present": false}, {"layer": "owner", "index": 6, "timestamp": "2026-05-09T13:35:00-07:00",
    "timezone_present": true}, {"layer": "owner", "index": 7, "timestamp": "2026-06-10T07:37:33.980020+00:00",
    "timezone_present": true}, {"layer": "owner", "index": 8, "timestamp": "2026-08-06T00:58:02.481264+00:00",
    "timezone_present": true}, {"layer": "owner", "index": 9, "timestamp": "2026-09-13T00:00:00-07:00",
    "timezone_present": true}, {"layer": "owner", "index": 10, "timestamp": "2026-10-05T19:29:05+00:00",
    "timezone_present": true}, {"layer": "owner", "index": 11, "timestamp": "2026-10-14T02:43:29.178060+00:00",
    "timezone_present": true}]}'
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/ccap_importer.py
  locator: Unconditional light/temperature assignments around lines179–184
  accessed_at: '2026-10-21T07:38:33Z'
  support: supports
  summary: Exact current light intensity, light cycle and temperature strings are
    unconditional importer defaults, not source-scoped cultivation observations.
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: organism_grows_in_medium_edge; transform
  accessed_at: '2026-10-21T07:38:33Z'
  support: supports
  summary: Current code omits truthy scoped_to_variant descriptors and otherwise emits
    a parent growth edge when a taxon is present. The two grounded diatom descriptors
    lack scope; the ungrounded Chaetoceros descriptor emits no taxon edge. Code was
    inspected, not exported. Existing tests/test_kgx_variant_growth_scope.py was read
    and not executed.
- evidence_id: prior-report
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/2asw.md
  locator: Entire historical report
  accessed_at: '2026-10-21T07:38:33Z'
  support: context_only
  summary: The prior report explicitly source-checked0/15 claims and is not current
    scientific validation; current source comparisons are independent.
- evidence_id: validate-terms-initial-network-attempt
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2ASW.yaml
  locator: Original attempt; later successful retry retained separately
  accessed_at: '2026-10-21T07:22:28.823234Z'
  support: context_only
  summary: "Validating ontology terms (MediaRecipe)...\n\nTraceback (most recent call\
    \ last):\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py\"\
    , line 204, in _new_conn\n    sock = connection.create_connection(\n        (self._dns_host,\
    \ self.port),\n    ...<2 lines>...\n        socket_options=self.socket_options,\n\
    \    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/util/connection.py\"\
    , line 60, in create_connection\n    for res in socket.getaddrinfo(host, port,\
    \ family, socket.SOCK_STREAM):\n               ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/Users/marcin/.local/share/uv/python/cpython-3.13.2-macos-aarch64-none/lib/python3.13/socket.py\"\
    , line 977, in getaddrinfo\n    for res in _socket.getaddrinfo(host, port, family,\
    \ type, proto, flags):\n               ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    socket.gaierror: [Errno 8] nodename nor servname provided, or not known\n\nThe\
    \ above exception was the direct cause of the following exception:\n\nTraceback\
    \ (most recent call last):\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py\"\
    , line 787, in urlopen\n    response = self._make_request(\n        conn,\n  \
    \  ...<10 lines>...\n        **response_kw,\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py\"\
    , line 488, in _make_request\n    raise new_e\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py\"\
    , line 464, in _make_request\n    self._validate_conn(conn)\n    ~~~~~~~~~~~~~~~~~~~^^^^^^\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py\"\
    , line 1093, in _validate_conn\n    conn.connect()\n    ~~~~~~~~~~~~^^\n  File\
    \ \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py\"\
    , line 759, in connect\n    self.sock = sock = self._new_conn()\n            \
    \           ~~~~~~~~~~~~~~^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connection.py\"\
    , line 211, in _new_conn\n    raise NameResolutionError(self.host, self, e) from\
    \ e\nurllib3.exceptions.NameResolutionError: HTTPSConnection(host='semanticsql.berkeleybop.io',\
    \ port=443): Failed to resolve 'semanticsql.berkeleybop.io' ([Errno 8] nodename\
    \ nor servname provided, or not known)\n\nThe above exception was the direct cause\
    \ of the following exception:\n\nTraceback (most recent call last):\n  File \"\
    /private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/adapters.py\"\
    , line 644, in send\n    resp = conn.urlopen(\n        method=request.method,\n\
    \    ...<9 lines>...\n        chunked=chunked,\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/connectionpool.py\"\
    , line 841, in urlopen\n    retries = retries.increment(\n        method, url,\
    \ error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/urllib3/util/retry.py\"\
    , line 535, in increment\n    raise MaxRetryError(_pool, url, reason) from reason\
    \  # type: ignore[arg-type]\n    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='semanticsql.berkeleybop.io',\
    \ port=443): Max retries exceeded with url: /ncbitaxon.db.gz (Caused by NameResolutionError(\"\
    HTTPSConnection(host='semanticsql.berkeleybop.io', port=443): Failed to resolve\
    \ 'semanticsql.berkeleybop.io' ([Errno 8] nodename nor servname provided, or not\
    \ known)\"))\n\nDuring handling of the above exception, another exception occurred:\n\
    \nTraceback (most recent call last):\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/utils/download.py\"\
    , line 202, in download\n    with requests.get(url, **kwargs) as response, path.open(\"\
    wb\") as file:  # noqa:S113\n         ~~~~~~~~~~~~^^^^^^^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/api.py\"\
    , line 73, in get\n    return request(\"get\", url, params=params, **kwargs)\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/api.py\"\
    , line 59, in request\n    return session.request(method=method, url=url, **kwargs)\n\
    \           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/sessions.py\"\
    , line 589, in request\n    resp = self.send(prep, **send_kwargs)\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/sessions.py\"\
    , line 703, in send\n    r = adapter.send(request, **kwargs)\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/requests/adapters.py\"\
    , line 677, in send\n    raise ConnectionError(e, request=request)\nrequests.exceptions.ConnectionError:\
    \ HTTPSConnectionPool(host='semanticsql.berkeleybop.io', port=443): Max retries\
    \ exceeded with url: /ncbitaxon.db.gz (Caused by NameResolutionError(\"HTTPSConnection(host='semanticsql.berkeleybop.io',\
    \ port=443): Failed to resolve 'semanticsql.berkeleybop.io' ([Errno 8] nodename\
    \ nor servname provided, or not known)\"))\n\nThe above exception was the direct\
    \ cause of the following exception:\n\nTraceback (most recent call last):\n  File\
    \ \"/private/tmp/culturemech-review-env/bin/linkml-term-validator\", line 10,\
    \ in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/cli.py\"\
    , line 431, in main\n    app()\n    ~~~^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py\"\
    , line 336, in __call__\n    raise e\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py\"\
    , line 319, in __call__\n    return get_command(self)(*args, **kwargs)\n     \
    \      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py\"\
    , line 1631, in __call__\n    return self.main(*args, **kwargs)\n           ~~~~~~~~~^^^^^^^^^^^^^^^^^\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/core.py\"\
    , line 814, in main\n    return _main(\n        self,\n    ...<6 lines>...\n \
    \       **extra,\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/core.py\"\
    , line 190, in _main\n    rv = self.invoke(ctx)\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py\"\
    , line 2032, in invoke\n    return _process_result(sub_ctx.command.invoke(sub_ctx))\n\
    \                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py\"\
    , line 1415, in invoke\n    return ctx.invoke(self.callback, **ctx.params)\n \
    \          ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/click/core.py\"\
    , line 910, in invoke\n    return callback(*args, **kwargs)\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/typer/main.py\"\
    , line 706, in wrapper\n    return callback(**use_params)\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/cli.py\"\
    , line 278, in validate_data\n    report = validator.validate_source(loader, target_class=target_class)\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml/validator/validator.py\"\
    , line 68, in validate_source\n    return ValidationReport(results=list(self.iter_results_from_source(loader,\
    \ target_class)))\n                                    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml/validator/validator.py\"\
    , line 105, in iter_results_from_source\n    for result in plugin.process(instance,\
    \ context):\n                  ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py\"\
    , line 192, in process\n    yield from self._process_recursive(\n    ...<4 lines>...\n\
    \    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py\"\
    , line 257, in _process_recursive\n    yield from self._process_recursive(\n \
    \   ...<4 lines>...\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py\"\
    , line 238, in _process_recursive\n    yield from self._validate_binding(\n  \
    \  ...<6 lines>...\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py\"\
    , line 335, in _validate_binding\n    yield from self._validate_term_exists(\n\
    \    ...<6 lines>...\n    )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/binding_plugin.py\"\
    , line 565, in _validate_term_exists\n    ontology_label = self.get_ontology_label(field_value)\n\
    \  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/base.py\"\
    , line 251, in get_ontology_label\n    adapter = self._get_adapter(prefix)\n \
    \ File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/linkml_term_validator/plugins/base.py\"\
    , line 219, in _get_adapter\n    adapter = get_adapter(adapter_string)\n  File\
    \ \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/selector.py\"\
    , line 155, in get_adapter\n    return res.implementation_class(res, **kwargs)\n\
    \           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^\n  File \"<string>\", line\
    \ 27, in __init__\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/implementations/sqldb/sql_implementation.py\"\
    , line 350, in __post_init__\n    db_path = FILE_CACHE.ensure_gunzip(\n      \
    \  url=url, autoclean=False, download_kwargs=SEMSQL_SQLITE_DOWNLOAD_KWARGS\n \
    \   )\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/oaklib/utilities/caching.py\"\
    , line 277, in ensure_gunzip\n    self._module.ensure_gunzip(\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~^\n\
    \        url=url,\n        ^^^^^^^^\n    ...<3 lines>...\n        download_kwargs=download_kwargs,\n\
    \        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n    )\n    ^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/impl.py\"\
    , line 455, in ensure_gunzip\n    path = self.ensure(\n        *subkeys,\n   \
    \ ...<3 lines>...\n        download_kwargs=download_kwargs,\n    )\n  File \"\
    /private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/impl.py\"\
    , line 284, in ensure\n    utils.download(\n    ~~~~~~~~~~~~~~^\n        url=url,\n\
    \        ^^^^^^^^\n    ...<3 lines>...\n        **(download_kwargs or {}),\n \
    \       ^^^^^^^^^^^^^^^^^^^^^^^^^^\n    )\n    ^\n  File \"/private/tmp/culturemech-review-env/lib/python3.13/site-packages/pystow/utils/download.py\"\
    , line 220, in download\n    raise DownloadError(backend, url, path, e) from e\n\
    pystow.utils.download.DownloadError: Failed with requests to download https://semanticsql.berkeleybop.io/ncbitaxon.db.gz\
    \ to /private/tmp/culturemech-review-pystow/oaklib/ncbitaxon.db.gz\nerror: recipe\
    \ `validate-terms` failed with exit code 1"
- evidence_id: validate-references-initial-network-attempt
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2ASW.yaml
  locator: Original attempt; later successful retry retained separately
  accessed_at: '2026-10-21T07:22:30.421952Z'
  support: context_only
  summary: 'Validating evidence references (MediaRecipe)...


    [ERROR] reference_validation: HTTPSConnectionPool(host=''www.ccap.ac.uk'', port=443):
    Max retries exceeded with url: /catalogue/strain-19-18 (Caused by NameResolutionError("HTTPSConnection(host=''www.ccap.ac.uk'',
    port=443): Failed to resolve ''www.ccap.ac.uk'' ([Errno 8] nodename nor servname
    provided, or not known)"))

    error: recipe `validate-references` failed with exit code 2'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '13 primary CHEBI identities resolve with matching labels; 0 of 0 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi17268
  - chebi17439
  - chebi17821
  - chebi26710
  - chebi27470
  - chebi31345
  - chebi34683
  - chebi46760
  - chebi49105
  - chebi63005
  details: 13 direct ingredient instances; CHEBI-primary instance linkage 13/13 (100.00%),
    verified secondary coverage 0/13 (0.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: Exact CCAP parent and study-medium boundaries
  outcome: concern
  summary: CCAP2ASW accession and current revision are supported. F/2ASW in Matsui
    and the defined modified F/2ASW in Tsuji are study formulations whose derivation
    from this CCAP parent is not established. Similar ASW names do not prove recipe
    ancestry. New owner variants retain explicit incomplete-formula limits.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - matsui2018cdn
  - tsuji2021supplement
  - spectrum2023xml
  - frontiers2015
- assessment_id: amounts
  area: quantity
  topic: All13 ingredient concentrations and three stock additions
  outcome: concern
  summary: 'correct: first3 values are extra-salts stock g/L and next8 are vitamin-stock
    g/L. Their nominal added contributions require7.50mL/L and2.50mL/L respectively.
    Last2 values are direct tricine/NaCl additions. The nitrate note acknowledges
    stock basis but does not provide a structured stock or dose. Soil extract25mL/L
    is omitted. Retain source stock compositions and dose hierarchy instead of merely
    overwriting with derived final contributions.'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - ccapSE1Marine
  - arithmetic
  details: '[{"field": "ingredients[0].concentration", "material": "NaNO3", "record_value_g_l":
    "15.00", "actual_source_basis": "g per litre of extra_salts stock", "source_stock_dose_ml_per_final_litre":
    "7.50", "derived_added_contribution_g_per_final_litre": "0.112500", "calculation":
    "15.00 g/L stock * 0.0075 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[1].concentration", "material": "Na2HPO4",
    "record_value_g_l": "0.60", "actual_source_basis": "g per litre of extra_salts
    stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre":
    "0.004500", "calculation": "0.60 g/L stock * 0.0075 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[2].concentration",
    "material": "K2HPO4", "record_value_g_l": "0.50", "actual_source_basis": "g per
    litre of extra_salts stock", "source_stock_dose_ml_per_final_litre": "7.50", "derived_added_contribution_g_per_final_litre":
    "0.003750", "calculation": "0.50 g/L stock * 0.0075 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[3].concentration",
    "material": "Biotin", "record_value_g_l": "0.0002", "actual_source_basis": "g
    per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "5.0E-7", "calculation": "0.0002
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[4].concentration", "material": "Calcium
    pantothenate", "record_value_g_l": "0.02", "actual_source_basis": "g per litre
    of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.000050", "calculation": "0.02 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[5].concentration",
    "material": "Cyanocobalamin", "record_value_g_l": "0.004", "actual_source_basis":
    "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "0.0000100", "calculation": "0.004
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[6].concentration", "material": "Folic
    acid", "record_value_g_l": "0.0004", "actual_source_basis": "g per litre of vitamins
    stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00000100", "calculation": "0.0004 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[7].concentration",
    "material": "Inositol", "record_value_g_l": "1.0", "actual_source_basis": "g per
    litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00250", "calculation": "1.0 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[8].concentration",
    "material": "Nicotinic acid", "record_value_g_l": "0.02", "actual_source_basis":
    "g per litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50",
    "derived_added_contribution_g_per_final_litre": "0.000050", "calculation": "0.02
    g/L stock * 0.0025 L stock / 1 L final medium", "decision": "correct representation:
    stock composition"}, {"field": "ingredients[9].concentration", "material": "Thiamine
    HCl", "record_value_g_l": "0.1", "actual_source_basis": "g per litre of vitamins
    stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00025", "calculation": "0.1 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[10].concentration",
    "material": "Thymine", "record_value_g_l": "0.6", "actual_source_basis": "g per
    litre of vitamins stock", "source_stock_dose_ml_per_final_litre": "2.50", "derived_added_contribution_g_per_final_litre":
    "0.00150", "calculation": "0.6 g/L stock * 0.0025 L stock / 1 L final medium",
    "decision": "correct representation: stock composition"}, {"field": "ingredients[11].concentration",
    "material": "Tricine", "record_value_g_l": "0.50", "actual_source_basis": "g added
    per final litre of medium", "source_stock_dose_ml_per_final_litre": null, "derived_added_contribution_g_per_final_litre":
    "0.50", "calculation": "No stock dilution: source directly states medium addition
    per litre.", "decision": "verified direct addition; not total seawater content"},
    {"field": "ingredients[12].concentration", "material": "NaCl", "record_value_g_l":
    "35.00", "actual_source_basis": "g added per final litre of medium", "source_stock_dose_ml_per_final_litre":
    null, "derived_added_contribution_g_per_final_litre": "35.00", "calculation":
    "No stock dilution: source directly states medium addition per litre.", "decision":
    "verified direct addition; not total seawater content"}]'
- assessment_id: base-preparation
  area: completeness
  topic: Water alternatives, pH and sterilization
  outcome: concern
  summary: 'add: make to1L with filtered natural seawater; alternative deionised water
    to1L plus33.6g Instant Ocean sea salts. Preserve this water-base alternative alongside
    listed35g NaCl without assuming the sea salts replace that addition. Source pH7.6–7.8
    uses1M NaOH or1M HCl before autoclaving15psi15min. These are absent from both
    local layers. Reagent strength is not final concentration; added titrant volumes
    and total seawater ion content are unknown.'
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - ccapSE1Marine
- assessment_id: grounding-detail
  area: grounding
  topic: Canonical labels and source specificity
  outcome: concern
  summary: All13 primary labels/IDs resolve and are not obsolete; no secondary keys
    are asserted. Primary linkage13/13(100%) and secondary0/13(0%) measure linkage
    only. Eleven exact preferred-name MIM rows agree. Inositol maps to myo-inositol
    although the source is nonspecific; Tricine maps to a broader class than pinned
    MIM. Neither discrepancy proves a different supplied chemical.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - arithmetic
  - mim
  - chebi17268
  - chebi46760
  - chebi24848
  - chebi39063
  - chebi46760children
  - chebi39063parents
- assessment_id: dunaliella
  area: evidence
  topic: D.salina CCAP19/18 parent maintenance and identifiers
  outcome: supported
  summary: Collection evidence supports the named strain in2ASW, axenic serial subculture
    at20–35C. Taxid3046 is species rank, while collection strain and genome metadata
    provide strain context. BioProject/assembly/WGS/BioSample identity support is
    distinct from cultivation evidence.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - ccap1918
  - taxonomyRetry
  - bioproject32771
  - genomeDsalina
  - genome2017xml
- assessment_id: diatoms
  area: grounding
  topic: Two Matsui diatom strain claims and harvest context
  outcome: concern
  summary: The paper supports UTEX642 and CCMP1335 in study F/2ASW with the stated20C,
    continuous light, CO2/air and harvest OD730 ranges. OD is a midlog sampling criterion,
    not terminal yield. CCMP1335 matches taxid296543 and independent genome identifiers.
    UTEX642 is CCAP1052/1A/Pt2, while asserted556484 is CCAP1055/1/Pt1 clone8.6; narrative
    caution cannot repair that strain mismatch.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - matsui2018cdn
  - ccap-1052-1a
  - ccap-1055-1
  - utex-0642
  - ncbi-taxonomy-556484
  - taxonomyRetry
  - genomeTpseudonana
- assessment_id: chaetoceros
  area: evidence
  topic: Sodium-response strain and variant claims
  outcome: unknown
  summary: The abstract supports species-level sodium/CO2 observations; TableS1 supports
    NaCl manipulation and0.1mM nonahydrate metasilicate. Its0.001micromolar selenite
    equals1nM, conflicting with the record10nM. Exact paper strain/preacclimation
    await full methods. UTEX verifies collection LB2658 naming, but authority/alias
    differences leave its taxon unresolved; no wrong taxon is asserted because the
    record has no term.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - tsuji2021publisher
  - tsuji2021supplement
  - chaetoceros-utex-lb-2658
  - chaetoceros-ncbi-taxonomy-240364-265525
- assessment_id: variant-growth
  area: scope
  topic: Structured growth scope and export consequences
  outcome: concern
  summary: The three non-Dunaliella descriptors describe study media in prose but
    lack scoped_to_variant. Current code would emit parent edges for the two grounded
    diatoms. Correct formulation relationships first, then scope or relocate growth.
    Current code suppresses scoped parent growth; it does not establish complete variant-growth
    export.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - matsui2018cdn
  - tsuji2021supplement
  - exporter
- assessment_id: later-studies
  area: evidence
  topic: Two owner-only study variants and taxonomic qualifications
  outcome: supported
  summary: Liang1.5M NaCl and Hiibel33.6g/L sea-salt substitution have exact narrow
    support; neither supplies a complete inherited parent recipe. All18 Dunaliella
    names/strains match Table1 and owner notes; genus-only rows and disputed UTEX
    LB200 remain qualified. D.bardawil is a taxonomic synonym of D.salina, not independent
    strain verification. Centrate results and other-medium cohorts are not promoted
    to2ASW growth.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - owner-0
  - spectrum2023xml
  - frontiers2015
  - taxonomyRetry
- assessment_id: freshness
  area: completeness
  topic: Later owner references and variants missing from generated target
  outcome: concern
  summary: Two bounded study variants, three paper references and the October14 citation
    event are absent from the generated record. Shared legacy recipe/strain errors
    remain in both layers and must be corrected before regeneration.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - spectrum2023xml
  - frontiers2015
  - genome2017xml
- assessment_id: metadata
  area: provenance
  topic: Citation identity, evidence placement, history and stale export notes
  outcome: concern
  summary: Five paper identities/authors/years and all asserted project/genome identifiers
    were checked. Four legacy history entries per layer lack timezones; retain uncertainty
    and append-only history. Most legacy claims lack exact excerpts, and CCMP1335
    genome support is attached only to a growth DOI. Owner references[6] and[7] incorrectly
    describe current KGX as ignoring variant scope.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - matsui2018metadata
  - tsuji2021metadata
  - spectrum2023metadata
  - genome2017metadata
  - frontiers2015
  - arithmetic
  - exporter
  - genomeTpseudonana
  - validate-references
- assessment_id: conditions-class
  area: scope
  topic: Generic conditions, classifications and applications
  outcome: concern
  summary: Algae/COMPLEX/UNDEFINED/LIQUID agrees with the seawater/soil-extract recipe;
    isolate describes separate named cultures, not universal axenicity. Light50–100,12:12/16:8
    and15–30C are importer defaults, not verified parent conditions. They must not
    replace collection20–35C or distinct experimental conditions. Marine is descriptive;35g
    NaCl is not total salinity. Process quality flags do not certify formulation accuracy.
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - ccap1918
  - matsui2018cdn
  - spectrum2023xml
  - frontiers2015
  - importer
findings:
- finding_id: f1
  issue_key: CM000038-stock-hierarchy
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock compositions are flattened into the medium recipe
  description: Eleven stock g/L values appear as direct ingredients; stock doses7.50/2.50mL
    per final litre and soil-extract25mL/L are absent. This cannot represent the source
    formulation.
  target_ids:
  - CultureMech:000038
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - ccapSE1Marine
  - arithmetic
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM000038-source-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source base alternatives and preparation are missing
  description: Neither layer represents filtered seawater/deionised-water plus Instant
    Ocean alternatives, final litre, pH7.6–7.8 with1M titrant or15psi15min autoclaving.
  target_ids:
  - CultureMech:000038
  field_paths:
  - ingredients
  - preparation_steps
  - ph_value
  - sterilization
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - ccapSE1Marine
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: CM000038-utex642-wrong-strain-taxon
  category: grounding
  severity: blocker
  status: open
  certainty: confirmed
  title: UTEX642 is assigned the taxon of a distinct collection strain
  description: Primary collection sources identify UTEX642 with CCAP1052/1A/Pt2; NCBITaxon556484
    names CCAP1055/1/Pt1 clone8.6. The PARTIAL prose caution does not make this asserted
    strain taxon correct.
  target_ids:
  - CultureMech:000038
  field_paths:
  - target_organisms[1].term
  - target_organisms[1].strain
  - target_organisms[1].evidence
  evidence_ids:
  - record
  - owner-0
  - matsui2018cdn
  - ccap-1052-1a
  - ccap-1055-1
  - ncbi-taxonomy-556484
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM000038-diatom-parent-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Diatom study media lack established CCAP parent ancestry
  description: Legacy variants treat F/2ASW and modified F/2ASW as descendants of
    this CCAP extra-salts/vitamin/soil-extract recipe. The inspected publications
    do not establish that relationship.
  target_ids:
  - CultureMech:000038
  field_paths:
  - variants[0]
  - variants[1]
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - matsui2018cdn
  - tsuji2021supplement
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f5
  issue_key: CM000038-selenite-source-conflict
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Recorded selenite is ten times the supplementary formulation
  description: The record10nM sodium selenite conflicts with TableS1 0.001micromolar=1nM.0.1mM
    metasilicate is supported, with nonahydrate form in the source.
  target_ids:
  - CultureMech:000038
  field_paths:
  - variants[1].modifications[0]
  evidence_ids:
  - record
  - owner-0
  - tsuji2021supplement
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f6
  issue_key: CM000038-variant-growth-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Variant-only growth lacks structured scope
  description: Three study-medium organism descriptors qualify scope only in prose.
    The grounded diatoms would become parent growth edges under current export code.
  target_ids:
  - CultureMech:000038
  field_paths:
  - target_organisms[1].scoped_to_variant
  - target_organisms[2].scoped_to_variant
  - target_organisms[3].scoped_to_variant
  evidence_ids:
  - record
  - owner-0
  - matsui2018cdn
  - tsuji2021supplement
  - exporter
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f7
  issue_key: CM000038-generic-culture-defaults
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Parent culture conditions are unsupported importer defaults
  description: The light intensity/cycle and temperature strings are unconditional
    importer values. Source maintenance and study conditions are different and strain-specific.
  target_ids:
  - CultureMech:000038
  field_paths:
  - light_intensity
  - light_cycle
  - temperature_range
  evidence_ids:
  - record
  - owner-0
  - importer
  - ccap1918
  - matsui2018cdn
  - frontiers2015
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f8
  issue_key: CM000038-generated-study-staleness
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits bounded owner study additions
  description: Two study variants, three references and later citation history are
    missing from the target despite their bounded support in the owner.
  target_ids:
  - CultureMech:000038
  field_paths:
  - variants
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - spectrum2023xml
  - frontiers2015
  - genome2017xml
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f9
  issue_key: CM000038-claim-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy claims lack narrow excerpts and identity sources
  description: Legacy ingredients, variants and organism observations mostly have
    source pointers/explanations without exact excerpts. CCMP1335 assembly/BioSample/WGS
    support requires the independent NCBI source.
  target_ids:
  - CultureMech:000038
  field_paths:
  - ingredients[*].evidence
  - variants[0:2].evidence
  - target_organisms[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - ccap2asw
  - matsui2018cdn
  - genomeTpseudonana
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f10
  issue_key: CM000038-grounding-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two mappings need source-specific granularity review
  description: CCAP Inositol does not specify myo stereochemistry; the pinned index
    uses generic inositol. Tricine target class is broader than the pinned molecular
    term. Canonical labels resolve and a wrong supplied chemical is not established.
  target_ids:
  - CultureMech:000038
  field_paths:
  - ingredients[7].term
  - ingredients[11].term
  evidence_ids:
  - record
  - owner-0
  - arithmetic
  - chebi17268
  - chebi24848
  - chebi46760children
  - chebi39063parents
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f11
  issue_key: CM000038-stale-export-notes
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Owner notes misstate current variant export behavior
  description: Two later owner citation notes say current KGX ignores scoped_to_variant;
    current code suppresses scoped parent growth.
  target_ids:
  - CultureMech:000038
  field_paths:
  - data/normalized_yaml/algae/2asw.yaml:references[6].notes
  - data/normalized_yaml/algae/2asw.yaml:references[7].notes
  evidence_ids:
  - owner-0
  - exporter
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f12
  issue_key: CM000038-history-timezone-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Four legacy history entries lack timezone context
  description: Each layer retains one date-only and three naive timestamps. Their
    timezone cannot be reconstructed from the text.
  target_ids:
  - CultureMech:000038
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - curation_history[2].timestamp
  - curation_history[5].timestamp
  evidence_ids:
  - record
  - owner-0
  - arithmetic
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Reconstruct verified stock composition and dose hierarchy in the maintained
    owner, including SE1 and its source preparation; preserve original stock concentrations
    and separate any derived contributions.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Add source-scoped alternatives, preparation and exact evidence, preserving
    seawater composition and titrant-volume uncertainty.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a3
  description: Resolve the supported strain identity or an explicitly qualified broader
    species mapping; retain UTEX642 paper evidence without transferring it to a different
    strain.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a4
  description: Verify exact recipe identity and ancestry; retain distinct study-media
    records or qualified relationships where full parent equivalence is unsupported.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a5
  description: Reconcile exact main-text/supplement protocol before changing the owner;
    preserve the observed discrepancy and inaccessible-methods limit, and cite the
    resolved quantity/form.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a6
  description: After resolving organism and formulation identity, scope each descriptor
    to its verified variant or linked medium; verify that no unsupported parent growth
    edge is emitted.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a7
  description: Remove or explicitly qualify generic defaults and retain only source-supported
    strain/formulation-scoped conditions.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a8
  description: After shared legacy errors and stale owner notes are curated, regenerate
    and verify narrow excerpts, study limits and taxonomic qualifications survive.
  finding_ids:
  - f8
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a9
  description: Attach short exact field-scoped excerpts and metadata while keeping
    growth, sequence identity, stock arithmetic and unresolved methods distinct.
  finding_ids:
  - f9
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a10
  description: Reconcile ontology granularity using source material identity and the
    packaged resolver; document unresolved inositol specificity rather than guessing
    another isomer.
  finding_ids:
  - f10
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a11
  description: Correct current-versus-historical wording on a future authorized owner
    edit and distinguish parent-edge suppression from actual variant-edge support.
  finding_ids:
  - f11
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a12
  description: Preserve append-only events and record any recoverable timestamp context
    in a new provenance event; do not invent a timezone or silently rewrite history.
  finding_ids:
  - f12
  target_ids:
  - CultureMech:000038
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Full Tsuji main methods and external Liang TableS2 were inaccessible. The exact
  paper strain/preacclimation and full Liang formulation remain unverified; no paid
  access or contact was attempted.
- Current CCAP PDF is the inspected revision; historical import-version identity was
  not reconstructed. No stock composition is inferred for soil extract or seawater,
  and no total NaCl or elemental salinity conversion is asserted.
- Exact UTEX642 taxon and UTEX2658 taxonomic assignment remain unresolved. Existing
  species/genus mappings do not independently verify physical strain identity. No
  growth/export or corpus regeneration was run.
tags:
- unreviewed-records
- batch-008
- generated-medium
```
