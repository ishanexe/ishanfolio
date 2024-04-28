document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        console.log("Scroll event triggered.");
        var button = document.getElementById('backToTopButton');
        // Adjust the scroll threshold as needed
        if (window.scrollY > 100) {
            button.style.display = 'block'; // Show the button when scrolled down a bit
        } else {
            button.style.display = 'none'; // Hide the button when not scrolled enough
        }
    });
});
