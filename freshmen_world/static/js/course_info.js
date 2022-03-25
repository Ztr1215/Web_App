$().ready( function() {
	$("#content-button").click(function() {
		loadDoc();
	});
});

function loadDoc() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var response = this.responseText;


			document.getElementById("xml-content").innerHTML = response;
		}
	};
	xhttp.open("GET", "uni_course_info.txt", false);
	xhttp.send();
}