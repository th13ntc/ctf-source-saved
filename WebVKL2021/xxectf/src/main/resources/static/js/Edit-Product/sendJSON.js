function sendJSON(){

            let name = document.querySelector('#name');
            let price = document.querySelector('#price');
            let number = document.querySelector('#number');
            let image = document.querySelector('#image');
            let id = document.querySelector('#id');
            // Creating a XHR object
            let xhr = new XMLHttpRequest();
            let url = "/admin/editProduct";
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
                    document.getElementById("msg").innerHTML = "Error: Hay thuc hien lai hanh dong";
                }
            };

            // Converting JSON data to string
            var data = JSON.stringify({ "name_product": name.value,
                                        "price": price.value,
                                        "number": number.value,
                                        "image": image.value,
                                        "id_product": id.value});

            // Sending data with the request
            xhr.send(data);
        }