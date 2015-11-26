$(document).ready(function() {

	$(".toHide").hide();

	 var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
     var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
	$(".expand-list").bind("click", function() {
		button = $(this).attr('id');
	    text = $(this).text().substring(2);
		$(this).html($(this).text() == '+ '+text?'- '+text : '+ '+text);
		
		button = "#"+button+"-list";
		$(button).toggle();
		return false;
	
	});
	
	$(".qLink").bind("click", function() {
		button = $(this).html();
		$(".chosen").removeClass("chosen");
		$(this).parent().toggleClass("chosen");
		$.getJSON("/compare/", {xhr:"true", question:button},
			function(data) {
			vectors.removeAllFeatures();
				colors = new Array();
				if (data.length != 0) {
				numOfChoices = data[0].choices.length;
				zeroStart = data[0].Zero;
				if (numOfChoices == 2) {
					colors = ["#fff08d", "black"];
					$(".add").empty();
				        $(".add").append("<div class=questext>"+button+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq1></div>"+data[0].choices[0].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq5></div>"+data[0].choices[1].split("(")[0]+"</div>");
				} else if (numOfChoices == 3) {
					var colors = ["#fff08d", "#ff0b00", "black"];
					
					$(".add").empty();
				        $(".add").append("<div class=questext>"+button+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq1></div>"+data[0].choices[0].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq4></div>"+data[0].choices[1].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq5></div>"+data[0].choices[2].split("(")[0]+"</div>");

				} else if (numOfChoices == 4) {
					var colors = ["#fff08d", "#ffbb4e", "#b0867f", "black"];
					
					$(".add").empty();
				        $(".add").append("<div class=questext>"+button+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq1></div>"+data[0].choices[0].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq2></div>"+data[0].choices[1].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq3></div>"+data[0].choices[2].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq5></div>"+data[0].choices[3].split("(")[0]+"</div>");
				} else if (numOfChoices == 5) {
					var colors = ["#fff08d", "#ffbb4e", "#ff0b00", "#b0867f", "black"];
					$(".add").empty();
				        $(".add").append("<div class=questext>"+button+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq1></div>"+data[0].choices[0].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq2></div>"+data[0].choices[1].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq4></div>"+data[0].choices[2].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq3></div>"+data[0].choices[3].split("(")[0]+"</div>");
					$(".add").append("<div class=key><div class = colorSq id = colorSq5></div>"+data[0].choices[4].split("(")[0]+"</div>");

				}
				var context = {
                getColor: function(feature) {
                    var response = feature.attributes["response"]
                    if (zeroStart == false)
						return colors[response-1];
					else
						return colors[response];
                },
            };
				
				var template = {pointRadius:6,
				strokeWidth: 1,
				strokeColor: '#808080',
				fillColor:"${getColor}"
				};
				var style = new OpenLayers.Style(template, {context: context});

				vectors.styleMap = new OpenLayers.StyleMap(style);
				
				$.each(data, function(i, data) {
					var coord = new OpenLayers.LonLat(data.longitude,data.latitude).transform(fromProjection, toProjection);
					var adding = new OpenLayers.Feature.Vector(
					new OpenLayers.Geometry.Point(coord.lon, coord.lat),
					{
						culture:data.culture,
						response:data.response,
					        slug:data.slug
					});

					vectors.addFeatures([adding]);
				});
				
				
				
				} 
			 $("html, body").animate({

scrollTop: $(".mapholder").offset().top});
	
		
			});
		return false;
	});
	
	
});
	
