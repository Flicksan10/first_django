const mapContainer = document.getElementById('mapContainer');
let isDown = false;
let startX;
let scrollLeft;
let scrollTop;

mapContainer.addEventListener('mousedown', (e) => {
    isDown = true;
    mapContainer.classList.add('grabbing');
    startX = e.pageX - mapContainer.offsetLeft;
    scrollLeft = mapContainer.scrollLeft;
    scrollTop = mapContainer.scrollTop;
});

mapContainer.addEventListener('mouseleave', () => {
    isDown = false;
    mapContainer.classList.remove('grabbing');
});

mapContainer.addEventListener('mouseup', () => {
    isDown = false;
    mapContainer.classList.remove('grabbing');
});

mapContainer.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - mapContainer.offsetLeft;
    const walkX = (x - startX) * 1; // Prędkość przewijania
    mapContainer.scrollLeft = scrollLeft - walkX;
    const y = e.pageY - mapContainer.offsetTop;
    const walkY = (y - startX) * 1; // Prędkość przewijania
    mapContainer.scrollTop = scrollTop - walkY;
});
