"""Literal official-recipe references alongside the upstream literature validator."""

from __future__ import annotations

import base64
import datetime
import hashlib
import io
import json
import os
import re
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pypdf
import requests
from bs4 import BeautifulSoup
from linkml_reference_validator.models import (
    ReferenceContent,
    ReferenceValidationConfig,
    SupportingTextMatch,
    ValidationResult,
    ValidationSeverity,
)
from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator

CACHE_VERSION = 1
PDF_CACHE_VERSION = 2
MAX_RESPONSE_BYTES = 5 * 1024 * 1024
MAX_PDF_PAGES = 50
MAX_PDF_CONTENT_BYTES = 20 * 1024 * 1024
PDF_EXTRACTION = {
    "library": "pypdf",
    "version": pypdf.__version__,
    "mode": "layout",
}
KOMODO_COLUMNS = ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"]
KOMODO_FEATURES = [
    "ID:",
    "Name:",
    "PH Info:",
    "Is Complex:",
    "Is Aerobic:",
    "Is SubMedium:",
    "Remarks:",
    "Instructions:",
]
KOMODO_AMOUNT_BASIS = (
    "Compounds in the medium listed by their compound names. Gram & Mol amounts are per "
    "Liter of medium. Trace metabolites & gases usually do not have amounts"
)


class RecipeReferenceError(ValueError):
    """An unavailable or invalid source must not become a matching fallback."""


@dataclass(frozen=True)
class RecipeSource:
    url: str
    provider: str
    accession: str


def recipe_source(reference_id: str) -> RecipeSource | None:
    url = reference_id.strip()
    if url.lower().startswith("url:"):
        url = url[4:]
    try:
        parsed = urlsplit(url)
    except ValueError:
        return None
    if parsed.scheme != "https" or parsed.fragment or parsed.username or parsed.password:
        return None
    query = parse_qs(parsed.query, keep_blank_values=True)
    if parsed.netloc == "togomedium.org" and parsed.path == "/sparqlist/api/gmdb_medium_by_gmid":
        ids = query.get("gm_id", [])
        if set(query) == {"gm_id"} and len(ids) == 1 and re.fullmatch(r"M[1-9][0-9]*", ids[0]):
            return RecipeSource(url, "togo", ids[0])
    if parsed.netloc == "www.jcm.riken.jp" and parsed.path == "/cgi-bin/jcm/jcm_grmd":
        ids = query.get("GRMD", [])
        if set(query) == {"GRMD"} and len(ids) == 1 and re.fullmatch(r"[1-9][0-9]*", ids[0]):
            return RecipeSource(url, "jcm", ids[0])
    if (
        parsed.netloc == "www.nite.go.jp"
        and parsed.path == "/nbrc/catalogue/NBRCMediumDetailServlet"
    ):
        ids = query.get("NO", [])
        if set(query) == {"NO"} and len(ids) == 1 and re.fullmatch(r"[1-9][0-9]*", ids[0]):
            return RecipeSource(url, "nbrc", ids[0])
    if parsed.netloc == "mediadive.dsmz.de" and not parsed.query:
        match = re.fullmatch(r"/rest/(medium|solution)/([A-Za-z0-9_-]+)", parsed.path)
        if match:
            return RecipeSource(url, "mediadive_" + match[1], match[2])
    if re.fullmatch(r"https://mediadb\.systemsbiology\.net/defined_media/media/[1-9][0-9]*/", url):
        return RecipeSource(url, "mediadb", parsed.path.split("/")[-2])
    if parsed.netloc == "www.dsmz.de" and not parsed.query:
        match = re.fullmatch(
            r"/microorganisms/medium/pdf/DSMZ_Medium([1-9][0-9]*[A-Za-z]?)\.pdf", parsed.path
        )
        if match:
            return RecipeSource(url, "dsmz_pdf", match[1])
    if parsed.netloc == "komodo.modelseed.org" and parsed.path in {
        "/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed",
        "/servlet/KomodoTomcatServerSideUtilitiesModelSeed",
    }:
        ids = query.get("MediaInfo", [])
        if (
            set(query) == {"MediaInfo"}
            and len(ids) == 1
            and re.fullmatch(
                r"[1-9][0-9]*[A-Za-z]?(?:\.[0-9]+)?(?:_[A-Za-z0-9][A-Za-z0-9_.,()+ -]*)?",
                ids[0],
            )
        ):
            return RecipeSource(url, "komodo", ids[0])
    return None


def whitespace(text: str) -> str:
    """Keep chemical case, punctuation, decimals and signs; fold whitespace only."""
    return " ".join(text.split())


def html_recipe_text(raw: str) -> tuple[str, str]:
    soup = BeautifulSoup(raw, "html.parser")
    title = whitespace(soup.title.get_text()) if soup.title else ""
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()
    for tag in soup.find_all("br"):
        tag.replace_with(" ")
    # Block/cell boundaries need spaces; inline sub/sup tags must keep formula digits adjacent.
    for tag in soup.find_all(["td", "th", "tr", "p", "div", "li", "h1", "h2", "h3", "table"]):
        tag.insert_before(" ")
        tag.insert_after(" ")
    return whitespace(soup.get_text()), title


def komodo_recipe_text(source: RecipeSource, raw: str) -> tuple[str, str]:
    """Match the recipe table, not the separate calculated SEED ion totals."""
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()
    titles = soup.find_all("title")
    if len(titles) != 1 or whitespace(titles[0].get_text()) != "KOMODO - the Known Media Database":
        raise RecipeReferenceError("source_metadata: unexpected KOMODO page title")
    title = whitespace(titles[0].get_text())

    def rows(table):
        return [
            [html_recipe_text(str(cell))[0] for cell in row.find_all(["td", "th"], recursive=False)]
            for row in table.find_all("tr")
            if row.find_parent("table") is table
        ]

    tables = [(table, rows(table)) for table in soup.find_all("table")]
    features = [(t, r) for t, r in tables if any(row and row[0] == "ID:" for row in r)]
    recipes = [(t, r) for t, r in tables if r and r[0] == KOMODO_COLUMNS]
    if len(features) != 1 or len(recipes) != 1:
        raise RecipeReferenceError("source_format: expected one KOMODO feature and recipe table")
    feature_table, feature_rows = features[0]
    recipe_table, recipe_rows = recipes[0]
    for table in (feature_table, recipe_table):
        if any(
            tag.has_attr("hidden")
            or tag.get("aria-hidden", "").lower() == "true"
            or re.search(
                r"(?:display\s*:\s*none|visibility\s*:\s*hidden)", tag.get("style", ""), re.I
            )
            for tag in [table, *table.parents, *table.find_all(True)]
        ):
            raise RecipeReferenceError("source_format: hidden KOMODO recipe content")
        if table.find("table") or any(
            cell.get(attr, "1") != "1"
            for cell in table.find_all(["td", "th"])
            for attr in ("rowspan", "colspan")
        ):
            raise RecipeReferenceError("source_format: ambiguous KOMODO table cell boundaries")
    if (
        any(len(row) != 2 for row in feature_rows)
        or [row[0] for row in feature_rows] != KOMODO_FEATURES
    ):
        raise RecipeReferenceError("source_format: unexpected or duplicate KOMODO feature rows")
    identity = dict(feature_rows)
    if identity["ID:"] != source.accession:
        raise RecipeReferenceError("source_identity: KOMODO accession mismatch")
    headings = [html_recipe_text(str(b))[0] for b in soup.find_all("b")]
    headings = [heading for heading in headings if heading.startswith("Medium:")]
    if not identity["Name:"] or headings != ["Medium: " + identity["Name:"]]:
        raise RecipeReferenceError("source_identity: KOMODO medium name/heading mismatch")
    # Require the provider's basis statement in the section immediately before its table.
    section = []
    for element in feature_table.next_elements:
        if element is recipe_table:
            break
        if isinstance(element, str) and element.find_parent("table") is None:
            section.append(str(element))
    else:
        raise RecipeReferenceError("source_format: KOMODO recipe table precedes features")
    if whitespace(" ".join(section)) != "Metabolites list " + KOMODO_AMOUNT_BASIS:
        raise RecipeReferenceError("source_format: KOMODO amount basis is missing or changed")
    if len(recipe_rows) < 2:
        raise RecipeReferenceError("source_unavailable: KOMODO has no ingredient rows")
    seen = set()
    for row in recipe_rows[1:]:
        if len(row) != 5 or any(not cell for cell in row) or row[0] in seen:
            raise RecipeReferenceError(
                "source_format: malformed or duplicate KOMODO ingredient row"
            )
        seen.add(row[0])
        if any(
            not re.fullmatch(
                r"null|[+-]?(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)(?:[Ee][+-]?[0-9]+)?", value
            )
            for value in row[3:]
        ):
            raise RecipeReferenceError("source_format: unexpected KOMODO amount text")
    content = "\n".join(
        [
            headings[0],
            *(" ".join(row) for row in feature_rows),
            "Metabolites list",
            KOMODO_AMOUNT_BASIS,
            *(" ".join(row) for row in recipe_rows),
        ]
    )
    return content, title


def nbrc_recipe_text(source: RecipeSource, raw: str) -> tuple[str, str]:
    """Read the identified catalogue recipe, excluding navigation and other page text."""
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()
    titles = soup.find_all("title")
    expected_title = "Catalogue Detail Medium | NITE - NBRC Culture Catalogue"
    if len(titles) != 1 or whitespace(titles[0].get_text()) != expected_title:
        raise RecipeReferenceError("source_metadata: unexpected NBRC page title")
    mains, compositions = soup.find_all("main"), soup.find_all(id="medium-comp")
    if len(mains) != 1 or len(compositions) != 1:
        raise RecipeReferenceError("source_format: expected one NBRC main/composition section")
    main, composition = mains[0], compositions[0]
    table = composition.find_parent("table")
    headings = [whitespace(h.get_text()) for h in main.find_all("h3")]
    if (
        headings != ["Medium Detail Information"]
        or table is None
        or table.find_parent("main") is not main
        or table.find_parent("table") is not None
        or composition.name != "td"
    ):
        raise RecipeReferenceError("source_format: unexpected NBRC detail section")
    if any(
        tag.has_attr("hidden")
        or tag.get("aria-hidden", "").lower() == "true"
        or set(tag.get("class", [])) & {"d-none", "invisible"}
        or re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden)", tag.get("style", ""), re.I)
        for tag in [table, *table.parents, *table.find_all(True)]
    ):
        raise RecipeReferenceError("source_format: hidden NBRC recipe content")
    rows = [r for r in table.find_all("tr") if r.find_parent("table") is table]
    cells = [r.find_all(["th", "td"], recursive=False) for r in rows]
    if [len(row) for row in cells] != [2, 2, 1, 1, 2]:
        raise RecipeReferenceError("source_format: unexpected or duplicate NBRC detail rows")

    def text(cell):
        return html_recipe_text(str(cell))[0]

    if (
        [text(cells[i][0]) for i in (0, 1, 2, 4)]
        != ["Medium No.", "Medium", "Composition", "Comment"]
        or cells[3][0] is not composition
        or any(cell.find("table") for i in (0, 1, 2, 4) for cell in cells[i])
    ):
        raise RecipeReferenceError("source_format: ambiguous NBRC identity/composition rows")
    if text(cells[0][1]) != source.accession or not text(cells[1][1]):
        raise RecipeReferenceError("source_identity: NBRC medium accession/name mismatch")
    # NBRC uses indented, spanning cells for stock sections; retain their order and text.
    recipe_tables = composition.find_all("table")
    if len(recipe_tables) != 1:
        raise RecipeReferenceError("source_format: expected one NBRC composition table")
    recipe_rows = recipe_tables[0].find_all("tr")
    if not recipe_rows or not text(composition):
        raise RecipeReferenceError("source_unavailable: NBRC composition is empty")
    for row in recipe_rows:
        row_cells = row.find_all(["td", "th"], recursive=False)
        if not row_cells or any(cell.get("rowspan", "1") != "1" for cell in row_cells):
            raise RecipeReferenceError("source_format: ambiguous NBRC composition row")
    content = "\n".join(
        [
            "Medium No. " + text(cells[0][1]),
            "Medium " + text(cells[1][1]),
            "Composition",
            *(text(row) for row in recipe_rows),
            "Comment " + text(cells[4][1]),
        ]
    )
    return content, expected_title


def mediadb_recipe_text(source: RecipeSource, raw: str) -> tuple[str, str]:
    """Read only the identified compound table, preserving unknown and literal amounts."""
    soup = BeautifulSoup(raw, "html.parser")
    titles = soup.find_all("title")
    sections = soup.find_all(id="contentcol")
    headings = soup.find_all("h2")
    if len(titles) != 1:
        raise RecipeReferenceError("source_metadata: expected one MediaDB title")
    title = whitespace(titles[0].get_text())
    if not re.fullmatch(r"Media: \S.*", title):
        raise RecipeReferenceError("source_metadata: unexpected MediaDB title")
    if len(sections) != 1 or len(headings) != 1:
        raise RecipeReferenceError("source_format: expected one MediaDB content section/heading")
    section, heading = sections[0], headings[0]
    if heading not in section.descendants or html_recipe_text(str(heading))[0] != title:
        raise RecipeReferenceError("source_identity: MediaDB title/heading mismatch")
    links = soup.find_all("a", href=re.compile(r"^/defined_media/media_text/"))
    if (
        len(links) != 1
        or links[0].get("href") != f"/defined_media/media_text/{source.accession}/"
        or links[0] not in section.descendants
        or html_recipe_text(str(links[0]))[0] != "Tab-delimited version"
    ):
        raise RecipeReferenceError("source_identity: MediaDB self-accession link mismatch")
    tables = section.find_all("table")
    if len(tables) != 1 or tables[0].find_parent("table") is not None:
        raise RecipeReferenceError("source_format: expected one unnested MediaDB compound table")
    table = tables[0]
    for node in (heading, links[0], table):
        if any(
            tag.name in {"template", "noscript", "script", "style", "head", "details", "dialog"}
            or tag.has_attr("hidden")
            or tag.get("aria-hidden", "").lower() == "true"
            or set(tag.get("class", [])) & {"hidden", "d-none", "invisible"}
            or re.search(
                r"(?:display\s*:\s*none|visibility\s*:\s*(?:hidden|collapse))",
                tag.get("style", ""),
                re.I,
            )
            for tag in [node, *node.parents, *node.find_all(True)]
        ):
            raise RecipeReferenceError("source_format: hidden MediaDB recipe content")
        allowed = {
            "table",
            "thead",
            "tbody",
            "tfoot",
            "tr",
            "th",
            "td",
            "a",
            "span",
            "b",
            "strong",
            "i",
            "em",
            "sub",
            "sup",
            "br",
        }
        if any(tag.name not in allowed for tag in node.find_all(True)) or any(
            tag.name in {"iframe", "object", "canvas", "svg", "math"} for tag in node.parents
        ):
            raise RecipeReferenceError("source_format: nonliteral MediaDB recipe content")
    if table.parent.name != "div":
        raise RecipeReferenceError("source_format: MediaDB compound count boundary missing")
    count_text = " ".join(
        html_recipe_text(str(node))[0] for node in table.parent.contents if node is not table
    )
    count = re.fullmatch(r"([1-9][0-9]*) Compounds:", whitespace(count_text))
    if not count:
        raise RecipeReferenceError("source_format: missing or ambiguous MediaDB compound count")
    rows = table.find_all("tr")
    cells = [row.find_all(["th", "td"], recursive=False) for row in rows]
    if (
        len(rows) != int(count[1]) + 1
        or any(row.find_parent("tr") is not None for row in rows)
        or any(len(row) != 2 for row in cells)
        or len(table.find_all(["th", "td"])) != 2 * len(rows)
        or any(
            cell.get(attr, "1") != "1"
            for row in cells
            for cell in row
            for attr in ("rowspan", "colspan")
        )
    ):
        raise RecipeReferenceError("source_format: malformed MediaDB rows or count mismatch")
    text_rows = [[html_recipe_text(str(cell))[0] for cell in row] for row in cells]
    if (
        text_rows[0] != ["Compound", "Amount (mM)"]
        or any(cell.name != "th" for cell in cells[0])
        or any(cell.name != "td" for row in cells[1:] for cell in row)
    ):
        raise RecipeReferenceError("source_format: MediaDB compound headers/units changed")
    seen_ids, seen_names = set(), set()
    for row, (name, amount) in zip(cells[1:], text_rows[1:], strict=True):
        compound_links = row[0].find_all("a")
        match = (
            re.fullmatch(
                r"/defined_media/compounds/([1-9][0-9]*)/", compound_links[0].get("href", "")
            )
            if len(compound_links) == 1
            else None
        )
        if (
            not match
            or not name
            or html_recipe_text(str(compound_links[0]))[0] != name
            or row[1].find("a")
            or match[1] in seen_ids
            or name in seen_names
        ):
            raise RecipeReferenceError("source_identity: malformed/duplicate MediaDB compound")
        if not re.fullmatch(
            r"None|[+-]?(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)(?:[Ee][+-]?[0-9]+)?", amount
        ):
            raise RecipeReferenceError("source_format: unexpected MediaDB amount text")
        seen_ids.add(match[1])
        seen_names.add(name)
    return "\n".join([title, *(" ".join(row) for row in text_rows)]), title


def extract_recipe_pdf(payload: bytes) -> tuple[str, int]:
    """Preserve layout text; unreadable pages require manual review, not OCR guesses."""
    if len(payload) > MAX_RESPONSE_BYTES or not payload.startswith(b"%PDF-"):
        raise RecipeReferenceError("source_format: invalid or oversized recipe PDF")
    try:
        reader = pypdf.PdfReader(io.BytesIO(payload))
        if reader.is_encrypted:
            raise RecipeReferenceError("source_format: encrypted recipe PDF")
        count = len(reader.pages)
        if not 0 < count <= MAX_PDF_PAGES:
            raise RecipeReferenceError("source_format: recipe PDF page count exceeds limits")
        texts, content_bytes, text_bytes = [], 0, 0
        for page in reader.pages:
            stream = page.get_contents()
            content_bytes += len(stream.get_data()) if stream is not None else 0
            if content_bytes > MAX_PDF_CONTENT_BYTES:
                raise RecipeReferenceError("source_format: recipe PDF content exceeds size limit")
            text = page.extract_text(extraction_mode="layout") if stream is not None else ""
            if not text or not text.strip():
                raise RecipeReferenceError(
                    "source_unavailable: recipe PDF contains a page without extractable text"
                )
            text_bytes += len(text.encode("utf-8")) + 2
            if text_bytes > MAX_RESPONSE_BYTES:
                raise RecipeReferenceError("source_format: recipe PDF text exceeds size limit")
            texts.append(text)
        return "\n\n".join(texts), count
    except RecipeReferenceError:
        raise
    except Exception as error:
        # Malformed fonts, object graphs and content streams raise varying parser errors.
        raise RecipeReferenceError(
            f"source_format: could not extract recipe PDF: {type(error).__name__}"
        ) from error


def parse_recipe(source: RecipeSource, raw: str, metadata: dict) -> ReferenceContent:
    title = None
    content = raw
    if source.provider == "dsmz_pdf":
        # Long DSMZ headings can wrap; the first blank line separates the title block.
        parts = re.split(r"\r?\n[ \t]*\r?\n", raw.lstrip(), maxsplit=1)
        if len(parts) != 2 or not parts[1].strip():
            raise RecipeReferenceError("source_metadata: recipe PDF title/body boundary missing")
        title = whitespace(parts[0])
        heading = re.fullmatch(r"([1-9][0-9]*[A-Za-z]?)[.:]\s+\S.*", title)
        if not heading or heading[1] != source.accession:
            raise RecipeReferenceError("source_identity: DSMZ PDF heading/accession mismatch")
    elif source.provider == "jcm":
        content, title = html_recipe_text(raw)
        if f"Search for medium no. = [{source.accession}]." not in content:
            raise RecipeReferenceError(
                "source_identity: JCM accession does not match the requested recipe"
            )
        if "Nothing found." in content:
            raise RecipeReferenceError("source_unavailable: JCM returned no recipe")
    elif source.provider == "komodo":
        content, title = komodo_recipe_text(source, raw)
    elif source.provider == "nbrc":
        content, title = nbrc_recipe_text(source, raw)
    elif source.provider == "mediadb":
        content, title = mediadb_recipe_text(source, raw)
    else:
        try:
            body = json.loads(raw)
            if source.provider == "togo":
                identity = body["meta"]
                if identity["gm"] != "http://togomedium.org/medium/" + source.accession:
                    raise RecipeReferenceError("source_identity: TOGO accession mismatch")
                if not isinstance(body["components"], list) or not body["components"]:
                    raise RecipeReferenceError("source_unavailable: TOGO has no recipe components")
            else:
                if body["status"] != 200:
                    raise RecipeReferenceError("source_unavailable: MediaDive API reports failure")
                identity = (
                    body["data"]["medium"]
                    if source.provider == "mediadive_medium"
                    else body["data"]
                )
                if str(identity["id"]) != source.accession:
                    raise RecipeReferenceError("source_identity: MediaDive accession mismatch")
                rows = (
                    body["data"]["solutions"]
                    if source.provider == "mediadive_medium"
                    else identity["recipe"]
                )
                if not isinstance(rows, list) or not rows:
                    raise RecipeReferenceError("source_unavailable: MediaDive has no recipe rows")
            title = identity["name"]
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise RecipeReferenceError("source_format: unexpected official recipe JSON") from error
    if not isinstance(title, str) or not title.strip():
        raise RecipeReferenceError("source_metadata: official recipe title is unavailable")
    return ReferenceContent(
        reference_id=source.url,
        title=title,
        content=content,
        content_type="official_recipe",
        metadata=metadata,
    )


def literal_match(quote: str, content: str) -> bool:
    query, text = whitespace(quote), whitespace(content)
    if not query:
        return False

    # A substring of a larger number, formula or word is not a complete exact excerpt.
    def token(char):
        return char.isalnum() or char in "_+-./%\u00b7\u2212\u00b1\u207a\u207b"

    start = text.find(query)
    while start >= 0:
        end = start + len(query)
        left_ok = not (start and token(query[0]) and token(text[start - 1]))
        right_ok = not (end < len(text) and token(query[-1]) and token(text[end]))
        # Decimal commas must not turn a fraction into a matching integer.
        if (
            start >= 2
            and query[0].isdigit()
            and text[start - 1] == ","
            and text[start - 2].isdigit()
        ):
            left_ok = False
        if (
            end + 1 < len(text)
            and query[-1].isdigit()
            and text[end] == ","
            and text[end + 1].isdigit()
        ):
            right_ok = False
        if left_ok and right_ok:
            return True
        start = text.find(query, start + 1)
    return False


class RecipeSourceCache:
    """Hash-checked raw captures; never reuse the generic lossy Markdown cache."""

    def __init__(self, config: ReferenceValidationConfig, *, refresh=False, session=None):
        self.directory = Path(config.cache_dir) / "official-recipes-v1"
        self.refresh = refresh
        self.delay = config.rate_limit_delay
        self.session = session or requests.Session()
        self.memory: dict[str, ReferenceContent | RecipeReferenceError] = {}

    def path(self, source: RecipeSource) -> Path:
        return self.directory / (hashlib.sha256(source.url.encode()).hexdigest() + ".json")

    def _read(self, source: RecipeSource, path: Path) -> dict:
        try:
            if path.is_symlink():
                raise ValueError("symlink cache entry")
            is_pdf = source.provider == "dsmz_pdf"
            if path.stat().st_size > MAX_RESPONSE_BYTES * (8 if is_pdf else 6) + 4096:
                raise ValueError("oversized cache entry")
            capture = json.loads(path.read_text(encoding="utf-8"))
            if not (
                isinstance(capture["raw"], str)
                and len(capture["raw"].encode("utf-8")) <= MAX_RESPONSE_BYTES
                and capture["version"] == (PDF_CACHE_VERSION if is_pdf else CACHE_VERSION)
                and capture["url"] == source.url
                and capture["response_url"] == source.url
                and capture["http_status"] == 200
                and hashlib.sha256(capture["raw"].encode("utf-8")).hexdigest() == capture["sha256"]
            ):
                raise ValueError("capture metadata or checksum mismatch")
            datetime.datetime.fromisoformat(capture["accessed_at"])
            if is_pdf:
                payload = base64.b64decode(capture["pdf_base64"], validate=True)
                if not (
                    capture["media_type"] == "application/pdf"
                    and capture["encoding"] == "utf-8"
                    and capture["extraction"] == PDF_EXTRACTION
                    and hashlib.sha256(payload).hexdigest() == capture["pdf_sha256"]
                ):
                    raise ValueError("PDF capture metadata or checksum mismatch")
                text, count = extract_recipe_pdf(payload)
                if text != capture["raw"] or count != capture["pdf_pages"]:
                    raise ValueError("PDF extraction does not match the captured binary")
            return capture
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise RecipeReferenceError(
                f"source_cache: invalid raw cache entry {path.name}; use --refresh"
            ) from error

    def _fetch(self, source: RecipeSource) -> dict:
        is_pdf = source.provider == "dsmz_pdf"
        extra = {}
        try:
            with self.session.get(
                source.url,
                timeout=(10, 45),
                allow_redirects=False,
                stream=True,
                headers={"User-Agent": "CultureMech-reference-validation/1.0"},
            ) as response:
                if response.status_code != 200 or response.url != source.url:
                    raise RecipeReferenceError(
                        f"source_access: unexpected HTTP {response.status_code} or redirect for {source.url}"
                    )
                if is_pdf:
                    media_type = response.headers.get("Content-Type", "").split(";", 1)[0]
                    if media_type.strip().lower() != "application/pdf":
                        raise RecipeReferenceError("source_format: recipe PDF MIME type mismatch")
                chunks, length = [], 0
                for chunk in response.iter_content(chunk_size=65536):
                    length += len(chunk)
                    if length > MAX_RESPONSE_BYTES:
                        raise RecipeReferenceError(
                            "source_format: official recipe response exceeds size limit"
                        )
                    chunks.append(chunk)
                payload = b"".join(chunks)
                if is_pdf:
                    raw, count = extract_recipe_pdf(payload)
                    extra = {
                        "pdf_base64": base64.b64encode(payload).decode("ascii"),
                        "pdf_sha256": hashlib.sha256(payload).hexdigest(),
                        "pdf_pages": count,
                        "media_type": "application/pdf",
                        "encoding": "utf-8",
                        "extraction": dict(PDF_EXTRACTION),
                    }
                else:
                    raw = payload.decode("utf-8")
        except (requests.RequestException, UnicodeError) as error:
            raise RecipeReferenceError(
                f"source_access: could not retrieve {source.url}: {type(error).__name__}"
            ) from error
        finally:
            if self.delay:
                time.sleep(self.delay)
        return {
            "version": PDF_CACHE_VERSION if is_pdf else CACHE_VERSION,
            "url": source.url,
            "response_url": source.url,
            "http_status": 200,
            "raw": raw,
            "sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "accessed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            **extra,
        }

    def fetch(self, source: RecipeSource) -> ReferenceContent:
        if source.url in self.memory:
            saved = self.memory[source.url]
            if isinstance(saved, RecipeReferenceError):
                raise saved
            return saved
        path = self.path(source)
        try:
            if path.is_symlink():
                raise RecipeReferenceError("source_cache: refuse a symlink cache entry")
            cached = path.exists() and not self.refresh
            capture = self._read(source, path) if cached else self._fetch(source)
            metadata = {k: v for k, v in capture.items() if k not in {"raw", "pdf_base64"}}
            reference = parse_recipe(source, capture["raw"], metadata)
            if not cached:
                self.directory.mkdir(parents=True, exist_ok=True)
                if path.is_symlink():
                    raise RecipeReferenceError("source_cache: refuse to replace a symlink")
                temp_name = None
                try:
                    with tempfile.NamedTemporaryFile(
                        mode="w",
                        encoding="utf-8",
                        dir=self.directory,
                        prefix=".capture-",
                        delete=False,
                    ) as stream:
                        temp_name = stream.name
                        json.dump(capture, stream, ensure_ascii=True)
                        stream.write("\n")
                    os.replace(temp_name, path)
                finally:
                    if temp_name:
                        Path(temp_name).unlink(missing_ok=True)
            self.memory[source.url] = reference
            return reference
        except OSError as error:
            failure = RecipeReferenceError(
                f"source_cache: cannot read/write official recipe cache: {type(error).__name__}"
            )
            self.memory[source.url] = failure
            raise failure from error
        except RecipeReferenceError as error:
            self.memory[source.url] = error
            raise


class RecipeTextValidator:
    """Plugin-compatible validator; literature references retain upstream behavior."""

    def __init__(self, config: ReferenceValidationConfig, *, cache=None, refresh=False):
        self.config = config
        self.cache = cache or RecipeSourceCache(config, refresh=refresh)
        self.fallback = SupportingTextValidator(config)
        self.results: list[ValidationResult] = []

    def _official(self, reference_id, quote, title, path):
        source = recipe_source(reference_id)
        try:
            reference = self.cache.fetch(source)
            if title is not None and whitespace(title) != whitespace(reference.title):
                message = f"title_mismatch: expected {title!r}; official source title is {reference.title!r}"
            elif quote is not None and not any(
                literal_match(quote, text)
                for text in (
                    reference.content.splitlines()
                    if source.provider == "mediadb"
                    else [reference.content]
                )
            ):
                message = "snippet_mismatch: literal excerpt not found; brackets, case, signs, formula digits and units are preserved"
            else:
                return ValidationResult(
                    is_valid=True,
                    reference_id=reference_id,
                    supporting_text=quote or "",
                    path=path,
                    severity=ValidationSeverity.INFO,
                    message="Official recipe literal reference check passed",
                    match_result=(
                        SupportingTextMatch(found=True, similarity_score=1.0, matched_text=quote)
                        if quote is not None
                        else None
                    ),
                )
        except RecipeReferenceError as error:
            message = str(error)
        return ValidationResult(
            is_valid=False,
            reference_id=reference_id,
            supporting_text=quote or "",
            path=path,
            severity=ValidationSeverity.ERROR,
            message=message,
        )

    def validate(self, supporting_text, reference_id, expected_title=None, path=None):
        result = (
            self._official(reference_id, supporting_text, expected_title, path)
            if recipe_source(reference_id)
            else self.fallback.validate(
                supporting_text, reference_id, expected_title=expected_title, path=path
            )
        )
        self.results.append(result)
        return result

    def validate_title(self, reference_id, expected_title, path=None):
        result = (
            self._official(reference_id, None, expected_title, path)
            if recipe_source(reference_id)
            else self.fallback.validate_title(reference_id, expected_title, path=path)
        )
        self.results.append(result)
        return result
