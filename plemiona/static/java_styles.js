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
            var info = this.querySelector('.foreground-image').getAttribute('data-info');
            var rect = this.getBoundingClientRect();
            infoBox.innerHTML = info;
            infoBox.classList.add('visible');
            infoBox.style.left = rect.left + window.scrollX + 'px';
            infoBox.style.top = rect.bottom + window.scrollY + 'px';
        });

        village.addEventListener('mouseout', function() {
            infoBox.classList.remove('visible');
        });
    });
});


