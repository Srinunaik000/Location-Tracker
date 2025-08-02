// static/map.js
let map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
let marker;

function fetchLocation() {
  fetch('/locations')
    .then(res => res.json())
    .then(data => {
      if (data.length > 0) {
        let latest = data[data.length - 1];
        let latlng = [latest.lat, latest.lon];
        if (!marker) {
          marker = L.marker(latlng).addTo(map);
        } else {
          marker.setLatLng(latlng);
        }
        map.setView(latlng, 15);
      }
    });
}

setInterval(fetchLocation, 3000);
