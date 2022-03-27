$().ready( function() {

	$("#body_block").css("background-image", 'url(../../static/images/taskmanagerbackground.jpg)');
    let dayCalculate = 1;
    let thirdPart = document.getElementById("thirdpart");

    for (var i = 0; i < 6; i++) {
        let perline = document.createElement("div");
        perline.setAttribute("class", "perline");
        for (var j = 0; j < 7; j++) {
            let date = document.createElement("div");
            let day = document.createElement("div");
            let message = document.createElement("div");
            date.setAttribute("class", "date");
            date.setAttribute("onclick", "showWindow(this)");
            day.setAttribute("class", "day");
            day.setAttribute("id", dayCalculate);
            var messageid = "message" + dayCalculate;
            message.setAttribute("class", "message");
            message.setAttribute("id", messageid.toString());
            date.appendChild(day);
            date.appendChild(message);
            perline.appendChild(date);
            dayCalculate += 1;
        }
        thirdPart.appendChild(perline);
    }
    update();
    addYearOptions();
    addMonthOptions();
    addDayOption();


});

// End of ready function

let date = new Date();
let currentMonth = date.getMonth();

function update_last_month() {
    date.setMonth(date.getMonth() - 1);
    update();
};

function update_next_month() {
    date.setMonth(date.getMonth() + 1);
    update();
};

function update() {
    let year = date.getFullYear();
    let month = date.getMonth();
    let day = date.getDate();
    let firstDay = new Date(year, month, 0).getDay();
    let monthLength = new Date(year, month + 1, 0).getDate();

    let array = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    $("#year").text(year);
    $("#month").text(array[month]);

    let j = firstDay;
    let z = 1;
    // Clearing information from last month, from before first day
    for (let i = 1; i <= j; i++) {
        $("#"+i.toString()).text("");
        $("#"+i.toString()).next(".message").text("");
    }
    // Clearing information from lat month, when month had more days/finished
    for (let i = monthLength; i < 42; i++) {
        $("#"+i.toString()).text("");
        $("#"+i.toString()).next(".message").text("");
    }

    for (let i = 1; i <= 42-j; i++) {
        getDayInfo(i, j, month+1, monthLength, year);
    }

    for (let i = 1; i <= monthLength; i++) {
        document.getElementById(j + i).innerHTML = z;
        if (document.getElementById(j + i).innerHTML == day && document.getElementById("month").innerHTML == array[currentMonth]) {
            document.getElementById(j + i).style.color = "red";
        } else {
            document.getElementById(j + i).style.color = "grey";
        }
        z++;
    }
}

let array = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
date = new Date();

function addYearOptions() {
    var option_day = document.getElementById("yearTime")
    for (var i = 2000; i < 2068 + 1; i++) {
        if (i == date.getFullYear()) {
            new_option = new Option(i, i.toString(), false, true);
        } else {
            new_option = new Option(i, i.toString());
        }
        option_day.add(new_option);
    };
};

function addMonthOptions() {
    var option_month = document.getElementById("monthTime");
    for (var i = 0; i < 12; i++) {
        if (i == date.getMonth()) {
            new_month = new Option(array[i], array[i], false, true);
        } else {
            new_month = new Option(array[i], array[i]);
        }
        option_month.add(new_month  )

        var option_day = document.getElementById("monthTime");
    };
};
function addDayOption() {
    var index = document.getElementById("monthTime").selectedIndex;
    var monthLength = new Date(date.getFullYear(), index + 1, 0).getDate();
    var option_day = document.getElementById("dayTime");
    option_day.options.length = 0;
    for (var i = 1; i < monthLength + 1; i++) {
        option_day.add(new Option(i, i.toString()));
    };
};

var showIndex;
function showWindow(obj) {
    document.getElementById("addTask").style.display = 'block';
    showIndex = obj.id;
};

function closeWindow() {
    document.getElementById("addTask").style.display = "none";
};

function getDayInfo(day, firstDay, month, monthLength, year) {
    var xhr = new XMLHttpRequest();
    if (day + firstDay > monthLength) {
        return;
    }
    xhr.open("POST", 'server/', true);
    let dayString = day.toString();
    let monthString = month.toString();
    let yearString = year.toString();
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function() { 
        if (this.readyState == 4 && this.status == 200) {
            let messageDictionary = JSON.parse(this.responseText);
            let tasks = messageDictionary.tasks;
            let actualDay = day + firstDay;
            if (tasks.length >= 1) {
                for (var i=0; i < tasks.length; i++) {
                    add_task_information(actualDay, tasks[i]);
                }
            } else {
                $("#"+actualDay.toString()).next(".message").text("");
            } 
        }
    }
    xhr.send("day="+dayString+"&month="+monthString+"&year="+yearString);
}

function add_task() {
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'add_task/', true);

    var task_name = $("#task").val().toString();
    var year = $("#yearTime").val();
    var month = $("#monthTime").val();
    var day = $("#dayTime").val();

    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function() { 
        if (this.readyState == 4 && this.status == 200) {
            let messageDictionary = JSON.parse(this.responseText);
            console.log(JSON.stringify(messageDictionary));
        }
    }
    xhr.send("task_name="+task_name+"&year="+year+"&month="+month+"&day="+day);
};

function add_task_information(i, task_information) {
    $("#"+i.toString()).next(".message").text(task_information); 
}