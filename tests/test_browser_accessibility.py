from html.parser import HTMLParser
from pathlib import Path


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.items = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

    def find(self, tag=None, **attrs):
        return [
            a
            for t, a in self.items
            if (tag is None or t == tag)
            and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in attrs.items())
        ]


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = "https://culturebotai.github.io/mechs/"


def test_browser_names_search_and_announces_result_changes():
    dom = Elements((ROOT / "app/browser.html").read_text())
    assert dom.find("label", for_="searchInput")
    assert dom.find(id="resultsCount", role="status", aria_live="polite")
    assert dom.find("a", href=DIRECTORY)


def test_generated_record_shell_has_mobile_landmarks_and_resolvable_theme(tmp_path):
    import yaml

    from culturemech.render_media_pages import render_pages

    source = tmp_path / "source.yaml"
    source.write_text(
        yaml.safe_dump({"id": "CultureMech:123456", "name": "Test", "ingredients": []})
    )
    index = tmp_path / "site/pages"
    output = index / "normalized"
    assert render_pages(source_files=[source], out_dir=output, index_dir=index) == 0
    for page in [index / "index.html", output / "123456.html"]:
        dom = Elements(page.read_text())
        assert dom.find("meta", name="viewport", content="width=device-width, initial-scale=1")
        assert dom.find("main", id="main-content")
        assert dom.find("button", id="record-theme")
        assert dom.find("a", href=DIRECTORY)
        theme = [
            a["src"] for a in dom.find("script") if a.get("src", "").endswith("record-theme.js")
        ]
        assert len(theme) == 1 and (page.parent / theme[0]).is_file()
        assert "unsafe-inline" not in page.read_text()


def test_browser_javascript_parses(tmp_path):
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser JavaScript syntax check")
    html = (ROOT / "app/browser.html").read_text()
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
    assert scripts
    for number, script in enumerate(scripts):
        source = tmp_path / f"inline-{number}.js"
        source.write_text(script)
        checked = subprocess.run([node, "--check", str(source)], capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr


def test_actual_loader_distinguishes_failed_initialization_from_empty_data(tmp_path):
    import json
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser loader runtime check")
    html = (ROOT / "app/browser.html").read_text()
    script = next(
        s
        for s in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
        if "function onDataReady" in s
    )
    harness = r"""
const vm = require('node:vm');
const source = SOURCE;
const schema = {facets:[], searchableFields:['name'], colors:{}, linkResolvers:{}};
const recipe = {name:'Salt medium', html_page:'normalized/1.html', category:'bacteria', medium_type:'defined'};
const cases = [
  ['empty', [], schema, false],
  ['record', [recipe], schema, false],
  ['missing-data', undefined, schema, true],
  ['null-row', [null], schema, true],
  ['missing-colors', [recipe], {facets:[],searchableFields:[]}, true],
  ['invalid-facet', [recipe], {...schema, facets:[null]}, true],
  ['render-throws', [{...recipe, target_organism_names:'invalid-array'}], schema, true],
];
function element() {return {textContent:'',innerHTML:'',value:'',style:{},dataset:{},children:[],
  addEventListener(){},appendChild(child){this.children.push(child);}};}
for (const [name, data, config, failed] of cases) {
  const elements = new Map();
  const document = {getElementById(id){if(!elements.has(id))elements.set(id,element());return elements.get(id);},
    createElement:element,createTextNode:element,querySelectorAll(){return []}};
  const context = {document,window:{culturemechData:data,searchSchema:config,location:{reload(){}}}};
  vm.createContext(context);vm.runInContext(source,context);
  const count=elements.get('resultsCount'), container=elements.get('resultsContainer');
  if(failed) {
    if(count.textContent!=='Recipes could not be loaded.')throw Error(name+': missing failure status');
    if(!container.children.some(child=>child.textContent==='Retry loading recipes'))throw Error(name+': no retry');
    if(vm.runInContext('dataReady',context))throw Error(name+': falsely ready');
    context.applyFilters();context.clearAllFilters();
    if(count.textContent!=='Recipes could not be loaded.')throw Error(name+': failure hidden');
  } else {
    if(!vm.runInContext('dataReady',context))throw Error(name+': valid catalog rejected');
    if(count.textContent!==`${data.length} recipe${data.length===1?'':'s'}`)throw Error(name+': wrong count');
    context.applyFilters();context.clearAllFilters();
  }
}
""".replace("SOURCE", json.dumps(script))
    runtime = tmp_path / "loader-contract.cjs"
    runtime.write_text(harness)
    checked = subprocess.run([node, str(runtime)], capture_output=True, text=True)
    assert checked.returncode == 0, checked.stderr
