	function getCurrentDate() {
		const now = new Date();
		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}
	
	// Calculate the due date which is 30 days from now
	function getDueDate() {
		const now = new Date();
		now.setDate(now.getDate() + 30);
		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}
	
	// Set the invoice date and due date in the HTML
	document.addEventListener('DOMContentLoaded', function() {
		const invoiceDateElement = document.querySelector('#invoice-date');
		const dueDateElement = document.querySelector('#due-date');
	
		const currentDate = getCurrentDate();
		const dueDate = getDueDate();
	
		invoiceDateElement.textContent = currentDate;
		dueDateElement.textContent = dueDate;
	});
//------------------------------------------pdf------------------------------------------------------------------------------------


        
// function generatePDF() {
// 	// Select the element containing the invoice details
// 	const element = document.querySelector(".invoice-box");

// 	// Options for PDF generation
// 	const options = {
// 		margin: 10,
// 		filename: 'invoice.pdf',
// 		image: { type: 'jpeg', quality: 1 }, // Maximum quality JPEG images
// 		html2canvas: { scale: 3 }, // Increase scale for better quality
		
// 	};

// 	// Generate PDF from HTML element
// 	html2pdf()
// 		.set(options)
// 		.from(element)
// 		.save();
// }

// // Wait for content to load before generating PDF
// document.addEventListener("DOMContentLoaded", function () {
// 	document.getElementById("downloadButton").addEventListener("click", generatePDF);
// });