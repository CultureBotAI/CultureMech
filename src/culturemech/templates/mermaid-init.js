// Keep the record's strict CSP. Mermaid's dynamic styles are confined to a
// sandboxed presentation frame with no same-origin or navigation permission.
const frameURL = new URL('composition-frame.html', import.meta.url);
for (const source of document.querySelectorAll('pre.mermaid')) {
  const frame = document.createElement('iframe');
  frame.title = 'Ingredient composition diagram';
  frame.className = 'composition-frame';
  frame.setAttribute('sandbox', 'allow-scripts');
  frame.height = '480';
  frame.src = frameURL.href;
  const send = () => frame.contentWindow.postMessage({type:'composition', source:source.textContent,
    dark: document.documentElement.dataset.theme === 'dark' || (!document.documentElement.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches)}, '*');
  window.addEventListener('message', event => {
    if (event.source !== frame.contentWindow) return;
    if (event.data?.type === 'composition-ready') send();
    if (event.data?.type === 'composition-rendered') {
      source.hidden = true;
      frame.height = String(Math.max(240, Math.min(1600, Number(event.data.height) || 480)));
    }
  });
  new MutationObserver(send).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change',send);
  source.after(frame);
}
