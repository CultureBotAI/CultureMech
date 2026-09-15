/* A map link appears only after the site builder publishes validated map status. */
(function () {
  "use strict";
  fetch("text_map_status.json", {cache: "no-store"})
    .then(function (response) {
      if (!response.ok) throw new Error("Map status unavailable");
      return response.json();
    })
    .then(function (status) {
      if (status && status.enabled === true) {
        document.querySelectorAll("[data-text-map-link]").forEach(function (link) {
          link.hidden = false;
        });
      }
    })
    .catch(function () { /* Keep unavailable maps hidden. */ });
}());
