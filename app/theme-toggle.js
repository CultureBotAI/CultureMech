/* Mech theme toggle — vendored byte-identical across all Mech sites.
 * Applies the saved theme to <html data-theme> (falling back to the OS
 * preference) before paint, and injects a self-contained fixed toggle button.
 * No dependencies; no per-page markup or CSS required beyond loading this file.
 * The page's own dark palette is supplied via :root[data-theme="dark"] and the
 * prefers-color-scheme media query in that page's stylesheet. */
(function () {
  var KEY = 'mech-theme';
  var root = document.documentElement;

  function osDark() {
    return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }
  function current() {
    return root.getAttribute('data-theme') || (osDark() ? 'dark' : 'light');
  }

  // Apply the saved preference as early as possible to avoid a flash.
  try {
    var saved = localStorage.getItem(KEY);
    if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
  } catch (e) {}

  function setIcon(btn) {
    var dark = current() === 'dark';
    btn.querySelector('.theme-toggle-icon').textContent = dark ? '☀' : '☾'; // sun / moon
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
  }
  function toggle(btn) {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
    setIcon(btn);
  }
  function mount() {
    if (document.querySelector('.theme-toggle')) return;

    var css =
      '.theme-toggle{position:fixed;bottom:18px;right:18px;z-index:2000;width:40px;height:40px;' +
      'border-radius:50%;border:1px solid var(--line,var(--border,rgba(128,128,128,.4)));' +
      'background:var(--card,var(--surface,var(--card-bg,#fff)));' +
      'color:var(--ink,var(--text,var(--fg,#1a1a1a)));font-size:18px;line-height:1;cursor:pointer;' +
      'display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.25);' +
      'transition:border-color .15s,transform .15s;}' +
      '.theme-toggle:hover{border-color:var(--accent,var(--primary,var(--brand-1,#888)));transform:translateY(-1px);}' +
      '.theme-toggle:focus-visible{outline:2px solid var(--accent,var(--primary,#888));outline-offset:2px;}' +
      '@media (prefers-reduced-motion: reduce){.theme-toggle{transition:none;}}';
    var st = document.createElement('style');
    st.textContent = css;
    document.head.appendChild(st);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle';
    btn.setAttribute('aria-label', 'Toggle dark mode');
    btn.title = 'Toggle light / dark';
    btn.innerHTML = '<span class="theme-toggle-icon" aria-hidden="true"></span>';
    btn.addEventListener('click', function () { toggle(btn); });
    document.body.appendChild(btn);
    setIcon(btn);

    // If the visitor has no explicit choice, follow live OS-theme changes.
    if (window.matchMedia) {
      try {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
          if (!root.getAttribute('data-theme')) setIcon(btn);
        });
      } catch (e) {}
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount);
  else mount();
})();
