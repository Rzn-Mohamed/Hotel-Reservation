document.addEventListener('DOMContentLoaded', function() {
    // Pagination logic
    var pageLinks = document.querySelectorAll('.pagination .page-link');
    pageLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            var page = this.textContent.trim(); // Get the page number
            // Reload the page with query parameter 'page'
            var url = updateQueryStringParameter(window.location.href, 'page', page);
            window.location.href = url;
        });
    });

    // Function to update query string parameter
    function updateQueryStringParameter(uri, key, value) {
        var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
        var separator = uri.indexOf('?') !== -1 ? "&" : "?";
        if (uri.match(re)) {
            return uri.replace(re, '$1' + key + "=" + value + '$2');
        } else {
            return uri + separator + key + "=" + value;
        }
    }
});