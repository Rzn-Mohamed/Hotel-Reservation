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
////////////////////////////////////////////////////////


function deleteReservation(reservationId) {
    if (confirm('Are you sure you want to delete this reservation?')) {
        // Perform AJAX request to delete the reservation
        // Example using Fetch API
        fetch(`/delete-reservation/${reservationId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            if (response.ok) {
                // Reload the page or update UI as needed
                location.reload(); // Example: reload the page
            } else {
                // Handle errors
                console.error('Failed to delete reservation');
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

// Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if the cookie name matches the csrf token name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
