$(document).ready(function() {


$(".table-title").bind("click", function() {
 button = $(this).children().attr('id');
                $(this).children().toggleHTML('+', '-');
                button = "#"+button+"-table";
                $(button).slideToggle();
                return false;


});




$.fn.toggleHTML = function(a, b) {
    this.html(function(_, html) {
        return $.trim(html) === a ? b : a;
    });
}
	$("#locationHold").hide();
	$(".data-table").hide();
	$(".sourceRow").hide();
	
	$(".expand-button").bind("click", function() {
		button = $(this).attr('id');
		$(this).toggleHTML('+', '-');
		button = "#"+button+"-table";
		$(button).slideToggle();
		return false;
	
	});
	
	$(".expandAll").bind("click", function() {
		button = $(this).attr('id');
		button = "#"+button+"-all";
	    if ($(this).html().indexOf("Expand")>-1) {
		$(button).children("div.data-table").slideDown();
		$(button).children("div.table-title").children("a.expand-button").html("-");
	    } else {
		$(button).children("div.data-table").slideUp();
		$(button).children("div.table-title").children("a.expand-button").html("+");
	    }

		$(this).toggleHTML('Expand All +', 'Collapse All -');
		//$(button).children("div.data-table").slideToggle();
	    //$(button).children("div.table-title").children("a.expand-button").toggleHTML('+', '-');
	    return false;
	});
	
	 $(".map-link").bind("click", function() {
			$("#locationHold").toggle();
			map.render("mapLocation");
			$(".map-link").toggleHTML('Hide Map of Location', 'Show Map of Location');
			return false;

		});
		
	
	$(".source-link").bind("click", function() {
		source = $(this).attr('id');
		source = "#"+source.substring(0, source.lastIndexOf("link"));
		$(source).toggle();
		return false;
	});
	
	
		$(".expandAllI").bind("click", function() {
			$(".data-tablei").show();
			return false;
		});
		
		$(".expandAllC").bind("click", function() {
			$(".data-tablec").show();
			return false;
		});
	
		
	});
	
