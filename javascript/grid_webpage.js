// Initialize map
const map = L.map('map').setView([49.5, -81.5], 5);
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}').addTo(map);

// Set url to titiler file
titilerBase = "http://127.0.0.1:8000";
const cogFilePath = `data/example_cog.tif`;
const tileUrl = `${titilerBase}/cog/tiles/WebMercatorQuad/{z}/{x}/{y}?url=${encodeURIComponent(cogFilePath)}`;

// Create leaflet layer
mapLayer = L.tileLayer(tileUrl, { opacity: 0.8 }).addTo(map);
