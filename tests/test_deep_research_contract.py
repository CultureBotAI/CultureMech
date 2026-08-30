from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
MODULE = REPO / "scripts" / "deep_research_contract.py"
SPEC = importlib.util.spec_from_file_location("deep_research_contract", MODULE)
assert SPEC and SPEC.loader
contract = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = contract
SPEC.loader.exec_module(contract)


def _payload(chars: int = 1_200, sources: int = 3):
    return {
        "report_markdown": "R" * chars,
        "sources": [
            {"title": f"Source {index}", "url": f"https://example.org/{index}"}
            for index in range(sources)
        ],
        "limitations": ["No full text for one candidate paper."],
    }


def test_codex_command_is_native_explicit_web_search_and_read_only(tmp_path):
    command = contract.build_codex_command(
        repo_root=REPO,
        schema_path=tmp_path / "schema.json",
        response_path=tmp_path / "response.json",
    )
    assert command[:5] == ["codex", "--search", "--ask-for-approval", "never", "exec"]
    assert "--ephemeral" in command
    assert command[command.index("--sandbox") + 1] == "read-only"
    assert "--output-schema" in command
    assert "--output-last-message" in command
    assert command[-1] == "-"


def test_prompt_template_must_be_fully_filled(tmp_path):
    template = tmp_path / "prompt.md"
    template.write_text("Target: {label}\nEvidence: {evidence}\n", encoding="utf-8")
    assert contract.render_prompt_template(
        template, {"label": "biofilm", "evidence": "none yet"}
    ) == "Target: biofilm\nEvidence: none yet\n"
    with pytest.raises(contract.ContractError, match="evidence"):
        contract.render_prompt_template(template, {"label": "biofilm"})


def test_validation_rejects_thin_or_duplicate_source_output():
    with pytest.raises(contract.ContractError, match="too short"):
        contract.validate_codex_payload(_payload(chars=20))
    payload = _payload()
    payload["sources"][2]["url"] = payload["sources"][0]["url"] + "#fragment"
    with pytest.raises(contract.ContractError, match="2 distinct sources"):
        contract.validate_codex_payload(payload)


def test_run_publishes_only_a_validated_atomic_markdown_artifact(tmp_path):
    destination = tmp_path / "report.md"

    def runner(command, **kwargs):
        response = Path(command[command.index("--output-last-message") + 1])
        response.write_text(json.dumps(_payload()), encoding="utf-8")
        assert kwargs["input"] == "filled research prompt"
        return subprocess.CompletedProcess(command, 0, "", "")

    summary = contract.run_codex_research(
        "filled research prompt", destination, repo_root=REPO, runner=runner
    )
    assert summary.sources == 3
    assert destination.read_text().endswith("No full text for one candidate paper.\n")
    assert "## Sources" in destination.read_text()
    assert not destination.with_name(f".{destination.name}.tmp").exists()


def test_invalid_codex_response_never_overwrites_an_existing_report(tmp_path):
    destination = tmp_path / "report.md"
    destination.write_text("curator-reviewed previous report\n")

    def runner(command, **kwargs):
        response = Path(command[command.index("--output-last-message") + 1])
        response.write_text(json.dumps(_payload(chars=10)), encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, "", "")

    with pytest.raises(contract.ContractError, match="too short"):
        contract.run_codex_research("prompt", destination, repo_root=REPO, runner=runner)
    assert destination.read_text() == "curator-reviewed previous report\n"


@pytest.mark.parametrize(
    "value,valid",
    [("researcher:secret", True), ("bare-token", False), (":secret", False), ("name:", False)],
)
def test_openscientist_credential_contract(value, valid):
    if valid:
        assert contract.validate_openscientist_credential(
            {"OPENSCIENTIST_API_KEY": value}
        ) == "researcher"
    else:
        with pytest.raises(contract.ContractError, match="name:secret"):
            contract.validate_openscientist_credential(
                {"OPENSCIENTIST_API_KEY": value}
            )


def test_openscientist_canary_discovers_provider_without_submitting_job():
    calls = []

    def runner(command, **kwargs):
        calls.append(command)
        return subprocess.CompletedProcess(command, 0, "openscientist available", "")

    result = contract.openscientist_canary(
        environ={"OPENSCIENTIST_API_KEY": "researcher:secret"}, runner=runner
    )
    assert result.ok
    assert calls == [["deep-research-client", "providers"]]
    assert "secret" not in result.detail


def test_openscientist_canary_accepts_an_isolated_multiword_client_command():
    calls = []

    def runner(command, **kwargs):
        calls.append(command)
        return subprocess.CompletedProcess(command, 0, "openscientist available", "")

    result = contract.openscientist_canary(
        environ={"OPENSCIENTIST_API_KEY": "researcher:secret"},
        client_command="uvx --from deep-research-client deep-research-client",
        runner=runner,
    )
    assert result.ok
    assert calls == [
        ["uvx", "--from", "deep-research-client", "deep-research-client", "providers"]
    ]
