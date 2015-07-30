function initialize() {
    // Create an array of styles.
    var styles = [{
        stylers: [
            { visibility: "off" }
        ]
    }];
    // Create a new StyledMapType object, passing it the array of styles,
    // as well as the name to be displayed on the map type control.
    var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
    // Create a map object, and include the MapTypeId to add
    // to the map type control.
    var mapOptions1 = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffffff',
        zoom: 8,
        center: {lat: 24.167622, lng: 119.391408},
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false
    };

    var mapOptions2 = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffffff',
        zoom: 10,
        center: {lat: 26.210017, lng: 120.144776},
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false
    };

    var mapOptions3 = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffffff',
        zoom: 10,
        center: {lat: 24.447879, lng: 118.338818},
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false
    };
    

    var map1 = new google.maps.Map(document.getElementById('map-canvas-1'), mapOptions1);
    var map2 = new google.maps.Map(document.getElementById('map-canvas-2'), mapOptions2);
    var map3 = new google.maps.Map(document.getElementById('map-canvas-3'), mapOptions3);
    //Associate the styled map with the MapTypeId and set it to display.
    map1.mapTypes.set('map_style', styledMap);
    map1.setMapTypeId('map_style');
    
    map2.mapTypes.set('map_style', styledMap);
    map2.setMapTypeId('map_style');
    map3.mapTypes.set('map_style', styledMap);
    map3.setMapTypeId('map_style');

    $.getJSON("static/county1.json", function(data){
        geoJsonObject1 = topojson.feature(data, data.objects["1031225_big5"])
        map1.data.addGeoJson(geoJsonObject1); 
      });
    $.getJSON("static/county2.json", function(data){
        geoJsonObject2 = topojson.feature(data, data.objects["1031225_big5"])
        map2.data.addGeoJson(geoJsonObject2); 
      });
    $.getJSON("static/county3.json", function(data){
        geoJsonObject3 = topojson.feature(data, data.objects["1031225_big5"])
        map3.data.addGeoJson(geoJsonObject3); 
      });
    var featureStyle = {
        fillColor: '#ccb267',
        fillOpacity: 1,
        strokeColor: '#604020',
        strokeWeight: 1
    }
    map1.data.setStyle(featureStyle);
    map2.data.setStyle(featureStyle);
    map3.data.setStyle(featureStyle);
    map1.data.addListener('mouseover', function(event) {
        map1.data.revertStyle();
        map1.data.overrideStyle(event.feature, {fillColor: '#FF9933'});
    });
    map1.data.addListener('mouseout', function(event) {
        map1.data.revertStyle();
    });
    map2.data.addListener('mouseover', function(event) {
        map2.data.revertStyle();
        map2.data.overrideStyle(event.feature, {fillColor: '#FF9933'});
    });
    map2.data.addListener('mouseout', function(event) {
        map2.data.revertStyle();
    });
    map3.data.addListener('mouseover', function(event) {
        map3.data.revertStyle();
        map3.data.overrideStyle(event.feature, {fillColor: '#FF9933'});
    });
    map3.data.addListener('mouseout', function(event) {
        map3.data.revertStyle();
    });
    markers = []
    dataVisual(map1, map2, map3, markers);
    for (var i = markers.length - 1; i >= 0; i--) {
        google.maps.event.addListener(markers[i], 'click', function() {
            map1.setZoom(10);
            map1.setCenter(this.getPosition());
            this.setVisible(false);
            var styles = [{
                stylers: [{ visibility: "on" }]
            }];
            var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
            map1.mapTypes.set('map_style', styledMap);
            map1.setMapTypeId('map_style');
            // map1.data.remove(map1.data.feature[0]);
            $('#map-canvas-2').hide();
            $('#map-canvas-3').hide();
            $('#blocker').hide();
        });
    };
}
google.maps.event.addDomListener(window, 'load', initialize);

function dataVisual (map1, map2, map3, markers) {
    var maxheight = 0;
    for (var i = fund_103.length - 1; i >= 0; i--) {
        var height = fund_103[i]['money__sum'];
        if (height > maxheight) {maxheight = height;}        
    };
    for (var i = fund_103.length - 1; i >= 0; i--) {
        var j = fund_103[i]['city'] - 1;
        if (county[j]) {
            var lat = county[j]['center_latitude'], lng = county[j]['center_longitude'];
        } else{
            console.log(j);
        };
        
        height = Math.round(fund_103[i]['money__sum']*100/maxheight);
        var canvas = document.createElement('canvas');
        canvas.width=15;
        canvas.height=100;
        var context = canvas.getContext('2d');
        context.fillStyle = "orange";
        context.fillRect(0,100 - height,5, height);
        context.fillStyle = "brown";
        context.fillRect(10,20,5,80);
        if (j > 19) {
            if (j == 20) {
                markers[i] = new google.maps.Marker({
                    icon : canvas.toDataURL(),
                    map : map3,
                    position : new google.maps.LatLng(lat, lng)
                });
            } else{
                markers[i] = new google.maps.Marker({
                    icon : canvas.toDataURL(),
                    map : map2,
                    position : new google.maps.LatLng(lat, lng)
                });
            };
        } else{
            markers[i] = new google.maps.Marker({
                icon : canvas.toDataURL(),
                map : map1,
                position : new google.maps.LatLng(lat, lng)
            });
        };
        
    };
}
