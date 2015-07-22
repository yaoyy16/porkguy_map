function initialize() {
	// Create an array of styles.
	var styles = [{
		stylers: [
			{ hue: "#ffa600" },
			{ saturation: -20 }
		]
	},{
		featureType: "road",
		elementType: "geometry",
		stylers: [
			{ lightness: 50 },
			{ visibility: "simplified" },
			{ color: '#ffffff' }
		]
	},{
		featureType: "road",
		elementType: "labels",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "landscape.natural",
		stylers: [
			{ "visibility": "off" }
		]
	},{
		featureType: "poi.park",
		stylers: [
			{ "visibility": "off" }
		]
	},{
		featureType: "road",
		elementType: "geometry.fill",
		stylers: [
			{ "visibility": "simplified" }
		]
	},{
		featureType: "landscape",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "poi.park",
		stylers: [
			{ visibility: "off" }
		]
	},{
		featureType: "road",
		elementType: "geometry",
		stylers: [
			{ "visibility": "off" }
		]
	},{
		featureType: "landscape.natural.terrain",
		stylers: [
			{ gamma: 9.99 }
		]
	},{
		featureType: "road",
		elementType: "labels",
		stylers: [
			{ "visibility": "off" }
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

	layer = new google.maps.FusionTablesLayer({
		query: {
			select: 'geometry',
			from: '1ertEwm-1bMBhpEwHhtNYT47HQ9k2ki_6sRa-UQ'
		},
		styles: [{
			polygonOptions: {
			fillColor: '#00FF00',
			fillOpacity: 0.3
			}
		},{
			where: 'birds > 300',
			polygonOptions: {
				fillColor: '#0000FF'
			}
		},{
			where: 'population > 5',
			polygonOptions: {
				fillOpacity: 1.0
			}
		}]
	});
	layer.setMap(map);
	var bound1 = new google.maps.LatLng(26.515947, 123.213976);
	var bound2 = new google.maps.LatLng(21.784257, 118.276845);
	var bounds = new google.maps.LatLngBounds();
	bounds.extend(bound1);
	bounds.extend(bound2);
	map.fitBounds(bounds);
}
google.maps.event.addDomListener(window, 'load', initialize);