import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from culturemech.convert.base import ConversionBatchError, JSONToRawYAMLConverter

CONVERTER_MODULES = [
    "atcc_raw_yaml",
    "bacdive_raw_yaml",
    "ccap_raw_yaml",
    "komodo_raw_yaml",
    "komodo_web_raw_yaml",
    "mediadb_raw_yaml",
    "mediadive_raw_yaml",
    "nbrc_raw_yaml",
    "sag_raw_yaml",
    "togo_raw_yaml",
    "utex_raw_yaml",
]


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def test_conversion_returns_summary_and_stable_relative_provenance(tmp_path: Path) -> None:
    source = tmp_path / "raw" / "atcc"
    _write_json(source / "records.json", [{"id": "one"}, {"id": "two"}])
    output = tmp_path / "raw_yaml"

    summary = JSONToRawYAMLConverter().convert_directory(source, output, "*.json")

    assert (summary.matched, summary.converted, summary.skipped, summary.failed) == (1, 1, 0, 0)
    converted = yaml.safe_load((output / "one.yaml").read_text())
    assert converted["_source"] == {"file": "atcc/records.json", "layer": "raw_yaml"}


def test_conversion_fails_fast_by_default_and_summarizes_partial_output(tmp_path: Path) -> None:
    source = tmp_path / "raw"
    source.mkdir()
    (source / "a_bad.json").write_text("not json")
    _write_json(source / "z_good.json", {"id": "good"})

    with pytest.raises(ConversionBatchError) as raised:
        JSONToRawYAMLConverter().convert_directory(source, tmp_path / "output", "*.json")

    summary = raised.value.summary
    assert (summary.matched, summary.converted, summary.skipped, summary.failed) == (2, 0, 1, 1)
    assert not (tmp_path / "output" / "good.yaml").exists()


def test_keep_going_attempts_remaining_files_but_still_fails(tmp_path: Path) -> None:
    source = tmp_path / "raw"
    source.mkdir()
    (source / "a_bad.json").write_text("not json")
    _write_json(source / "z_good.json", {"id": "good"})

    with pytest.raises(ConversionBatchError) as raised:
        JSONToRawYAMLConverter().convert_directory(
            source,
            tmp_path / "output",
            "*.json",
            keep_going=True,
        )

    summary = raised.value.summary
    assert (summary.matched, summary.converted, summary.skipped, summary.failed) == (2, 1, 0, 1)
    assert (tmp_path / "output" / "good.yaml").is_file()


def test_empty_input_requires_explicit_opt_in(tmp_path: Path) -> None:
    source = tmp_path / "empty"
    source.mkdir()
    converter = JSONToRawYAMLConverter()

    with pytest.raises(FileNotFoundError, match="--allow-empty"):
        converter.convert_directory(source, tmp_path / "output", "*.json")

    summary = converter.convert_directory(
        source,
        tmp_path / "output",
        "*.json",
        allow_empty=True,
    )
    assert summary.matched == summary.converted == summary.failed == 0


def test_representative_converter_cli_exits_nonzero_for_corrupt_input(tmp_path: Path) -> None:
    source = tmp_path / "raw"
    source.mkdir()
    (source / "bad.json").write_text("not json")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "culturemech.convert.atcc_raw_yaml",
            "--input",
            str(source),
            "--output",
            str(tmp_path / "output"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "Conversion summary" in result.stdout


@pytest.mark.parametrize("module", CONVERTER_MODULES)
def test_every_converter_cli_exposes_batch_controls(module: str) -> None:
    result = subprocess.run(
        [sys.executable, "-m", f"culturemech.convert.{module}", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "--keep-going" in result.stdout
    assert "--allow-empty" in result.stdout
