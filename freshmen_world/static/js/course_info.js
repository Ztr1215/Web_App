$().ready( function() {
	$("#content-button").click(function() {
		loadDoc();
	});
});

function loadDoc() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			console.log("At this point");
			document.getElementById("xml-content").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "uni_course_info.txt", true);
	xhttp.send();
}