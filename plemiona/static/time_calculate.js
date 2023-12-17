// java_styles.js
function updateCountdown() {
    var countdownElements = document.querySelectorAll('[data-arrival-time]');

    countdownElements.forEach(function(element) {
        var arrivalTime = new Date(element.getAttribute('data-arrival-time')).getTime();
        var now = new Date().getTime();
        var distance = arrivalTime - now;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        element.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        if (distance < 0) {
            element.innerHTML = "Zakończone";
        }
    });
}
// Aktualizuj odliczanie co sekundę
setInterval(updateCountdown, 1000);
