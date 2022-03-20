$(document).ready( function() {
    if (location.pathname == '/' || location.pathname == '/WOF/') {
    	$("a[href$='" + location.pathname + "']").addClass("current");
    	console.log("WORKING NOW");
    } else {
    	$("a[href*='" + location.pathname + "']").addClass("current");
    }
    console.log(location.pathname);
});