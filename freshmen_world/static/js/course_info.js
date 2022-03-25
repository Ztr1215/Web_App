$().ready( function() {
	$("#content-button").click(function() {
		loadDoc();
	});
});

function loadDoc() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			let message = this.responseText;
			// JSON.parse() used to get rid of double quotes from JSON string.
			document.getElementById("xml-content").innerHTML = JSON.parse(message);
		}
	};
	xhttp.open("GET", "uni_course_info.txt", false);
	xhttp.send();
}