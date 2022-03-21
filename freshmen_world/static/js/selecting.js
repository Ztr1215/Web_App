$(document).ready( function() {
    let nameOfCourses = document.getElementById('nameOfCourses');
    let icon = document.getElementById('icon')
    let selectingTable = document.getElementById('selecting_part');
    nameOfCourses.style.display = "grid";
    nameOfCourses.style.gridTemplateRows = "repeat(" + length + ",50px)";
    icon.style.display = "grid";
    icon.style.gridTemplateRows = "repeat(" + length + ",50px)";
    selectingTable.style.display = 'grid';
    selectingTable.style.gridTemplateRows = "repeat(" + rows + ",1fr)";

    for (var i = 0; i < length; i++) {
        var courseName = document.createElement("div");
        courseName.innerHTML = arr[i];
        nameOfCourses.appendChild(courseName);
        var iconName = document.createElement("div");
        iconName.innerHTML = arr[i].charAt(0);
        icon.appendChild(iconName);
    }
});

var arr = ["NOSE", "OOSE", "ADS2","CS1F","CS1S"];
let length = arr.length;
let rows = length + 2;
let isClose = true;

function close_extend() {
    var obj = document.getElementById('side_bar');
    var table = document.getElementById('selecting_part');
    if (isClose) {
        obj.style.animationName = 'side_bar_extend'
        table.style.animationName = 'small'
        isClose = false;
    } else {
        obj.style.animationName = 'side_bar_close'
        table.style.animationName = 'large'
        isClose = true;
    }
}
