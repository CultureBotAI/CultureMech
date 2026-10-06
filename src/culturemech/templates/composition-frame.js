(async () => {
  const status = document.getElementById('status');
  try {
    const {default: mermaid} = await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs');
    let generation = 0;
    let queue = Promise.resolve();
    window.addEventListener('message', event => {
      if (event.source !== parent || event.data?.type !== 'composition' || typeof event.data.source !== 'string') return;
      const data = event.data, own = ++generation;
      queue = queue.then(async () => {
        if (own !== generation) return;
        document.body.classList.toggle('dark', !!data.dark);
        mermaid.initialize({startOnLoad:false,theme:data.dark?'dark':'neutral',securityLevel:'strict',htmlLabels:false,
          themeVariables:{fontSize:'12px',fontFamily:'system-ui, sans-serif'},flowchart:{htmlLabels:false,padding:4,nodeSpacing:26,rankSpacing:42,useMaxWidth:true}});
        try {
          const {svg} = await mermaid.render('composition-'+own, data.source);
          if (own !== generation) return;
          document.getElementById('diagram').innerHTML = svg;
          status.textContent = '';
          parent.postMessage({type:'composition-rendered',height:document.body.scrollHeight+20}, '*');
        } catch (_error) { status.textContent = 'The composition diagram could not be rendered. The ingredient table in the record remains available.'; }
      });
    });
    parent.postMessage({type:'composition-ready'}, '*');
  } catch (_error) { status.textContent = 'The composition diagram could not be loaded. The ingredient table in the record remains available. Reload to retry.'; }
})();
