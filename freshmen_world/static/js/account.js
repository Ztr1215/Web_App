function submit_delete(university_slug) {
	if (confirm("Are you sure you want to delete this university? You will delete all courses associated")) {
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "delete_university/", "true");
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send("university_slug="+university_slug);
		location.reload();
	} else {
		return null;
	}
}