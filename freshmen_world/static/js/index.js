let images_arr = ["img_1.jpg", "img_2.jpg", "img_3.jpg", "img_4.jpg", "img_5.jpg"];

$().ready( function () {
    document.getElementById("content").style.backgroundImage = "url(/static/images/homepagebc.jpg)"
    document.getElementById("info_of_uni").style.backgroundImage = "url(/static/images/homepagebc.jpg)"
    document.getElementById("helper").style.backgroundImage = "url(/static/images/homepagebc.jpg)"
    document.getElementById("weather").style.backgroundImage = "url(/static/images/homepagebc.jpg)"
    document.getElementById("img1").style.backgroundImage = "url(/static/images/img_1.jpg)"
    document.getElementById("img2").style.backgroundImage = "url(/static/images/img_2.jpg)"
    document.getElementById("img3").style.backgroundImage = "url(/static/images/img_3.jpg)"
    document.getElementById("img4").style.backgroundImage = "url(/static/images/img_4.jpg)"
    document.getElementById("img5").style.backgroundImage = "url(/static/images/img_5.jpg)"

    // If the University is in the Glasgow
    // var url = "http://api.weatherapi.com/v1/current.json?key=9df25054928f44b4975134755222403&q=Glasgow&aqi=yes";

    // If the University is in the Melrose
    var url = "http://api.weatherapi.com/v1/current.json?key=9df25054928f44b4975134755222403&q=Melrose&aqi=yes";

    var request;
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest();
    }
    request.onreadystatechange = function () {
        if (request.readyState == 4) {
            var jsonObj = JSON.parse(request.responseText);
            document.getElementById("city").innerHTML = jsonObj.location.name;
            document.getElementById("update_time").innerHTML = jsonObj.current.last_updated;
            document.getElementById("weather_text").innerHTML = jsonObj.current.condition.text;
        }
    }
    request.open("GET", url, true);
    request.send();
});

let index = 1;
let position = -40;
function right() {
    if (index >= 1 && index < 5) {
        position = position - 680;
        document.getElementById("images").style.left = position + "px";
        index += 1;
    } else if (index = 5) {
        document.getElementById("images").style.left = "-40px";
        index = 1;
        position = -40;
    }
}

function left() {
    if (index > 1 && index <= 5) {
        position = position + 680;
        document.getElementById("images").style.left = position + "px";
        index -= 1;
    } else if (index = 1) {
        document.getElementById("images").style.left = "-2760px";
        index = 5;
        position = -2760
    }
}

function dot1() {
    document.getElementById("images").style.left = -40 + "px";
    index = 1;
    position = -40
}
function dot2() {
    document.getElementById("images").style.left = -720 + "px";
    index = 2;
    position = -720
}
function dot3() {
    document.getElementById("images").style.left = -1400 + "px";
    index = 3;
    position = -1400
}
function dot4() {
    document.getElementById("images").style.left = -2080 + "px";
    index = 4;
    position = -2080
}
function dot5() {
    document.getElementById("images").style.left = -2760 + "px";
    index = 5;
    position = -2760
}