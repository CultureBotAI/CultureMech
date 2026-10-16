#!/usr/bin/env python3
"""Project CultureMech text embeddings to 2D (PaCMAP + PCA) and render app/text_map.html."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_NPZ = REPO_ROOT / "data" / "embeddings" / "records.npz"
DEFAULT_JSON = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"
DEFAULT_HTML = REPO_ROOT / "app" / "text_map.html"
TEMPLATES_DIR = REPO_ROOT / "src" / "culturemech" / "templates"


def _pca_2d(vectors: np.ndarray) -> np.ndarray:
    centered = vectors - vectors.mean(axis=0, keepdims=True)
    if centered.shape[0] < 2:
        return np.zeros((centered.shape[0], 2), dtype=np.float32)
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    coords = centered @ vt[:2].T
    return coords.astype(np.float32)


def _pacmap_2d(vectors: np.ndarray, random_state: int = 42) -> np.ndarray:
    n = vectors.shape[0]
    if n < 4:
        return _pca_2d(vectors)
    try:
        import pacmap

        n_neighbors = min(15, max(2, n - 1))
        reducer = pacmap.PaCMAP(
            n_components=2,
            n_neighbors=n_neighbors,
            MN_ratio=0.5,
            FP_ratio=2.0,
            random_state=random_state,
             apply_pca=vectors.shape[1] > 100,
        )
        coords = reducer.fit_transform(vectors)
        return np.asarray(coords, dtype=np.float32)
    except Exception:
        return _pca_2d(vectors)


def build_corpus_map(
    npz_path: Path = DEFAULT_NPZ,
    output_json: Path = DEFAULT_JSON,
    output_html: Path = DEFAULT_HTML,
    random_state: int = 42,
) -> dict[str, Any]:
    if not npz_path.exists():
        raise FileNotFoundError(
            f"Embeddings archive not found at {npz_path}. Run scripts/embed_records.py first."
        )

    archive = np.load(npz_path, allow_pickle=False)
    vectors = np.asarray(archive["embeddings"], dtype=np.float32)
    ids = [str(x) for x in archive["ids"].tolist()]
    titles = [str(x) for x in archive["titles"].tolist()]
    urls = [str(x) for x in archive["urls"].tolist()]
    facets_raw = [json.loads(str(x)) for x in archive["facets_json"].tolist()]
    model_name = str(archive["model_name"])

    print(f"Projecting {len(ids):,} records ({vectors.shape[1]}d) with PaCMAP + PCA...")
    coords_pacmap = _pacmap_2d(vectors, random_state=random_state)
    coords_pca = _pca_2d(vectors)

    records = []
    for i, rec_id in enumerate(ids):
        records.append(
            {
                "id": rec_id,
                "title": titles[i],
                "url": urls[i],
                "x": round(float(coords_pacmap[i, 0]), 4),
                "y": round(float(coords_pacmap[i, 1]), 4),
                "pca_x": round(float(coords_pca[i, 0]), 4),
                "pca_y": round(float(coords_pca[i, 1]), 4),
                "facets": facets_raw[i],
            }
        )

    payload: dict[str, Any] = {
        "repo": "CultureMech",
        "model": model_name,
        "method": "PaCMAP",
        "dim": int(vectors.shape[1]),
        "count": len(records),
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "records": records,
    }

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records):,} records to {output_json}")

    if TEMPLATES_DIR.exists() and (TEMPLATES_DIR / "text_map.html").exists():
        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=select_autoescape(["html"]),
        )
        template = env.get_template("text_map.html")
        html = template.render(corpus_map_json=json.dumps(payload).replace("</", "<\\/"))
        output_html.parent.mkdir(parents=True, exist_ok=True)
        output_html.write_text(html, encoding="utf-8")
        print(f"Rendered interactive text map: {output_html}")

    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Build 2D corpus map JSON from records.npz.")
    parser.add_argument("--input", type=Path, default=DEFAULT_NPZ)
    parser.add_argument("--output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    build_corpus_map(args.input, args.output, args.html, args.seed)


if __name__ == "__main__":
    main()
