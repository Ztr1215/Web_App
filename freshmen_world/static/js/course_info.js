$().ready( function() {
	$("#content-button").click(function() {
		loadDoc();
	});
});

function loadDoc() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		console.log("readyState : " + this.readyState + " status : " + this.status);
		if (this.readyState == 4 && this.status == 200) {
			let message = JSON.parse(this.responseText);
			// JSON.parse() used to read dictionary.
			document.getElementById("xml-content").innerHTML = message.course_text;
		}
	};
	xhttp.open("GET", "uni_course_info.txt", true);
	xhttp.send();
}