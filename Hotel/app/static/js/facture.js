
		// Get today's date
		var today = new Date();
		var dd = String(today.getDate()).padStart(2, '0');
		var mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
		var yyyy = today.getFullYear();
	
		today = mm + '/' + dd + '/' + yyyy;
	
		// Calculate due date (one month from today)
		var dueDate = new Date(today);
		dueDate.setMonth(dueDate.getMonth() + 1);
		var due_dd = String(dueDate.getDate()).padStart(2, '0');
		var due_mm = String(dueDate.getMonth() + 1).padStart(2, '0');
		var due_yyyy = dueDate.getFullYear();
	
		dueDate = due_mm + '/' + due_dd + '/' + due_yyyy;
	
		// Insert today's date and due date into the respective HTML elements
		document.getElementById("createdDate").innerHTML = today;
		document.getElementById("dueDate").innerHTML = dueDate;
	
//------------------------------------------pdf------------------------------------------------------------------------------------


        
        