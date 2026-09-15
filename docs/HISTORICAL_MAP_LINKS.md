# Retained historical media maps

`app/umap.html` and `app/umap_graph.html` retain their historical point populations and coordinates. Their embedding input and reducer lineage remain unverified; repairing record links does not establish that provenance or borrow the ingredient-map receipt.

The historical generator uses the source YAML filename stem as `medium_id` (`embedding/aggregator_yaml_source.py`), and `visualization/umap_generator.py` copies it into each point ID. The route repair joins that exact ID to current `app/data.js` source filenames, first by category plus stem, then by a globally unique stem when categories moved. It never joins display labels. Ambiguous or missing identities open the working media browser, with an explicit tooltip explanation.

After regenerating browser data and normalized record pages, run `just repair-historical-map-links` to preview, `just repair-historical-map-links --apply` to update, or `just repair-historical-map-links --check` to verify. Pages runs the repair after both page renderers and before site staging. All current browser rows must match the ignored-inclusive YAML corpus, current record IDs and renderer routes, and existing page files. Each retained point preserves every field except its route and added link-resolution metadata. The command reports point counts, resolution counts, source bytes and preserved payload hashes.

All inputs and both replacement files are validated before writing. Individual HTML replacements are atomic; replacing the pair is not a multi-file transaction. A failed Pages step prevents deployment, and rerunning the repair is idempotent.
