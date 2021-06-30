console.log("JS Connected")

// Array the html will pull from
var numLikes = [9,12,9];
var firstLikes = document.querySelector("#firstLikes");
var secondLikes = document.querySelector("#secondLikes");
var thirdLikes = document.querySelector("#thirdLikes");

// To increment likes
function addLikes1(){
    numLikes[0]++;
    firstLikes.innerText = numLikes[0]+" like(s)";
}

function addLikes2(){
    numLikes[1]++;
    secondLikes.innerText = numLikes[1]+" like(s)";
}

function addLikes3(){
    numLikes[2]++;
    thirdLikes.innerText = numLikes[2]+" like(s)";
}