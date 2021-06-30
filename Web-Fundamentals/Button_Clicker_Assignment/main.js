console.log("JS files connected");

function changeLogin(element){
    if(element.innerText == "Login"){
        element.innerHTML = "Logout";
    } 
    else {
        element.innerText = "Login";
    }
}

function addLikes(element) {
    likes[0]++;
    element.innerText = likes[0] + " likes";
    alert("Ninja was liked!");
}

function removeDef(element) {
    element.remove();
}