function sendJSON(){

            let name = document.querySelector('#name');
            let email = document.querySelector('#email');
            let age = document.querySelector('#age');
            let pass = document.querySelector('#pass');
	    let preferred = document.querySelector('#preferred');


            // Creating a XHR object
            let xhr = new XMLHttpRequest();
            let url = "/informationUser/edit";

            // open a connection
            xhr.open("POST", url, true);

            // Set the request header i.e. which type of content you are sending
            xhr.setRequestHeader("Content-Type", "application/json");

            // Create a state change callback
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {

                    // Print received data from server
                    location.replace(this.responseText);

                }
                else {
                    document.getElementById("demo").innerHTML = "Error: Hay thuc hien lai hanh dong";
                }
            };

            // Converting JSON data to string
            var data = JSON.stringify({ "name": name.value,
                                        "email": email.value,
                                        "age": age.value,
					"preferred": preferred.value,
                                        "password": pass.value,});

            // Sending data with the request
            xhr.send(data);
        }