function res_form(price, services) {
  let servicesHTML = '';
  if (services && services.length > 0) {
    servicesHTML += `<div class="grid grid-cols-2 gap-2">`; // Start the grid outside the loop
    for (let i = 0; i < services.length; i++) {
      servicesHTML += `
        <div>
          ${services[i]}
          <input type="checkbox" name="service_${i}" id="service_${i}" class="border mt-1 rounded px-2 w-full bg-gray-50" value="${services[i]}"/>
        </div>
      `;
    }
    servicesHTML += `</div>`; // Close the grid after the loop
  }

  Swal.fire({
    html: `
    <form id="reservationForm" action="clientAddreservation" method="POST">
      
      <div class="lg:col-span-2 mr-2">
        <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-5">
          <div class="md:col-span-5">
            <label for="checkin">Check-in</label>
            <input type="date" name="checkin" id="checkin" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" />
          </div>
          <div class="md:col-span-5">
            <label for="checkout">Check-out</label>
            <input type="date" name="checkout" id="checkout" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" />
          </div>
          <div class="md:col-span-3">
            <label for="room_price">Room price</label>
            <input type="text" name="room_price" id="room_price" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="${price}" placeholder="" disabled/>
          </div>
          <div class="md:col-span-3">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </div>
        ${servicesHTML}
      </div>
    </form>
    `,
    showCloseButton: true,
    focusConfirm: false,
    confirmButtonText: '<i class="fa fa-thumbs-up"></i> Submit',
    confirmButtonAriaLabel: "Thumbs up, great!"
  });
  
  // Handle form submission
  document.getElementById("reservationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch("clientAddreservation", {
      method: "POST",
      body: formData
    }).then(response => {
      console.log('ok')
    }).catch(error => {
      // Handle error
    });
  });
}
