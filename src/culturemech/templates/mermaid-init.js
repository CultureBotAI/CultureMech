import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

// Node geometry is computed in JS at layout time from these values, not from
// the stylesheet, so this is the only place node size can actually be set —
// a CSS `font-size` on `.nodeLabel` restyles the text after the box has
// already been measured and leaves the box exactly as large as it was.
//
// `htmlLabels: false` matters most. With HTML labels mermaid measures a
// `<foreignObject>` div, but this page's Content-Security-Policy is
// `style-src 'self'`, which blocks the inline stylesheet mermaid injects to
// size that div. The measurement then falls back to unstyled browser
// defaults and every node comes out far larger than its label needs. Plain
// SVG `<text>` is measured from the font metrics the browser actually uses,
// so the box fits the label.
mermaid.initialize({
  startOnLoad: true,
  theme: "neutral",
  securityLevel: "strict",
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
