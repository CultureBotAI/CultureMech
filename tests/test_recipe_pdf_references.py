"""Official PDFs must retain exact source text and fail closed on extraction errors."""

from __future__ import annotations

import base64
import hashlib
import io
import json
from pathlib import Path
from unittest.mock import Mock

import pypdf
import pytest
import requests
from linkml_reference_validator.models import ReferenceValidationConfig
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject, NumberObject
from validate_recipe_references import validate_data

from culturemech.validation import recipe_references as rr
from culturemech.validation.write_validated import DEFAULT_SCHEMA_PATH

FIXTURES = Path(__file__).parent / "fixtures" / "recipe_references"


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def fail(*args, **kwargs):
        pytest.fail("Unexpected network access in PDF reference regression tests")

    monkeypatch.setattr(requests.Session, "get", fail)


@pytest.fixture
def config(tmp_path):
    return ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)


def capture(name="DSMZ751"):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def seed(config, name="DSMZ751"):
    entry = capture(name)
    cache = rr.RecipeSourceCache(config)
    source = rr.recipe_source(entry["url"])
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(source).write_text(json.dumps(entry))
    return cache, source


def session_for(payload, *, media_type="application/pdf", status=200, url=None):
    response = Mock(status_code=status, url=url or capture()["url"])
    response.headers = {"Content-Type": media_type}
    response.iter_content.return_value = [payload]
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    session = Mock()
    session.get.return_value = response
    return session


def synthetic_pdf(pages=("751. SC MEDIUM\n\nNaCl 0.1 g",), *, encrypted=False):
    """Tiny in-memory PDFs exercise parser failures without external test dependencies."""
    writer = pypdf.PdfWriter()
    for text in pages:
        page = writer.add_blank_page(width=612, height=792)
        if text is None:
            continue
        page[NameObject("/Resources")] = DictionaryObject(
            {
                NameObject("/Font"): DictionaryObject(
                    {
                        NameObject("/F1"): DictionaryObject(
                            {
                                NameObject("/Type"): NameObject("/Font"),
                                NameObject("/Subtype"): NameObject("/Type1"),
                                NameObject("/BaseFont"): NameObject("/Helvetica"),
                            }
                        )
                    }
                )
            }
        )
        stream = DecodedStreamObject()
        lines = [
            line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            for line in text.splitlines()
        ]
        operators = " T* ".join(f"({line}) Tj" for line in lines)
        stream.set_data(f"BT /F1 12 Tf 14 TL 40 740 Td {operators} ET".encode("ascii"))
        page[NameObject("/Contents")] = stream.flate_encode()
    if encrypted:
        writer.encrypt("not-readable")
    result = io.BytesIO()
    writer.write(result)
    return result.getvalue()


@pytest.mark.parametrize(
    "name,title,quote",
    [
        ("DSMZ403", "403. BSK-MEDIUM", "Dissolve 50.05 g bovine serum albumine"),
        ("DSMZ751", "751. SC MEDIUM", "10% glucose 5.0 ml"),
        ("DSMZ1829", "1829: BSKII medium (Borrelia)", "Final volume: 100 ml"),
        (
            "DSMZ261",
            "261. MEDIUM FOR CHEMOLITHOTROPHIC GROWTH OF BACILLUS SCHLEGELII",
            "Use medium 260 without pyruvate.",
        ),
        (
            "DSMZ605a",
            "605a. NUTRIENT AGAR (OXOID CM3) WITH PHOSPHATE",
            "add 0.45 g/l KH2PO4",
        ),
        ("DSMZ104a", "104a: ANAEROBACULUM MEDIUM", "Salt solution 40.00 ml"),
    ],
)
def test_real_pdf_binary_text_and_metadata(config, name, title, quote):
    cache, source = seed(config, name)
    entry = capture(name)
    binary = base64.b64decode(entry["pdf_base64"])
    text, count = rr.extract_recipe_pdf(binary)
    assert text == entry["raw"] and count == 1
    assert hashlib.sha256(binary).hexdigest() == entry["pdf_sha256"]
    validator = rr.RecipeTextValidator(config, cache=cache)
    assert validator.validate(quote, "url:" + source.url, expected_title=title).is_valid
    assert validator.validate_title(source.url, title).is_valid
    result = cache.fetch(source)
    assert result.metadata["extraction"] == rr.PDF_EXTRACTION
    assert result.metadata["response_url"] == source.url
    assert "pdf_base64" not in result.metadata
    assert "year" not in result.metadata and "authors" not in result.metadata


@pytest.mark.parametrize(
    "name,quote",
    [
        ("DSMZ403", "Dissolve 50.5 g bovine serum albumine"),
        ("DSMZ403", "MgCl2 x 7 H2O 0.3 g"),
        ("DSMZ751", "10% glucose 1.0 ml"),
        ("DSMZ751", "Hemin (0.1% in 0.05M NaOH) 15.0 ml"),
        ("DSMZ751", "MgSO4 x 7 H2O 0.2 mg"),
        ("DSMZ1829", "Final volume: 1000 ml"),
    ],
)
def test_wrong_pdf_amounts_units_hydrates_and_doses_fail(config, name, quote):
    cache, source = seed(config, name)
    result = rr.RecipeTextValidator(config, cache=cache).validate(quote, source.url)
    assert not result.is_valid and "snippet_mismatch" in result.message


@pytest.mark.parametrize(
    "url",
    [
        "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf",
        "https://www.dsmz.de.evil.invalid/microorganisms/medium/pdf/DSMZ_Medium751.pdf",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf?download=1",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf#other",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium0751.pdf",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751AB.pdf",
        "https://www.dsmz.de/microorganisms/medium/pdf/../DSMZ_Medium751.pdf",
        "https://user:pass@www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf",
    ],
)
def test_pdf_adapter_only_accepts_explicit_source_urls(url):
    assert rr.recipe_source(url) is None


def test_pdf_live_fetch_cache_replay_refresh_and_memoization(config):
    entry = capture()
    binary = base64.b64decode(entry["pdf_base64"])
    session = session_for(binary, media_type="application/pdf; charset=binary")
    cache = rr.RecipeSourceCache(config, session=session)
    source = rr.recipe_source(entry["url"])
    result = cache.fetch(source)
    assert result.content == entry["raw"]
    assert cache.fetch(source) is result
    session.get.assert_called_once()
    assert session.get.call_args.kwargs["allow_redirects"] is False
    assert session.get.call_args.kwargs["stream"] is True
    assert rr.RecipeSourceCache(config).fetch(source).content == result.content
    assert not list(cache.directory.glob(".capture-*"))
    cache.path(source).write_text("corrupt")
    assert (
        rr.RecipeSourceCache(config, refresh=True, session=session).fetch(source).content
        == result.content
    )
    assert session.get.call_count == 2


@pytest.mark.parametrize(
    "field,value",
    [
        ("pdf_sha256", "wrong"),
        ("pdf_base64", "not base64!"),
        ("pdf_pages", 2),
        ("media_type", "text/plain"),
        ("extraction", {"library": "OCR"}),
        ("encoding", "latin-1"),
        ("version", rr.CACHE_VERSION),
        ("response_url", "https://example.org/redirect"),
        ("http_status", 404),
    ],
)
def test_pdf_cache_corruption_fails_without_generic_fallback(config, field, value):
    cache, source = seed(config)
    entry = capture()
    entry[field] = value
    cache.path(source).write_text(json.dumps(entry))
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    result = validator.validate("10% glucose 5.0 ml", source.url)
    assert not result.is_valid and "source_cache" in result.message
    validator.fallback.validate.assert_not_called()


def test_rehashed_text_tampering_still_must_match_pdf_binary(config):
    cache, source = seed(config)
    entry = capture()
    entry["raw"] += "\nInvented reagent 999 g"
    entry["sha256"] = hashlib.sha256(entry["raw"].encode()).hexdigest()
    cache.path(source).write_text(json.dumps(entry))
    with pytest.raises(rr.RecipeReferenceError, match="source_cache"):
        cache.fetch(source)


@pytest.mark.parametrize("refresh", [False, True])
def test_pdf_symlink_cache_rejected(config, refresh):
    cache = rr.RecipeSourceCache(config, refresh=refresh)
    source = rr.recipe_source(capture()["url"])
    cache.directory.mkdir()
    cache.path(source).symlink_to(config.cache_dir / "missing")
    with pytest.raises(rr.RecipeReferenceError, match="symlink"):
        cache.fetch(source)


@pytest.mark.parametrize(
    "payload,options,error",
    [
        pytest.param(b"%PDF-1.4 broken", {}, "source_format", id="broken-pdf"),
        pytest.param(b"<html>maintenance</html>", {}, "source_format", id="html-body"),
        pytest.param(
            b"%PDF-1.4", {"media_type": "text/html"}, "source_format", id="html-content-type"
        ),
        pytest.param(b"%PDF-1.4", {"media_type": ""}, "source_format", id="missing-content-type"),
        pytest.param(b"%PDF-1.4", {"status": 302}, "source_access", id="redirect-status"),
        pytest.param(b"%PDF-1.4", {"status": 404}, "source_access", id="not-found"),
        pytest.param(
            b"%PDF-1.4", {"url": "https://example.org/other.pdf"}, "source_access", id="changed-url"
        ),
        pytest.param(
            b"x" * (rr.MAX_RESPONSE_BYTES + 1), {}, "source_format", id="oversized-response"
        ),
    ],
)
def test_pdf_bad_responses_fail_and_are_not_cached(config, payload, options, error):
    session = session_for(payload, **options)
    cache = rr.RecipeSourceCache(config, session=session)
    source = rr.recipe_source(capture()["url"])
    for _ in range(2):
        with pytest.raises(rr.RecipeReferenceError, match=error):
            cache.fetch(source)
    session.get.assert_called_once()
    assert not cache.path(source).exists()


@pytest.mark.parametrize("pages", [(None,), ("",), ("751. SC MEDIUM\nNaCl 0.1 g", None)])
def test_blank_or_image_only_page_requires_manual_review(pages):
    with pytest.raises(rr.RecipeReferenceError, match="without extractable text"):
        rr.extract_recipe_pdf(synthetic_pdf(pages))


def test_scanned_only_image_is_not_treated_as_valid_recipe_text():
    writer = pypdf.PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    bitmap = DecodedStreamObject()
    bitmap.set_data(b"\x00")
    bitmap.update(
        {
            NameObject("/Type"): NameObject("/XObject"),
            NameObject("/Subtype"): NameObject("/Image"),
            NameObject("/Width"): NumberObject(1),
            NameObject("/Height"): NumberObject(1),
            NameObject("/BitsPerComponent"): NumberObject(8),
            NameObject("/ColorSpace"): NameObject("/DeviceGray"),
        }
    )
    page[NameObject("/Resources")] = DictionaryObject(
        {NameObject("/XObject"): DictionaryObject({NameObject("/Image1"): bitmap})}
    )
    stream = DecodedStreamObject()
    stream.set_data(b"q 100 0 0 100 50 50 cm /Image1 Do Q")
    page[NameObject("/Contents")] = stream
    output = io.BytesIO()
    writer.write(output)
    with pytest.raises(rr.RecipeReferenceError, match="without extractable text"):
        rr.extract_recipe_pdf(output.getvalue())


def test_pdf_text_expansion_is_bounded(monkeypatch):
    payload = synthetic_pdf()
    page = Mock()
    page.get_contents.return_value.get_data.return_value = b"small stream"
    page.extract_text.return_value = "x" * (len(payload) + 1)
    reader = Mock(is_encrypted=False, pages=[page])
    monkeypatch.setattr(rr.pypdf, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(rr, "MAX_RESPONSE_BYTES", len(payload))
    with pytest.raises(rr.RecipeReferenceError, match="text exceeds"):
        rr.extract_recipe_pdf(payload)


def test_pdf_network_timeout_is_an_error_not_a_literature_fallback(config):
    session = Mock()
    session.get.side_effect = requests.Timeout("unavailable")
    cache = rr.RecipeSourceCache(config, session=session)
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    for _ in range(2):
        result = validator.validate("10% glucose 5.0 ml", capture()["url"])
        assert not result.is_valid and "source_access" in result.message
    session.get.assert_called_once()
    validator.fallback.validate.assert_not_called()


def test_pdf_resource_limits_and_encryption(monkeypatch):
    with pytest.raises(rr.RecipeReferenceError, match="encrypted"):
        rr.extract_recipe_pdf(synthetic_pdf(encrypted=True))
    with monkeypatch.context() as patch:
        patch.setattr(rr, "MAX_PDF_PAGES", 1)
        with pytest.raises(rr.RecipeReferenceError, match="page count"):
            rr.extract_recipe_pdf(synthetic_pdf(("751. SC MEDIUM\nNaCl 0.1 g",) * 2))
    with monkeypatch.context() as patch:
        patch.setattr(rr, "MAX_PDF_CONTENT_BYTES", 1)
        with pytest.raises(rr.RecipeReferenceError, match="content exceeds"):
            rr.extract_recipe_pdf(synthetic_pdf())


def test_pdf_extraction_cache_is_bound_to_bytes_reader_and_limits(monkeypatch):
    payload = synthetic_pdf(("751. SC MEDIUM\nNaCl 0.1 g",) * 2)
    original_reader = rr.pypdf.PdfReader
    reader = Mock(wraps=original_reader)
    rr._small_recipe_pdf.cache_clear()
    monkeypatch.setattr(rr.pypdf, "PdfReader", reader)
    try:
        original = rr.extract_recipe_pdf(payload)
        assert rr.extract_recipe_pdf(payload) == original
        assert reader.call_count == 1
        altered = synthetic_pdf(("751. SC MEDIUM\nNaCl 0.1 mg",) * 2)
        assert rr.extract_recipe_pdf(altered) != original
        assert reader.call_count == 2
        for setting, limit, error in (
            ("MAX_PDF_PAGES", 1, "page count"),
            ("MAX_PDF_CONTENT_BYTES", 1, "content exceeds"),
            ("MAX_RESPONSE_BYTES", 1, "oversized"),
        ):
            with monkeypatch.context() as patch:
                patch.setattr(rr, setting, limit)
                with pytest.raises(rr.RecipeReferenceError, match=error):
                    rr.extract_recipe_pdf(payload)
        with monkeypatch.context() as patch:
            patch.setattr(rr.pypdf, "PdfReader", Mock(side_effect=ValueError("reader failed")))
            with pytest.raises(rr.RecipeReferenceError, match="could not extract"):
                rr.extract_recipe_pdf(payload)
        assert rr.extract_recipe_pdf(payload) == original
        for value in range(12):
            rr.extract_recipe_pdf(synthetic_pdf((f"751. Medium {value}",)))
        assert rr._small_recipe_pdf.cache_info().currsize == 8
    finally:
        rr._small_recipe_pdf.cache_clear()


def test_large_pdf_extraction_bypasses_cache(monkeypatch):
    reader = Mock(wraps=rr.pypdf.PdfReader)
    monkeypatch.setattr(rr.pypdf, "PdfReader", reader)
    payload = synthetic_pdf() + b"\n%" + b"x" * (256 * 1024)
    assert rr.extract_recipe_pdf(payload) == rr.extract_recipe_pdf(payload)
    assert reader.call_count == 2


@pytest.mark.parametrize("heading", ["752. SC MEDIUM", "751", "SC MEDIUM", "Error page"])
def test_wrong_or_missing_heading_is_not_a_title_fallback(config, heading):
    session = session_for(synthetic_pdf((heading + "\n\nNaCl 0.1 g",)))
    cache = rr.RecipeSourceCache(config, session=session)
    with pytest.raises(rr.RecipeReferenceError, match="source_identity"):
        cache.fetch(rr.recipe_source(capture()["url"]))


def test_pdf_title_requires_a_delimited_heading_and_body():
    source = rr.recipe_source(capture()["url"])
    for raw in ("751. SC MEDIUM", "751. SC MEDIUM\nNaCl 0.1 g", "751. SC MEDIUM\n\n"):
        with pytest.raises(rr.RecipeReferenceError, match="title/body boundary"):
            rr.parse_recipe(source, raw, {})


@pytest.mark.parametrize("wrong", ["605", "605b", "605A"])
def test_pdf_variant_cannot_borrow_base_or_other_variant(wrong):
    entry = capture("DSMZ605a")
    source = rr.RecipeSource(entry["url"], "dsmz_pdf", wrong)
    with pytest.raises(rr.RecipeReferenceError, match="source_identity"):
        rr.parse_recipe(source, entry["raw"], {})


def test_pdf_nested_evidence_and_bibliography_checks(config):
    cache, source = seed(config)
    validator = rr.RecipeTextValidator(config, cache=cache)
    medium = {
        "name": "SC",
        "solutions": [
            {
                "composition": [
                    {"evidence": [{"reference": source.url, "snippet": "10% glucose 5.0 ml"}]}
                ]
            }
        ],
        "references": [{"reference": source.url, "title": "751. SC MEDIUM"}],
    }
    assert not validate_data(medium, DEFAULT_SCHEMA_PATH, validator)
    assert len(validator.results) == 2
    medium["references"][0]["title"] = "Invented title"
    issues = validate_data(medium, DEFAULT_SCHEMA_PATH, validator)
    assert len(issues) == 1 and "title_mismatch" in issues[0].message
