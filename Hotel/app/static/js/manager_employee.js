
    document.addEventListener("DOMContentLoaded", function() {
        var modal = document.getElementById('exampleModalCenter');
        var btn = document.getElementById("openModalBtn");
        var span = document.querySelector(".modal-header .close");

        btn.onclick = function() {
          
            modal.classList.add('show');
            modal.style.display = "block";
            document.body.classList.add('modal-open');
        }

        span.onclick = function() {
            modal.classList.remove('show');
            modal.style.display = "none";
            document.body.classList.remove('modal-open');
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.classList.remove('show');
                modal.style.display = "none";
                document.body.classList.remove('modal-open');
            }
        }
    });
