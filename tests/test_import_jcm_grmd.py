from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "import_jcm_grmd.py"


def load_script():
    spec = importlib.util.spec_from_file_location("import_jcm_grmd", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_ingested_grmd_numbers_finds_source_records_without_auxiliary_refs(
    tmp_path: Path,
    monkeypatch,
) -> None:
    module = load_script()
    normalized = tmp_path / "data" / "normalized_yaml"
    bacterial = normalized / "bacterial"
    bacterial.mkdir(parents=True)
    monkeypatch.setattr(module, "NORMALIZED_DIR", normalized)

    (bacterial / "direct.yaml").write_text(
        "media_term:\n" "  term:\n" "    id: jcm.grmd:1333\n",
        encoding="utf-8",
    )
    (bacterial / "mediadive.yaml").write_text(
        "media_term:\n" "  term:\n" "    id: mediadive.medium:J20\n",
        encoding="utf-8",
    )
    (bacterial / "togo.yaml").write_text(
        "notes: 'Source: https://togomedium.org/medium/M150\n\n"
        "  Original source: JCM - JCM_M150\n\n"
        "  Original URL: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=159'\n",
        encoding="utf-8",
    )
    (bacterial / "jcm_note.yaml").write_text(
        "notes: 'Source: JCM | Link: " "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1467'\n",
        encoding="utf-8",
    )
    (bacterial / "auxiliary_only.yaml").write_text(
        "notes: 'Source: JCM | Link: "
        "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1481 | "
        "Derivative medium: ingredients inherited from JCM GRMD=1462.'\n"
        "curation_history:\n"
        "- source: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=999\n",
        encoding="utf-8",
    )

    assert module.ingested_grmd_numbers() == {20, 159, 1333, 1467, 1481}


def test_detect_missing_skips_exact_name_duplicates(
    tmp_path: Path,
    monkeypatch,
) -> None:
    module = load_script()
    normalized = tmp_path / "data" / "normalized_yaml"
    bacterial = normalized / "bacterial"
    bacterial.mkdir(parents=True)
    monkeypatch.setattr(module, "NORMALIZED_DIR", normalized)

    (bacterial / "marine_broth_2216.yaml").write_text(
        "id: CultureMech:015554\n" "name: marine broth 2216\n",
        encoding="utf-8",
    )

    pages = {
        41: "<FONT SIZE=3>41&nbsp;MARINE BROTH 2216</FONT>",
        1338: "<FONT SIZE=3>1338&nbsp;PYG MEDIUM (K)</FONT>",
    }
    monkeypatch.setattr(module, "fetch", lambda grmd: pages.get(grmd))

    missing = module.detect_missing(1338)

    assert set(missing) == {1338}


def test_detect_missing_skips_known_unsafe_multitable_pages(
    tmp_path: Path,
    monkeypatch,
) -> None:
    module = load_script()
    normalized = tmp_path / "data" / "normalized_yaml"
    normalized.mkdir(parents=True)
    monkeypatch.setattr(module, "NORMALIZED_DIR", normalized)
    monkeypatch.setattr(module, "SKIP_GRMDS", {2})

    pages = {
        1: "<FONT SIZE=3>1&nbsp;SIMPLE MEDIUM</FONT>",
        2: "<FONT SIZE=3>2&nbsp;MULTI TABLE MEDIUM</FONT>",
    }
    monkeypatch.setattr(module, "fetch", lambda grmd: pages.get(grmd))

    missing = module.detect_missing(2)

    assert set(missing) == {1}
