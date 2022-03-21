$(document).ready( function() {
    if (location.pathname == '/' || location.pathname == '/WOF/') {
    	$("a[href$='" + location.pathname + "']").addClass("current");
    } else {
    	$("a[href*='" + location.pathname + "']").addClass("current");
    }
});