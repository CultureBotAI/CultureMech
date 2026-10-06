/* Retained points keep their original data; navigation uses verified identities. */
const mapLinks = fetch('map-record-links.json').then(response => {
  if (!response.ok) throw new Error('Record links unavailable');
  return response.json();
}).catch(() => null);
window.openMapRecord = async function (point) {
  let notice = document.getElementById('map-record-status');
  if (!notice) {
    notice = document.createElement('p'); notice.id = 'map-record-status';
    notice.setAttribute('role', 'status'); notice.className = 'snapshot-note';
    document.querySelector('header').appendChild(notice);
  }
  const inventory = await mapLinks;
  const target = inventory?.links?.[point.category + '/' + point.id] || inventory?.links?.['*/' + point.id];
  if (target && /^\.\.\/pages\/normalized\/\d{6}\.html$/.test(target)) {
    location.href = target;
  } else {
    notice.textContent = inventory ? 'No verified current record link is available for this historical point. ' : 'Record links could not be loaded. Reload to retry, or browse current records. ';
    const browse = document.createElement('a'); browse.href = 'browser.html'; browse.textContent = 'Browse current records'; notice.appendChild(browse);
    notice.scrollIntoView({block:'nearest'});
  }
};
