#!/usr/bin/env python3
"""Build provenance-bound semantic-text maps from a Mech's JSONL adapter.

Inspection and verification use the standard library. Model inference and
projection are explicit operations with separately installed dependencies.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import heapq
import importlib.metadata
import json
import math
import os
import re
import shutil
import sqlite3
import struct
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

FORMAT_VERSION = 1
MODEL = "BAAI/bge-large-en-v1.5"
MODEL_REVISION = "d4aa6901d3a41ba39fb536a557fa166f842b0e09"
MODEL_DIMENSION = 1024
MAX_SEQ_LENGTH = 512
REQUIRED_FIELDS = (
    "identifier",
    "label",
    "category",
    "page",
    "source_path",
    "text",
    "text_sha256",
    "adapter_version",
)


class ContractError(ValueError):
    """Malformed input or an unverified artifact; never a successful map."""


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def framed_update(digest, *values: str) -> None:
    for value in values:
        encoded = value.encode("utf-8")
        digest.update(struct.pack(">Q", len(encoded)))
        digest.update(encoded)


def local_link(value: str) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlsplit(value)
    decoded = unquote(parsed.path)
    return bool(value) and not (
        parsed.scheme
        or parsed.netloc
        or decoded.startswith("/")
        or "\\" in decoded
        or ".." in decoded.split("/")
        or any(ord(char) < 32 for char in unquote(value))
    )


def records(path: Path, *, raw_digest=None):
    """Read one adapter record at a time; no YAML or biological policy here."""
    with path.open("rb") as stream:
        for number, line in enumerate(stream, 1):
            if raw_digest is not None:
                raw_digest.update(line)
            try:
                record = json.loads(line.decode("utf-8"))
            except (ValueError, UnicodeError) as exc:
                raise ContractError(f"invalid JSONL record at line {number}") from exc
            if not isinstance(record, dict) or any(
                not isinstance(record.get(key), str) or not record[key].strip()
                for key in REQUIRED_FIELDS
            ):
                raise ContractError(f"line {number}: required fields must be nonempty strings")
            if not local_link(record["page"]) or not local_link(record["source_path"]):
                raise ContractError(f"line {number}: page and source paths must be local")
            if record["text_sha256"] != hashlib.sha256(record["text"].encode()).hexdigest():
                raise ContractError(f"line {number}: text checksum mismatch")
            yield record


def inspect_inputs(path: Path) -> dict:
    """Validate full ordered inputs, using disk for duplicate detection."""
    content = hashlib.sha256()
    display = hashlib.sha256()
    raw = hashlib.sha256()
    counts: dict[str, int] = {}
    versions: set[str] = set()
    count = 0
    with (
        tempfile.TemporaryDirectory(prefix="embedding-inputs-") as tmp,
        sqlite3.connect(str(Path(tmp) / "ids.sqlite")) as db,
    ):
        db.execute("CREATE TABLE ids (id TEXT PRIMARY KEY)")
        for record in records(path, raw_digest=raw):
            try:
                db.execute("INSERT INTO ids VALUES (?)", (record["identifier"],))
            except sqlite3.IntegrityError as exc:
                raise ContractError(f"duplicate identifier: {record['identifier']}") from exc
            framed_update(content, record["identifier"], record["text"])
            framed_update(display, canonical(record).decode())
            counts[record["category"]] = counts.get(record["category"], 0) + 1
            versions.add(record["adapter_version"])
            count += 1
    if not count:
        raise ContractError("adapter input contains no records")
    if len(versions) != 1:
        raise ContractError("adapter versions must agree within one input")
    if digest_file(path) != raw.hexdigest():
        raise ContractError("adapter input changed while inspecting; rerun")
    return {
        "count": count,
        "corpus_sha256": content.hexdigest(),
        "records_sha256": display.hexdigest(),
        "input_sha256": raw.hexdigest(),
        "categories": counts,
        "adapter_version": versions.pop(),
    }


def encoder_profile(*, library_versions: dict | None = None, device: str = "cpu") -> dict:
    return {
        "format_version": FORMAT_VERSION,
        "model": MODEL,
        "revision": MODEL_REVISION,
        "dimension": MODEL_DIMENSION,
        "normalized": True,
        "dtype": "float32-le",
        "max_seq_length": MAX_SEQ_LENGTH,
        "pooling": "sentence-transformers-model",
        "truncation": "tail",
        "inference_device": device,
        "weight_dtype": "torch.float32",
        "query_instruction": None,
        "library_versions": library_versions or {},
    }


def validate_profile(profile: dict) -> None:
    if not isinstance(profile, dict) or not re.fullmatch(
        r"[0-9a-f]{40}", str(profile.get("revision", ""))
    ):
        raise ContractError("encoder profile must identify an immutable model revision")
    if (
        type(profile.get("format_version")) is not int
        or profile["format_version"] != FORMAT_VERSION
        or not isinstance(profile.get("model"), str)
        or not profile["model"]
        or type(profile.get("dimension")) is not int
        or profile["dimension"] < 2
        or profile.get("normalized") is not True
        or profile.get("dtype") != "float32-le"
        or type(profile.get("max_seq_length")) is not int
        or profile["max_seq_length"] < 1
        or profile.get("pooling") != "sentence-transformers-model"
        or profile.get("truncation") != "tail"
        or not re.fullmatch(
            r"cpu|mps(?::\d+)?|cuda(?::\d+)?", str(profile.get("inference_device", ""))
        )
        or profile.get("weight_dtype") != "torch.float32"
        or "query_instruction" not in profile
        or profile["query_instruction"] is not None
    ):
        raise ContractError("invalid encoder profile")
    validate_versions(profile.get("library_versions"), "encoder")
    canonical(profile)


def validate_versions(value, context: str) -> None:
    if (
        not isinstance(value, dict)
        or not value
        or any(
            not isinstance(name, str)
            or not name.strip()
            or not isinstance(version, str)
            or not version.strip()
            for name, version in value.items()
        )
    ):
        raise ContractError(f"{context} requires recorded software versions")


def profile_id(profile: dict) -> str:
    validate_profile(profile)
    return hashlib.sha256(canonical(profile)).hexdigest()


def vector_bytes(vector, dimension: int) -> bytes:
    values = [float(value) for value in vector]
    if len(values) != dimension or not all(math.isfinite(value) for value in values):
        raise ContractError("vector dimension or finiteness check failed")
    norm = math.sqrt(sum(value * value for value in values))
    if not 0.999 <= norm <= 1.001:
        raise ContractError("embedding vector must have unit norm")
    return struct.pack("<" + "f" * dimension, *values)


def unpack_vector(blob: bytes, dimension: int):
    if len(blob) != dimension * 4:
        raise ContractError("cached vector byte length does not match its dimension")
    values = struct.unpack("<" + "f" * dimension, blob)
    vector_bytes(values, dimension)
    return values


@contextlib.contextmanager
def cache_connection(path: Path, *, writable: bool = False):
    if writable:
        path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(path, timeout=30)
        connection.execute("PRAGMA synchronous=FULL")
        connection.execute("CREATE TABLE IF NOT EXISTS profiles (id TEXT PRIMARY KEY, json TEXT)")
        connection.execute("""CREATE TABLE IF NOT EXISTS vectors (
            profile TEXT, identifier TEXT, text_sha256 TEXT, vector BLOB, vector_sha256 TEXT,
            PRIMARY KEY (profile, identifier, text_sha256))""")
    else:
        connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        yield connection
    finally:
        connection.close()


def cached_vector(db, key: str, record: dict, dimension: int):
    row = db.execute(
        "SELECT vector, vector_sha256 FROM vectors "
        "WHERE profile=? AND identifier=? AND text_sha256=?",
        (key, record["identifier"], record["text_sha256"]),
    ).fetchone()
    if row is None:
        return None
    blob, checksum = row
    if hashlib.sha256(blob).hexdigest() != checksum:
        raise ContractError("cached vector checksum mismatch")
    unpack_vector(blob, dimension)
    return blob


def populate_cache(
    input_path: Path, cache_path: Path, profile: dict, encoder, *, batch_size: int = 64
) -> dict:
    """Reuse exact records and atomically commit each verified encoded batch."""
    if batch_size < 1:
        raise ContractError("batch size must be positive")
    identity = inspect_inputs(input_path)
    key = profile_id(profile)
    encoded_count = reused = 0
    pending = []
    with cache_connection(cache_path, writable=True) as db:
        previous = db.execute("SELECT json FROM profiles WHERE id=?", (key,)).fetchone()
        if previous is not None and previous[0] != canonical(profile).decode():
            raise ContractError("cache profile metadata is inconsistent with its identity")

        def save_batch():
            nonlocal encoded_count
            vectors = encoder([record["text"] for record in pending])
            if len(vectors) != len(pending):
                raise ContractError("encoder returned the wrong number of vectors")
            # Validate the WHOLE batch before starting its transaction.
            blobs = [vector_bytes(vector, profile["dimension"]) for vector in vectors]
            with db:
                db.execute(
                    "INSERT OR IGNORE INTO profiles VALUES (?, ?)",
                    (key, canonical(profile).decode()),
                )
                for record, blob in zip(pending, blobs, strict=True):
                    db.execute(
                        "INSERT OR REPLACE INTO vectors VALUES (?, ?, ?, ?, ?)",
                        (
                            key,
                            record["identifier"],
                            record["text_sha256"],
                            blob,
                            hashlib.sha256(blob).hexdigest(),
                        ),
                    )
            encoded_count += len(pending)
            pending.clear()

        for record in records(input_path):
            if cached_vector(db, key, record, profile["dimension"]) is not None:
                reused += 1
            else:
                pending.append(record)
                if len(pending) == batch_size:
                    save_batch()
        if pending:
            save_batch()
    if digest_file(input_path) != identity["input_sha256"]:
        raise ContractError("adapter input changed while embedding; rerun")
    return {**identity, "profile_id": key, "encoded": encoded_count, "reused": reused}


def versions(names: tuple[str, ...]) -> dict[str, str]:
    return {name: importlib.metadata.version(name) for name in names}


def local_encoder(device: str | None = None):
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(
        MODEL, revision=MODEL_REVISION, trust_remote_code=False, device=device
    )
    model.max_seq_length = MAX_SEQ_LENGTH
    model.tokenizer.truncation_side = "right"
    profile = encoder_profile(
        library_versions=versions(
            ("sentence-transformers", "transformers", "tokenizers", "torch", "numpy")
        ),
        device=str(model.device),
    )
    if str(next(model.parameters()).dtype) != profile["weight_dtype"]:
        raise ContractError("model weights must use the declared float32 precision")
    if model.get_sentence_embedding_dimension() != MODEL_DIMENSION:
        raise ContractError("model returned an unexpected embedding dimension")

    def encode(texts):
        return model.encode(
            texts,
            batch_size=len(texts),
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

    return profile, encode


def select_records(input_path: Path, maximum: int, seed: int) -> list[dict]:
    if maximum < 3:
        raise ContractError("map selection maximum must be at least three")

    # Bottom-k hashes are deterministic, bounded and independent of input order.
    def ranked():
        for record in records(input_path):
            key = hashlib.sha256(canonical([seed, record["identifier"]])).digest()
            yield key, record["identifier"], record

    return [record for _, _, record in heapq.nsmallest(maximum, ranked())]


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, filename = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    temporary = Path(filename)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(canonical(value) + b"\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def manifest_identity(manifest: dict) -> str:
    return hashlib.sha256(canonical(manifest)).hexdigest()


def build_map(
    input_path: Path,
    cache_path: Path,
    output: Path,
    profile: dict,
    *,
    maximum: int = 50000,
    seed: int = 42,
    neighbors: int = 15,
    projector=None,
    projection_versions: dict | None = None,
    title: str = "Semantic text map",
) -> dict:
    import numpy as np

    inputs = inspect_inputs(input_path)
    key = profile_id(profile)
    selected = select_records(input_path, maximum, seed)
    if len(selected) < 3:
        raise ContractError("PaCMAP map requires at least three input records")
    if neighbors < 1:
        raise ContractError("neighbors must be positive")
    neighbor_count = min(neighbors, len(selected) - 1)
    matrix = np.empty((len(selected), profile["dimension"]), dtype="<f4")
    with cache_connection(cache_path) as db:
        profile_row = db.execute("SELECT json FROM profiles WHERE id=?", (key,)).fetchone()
        if profile_row is None or profile_row[0] != canonical(profile).decode():
            raise ContractError("cache does not contain the exact encoder profile")
        # All rows must be cached, including those not displayed in this projection.
        for record in records(input_path):
            if cached_vector(db, key, record, profile["dimension"]) is None:
                raise ContractError(f"missing verified embedding: {record['identifier']}")
        for index, record in enumerate(selected):
            blob = cached_vector(db, key, record, profile["dimension"])
            matrix[index] = np.frombuffer(blob, dtype="<f4")
    vector_checksum = hashlib.sha256(memoryview(matrix)).hexdigest()
    projection_details = {"implementation": "injected-projector", "effective_pairs": None}
    if projector is None:
        import pacmap

        projection_versions = versions(("pacmap", "numpy", "numba", "scikit-learn", "faiss-cpu"))
        reducer = pacmap.PaCMAP(
            n_components=2,
            n_neighbors=neighbor_count,
            MN_ratio=0.5,
            FP_ratio=2.0,
            random_state=seed,
            distance="euclidean",
            lr=1.0,
            num_iters=(100, 100, 250),
            apply_pca=True,
            knn_backend="faiss",
        )
        coordinates = reducer.fit_transform(matrix, init="pca")
        neighbor_count = int(reducer.n_neighbors)
        projection_details = {
            "implementation": "pacmap.PaCMAP",
            "effective_pairs": {
                "neighbors": neighbor_count,
                "mid_near": int(reducer.n_MN),
                "further": int(reducer.n_FP),
            },
        }
    else:
        coordinates = projector(matrix, seed=seed, neighbors=neighbor_count)
    coordinates = np.asarray(coordinates, dtype=np.float64)
    if coordinates.shape != (len(selected), 2) or not np.isfinite(coordinates).all():
        raise ContractError("projector returned invalid coordinates")
    if digest_file(input_path) != inputs["input_sha256"]:
        raise ContractError("adapter input changed while projecting; rerun")
    output.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".building-", dir=output))
    try:
        map_rows = []
        for record, xy in zip(selected, coordinates, strict=True):
            map_rows.append(
                {name: record[name] for name in REQUIRED_FIELDS if name != "text"}
                | {"x": float(xy[0]), "y": float(xy[1])}
            )
        (stage / "points.json").write_bytes(canonical(map_rows) + b"\n")
        (stage / "index.html").write_text(
            render_html(title, map_rows, inputs["count"]), encoding="utf-8"
        )
        manifest = {
            "format_version": FORMAT_VERSION,
            "representation": "semantic-text",
            "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "encoder": profile,
            "encoder_profile_sha256": key,
            "inputs": inputs,
            "projection": {
                "method": "pacmap",
                "dimensions": 2,
                "seed": seed,
                "requested_neighbors": neighbors,
                "neighbors": neighbor_count,
                "MN_ratio": 0.5,
                "FP_ratio": 2.0,
                "distance": "euclidean",
                "learning_rate": 1.0,
                "iterations": [100, 100, 250],
                "apply_pca": True,
                "knn_backend": "faiss",
                "initialization": "pca",
                "library_versions": projection_versions or {},
                **projection_details,
            },
            "coverage": {
                "total": inputs["count"],
                "eligible": inputs["count"],
                "displayed": len(selected),
                "omitted": inputs["count"] - len(selected),
                "selection": "bottom-k-sha256(seed,identifier)",
                "maximum": maximum,
            },
            "source_vectors": {
                "sha256": vector_checksum,
                "shape": list(matrix.shape),
                "dtype": "float32-le",
                "order": "points.json",
                "storage": "local-profile-bound-cache",
            },
            "files": {name: digest_file(stage / name) for name in ("points.json", "index.html")},
        }
        (stage / "manifest.json").write_bytes(canonical(manifest) + b"\n")
        validate_bundle(stage, input_path=input_path)
        bundle = manifest_identity(manifest)
        destination = output / bundle
        os.rename(stage, destination)
        atomic_json(
            output / "current.json",
            {"bundle": bundle, "manifest_sha256": digest_file(destination / "manifest.json")},
        )
        return {"bundle": str(destination), "coverage": manifest["coverage"]}
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def validate_bundle(
    bundle: Path, *, input_path: Path | None = None, cache_path: Path | None = None
) -> dict:
    if bundle.is_symlink() or (bundle / "manifest.json").is_symlink():
        raise ContractError("bundle and manifest must not be symbolic links")
    manifest = json.loads((bundle / "manifest.json").read_text())
    if not isinstance(manifest, dict) or manifest.get("format_version") != FORMAT_VERSION:
        raise ContractError("unsupported map bundle format")
    if manifest.get("representation") != "semantic-text" or any(
        not isinstance(manifest.get(name), dict)
        for name in ("encoder", "inputs", "files", "coverage", "projection", "source_vectors")
    ):
        raise ContractError("invalid map bundle metadata")
    if manifest.get("encoder_profile_sha256") != profile_id(manifest["encoder"]):
        raise ContractError("encoder profile checksum mismatch")
    expected = {"points.json", "index.html"}
    if set(manifest.get("files", {})) != expected:
        raise ContractError("bundle must contain exactly the required artifact checksums")
    for filename, checksum in manifest["files"].items():
        path = bundle / filename
        if path.is_symlink() or digest_file(path) != checksum:
            raise ContractError(f"artifact checksum mismatch: {filename}")
    if input_path is not None and inspect_inputs(input_path) != manifest["inputs"]:
        raise ContractError("map is stale relative to current adapter input")
    points = json.loads((bundle / "points.json").read_text())
    if not isinstance(points, list) or len(points) < 3:
        raise ContractError("map points must contain at least three records")
    coverage = manifest["coverage"]
    projection = manifest["projection"]
    if (
        projection.get("method") != "pacmap"
        or projection.get("dimensions") != 2
        or type(projection.get("seed")) is not int
        or type(projection.get("neighbors")) is not int
        or not 1 <= projection["neighbors"] < len(points)
        or type(projection.get("requested_neighbors")) is not int
        or projection["requested_neighbors"] < 1
        or projection.get("initialization") != "pca"
        or projection.get("MN_ratio") != 0.5
        or projection.get("FP_ratio") != 2.0
        or projection.get("distance") != "euclidean"
        or projection.get("learning_rate") != 1.0
        or projection.get("iterations") != [100, 100, 250]
        or projection.get("apply_pca") is not True
        or projection.get("knn_backend") != "faiss"
    ):
        raise ContractError("invalid PaCMAP projection metadata")
    validate_versions(projection.get("library_versions"), "projection")
    if projection.get("implementation") == "pacmap.PaCMAP":
        pairs = projection.get("effective_pairs")
        if (
            not isinstance(pairs, dict)
            or any(
                type(pairs.get(name)) is not int or not 0 <= pairs[name] < len(points)
                for name in ("neighbors", "mid_near", "further")
            )
            or pairs["neighbors"] != projection["neighbors"]
            or pairs["further"] < 1
        ):
            raise ContractError("invalid effective PaCMAP pair counts")
    elif projection.get("implementation") != "injected-projector":
        raise ContractError("unidentified projection implementation")
    if (
        not isinstance(points, list)
        or len(points) < 3
        or any(
            type(coverage.get(name)) is not int
            for name in ("displayed", "eligible", "total", "omitted", "maximum")
        )
        or not 3 <= len(points) <= coverage["maximum"]
        or coverage["omitted"] < 0
        or coverage.get("selection") != "bottom-k-sha256(seed,identifier)"
    ):
        raise ContractError("invalid map selection coverage")
    source_vectors = manifest["source_vectors"]
    if (
        source_vectors.get("shape") != [len(points), manifest["encoder"]["dimension"]]
        or source_vectors.get("dtype") != "float32-le"
        or source_vectors.get("order") != "points.json"
        or source_vectors.get("storage") != "local-profile-bound-cache"
        or not re.fullmatch(r"[0-9a-f]{64}", str(source_vectors.get("sha256", "")))
    ):
        raise ContractError("invalid source vector receipt")
    for row in points:
        if (
            not isinstance(row, dict)
            or any(
                not isinstance(row.get(name), str) or not row[name].strip()
                for name in REQUIRED_FIELDS
                if name != "text"
            )
            or not local_link(row["page"])
            or not local_link(row["source_path"])
            or not re.fullmatch(r"[0-9a-f]{64}", row["text_sha256"])
            or not all(
                type(row.get(name)) in (int, float) and math.isfinite(row[name])
                for name in ("x", "y")
            )
        ):
            raise ContractError("invalid map coordinate or record metadata")
    if (
        coverage["displayed"] != len(points)
        or coverage["total"] != manifest["inputs"]["count"]
        or coverage["eligible"] != coverage["total"]
        or coverage["omitted"] != coverage["total"] - len(points)
        or len({row["identifier"] for row in points}) != len(points)
    ):
        raise ContractError("map coverage or identifiers are inconsistent")
    if input_path is not None:
        selected = select_records(input_path, coverage["maximum"], projection["seed"])
        expected = [{key: row[key] for key in REQUIRED_FIELDS if key != "text"} for row in selected]
        observed = [{key: row[key] for key in REQUIRED_FIELDS if key != "text"} for row in points]
        if observed != expected:
            raise ContractError("map records differ from the declared input selection")
    if cache_path is not None:
        digest = hashlib.sha256()
        with cache_connection(cache_path) as db:
            profile_row = db.execute(
                "SELECT json FROM profiles WHERE id=?", (manifest["encoder_profile_sha256"],)
            ).fetchone()
            if profile_row is None or profile_row[0] != canonical(manifest["encoder"]).decode():
                raise ContractError("cache does not contain the exact encoder profile")
            for row in points:
                blob = cached_vector(
                    db, manifest["encoder_profile_sha256"], row, manifest["encoder"]["dimension"]
                )
                if blob is None:
                    raise ContractError("source vector is missing from the verified cache")
                digest.update(blob)
        if digest.hexdigest() != source_vectors["sha256"]:
            raise ContractError("map source vector receipt differs from the cache")
    return manifest


def current_bundle(output: Path) -> Path:
    pointer_path = output / "current.json"
    if pointer_path.is_symlink():
        raise ContractError("active map pointer must not be a symbolic link")
    pointer = json.loads(pointer_path.read_text())
    if not re.fullmatch(r"[0-9a-f]{64}", str(pointer.get("bundle", ""))):
        raise ContractError("invalid current bundle identifier")
    bundle = output / pointer["bundle"]
    manifest_path = bundle / "manifest.json"
    if bundle.is_symlink() or manifest_path.is_symlink():
        raise ContractError("bundle and manifest must not be symbolic links")
    if digest_file(manifest_path) != pointer["manifest_sha256"]:
        raise ContractError("active manifest checksum mismatch")
    manifest = json.loads(manifest_path.read_text())
    if manifest_identity(manifest) != bundle.name:
        raise ContractError("active manifest checksum does not match its immutable generation")
    return bundle


def stage_map(
    output: Path, published_dir: Path, *, input_path: Path, expected_bundle: str | None = None
) -> dict:
    """Stage a verified map into a site build, restoring old files on exceptions.

    The caller owns the repository/build lock. The site's later deployment is
    its publication boundary; the two directory renames are not a live-server
    transaction. An interrupted machine may leave a named recovery directory.
    Policy-checking callers pass the generation name they approved at preflight;
    both the selection and its content identity must still match before writes.
    """
    source = current_bundle(output)
    if expected_bundle is not None and source.name != expected_bundle:
        raise ContractError("map generation changed after site preflight")
    manifest = validate_bundle(source, input_path=input_path)
    if manifest_identity(manifest) != source.name:
        raise ContractError("map manifest differs from its immutable generation identity")
    if manifest["projection"]["implementation"] != "pacmap.PaCMAP":
        raise ContractError("site publication requires the actual PaCMAP implementation")
    if (
        published_dir.is_symlink()
        or (published_dir.exists() and not published_dir.is_dir())
        or source.resolve().is_relative_to(published_dir.resolve())
        or published_dir.resolve().is_relative_to(output.resolve())
        or input_path.resolve().is_relative_to(published_dir.resolve())
    ):
        raise ContractError("unsafe map staging destination")
    published_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".text-map-stage-", dir=published_dir.parent))
    backup = None
    try:
        for name in ("index.html", "points.json", "manifest.json"):
            shutil.copyfile(source / name, temporary / name)
        copied = validate_bundle(temporary, input_path=input_path)
        if copied != manifest:
            raise ContractError("map source changed during site staging")
        if published_dir.exists():
            backup = Path(tempfile.mkdtemp(prefix=".text-map-recovery-", dir=published_dir.parent))
            backup.rmdir()
            os.rename(published_dir, backup)
        try:
            os.rename(temporary, published_dir)
        except BaseException:
            if backup is not None:
                os.rename(backup, published_dir)
            raise
        if backup is not None:
            shutil.rmtree(backup)
        return manifest
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def render_html(title: str, points: list[dict], total: int) -> str:
    import html

    payload = canonical(points).decode().replace("<", "\\u003c").replace("&", "\\u0026")
    # The site adapter publishes this directory at text-map/. Record pages are
    # relative to the site root, one level above this self-contained page.
    return f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>{html.escape(title)}</title>
<style>body{{font:16px system-ui;margin:2rem;color:#17252e}}canvas{{width:100%;height:55vh;
border:1px solid #bbc9cc}}a{{color:#165b80}}#detail{{min-height:3em}}
#matches{{columns:2;padding-left:1.3rem}}#matches li{{padding:.2rem;break-inside:avoid}}
@media(max-width:600px){{body{{margin:1rem}}#matches{{columns:1}}}}</style>
<h1>{html.escape(title)}</h1><p>Showing {len(points):,} of {total:,} input records.
PaCMAP positions summarize similarity between record descriptions.</p>
<label>Find a record <input id="search" type="search" placeholder="Name or identifier"></label>
<p id="detail" aria-live="polite">Select a point to open its record.</p>
<canvas id="map" aria-label="Interactive map of record descriptions" role="img"></canvas>
<p id="match-count" aria-live="polite"></p><ul id="matches" aria-label="Matching records"></ul>
<p><a href="manifest.json">Map provenance and coverage</a></p>
<script id="points" type="application/json">{payload}</script>
<script>
const rows=JSON.parse(document.getElementById('points').textContent),
c=document.getElementById('map'),ctx=c.getContext('2d'),detail=document.getElementById('detail'),
search=document.getElementById('search');
const matches=document.getElementById('matches'),matchCount=document.getElementById('match-count');
let displayed=[];
function draw(){{c.width=c.clientWidth*devicePixelRatio;c.height=c.clientHeight*devicePixelRatio;
const xs=rows.map(r=>r.x),ys=rows.map(r=>r.y),
minX=xs.reduce((a,b)=>Math.min(a,b)),maxX=xs.reduce((a,b)=>Math.max(a,b)),
minY=ys.reduce((a,b)=>Math.min(a,b)),maxY=ys.reduce((a,b)=>Math.max(a,b));
ctx.clearRect(0,0,c.width,c.height);const q=search.value.toLowerCase();displayed=[];
for(const r of rows){{const x=20+(r.x-minX)/(maxX-minX||1)*(c.width-40),
y=20+(r.y-minY)/(maxY-minY||1)*(c.height-40),hit=!q||(r.label+' '+r.identifier).toLowerCase().includes(q);
ctx.fillStyle=hit?'#16778b':'#dce4e6';ctx.beginPath();ctx.arc(x,y,hit?3:1.5,0,Math.PI*2);ctx.fill();
if(hit)displayed.push([x,y,r]);}}
matches.replaceChildren();matchCount.textContent=displayed.length.toLocaleString()+' matching records. '+
(displayed.length>20?'Showing the first 20 links; narrow the search to find a record.':'');
for(const [,,r] of displayed.slice(0,20)){{
const li=document.createElement('li'),a=document.createElement('a');
a.href='../'+r.page;a.textContent=r.label+' ('+r.identifier+')';li.append(a);matches.append(li);}}}}
c.addEventListener('click',event=>{{
const b=c.getBoundingClientRect(),x=(event.clientX-b.left)*devicePixelRatio,
y=(event.clientY-b.top)*devicePixelRatio;let nearest=null,distance=225;
for(const [px,py,r] of displayed){{const d=(x-px)**2+(y-py)**2;if(d<distance){{distance=d;nearest=r;}}}}
if(nearest){{detail.textContent='';const a=document.createElement('a');a.href='../'+nearest.page;
a.textContent=nearest.label+' ('+nearest.identifier+')';detail.append(a);}}}});
search.addEventListener('input',draw);window.addEventListener('resize',draw);draw();
</script></html>"""


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inspect_parser = sub.add_parser("inspect")
    inspect_parser.add_argument("--input", type=Path, required=True)
    embed_parser = sub.add_parser("embed")
    embed_parser.add_argument("--input", type=Path, required=True)
    embed_parser.add_argument("--cache", type=Path, required=True)
    embed_parser.add_argument("--profile-output", type=Path, required=True)
    embed_parser.add_argument("--batch-size", type=int, default=64)
    embed_parser.add_argument("--device", choices=("cpu", "mps", "cuda"))
    project_parser = sub.add_parser("project")
    for name in ("input", "cache", "profile", "output"):
        project_parser.add_argument("--" + name, type=Path, required=True)
    project_parser.add_argument("--max-points", type=int, default=50000)
    project_parser.add_argument("--seed", type=int, default=42)
    project_parser.add_argument("--neighbors", type=int, default=15)
    project_parser.add_argument("--title", default="Semantic text map")
    check_parser = sub.add_parser("check")
    check_parser.add_argument("--output", type=Path, required=True)
    check_parser.add_argument("--input", type=Path)
    check_parser.add_argument("--cache", type=Path)
    stage_parser = sub.add_parser("stage")
    stage_parser.add_argument("--output", type=Path, required=True)
    stage_parser.add_argument("--input", type=Path, required=True)
    stage_parser.add_argument("--published-dir", type=Path, required=True)
    stage_parser.add_argument("--expected-bundle")
    args = parser.parse_args(argv)
    try:
        if args.command == "inspect":
            result = inspect_inputs(args.input)
        elif args.command == "embed":
            inspect_inputs(args.input)  # fail before loading model weights
            profile, encoder = local_encoder(args.device)
            result = populate_cache(
                args.input, args.cache, profile, encoder, batch_size=args.batch_size
            )
            atomic_json(args.profile_output, profile)
        elif args.command == "project":
            profile = json.loads(args.profile.read_text())
            result = build_map(
                args.input,
                args.cache,
                args.output,
                profile,
                maximum=args.max_points,
                seed=args.seed,
                neighbors=args.neighbors,
                title=args.title,
            )
        elif args.command == "check":
            result = validate_bundle(
                current_bundle(args.output), input_path=args.input, cache_path=args.cache
            )
        else:
            result = stage_map(
                args.output,
                args.published_dir,
                input_path=args.input,
                expected_bundle=args.expected_bundle,
            )
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (
        ContractError,
        OSError,
        ValueError,
        KeyError,
        sqlite3.Error,
        importlib.metadata.PackageNotFoundError,
    ) as exc:
        print(f"embedding-pipeline: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
