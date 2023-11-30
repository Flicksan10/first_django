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

document.addEventListener('DOMContentLoaded', function() {
    const villages = document.querySelectorAll('.image-container a');
    const infoBox = document.getElementById('village-info');

    villages.forEach(village => {
        village.addEventListener('mouseover', function(event) {
            const villageData = this.querySelector('.foreground-image').title;
            infoBox.innerHTML = villageData;
            infoBox.style.display = 'block';
            infoBox.style.left = event.pageX + 'px';
            infoBox.style.top = event.pageY + 'px';
        });

        village.addEventListener('mouseout', function() {
            infoBox.style.display = 'none';
        });
    });
});
