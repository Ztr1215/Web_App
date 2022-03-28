// put the array of pictures' name which is got from database.
let images_arr = ["img_1.jpg", "img_2.jpg", "img_3.jpg", "img_4.jpg", "img_5.jpg"];

let index = 0;
let dotlist;

$().ready(function () {
    document.getElementById("content").style.backgroundImage = "url(/static/images/homepagebc.jpg)";
    document.getElementById("info_of_uni").style.backgroundImage = "url(/static/images/homepagebc.jpg)";
    document.getElementById("helper").style.backgroundImage = "url(/static/images/homepagebc.jpg)";
    document.getElementById("weather").style.backgroundImage = "url(/static/images/homepagebc.jpg)";

    let schoolimg = document.getElementById("schoolimg");

    schoolimg.style.backgroundImage = "url(/static/images/" + images_arr[index] + ")";

    // If the University is in the Glasgow
    var url = "http://api.weatherapi.com/v1/current.json?key=9df25054928f44b4975134755222403&q=Glasgow&aqi=yes";

    // If the University is in the Melrose
    // var url = "http://api.weatherapi.com/v1/current.json?key=9df25054928f44b4975134755222403&q=Melrose&aqi=yes";

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

// to change the background image.
function right() {
    if (index >= 0 && index < images_arr.length - 1) {
        index += 1;
        schoolimg.style.backgroundImage = "url(/static/images/" + images_arr[index] + ")";
    } else {
        index = 0;
        schoolimg.style.backgroundImage = "url(/static/images/" + images_arr[index] + ")";
    }
}

// to change the background image.
function left() {
    if (index > 0 && index <= images_arr.length - 1) {
        index -= 1;
        schoolimg.style.backgroundImage = "url(/static/images/" + images_arr[index] + ")";
    } else {
        index = images_arr.length - 1;
        schoolimg.style.backgroundImage = "url(/static/images/" + images_arr[index] + ")";
    }
}