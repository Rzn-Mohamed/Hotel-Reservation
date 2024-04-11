document.addEventListener("DOMContentLoaded", function() {
    var dropdownButtons = document.querySelectorAll("[data-dropdown-toggle]");
    dropdownButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.stopPropagation();
            var dropdownId = button.getAttribute("data-dropdown-toggle");
            var dropdownMenu = document.getElementById(dropdownId);
            dropdownMenu.classList.toggle("hidden");
        });
    });

    document.addEventListener("click", function(event) {
        dropdownButtons.forEach(function(button) {
            var dropdownId = button.getAttribute("data-dropdown-toggle");
            var dropdownMenu = document.getElementById(dropdownId);
            if (!dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.add("hidden");
            }
        });
    });
});
