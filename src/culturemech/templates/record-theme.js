/* The record CSP permits external scripts and styles only. Share the browser's
 * preference key without injecting inline style or weakening the policy. */
(function () {
  const root = document.documentElement;
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  try {
    const saved = localStorage.getItem('mech-theme');
    if (saved === 'dark' || saved === 'light') root.dataset.theme = saved;
  } catch (error) { /* Storage may be disabled; the OS preference still works. */ }
  function mount() {
  const button = document.getElementById('record-theme');
  function refresh() {
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : preference.matches;
    button.setAttribute('aria-pressed', String(dark));
    button.textContent = dark ? 'Light mode' : 'Dark mode';
  }
  button.addEventListener('click', function () {
    const dark = button.getAttribute('aria-pressed') === 'true';
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('mech-theme', root.dataset.theme); } catch (error) {}
    refresh();
  });
  preference.addEventListener('change', refresh);
  refresh();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount);
  else mount();
})();
