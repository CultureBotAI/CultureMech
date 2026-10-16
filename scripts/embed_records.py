#!/usr/bin/env python3
"""Generate dense text embeddings for CultureMech media recipes.

Reads curated YAML files from data/merge_yaml/merged/ (or --input-dir), serializes
each recipe's name, category, medium type, physical state, ingredients, solutions,
target organisms, applications, and notes into a structured text passage, and encodes
with BAAI/bge-small-en-v1.5 into data/embeddings/records.npz.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import yaml

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

MODEL_NAME = "BAAI/bge-small-en-v1.5"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_YAML_DIR = REPO_ROOT / "data" / "merge_yaml" / "merged"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "embeddings" / "records.npz"


def _infer_source_db(data: dict[str, Any]) -> str:
    media_term = data.get("media_term")
    if isinstance(media_term, dict):
        term = media_term.get("term")
        if isinstance(term, dict) and term.get("id"):
            tid = str(term["id"])
            if ":" in tid:
                prefix = tid.split(":", 1)[0]
                if prefix == "mediadive.medium":
                    suffix = tid.split(":", 1)[1]
                    if suffix.startswith("J"):
                        return "JCM"
                    if suffix.startswith("D") or suffix.isdigit():
                        return "DSMZ"
                    return "MediaDive"
                return prefix
    for entry in data.get("curation_history") or []:
        if isinstance(entry, dict):
            curator = str(entry.get("curator") or "").lower()
            for tag, label in (
                ("dsmz", "DSMZ"),
                ("jcm", "JCM"),
                ("atcc", "ATCC"),
                ("nbrc", "NBRC"),
                ("utex", "UTEX"),
                ("ccap", "CCAP"),
                ("sag", "SAG"),
                ("togo", "TOGO"),
                ("komodo", "KOMODO"),
                ("mediadive", "MediaDive"),
            ):
                if tag in curator:
                    return label
    return "Other"


def extract_record(yaml_path: Path) -> dict[str, Any] | None:
    """Extract text passage and facet metadata from a CultureMech YAML file."""
    try:
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f, Loader=SafeLoader)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None

    record_id = str(data.get("id") or yaml_path.stem).strip()
    snake_name = str(data.get("name") or yaml_path.stem).strip()
    media_term = data.get("media_term") if isinstance(data.get("media_term"), dict) else {}
    display_name = (
        str(data.get("original_name") or media_term.get("preferred_term") or snake_name)
        .strip()
    )
    category = str(data.get("category") or yaml_path.parent.name or "unknown").lower()
    medium_type = str(
        data.get("medium_type") or data.get("composition_type") or "unknown"
    ).lower()
    physical_state = str(data.get("physical_state") or "unknown").lower()
    source_db = _infer_source_db(data)

    ingredients: list[str] = []
    roles: set[str] = set()
    for ing in data.get("ingredients") or []:
        if not isinstance(ing, dict):
            continue
        pt = str(ing.get("preferred_term") or "").strip()
        if pt:
            ingredients.append(pt)
        for r in ing.get("nutritional_roles") or []:
            if r:
                roles.add(str(r))
        for r in ing.get("physicochemical_roles") or []:
            if r:
                roles.add(str(r))

    solutions: list[str] = []
    for sol in data.get("solutions") or []:
        if not isinstance(sol, dict):
            continue
        pt = str(sol.get("preferred_term") or "").strip()
        if pt:
            solutions.append(pt)

    organisms: list[str] = []
    for org in (data.get("target_organisms") or data.get("organisms") or []):
        if isinstance(org, dict):
            pt = str(org.get("preferred_term") or org.get("scientific_name") or "").strip()
            if pt:
                organisms.append(pt)
        elif isinstance(org, str) and org.strip():
            organisms.append(org.strip())

    applications = [
        str(app).strip()
        for app in (data.get("applications") or [])
        if str(app).strip()
    ]
    description = str(data.get("description") or "").strip()
    notes = str(data.get("notes") or "").strip()

    lines = [f"Title: {display_name} ({snake_name}) [{record_id}]"]
    lines.append(
        f"Category: {category} | Type: {medium_type} | State: {physical_state} | Source: {source_db}"
    )
    if description:
        lines.append(f"Description: {description}")
    if notes and notes != description:
        lines.append(f"Notes: {notes[:300]}")
    if ingredients:
        lines.append("Ingredients: " + ", ".join(ingredients[:40]))
    if solutions:
        lines.append("Solutions: " + ", ".join(solutions[:20]))
    if organisms:
        lines.append("Target organisms: " + ", ".join(organisms[:20]))
    if applications:
        lines.append("Applications: " + ", ".join(applications[:10]))
    if roles:
        lines.append("Nutritional roles: " + ", ".join(sorted(roles)))

    passage = "\n".join(lines)
    text_hash = hashlib.sha256(passage.encode("utf-8")).hexdigest()[:16]

    if record_id.startswith("CultureMech:"):
        num_part = record_id.split(":", 1)[1]
        url = f"../pages/normalized/{num_part}.html"
    else:
        url = f"../pages/{yaml_path.stem}.html"

    summary = description or (
        f"{category.capitalize()} {medium_type} medium ({physical_state}) with "
        f"{len(ingredients)} ingredients"
    )

    facets = {
        "category": category,
        "medium_type": medium_type,
        "physical_state": physical_state,
        "source_database": source_db,
        "num_ingredients": len(ingredients),
        "num_solutions": len(solutions),
        "num_organisms": len(organisms),
        "top_ingredients": ingredients[:8],
        "organisms": organisms[:5],
        "summary": summary[:240],
    }

    return {
        "id": record_id,
        "title": display_name,
        "url": url,
        "passage": passage,
        "text_hash": text_hash,
        "facets": facets,
    }


def collect_yaml_files(yaml_dir: Path) -> list[Path]:
    direct = sorted(yaml_dir.glob("*.yaml"))
    if direct:
        return direct
    files: list[Path] = []
    for sub in sorted(yaml_dir.iterdir()):
        if sub.is_dir():
            files.extend(sorted(sub.glob("*.yaml")))
    return files


def embed_records(
    yaml_dir: Path = DEFAULT_YAML_DIR,
    output_path: Path = DEFAULT_OUTPUT,
    model_name: str = MODEL_NAME,
    force: bool = False,
) -> None:
    yaml_files = collect_yaml_files(yaml_dir)
    if not yaml_files:
        raise FileNotFoundError(f"No YAML files found in {yaml_dir}")

    print(f"Scanning {len(yaml_files):,} YAML files in {yaml_dir}...")
    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for path in yaml_files:
        rec = extract_record(path)
        if rec and rec["id"] not in seen_ids:
            seen_ids.add(rec["id"])
            records.append(rec)

    cached_vecs: dict[tuple[str, str], np.ndarray] = {}
    if output_path.exists() and not force:
        try:
            old = np.load(output_path, allow_pickle=False)
            if str(old["model_name"]) == model_name:
                old_ids = old["ids"].tolist()
                old_hashes = old["text_hashes"].tolist()
                old_embs = old["embeddings"]
                for rid, rhash, vec in zip(old_ids, old_hashes, old_embs):
                    cached_vecs[(str(rid), str(rhash))] = vec
        except Exception:
            cached_vecs = {}

    to_encode_idx: list[int] = []
    to_encode_texts: list[str] = []
    for idx, rec in enumerate(records):
        if (rec["id"], rec["text_hash"]) not in cached_vecs:
            to_encode_idx.append(idx)
            to_encode_texts.append(rec["passage"])

    dim = 384
    if cached_vecs:
        dim = next(iter(cached_vecs.values())).shape[0]

    embeddings = np.zeros((len(records), dim), dtype=np.float32)
    for idx, rec in enumerate(records):
        vec = cached_vecs.get((rec["id"], rec["text_hash"]))
        if vec is not None:
            embeddings[idx] = vec

    if to_encode_texts:
        from sentence_transformers import SentenceTransformer

        print(f"Encoding {len(to_encode_texts):,}/{len(records):,} records with {model_name}...")
        model = SentenceTransformer(model_name)
        encoded = model.encode(
            to_encode_texts,
            batch_size=128,
            show_progress_bar=True,
            normalize_embeddings=True,
        )
        encoded = np.asarray(encoded, dtype=np.float32)
        if embeddings.shape[1] != encoded.shape[1]:
            embeddings = np.zeros((len(records), encoded.shape[1]), dtype=np.float32)
        for i, rec_idx in enumerate(to_encode_idx):
            embeddings[rec_idx] = encoded[i]
    else:
        print(f"All {len(records):,} records matched cached embeddings in {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        output_path,
        embeddings=embeddings,
        ids=np.array([r["id"] for r in records]),
        titles=np.array([r["title"] for r in records]),
        urls=np.array([r["url"] for r in records]),
        facets_json=np.array([json.dumps(r["facets"], sort_keys=True) for r in records]),
        text_hashes=np.array([r["text_hash"] for r in records]),
        model_name=np.array(model_name),
    )
    print(f"Saved {len(records):,} embeddings ({embeddings.shape[1]}d) to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Embed CultureMech YAML records.")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_YAML_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    embed_records(args.input_dir, args.output, args.model, args.force)


if __name__ == "__main__":
    main()
