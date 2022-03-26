$(document).ready( function() {
    if (location.pathname == '/') {
    	$("a[href$='" + location.pathname + "']").addClass("current");
        $("#course-button").addClass("current");
    } else if (location.pathname == '/WOF/'){
        $("a[href$='" + location.pathname + "']").addClass("current");
    } else {
        $("a[href*='" + location.pathname + "']").addClass("current");
    }
});