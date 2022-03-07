$(document).ready( function() {
	alert("We are ready as well");

	$('.bar_link').on({
		mouseover: function() {
			$(this).css("background-color", "red") },
		mouseleave: function() {
			$(this).css("background-color", "skyblue") },
	});
});
