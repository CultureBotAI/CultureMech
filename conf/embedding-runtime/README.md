# Optional text-map runtime

This governed Python 3.13 environment is for explicit local embedding and
PaCMAP builds. Normal tests, record validation and Pages rendering do not
install it. The lock pins numerical/model dependencies independently of a
Mech's curation environment; the encoder and map receipts record actual
installed library versions as well.

From a Mech repository root, export current semantic input with its domain
adapter, inspect it, and then explicitly run inference and projection:

```bash
uv run python scripts/text_map_inputs.py --output workspace/text-map-inputs.jsonl
uv run python scripts/embedding_pipeline.py inspect --input workspace/text-map-inputs.jsonl
uv run --locked --project conf/embedding-runtime python scripts/embedding_pipeline.py embed --input workspace/text-map-inputs.jsonl --cache workspace/text-map-vectors.sqlite --profile-output workspace/text-map-profile.json --device cpu
uv run --locked --project conf/embedding-runtime python scripts/embedding_pipeline.py project --input workspace/text-map-inputs.jsonl --cache workspace/text-map-vectors.sqlite --profile workspace/text-map-profile.json --output data/text_map
uv run python scripts/embedding_pipeline.py check --output data/text_map --input workspace/text-map-inputs.jsonl --cache workspace/text-map-vectors.sqlite
```

Run one small explicit `--limit` adapter canary first, with separate output and
cache paths. Verify its vector count, finite coordinates, source receipt,
rendered page and repeat-run cache reuse before a full build. A canary is not a
complete-corpus artifact and cannot satisfy an enabled site's full-input check.

The default display limit is 50,000 records selected deterministically. All
input records must have a verified cache entry; the map reports omitted display
records. No all-pairs similarity matrix is allocated.

Model weights are downloaded only by the explicit `embed` command. A cached
model can be used with `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`. There are no
provider API calls. Old unpinned vector caches are not assigned this profile.

The existing site renderer stages a validated bundle at `text-map/` only after
the repository enables it in `conf/text_map.yaml`. Its normal Python environment
runs this verification without importing Torch, NumPy or PaCMAP. The build must
fail if an enabled map is absent, stale or invalid. Preflight checks the exact
BGE model/revision, 1024 dimensions and the fleet's 512-token window. The staging
call passes the approved generation name through `expected_bundle`, rejecting
a different pointer or altered generation before changing site files.
Site deployment remains the
publication boundary. A machine interruption during directory staging may
leave `.text-map-recovery-*` beside the destination; preserve it for recovery.

The runtime has been exercised on macOS Apple Silicon. Platform-specific model
wheels may constrain where heavy builds run; the standard-library verifier is
independent of those wheels. Cross-platform reproducibility is not implied by
the lock or a fixed random seed.
