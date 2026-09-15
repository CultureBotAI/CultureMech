# CultureMech ingredient graph provenance

Graph maps retain their KG-Microbe DeepWalk features and domain matching policies. The fleet's common BGE text map is a separate view. This work follows #471 and #472.

Run `python scripts/generate_ingredient_umap.py --embeddings-path /path/to/source.tsv.gz --method pacmap` from the repository root. Supply `--name-to-chebi` and `--unified-mapping` for the optional mapping files used in that run. The default corpus is `data/normalized_yaml`; the default output is `app/ingredient_umap.html` with sibling `.points.json` and `.metadata.json` artifacts. `--method umap` is an explicit alternative and changes the visible algorithm label.

The population is unique resolved CHEBI ingredients in top-level ingredient lists. The ledger records every resolved ingredient, per-record occurrences and resolution method, minimum-occurrence exclusions and missing source vectors. Unresolved occurrences are listed separately; they are not assigned invented coordinates. Optional name-map and annotation bytes are checksummed. This receipt belongs to the ingredient view; it does not establish provenance for the separate historical media graph.

New generation reads the selected TSV or TSV.gz stream directly and hashes the exact bytes while parsing. Old basename/size/mtime pickle caches are ignored, including when `force_reload` is false. The scan is streaming and retains only required node vectors; the full source file is still read once per generation. Do not infer source identity by hashing a different file beside old coordinates.

Schema-v2 receipts bind the full corpus, matching/omission ledger, ordered reducer matrix, actual algorithm/normalization/settings and installed backend versions to checksums of every output. PaCMAP records fitted pair counts. The sfdp backend, where available, records the symmetric union-kNN construction, DOT checksum, Graphviz version and command arguments. Failed generation leaves previous outputs unchanged; publication rolls back ordinary write failures. A process kill can leave a `.graph-recovery-*` directory for recovery and is not claimed to be an atomic website deployment.

Validate a completed generation with:

```python
from pathlib import Path
from culturemech.graph_embedding_receipts import load_receipt

receipt = load_receipt(Path("path/to/projection.metadata.json"))
```

This verifies all sibling artifacts declared by the receipt. It is not a tool for attaching newly guessed provenance to legacy arrays. Full published artifacts must be regenerated from reviewed current inputs before the graph correction is considered complete.

## Deployment gate

`python scripts/check_graph_receipts.py` verifies the complete intended HTML/points/receipt sets against the current corpus before Pages publication. It rejects missing or altered artifacts, wrong output membership or reducer, invalid point identities/coordinates, and changed source YAML. This check uses only the Python standard library and reads no source graph vectors or model. The retained historical media views, where present, do not borrow these verified graph receipts.
