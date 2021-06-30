console.log("page loaded...");

function autoPlay() {
    var video = document.querySelector("#video");
    video.muted = true;
    video.play();
}

function offPause() {
    var video = document.querySelector("#video");
    video.currentTime = 0;
    video.pause();
}