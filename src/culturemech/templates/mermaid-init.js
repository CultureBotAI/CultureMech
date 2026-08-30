import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

// Node geometry is computed in JS at layout time from these values, not from
// the stylesheet, so this is the only place node size can actually be set —
// a CSS `font-size` on `.nodeLabel` restyles the text after the box has
// already been measured and leaves the box exactly as large as it was.
//
// `htmlLabels: false` is the load-bearing setting, and it MUST be at the top
// level. Setting it only under `flowchart` leaves mermaid emitting
// `<foreignObject>` labels; measured under this page's CSP with mermaid 11,
// the four-ingredient diagram on CultureMech:000001 gives:
//
//     old config                       9 foreignObjects, 86px nodes, 77254px²
//     flowchart.htmlLabels only        5 foreignObjects, 64px nodes, 43411px²
//     top-level htmlLabels             0 foreignObjects, 26px nodes, 24375px²
//
// Both are set below: the top-level key is the one that works today, and the
// flowchart one costs nothing and states the same intent locally.
//
// Why HTML labels are so much worse *here* specifically: mermaid measures a
// `<foreignObject>` div, but this page's Content-Security-Policy is
// `style-src 'self'` (see media.html.j2), which blocks the inline stylesheet
// mermaid injects to size that div. The measurement falls back to unstyled
// browser defaults — the label computes at 16px with `line-height: normal`
// no matter what `themeVariables.fontSize` says. Plain SVG `<text>` is
// measured from the font the browser actually uses, so the box fits the label.
mermaid.initialize({
  startOnLoad: true,
  theme: "neutral",
  securityLevel: "strict",
  htmlLabels: false,
  themeVariables: {
    fontSize: "12px",
    fontFamily: "ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif",
  },
  flowchart: {
    htmlLabels: false,
    padding: 4,
    nodeSpacing: 26,
    rankSpacing: 42,
    useMaxWidth: true,
    curve: "basis",
  },
});
