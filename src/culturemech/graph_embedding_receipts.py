"""Source-bound receipts for graph maps. Standard library; no legacy cache loading.

Consumers own matching, aggregation and projection. Verified generation reads
the source stream directly and stages new outputs; historical arrays cannot
acquire provenance by passing an old cache to this module.
"""

from __future__ import annotations

import gzip
import hashlib
import importlib.metadata
import io
import json
import math
import os
import re
import shutil
import struct
import tempfile
from pathlib import Path

SCHEMA_VERSION = 2


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _frame(digest, value: str) -> None:
    payload = value.encode("utf-8")
    digest.update(struct.pack(">Q", len(payload)))
    digest.update(payload)


class _HashingReader(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
        self.digest = hashlib.sha256()
        self.count = 0

    def readable(self):
        return True

    def readinto(self, buffer):
        data = self.stream.read(len(buffer))
        buffer[: len(data)] = data
        self.digest.update(data)
        self.count += len(data)
        return len(data)


class GraphSource:
    """Read selected node vectors while hashing the exact source bytes consumed.

    Exhaust the iterator before using ``receipt``. Empty selection is recorded;
    malformed selected rows, repeated IDs, inconsistent dimensions and nonfinite
    values are errors. No basename/mtime cache or pickle is consulted.
    """

    def __init__(self, path: Path, prefixes, *, node_ids=None, node_filter=None, filter_name=None):
        self.path = Path(path)
        self.prefixes = tuple(sorted({p.rstrip(":") for p in prefixes}))
        self.node_ids = None if node_ids is None else frozenset(node_ids)
        if (node_filter is None) != (filter_name is None):
            raise ValueError("a graph node filter requires an explicit policy name")
        self.node_filter = node_filter
        self.filter_name = filter_name
        self.receipt: dict | None = None
        self._started = False

    def __iter__(self):
        if self._started:
            raise ValueError("graph source reader is single-use")
        self._started = True
        seen = set()
        dimension = None
        lines = 0
        with self.path.open("rb") as raw:
            before = os.fstat(raw.fileno())
            meter = _HashingReader(raw)
            binary = (
                gzip.GzipFile(fileobj=meter, mode="rb")
                if self.path.suffix == ".gz"
                else io.BufferedReader(meter)
            )
            with io.TextIOWrapper(binary, encoding="utf-8") as stream:
                for line in stream:
                    lines += 1
                    node, separator, rest = line.rstrip("\r\n").partition("\t")
                    if not any(node.startswith(prefix + ":") for prefix in self.prefixes):
                        continue
                    if self.node_ids is not None and node not in self.node_ids:
                        continue
                    if self.node_filter is not None and not self.node_filter(node):
                        continue
                    if node in seen:
                        raise ValueError(f"duplicate selected graph node: {node}")
                    if not separator:
                        raise ValueError(f"missing vector for selected graph node: {node}")
                    try:
                        vector = [float(value) for value in rest.split("\t")]
                    except ValueError as error:
                        raise ValueError(f"malformed graph vector for {node}") from error
                    if (
                        len(vector) < 2
                        or not all(math.isfinite(v) for v in vector)
                        or not any(vector)
                    ):
                        raise ValueError(f"invalid graph vector for {node}")
                    if dimension is None:
                        dimension = len(vector)
                    if len(vector) != dimension:
                        raise ValueError(f"inconsistent graph vector dimension for {node}")
                    seen.add(node)
                    yield node, vector
            after = os.fstat(raw.fileno())
            if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
                after.st_dev,
                after.st_ino,
                after.st_size,
                after.st_mtime_ns,
            ) or meter.count != before.st_size:
                raise ValueError("graph source changed or was not completely consumed")
        self.receipt = {
            "filename": self.path.name,
            "sha256": meter.digest.hexdigest(),
            "bytes": meter.count,
            "physical_lines": lines,
            "parser": "graph-tsv-numeric-v1",
            "prefixes": list(self.prefixes),
            "selection": "prefixes" if self.node_ids is None else "explicit-node-ids",
            "filter_policy": self.filter_name,
            "requested_node_ids_sha256": (
                None
                if self.node_ids is None
                else hashlib.sha256(canonical(sorted(self.node_ids))).hexdigest()
            ),
            "selected_nodes": len(seen),
            "dimensions": dimension,
            "selected_node_ids_sha256": hashlib.sha256(canonical(sorted(seen))).hexdigest(),
            "lineage": "parsed-source-bytes",
        }


def corpus_receipt(paths, root: Path) -> dict:
    root = Path(root).resolve()
    digest = hashlib.sha256()
    entries = []
    for path in sorted(Path(p) for p in paths):
        if path.is_symlink():
            raise ValueError(f"corpus symlink refused: {path}")
        relative = path.resolve().relative_to(root).as_posix()
        checksum = file_sha256(path)
        _frame(digest, relative)
        _frame(digest, checksum)
        entries.append({"path": relative, "sha256": checksum})
    if not entries or len({e["path"] for e in entries}) != len(entries):
        raise ValueError("corpus must contain unique input files")
    return {"count": len(entries), "sha256": digest.hexdigest(), "files": entries}


def matrix_receipt(rows, identifiers, *, dtype="float32-le") -> dict:
    formats = {"float32-le": "f", "float64-le": "d"}
    if dtype not in formats:
        raise ValueError("unsupported graph vector storage dtype")
    ids = list(identifiers)
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate projected record identity")
    digest = hashlib.sha256()
    dimension = None
    count = 0
    for identifier, row in zip(ids, rows, strict=True):
        count += 1
        if not isinstance(identifier, str) or not identifier:
            raise ValueError("projected record identity must be nonempty")
        values = [float(v) for v in row]
        if len(values) < 2 or not all(math.isfinite(v) for v in values) or not any(values):
            raise ValueError("projected vectors must be finite and nonzero")
        dimension = len(values) if dimension is None else dimension
        if len(values) != dimension:
            raise ValueError("projected vectors have inconsistent dimensions")
        digest.update(struct.pack("<" + formats[dtype] * dimension, *values))
    if count < 1:
        raise ValueError("projection requires at least one graph vector")
    return {
        "sha256": digest.hexdigest(),
        "shape": [count, dimension],
        "dtype": dtype,
        "row_ids": ids,
        "row_ids_sha256": hashlib.sha256(canonical(ids)).hexdigest(),
    }


def software_versions(*names) -> dict:
    return {name: importlib.metadata.version(name) for name in names}


def projection_receipt(
    method, parameters, *, normalization, initialization=None, reducer=None, graph=None
) -> dict:
    if method not in {"pacmap", "umap", "sfdp"}:
        raise ValueError(f"unknown projection method: {method}")
    result = {
        "method": method,
        "parameters": parameters,
        "normalization": normalization,
        "initialization": initialization,
    }
    if method == "pacmap":
        result.update(
            implementation="pacmap.PaCMAP",
            effective_pairs={
                "neighbors": int(reducer.n_neighbors),
                "mid_near": int(reducer.n_MN),
                "further": int(reducer.n_FP),
            },
            library_versions=software_versions(
                "pacmap", "numpy", "numba", "scikit-learn", "faiss-cpu"
            ),
        )
    elif method == "umap":
        result.update(
            implementation="umap.UMAP",
            effective_neighbors=int(reducer._n_neighbors),
            library_versions=software_versions("umap-learn", "numpy", "numba", "scikit-learn"),
        )
    else:
        if not graph:
            raise ValueError("sfdp requires actual graph/backend provenance")
        result.update(
            implementation="graphviz.sfdp",
            graph=graph,
            library_versions=software_versions("numpy", "scikit-learn"),
        )
    canonical(result)
    return result


def make_receipt(*, source, corpus, ledger, matrix, projection, coverage, auxiliary=None):
    if not source or source.get("lineage") != "parsed-source-bytes":
        raise ValueError("graph provenance requires a freshly parsed source receipt")
    if (
        coverage.get("projected") != matrix["shape"][0]
        or coverage.get("eligible", 0) < coverage["projected"]
    ):
        raise ValueError("graph coverage is inconsistent with projected vectors")
    result = {
        "schema_version": SCHEMA_VERSION,
        "embedding_family": "kg_microbe_deepwalk",
        "source": source,
        "corpus": corpus,
        "auxiliary_inputs": auxiliary or {},
        "matching": {"sha256": hashlib.sha256(canonical(ledger)).hexdigest(), "rows": ledger},
        "matrix": matrix,
        "input_dimensions": matrix["shape"][1],
        "projection": projection,
        "coverage": coverage,
    }
    _validate_core(result)
    return result


def _validate_core(receipt):
    def checksum(value):
        return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value)

    source, matrix = receipt["source"], receipt["matrix"]
    corpus, matching, projection = receipt["corpus"], receipt["matching"], receipt["projection"]
    if (
        receipt.get("schema_version") != SCHEMA_VERSION
        or receipt.get("embedding_family") != "kg_microbe_deepwalk"
        or source.get("lineage") != "parsed-source-bytes"
        or not checksum(source.get("sha256"))
        or type(source.get("bytes")) is not int
        or source["bytes"] < 1
        or not isinstance(source.get("filename"), str)
        or not source["filename"]
        or not checksum(corpus.get("sha256"))
        or type(corpus.get("count")) is not int
        or corpus["count"] < 1
        or corpus.get("count") != len(corpus.get("files", []))
    ):
        raise ValueError("invalid graph source or corpus receipt")
    corpus_digest = hashlib.sha256()
    corpus_paths = []
    for entry in corpus["files"]:
        name = entry.get("path")
        if (
            not isinstance(name, str)
            or not name
            or Path(name).is_absolute()
            or ".." in Path(name).parts
            or not checksum(entry.get("sha256"))
        ):
            raise ValueError("invalid graph corpus input identity")
        corpus_paths.append(name)
        _frame(corpus_digest, name)
        _frame(corpus_digest, entry["sha256"])
    if len(set(corpus_paths)) != len(corpus_paths) or corpus_digest.hexdigest() != corpus["sha256"]:
        raise ValueError("graph corpus ledger checksum mismatch")
    shape = matrix.get("shape")
    ids = matrix.get("row_ids")
    if (
        not isinstance(shape, list)
        or len(shape) != 2
        or any(type(size) is not int for size in shape)
        or shape[0] < 1
        or shape[1] < 2
        or not isinstance(ids, list)
        or len(ids) != shape[0]
        or any(not isinstance(identifier, str) or not identifier for identifier in ids)
        or len(set(ids)) != len(ids)
        or not checksum(matrix.get("sha256"))
        or matrix.get("dtype") not in {"float32-le", "float64-le"}
        or hashlib.sha256(canonical(ids)).hexdigest() != matrix.get("row_ids_sha256")
        or receipt.get("input_dimensions") != shape[1]
    ):
        raise ValueError("invalid ordered graph matrix receipt")
    rows = matching.get("rows")
    if (
        not isinstance(rows, list)
        or hashlib.sha256(canonical(rows)).hexdigest() != matching.get("sha256")
        or any(
            not isinstance(row, dict)
            or not isinstance(row.get("identifier"), str)
            or not row["identifier"]
            or not isinstance(row.get("source_nodes"), list)
            or any(not isinstance(node, str) or not node for node in row["source_nodes"])
            or not isinstance(row.get("status"), str)
            or (row["status"] == "projected" and not row["source_nodes"])
            for row in rows
        )
        or len({row["identifier"] for row in rows}) != len(rows)
        or {row["identifier"] for row in rows if row["status"] == "projected"} != set(ids)
    ):
        raise ValueError("invalid graph matching ledger")
    coverage = receipt["coverage"]
    if (
        type(coverage.get("projected")) is not int
        or coverage["projected"] != shape[0]
        or type(coverage.get("eligible")) is not int
        or coverage["eligible"] < shape[0]
        or coverage["eligible"] != len(rows)
        or projection.get("method") not in {"pacmap", "umap", "sfdp"}
        or not isinstance(projection.get("parameters"), dict)
        or projection.get("normalization") not in {"l2", "none"}
        or not isinstance(projection.get("library_versions"), dict)
        or not projection["library_versions"]
        or any(
            not isinstance(version, str) or not version
            for version in projection["library_versions"].values()
        )
    ):
        raise ValueError("invalid graph coverage or reducer provenance")
    method = projection["method"]
    if method == "pacmap":
        pairs = projection.get("effective_pairs", {})
        if (
            projection.get("implementation") != "pacmap.PaCMAP"
            or set(pairs) != {"neighbors", "mid_near", "further"}
            or any(type(count) is not int or count < 0 for count in pairs.values())
            or pairs["neighbors"] < 1
            or pairs["further"] < 1
        ):
            raise ValueError("invalid effective PaCMAP reducer provenance")
    elif method == "umap":
        if (
            projection.get("implementation") != "umap.UMAP"
            or type(projection.get("effective_neighbors")) is not int
            or projection["effective_neighbors"] < 1
        ):
            raise ValueError("invalid effective UMAP reducer provenance")
    else:
        graph = projection.get("graph", {})
        if (
            projection.get("implementation") != "graphviz.sfdp"
            or graph.get("construction") != "symmetric_union_knn"
            or not checksum(graph.get("dot_sha256"))
            or not graph.get("graphviz_version")
            or not graph.get("arguments")
            or type(graph.get("effective_k")) is not int
            or graph["effective_k"] < 1
            or type(graph.get("edges")) is not int
            or graph["edges"] < 1
        ):
            raise ValueError("invalid actual sfdp graph provenance")
    canonical(receipt)


def validate_receipt(receipt, files: dict[str, Path]) -> None:
    if receipt.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported graph receipt schema")
    _validate_core(receipt)
    if receipt["source"].get("lineage") != "parsed-source-bytes":
        raise ValueError("unverified graph source lineage")
    if set(receipt.get("outputs", {})) != set(files):
        raise ValueError("graph output set differs from the receipt")
    if (
        hashlib.sha256(canonical(receipt["matching"]["rows"])).hexdigest()
        != receipt["matching"]["sha256"]
    ):
        raise ValueError("graph matching receipt checksum mismatch")
    for name, path in files.items():
        if Path(path).is_symlink() or file_sha256(path) != receipt["outputs"][name]:
            raise ValueError(f"graph output checksum mismatch: {name}")


def load_receipt(path: Path) -> dict:
    path = Path(path)
    if path.is_symlink():
        raise ValueError("symlinked graph receipt refused")
    receipt = json.loads(path.read_text())
    if not isinstance(receipt, dict):
        raise ValueError("graph receipt must be a JSON object")
    names = receipt.get("outputs", {})
    if (
        not isinstance(names, dict)
        or not names
        or any(not isinstance(name, str) or not name or Path(name).name != name for name in names)
    ):
        raise ValueError("graph receipt outputs must name sibling artifacts")
    validate_receipt(receipt, {name: path.parent / name for name in names})
    return receipt


def publish_artifacts(staged: dict[Path, Path], receipt_path: Path, receipt: dict) -> dict:
    """Promote generated files and their receipt, restoring originals on errors.

    Caller owns the repository lock. Receipts are promoted last. A process kill
    may leave a recovery directory; retain it instead of claiming atomic live
    serving. All artifacts must have distinct basenames for unambiguous checks.
    """
    receipt_path = Path(receipt_path)
    destinations = [Path(path) for path in staged]
    if (
        not destinations
        or receipt_path.is_symlink()
        or len({p.name for p in destinations}) != len(destinations)
        or any(p.parent.resolve() != receipt_path.parent.resolve() for p in destinations)
        or receipt_path.resolve() in {path.resolve() for path in destinations}
        or any(p.is_symlink() for p in destinations)
    ):
        raise ValueError("graph artifacts must have distinct, non-symlinked sibling destinations")
    metadata = {
        **receipt,
        "outputs": {target.name: file_sha256(origin) for target, origin in staged.items()},
    }
    validate_receipt(metadata, {target.name: origin for target, origin in staged.items()})
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    recovery = Path(tempfile.mkdtemp(prefix=".graph-recovery-", dir=receipt_path.parent))
    changes = []
    success = False
    try:
        receipt_stage = recovery / "new-receipt.json"
        receipt_stage.write_bytes(canonical(metadata) + b"\n")
        for index, (target, origin) in enumerate([*staged.items(), (receipt_path, receipt_stage)]):
            target = Path(target)
            target.parent.mkdir(parents=True, exist_ok=True)
            backup = recovery / f"previous-{index}"
            existed = target.exists()
            if existed:
                shutil.copyfile(target, backup)
            changes.append((target, backup if existed else None))
            # Stage in each destination filesystem before atomic replacement.
            fd, temporary_name = tempfile.mkstemp(prefix=".graph-publish-", dir=target.parent)
            os.close(fd)
            temporary = Path(temporary_name)
            try:
                shutil.copyfile(origin, temporary)
                expected = (
                    file_sha256(receipt_stage)
                    if target == receipt_path
                    else metadata["outputs"][target.name]
                )
                if file_sha256(temporary) != expected:
                    raise ValueError(
                        f"staged graph artifact changed during publication: {target.name}"
                    )
                os.replace(temporary, target)
            finally:
                temporary.unlink(missing_ok=True)
        success = True
    except BaseException:
        for target, previous_path in reversed(changes):
            if previous_path is None:
                target.unlink(missing_ok=True)
            else:
                os.replace(previous_path, target)
        raise
    finally:
        if success or not any(recovery.glob("previous-*")):
            shutil.rmtree(recovery)
    return metadata
