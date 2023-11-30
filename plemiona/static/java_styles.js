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
    const hitboxes = document.querySelectorAll('.hitbox');
    const infoBox = document.getElementById('village-info');

    hitboxes.forEach(hitbox => {
        hitbox.addEventListener('mouseover', function(event) {
            var info = this.getAttribute('data-info');
            infoBox.innerHTML = info;
            infoBox.classList.add('visible');

            // Dodajemy stałą wartość do pozycji, aby przesunąć infoBox dalej od kursora
            const offset = 20; // Możesz dostosować tę wartość według potrzeb
            infoBox.style.left = (event.clientX + offset) + 'px';
            infoBox.style.top = (event.clientY + offset) + 'px';
        });

        hitbox.addEventListener('mouseout', function() {
            infoBox.classList.remove('visible');
        });
    });
});





