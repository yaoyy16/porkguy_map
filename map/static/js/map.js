function initialize() {
	// Create an array of styles.
	var styles = [{
		featureType: "road",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "poi",
		stylers: [
			{ "visibility": "off" }
		]
	},{
		featureType: "landscape",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "road",
		elementType: "labels",
		stylers: [
			{ "visibility": "off" }
		]
	},{
		featureType: "water",
		elementType: "labels",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "administrative",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "transit",
		stylers: [
			{ visibility: "off" }
		]
	}];
	// Create a new StyledMapType object, passing it the array of styles,
	// as well as the name to be displayed on the map type control.
	var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
	// Create a map object, and include the MapTypeId to add
	// to the map type control.
	var mapOptions = {
		mapTypeControlOptions: {
			mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
		}
	};
	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
		
	//Associate the styled map with the MapTypeId and set it to display.
	map.mapTypes.set('map_style', styledMap);
	map.setMapTypeId('map_style');
	var bound1 = new google.maps.LatLng(26.515947, 123.213976);
	var bound2 = new google.maps.LatLng(21.784257, 118.276845);
	var bounds = new google.maps.LatLngBounds();
	bounds.extend(bound1);
	bounds.extend(bound2);
	map.fitBounds(bounds);
	map.data.loadGeoJson('static/bounds.json');
	var featureStyle = {
		fillColor: 'brown',
		strokeWeight: 1
	}
	map.data.setStyle(featureStyle);
}
google.maps.event.addDomListener(window, 'load', initialize);