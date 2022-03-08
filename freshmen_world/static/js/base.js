$(document).ready( function() {

	$('.bar_link').on({
		mouseover: function() {
			$(this).css("background-color", "red") },
		mouseleave: function() {
			$(this).css("background-color", "skyblue") },
	});
});
