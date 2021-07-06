// Confirm JS has been connected
console.log("JS Connected");

// Function to alert city has been clicked 
function message() {
    alert("Loading weather report...");
}

// Clicking "I Accept" button will eliminate the cookie pop-up
function elimCookie() {
    var cookie = document.querySelector(".cookie");
    cookie.remove();
}

function c2f(tChange) {
     return (9/5) * temp + 32;
}

// Changes temperature from Celsius to Farenheight
function tempChange(element) {
    var tChange = document.querySelectorAll("#convertT");
    console.log(tChange);
}



// In future, I want to check which temperature degree is chosen, and change it if the other drop down item is selected.