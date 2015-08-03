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
        backgroundColor:'#ffe24d',
        zoom: 8,
        center: {lat: 24.167622, lng: 119.391408},
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false,
        disableDoubleClickZoom: true
    };

    var mapOptions2 = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffe24d',
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false,
        disableDoubleClickZoom: true
    };

    var mapOptions3 = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffe24d',
        scrollwheel: false,
        draggable: false,
        panControl: false,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false,
        disableDoubleClickZoom: true
    };
    
    var mapOptions_detail = {
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        },
        backgroundColor:'#ffe24d',
        scrollwheel: true,
        draggable: true,
        disableDoubleClickZoom: false,
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

    var map2_sw = new google.maps.LatLng(county[21]['sw_latitude'], county[21]['sw_longitude']);
    var map2_ne = new google.maps.LatLng(county[21]['ne_latitude'], county[21]['ne_longitude']);
    var map2_bounds = new google.maps.LatLngBounds(map2_sw,map2_ne);
    map2.fitBounds(map2_bounds);

    var map3_sw = new google.maps.LatLng(county[20]['sw_latitude'], county[20]['sw_longitude']);
    var map3_ne = new google.maps.LatLng(county[20]['ne_latitude'], county[20]['ne_longitude']);
    var map3_bounds = new google.maps.LatLngBounds(map3_sw,map3_ne);
    map3.fitBounds(map3_bounds);

    var map1_features;
    var map2_features;
    var map3_features;
    $.getJSON("static/county1.json", function(data){
        geoJsonObject1 = topojson.feature(data, data.objects["1031225_big5"])
        map1_features = map1.data.addGeoJson(geoJsonObject1); 
      });
    $.getJSON("static/county2.json", function(data){
        geoJsonObject2 = topojson.feature(data, data.objects["1031225_big5"])
        map2_features = map2.data.addGeoJson(geoJsonObject2); 
      });
    $.getJSON("static/county3.json", function(data){
        geoJsonObject3 = topojson.feature(data, data.objects["1031225_big5"])
        map3_features = map3.data.addGeoJson(geoJsonObject3); 
      });
    var featureStyle = {
        fillColor: '#158c28',
        fillOpacity: 1,
        strokeColor: '#ffe24d',
        strokeWeight: 3
    }
    map1.data.setStyle(featureStyle);
    map2.data.setStyle(featureStyle);
    map3.data.setStyle(featureStyle);
    var map1_mouse_event_1, map1_mouse_event_2, map2_mouse_event_1, map2_mouse_event_2, map3_mouse_event_1, map3_mouse_event_2;
    map1_mouse_event_1 = map1.data.addListener('mouseover', function(event) {
        var name = event.feature['G']['C_Name'];
        var city_id, money1, money2, money3, count1, count2, funds;
        if (yearshow == 103) {funds = fund_103;}
        else if (yearshow == 102) {funds = fund_102} 
        else if (yearshow == 101) {funds = fund_101}
        else {funds = fund_100};
        for (var i = 19; i >= 0; i--) {
            if (county[i]['name'] == name) {
                city_id = i + 1;
            };
        }
        for (var i = 21; i >= 0; i--) {
            if (funds[i]['city'] == city_id) {
                money1 = funds[i]['money__sum'];
            };
            if (surp_103[i]['city'] == city_id) {
                money2 = surp_103[i]['surplus__sum'];
            };
            if (prizes[i]) {
                if (prizes[i]['city'] == city_id) {
                    money3 = prizes[i]['firstprize_times__sum'];
                };
            }else{
                money3 = 0;
            };
            if (store_count[i]) {
                if (store_count[i]['city'] == city_id) {
                    count1 = store_count[i]['address__count'];
                };
            }else{
                count1 = 0;
            };
            if (org_count[i]) {
                if (org_count[i]['city'] == city_id) {
                    count2 = org_count[i]['address__count'];
                };
            }else{
                count2 = 0;
            };
        }
        var content = '<div id="content"> '+name+'</div>'+
        '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
        '<div>103年彩券盈餘分配金: '+money2+'</div>'+
        '<div>103年起中頭獎次數: '+money3+'</div>'+
        '<div>彩券行: '+count1+' 家</div>'+
        '<div>社福機構: '+count2+' 家</div>'
        ;
        $('#county_detail').html(content);
        if ($('#county_detail').is(':hidden')) {
                $('#county_detail').show();
        };
    });
    map1_mouse_event_2 = map1.data.addListener('mouseout', function(event) {
        $('#county_detail').hide();
    });
    map2_mouse_event_1 = map2.data.addListener('mouseover', function(event) {
        var name = event.feature['G']['C_Name'];
        var city_id, money1, money2, money3, count1, count2, funds;
        if (yearshow == 103) {funds = fund_103;}
        else if (yearshow == 102) {funds = fund_102} 
        else if (yearshow == 101) {funds = fund_101}
        else {funds = fund_100};
        city_id = 22;
        for (var i = 21; i >= 0; i--) {
            if (funds[i]['city'] == city_id) {
                money1 = funds[i]['money__sum'];
            };
            if (surp_103[i]['city'] == city_id) {
                money2 = surp_103[i]['surplus__sum'];
            };
            if (prizes[i]) {
                if (prizes[i]['city'] == city_id) {
                    money3 = prizes[i]['firstprize_times__sum'];
                };
            }else{
                money3 = 0;
            };
            if (store_count[i]) {
                if (store_count[i]['city'] == city_id) {
                    count1 = store_count[i]['address__count'];
                };
            }else{
                count1 = 0;
            };
            if (org_count[i]) {
                if (org_count[i]['city'] == city_id) {
                    count2 = org_count[i]['address__count'];
                };
            }else{
                count2 = 0;
            };
        }
        var content = '<div id="content"> '+name+'</div>'+
        '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
        '<div>103年彩券盈餘分配金: '+money2+'</div>'+
        '<div>103年起中頭獎次數: '+money3+'</div>'+
        '<div>彩券行: '+count1+' 家</div>'+
        '<div>社福機構: '+count2+' 家</div>'
        ;
        $('#county_detail').html(content);
        if ($('#county_detail').is(':hidden')) {
                $('#county_detail').show();
        };    
    });
    map2_mouse_event_2 = map2.data.addListener('mouseout', function(event) {
        $('#county_detail').hide();
    });
    map3_mouse_event_1 = map3.data.addListener('mouseover', function(event) {
        var name = event.feature['G']['C_Name'];
        var city_id, money1, money2, money3, count1, count2, funds;
        if (yearshow == 103) {funds = fund_103;}
        else if (yearshow == 102) {funds = fund_102} 
        else if (yearshow == 101) {funds = fund_101}
        else {funds = fund_100};
        city_id = 21;
        for (var i = 21; i >= 0; i--) {
            if (funds[i]['city'] == city_id) {
                money1 = funds[i]['money__sum'];
            };
            if (surp_103[i]['city'] == city_id) {
                money2 = surp_103[i]['surplus__sum'];
            };
            if (prizes[i]) {
                if (prizes[i]['city'] == city_id) {
                    money3 = prizes[i]['firstprize_times__sum'];
                };
            }else{
                money3 = 0;
            };
            if (store_count[i]) {
                if (store_count[i]['city'] == city_id) {
                    count1 = store_count[i]['address__count'];
                };
            }else{
                count1 = 0;
            };
            if (org_count[i]) {
                if (org_count[i]['city'] == city_id) {
                    count2 = org_count[i]['address__count'];
                };
            }else{
                count2 = 0;
            };
        }
        var content = '<div id="content"> '+name+'</div>'+
        '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
        '<div>103年彩券盈餘分配金: '+money2+'</div>'+
        '<div>103年起中頭獎次數: '+money3+'</div>'+
        '<div>彩券行: '+count1+' 家</div>'+
        '<div>社福機構: '+count2+' 家</div>'
        ;
        $('#county_detail').html(content);
        if ($('#county_detail').is(':hidden')) {
            $('#county_detail').show();
        };
    });
    map3_mouse_event_2 = map3.data.addListener('mouseout', function(event) {
        $('#county_detail').hide();
    });

    map1.data.addListener('click', function(event) {
        google.maps.event.removeListener(map1_mouse_event_1);
        google.maps.event.removeListener(map1_mouse_event_2);
        google.maps.event.removeListener(map2_mouse_event_1);
        google.maps.event.removeListener(map2_mouse_event_2);
        google.maps.event.removeListener(map3_mouse_event_1);
        google.maps.event.removeListener(map3_mouse_event_2);
        var map1_sw;
        var map1_ne;
        var map1_bounds;
        for (var i = county.length - 1; i >= 0; i--) {
            if (county[i]['name'] == event.feature['G']['C_Name']) {
                map1_sw = new google.maps.LatLng(county[i]['sw_latitude'], county[i]['sw_longitude']);
                map1_ne = new google.maps.LatLng(county[i]['ne_latitude'], county[i]['ne_longitude']);
                map1_bounds = new google.maps.LatLngBounds(map1_sw,map1_ne);
                map1.fitBounds(map1_bounds);
            };
        }
        chart_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        store_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        organization_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        var styles = [{
            stylers: [{ visibility: "on" }]
        }];
        var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
        map1.setOptions(mapOptions_detail);
        map1.mapTypes.set('map_style', styledMap);
        map1.setMapTypeId('map_style');
        for (var i = 0; i < map1_features.length; i++){
            map1.data.remove(map1_features[i]);
        };
        $('#map-canvas-2').hide();
        $('#map-canvas-3').hide();
        $('#blocker').hide();
        $('#return').show();
        $('#county_detail').show();
    });
    map2.data.addListener('click', function(event) {
        google.maps.event.removeListener(map1_mouse_event_1);
        google.maps.event.removeListener(map1_mouse_event_2);
        google.maps.event.removeListener(map2_mouse_event_1);
        google.maps.event.removeListener(map2_mouse_event_2);
        google.maps.event.removeListener(map3_mouse_event_1);
        google.maps.event.removeListener(map3_mouse_event_2);
        var map1_sw;
        var map1_ne;
        var map1_bounds;
        for (var i = county.length - 1; i >= 0; i--) {
            if (county[i]['name'] == event.feature['G']['C_Name']) {
                map1_sw = new google.maps.LatLng(county[i]['sw_latitude'], county[i]['sw_longitude']);
                map1_ne = new google.maps.LatLng(county[i]['ne_latitude'], county[i]['ne_longitude']);
                map1_bounds = new google.maps.LatLngBounds(map1_sw,map1_ne);
                map1.fitBounds(map1_bounds);
            };
        }
        chart_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        store_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        organization_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        var styles = [{
            stylers: [{ visibility: "on" }]
        }];
        var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
        map1.setOptions(mapOptions_detail);
        map1.mapTypes.set('map_style', styledMap);
        map1.setMapTypeId('map_style');
        for (var i = 0; i < map1_features.length; i++){
            map1.data.remove(map1_features[i]);
        };
        $('#map-canvas-2').hide();
        $('#map-canvas-3').hide();
        $('#blocker').hide();
        $('#return').show();
        $('#county_detail').show();
    });
    map3.data.addListener('click', function(event) {
        google.maps.event.removeListener(map1_mouse_event_1);
        google.maps.event.removeListener(map1_mouse_event_2);
        google.maps.event.removeListener(map2_mouse_event_1);
        google.maps.event.removeListener(map2_mouse_event_2);
        google.maps.event.removeListener(map3_mouse_event_1);
        google.maps.event.removeListener(map3_mouse_event_2);
        var map1_sw;
        var map1_ne;
        var map1_bounds;
        for (var i = county.length - 1; i >= 0; i--) {
            if (county[i]['name'] == event.feature['G']['C_Name']) {
                map1_sw = new google.maps.LatLng(county[i]['sw_latitude'], county[i]['sw_longitude']);
                map1_ne = new google.maps.LatLng(county[i]['ne_latitude'], county[i]['ne_longitude']);
                map1_bounds = new google.maps.LatLngBounds(map1_sw,map1_ne);
                map1.fitBounds(map1_bounds);
            };
        }
        chart_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        store_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        organization_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        var styles = [{
            stylers: [{ visibility: "on" }]
        }];
        var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
        map1.setOptions(mapOptions_detail);
        map1.mapTypes.set('map_style', styledMap);
        map1.setMapTypeId('map_style');
        for (var i = 0; i < map1_features.length; i++){
            map1.data.remove(map1_features[i]);
        };
        $('#map-canvas-2').hide();
        $('#map-canvas-3').hide();
        $('#blocker').hide();
        $('#return').show();
        $('#county_detail').show();
    });
    chart_markers = []
    for (var i = county.length - 1; i >= 0; i--) {
        var lat = county[i]['center_latitude'], lng = county[i]['center_longitude'];
        if (i > 19) {
            if (i == 20) {
                chart_markers[i] = new google.maps.Marker({
                    map: map3,
                    position: new google.maps.LatLng(lat, lng)
                });
            } else{
                chart_markers[i] = new google.maps.Marker({
                    map: map2,
                    position: new google.maps.LatLng(lat, lng)
                });
            };
        } else{
            chart_markers[i] = new google.maps.Marker({
                map: map1,
                position: new google.maps.LatLng(lat, lng)
            });
        };
    };
    var yearshow = document.getElementById('demo-category').value;
    var fundshow = document.getElementById('profit-distribut').checked;
    var surpshow = document.getElementById('charity').checked;
    var prizeshow = document.getElementById('prize').checked;
    dataVisual(yearshow, chart_markers, fundshow, surpshow, prizeshow);

    document.getElementById('demo-category').addEventListener('change', function() {
        yearshow = document.getElementById('demo-category').value;
        dataVisual(yearshow, chart_markers, fundshow, surpshow, prizeshow);
    });

    $('input').on('click', function(){
        if(this.id == 'profit-distribut'){ fundshow = this.checked};
        if(this.id == 'charity'){ surpshow = this.checked};
        if(this.id == 'prize'){ prizeshow = this.checked};
        dataVisual(yearshow, chart_markers, fundshow, surpshow, prizeshow);
    });
    
    document.getElementById('return').addEventListener('click', function() {
        var styles = [{
            stylers: [{ visibility: "off" }]
        }];
        var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
        map1.mapTypes.set('map_style', styledMap);
        map1.setMapTypeId('map_style');
        $.getJSON("static/county1.json", function(data){
            geoJsonObject1 = topojson.feature(data, data.objects["1031225_big5"])
            map1_features = map1.data.addGeoJson(geoJsonObject1); 
        });
        map1.setZoom(8);
        map1.setCenter({lat: 24.167622, lng: 119.391408});
        map1_mouse_event_1 = map1.data.addListener('mouseover', function(event) {
            var name = event.feature['G']['C_Name'];
            var city_id, money1, money2, money3, count1, count2, funds;
            if (yearshow == 103) {funds = fund_103;}
            else if (yearshow == 102) {funds = fund_102} 
            else if (yearshow == 101) {funds = fund_101}
            else {funds = fund_100};
            for (var i = 19; i >= 0; i--) {
                if (county[i]['name'] == name) {
                    city_id = i + 1;
                };
            }
            for (var i = 21; i >= 0; i--) {
                if (funds[i]['city'] == city_id) {
                    money1 = funds[i]['money__sum'];
                };
                if (surp_103[i]['city'] == city_id) {
                    money2 = surp_103[i]['surplus__sum'];
                };
                if (prizes[i]) {
                    if (prizes[i]['city'] == city_id) {
                        money3 = prizes[i]['firstprize_times__sum'];
                    };
                }else{
                    money3 = 0;
                };
                if (store_count[i]) {
                    if (store_count[i]['city'] == city_id) {
                        count1 = store_count[i]['address__count'];
                    };
                }else{
                    count1 = 0;
                };
                if (org_count[i]) {
                    if (org_count[i]['city'] == city_id) {
                        count2 = org_count[i]['address__count'];
                    };
                }else{
                    count2 = 0;
                };
            }
            var content = '<div id="content"> '+name+'</div>'+
            '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
            '<div>103年彩券盈餘分配金: '+money2+'</div>'+
            '<div>103年起中頭獎次數: '+money3+'</div>'+
            '<div>彩券行: '+count1+' 家</div>'+
            '<div>社福機構: '+count2+' 家</div>'
            ;
            $('#county_detail').html(content);
            if ($('#county_detail').is(':hidden')) {
                    $('#county_detail').show();
            };
        });
        map1_mouse_event_2 = map1.data.addListener('mouseout', function(event) {
            $('#county_detail').hide();
        });
        map2_mouse_event_1 = map2.data.addListener('mouseover', function(event) {
            var name = event.feature['G']['C_Name'];
            var city_id, money1, money2, money3, count1, count2, funds;
            if (yearshow == 103) {funds = fund_103;}
            else if (yearshow == 102) {funds = fund_102} 
            else if (yearshow == 101) {funds = fund_101}
            else {funds = fund_100};
            city_id = 22;
            for (var i = 21; i >= 0; i--) {
                if (funds[i]['city'] == city_id) {
                    money1 = funds[i]['money__sum'];
                };
                if (surp_103[i]['city'] == city_id) {
                    money2 = surp_103[i]['surplus__sum'];
                };
                if (prizes[i]) {
                    if (prizes[i]['city'] == city_id) {
                        money3 = prizes[i]['firstprize_times__sum'];
                    };
                }else{
                    money3 = 0;
                };
                if (store_count[i]) {
                    if (store_count[i]['city'] == city_id) {
                        count1 = store_count[i]['address__count'];
                    };
                }else{
                    count1 = 0;
                };
                if (org_count[i]) {
                    if (org_count[i]['city'] == city_id) {
                        count2 = org_count[i]['address__count'];
                    };
                }else{
                    count2 = 0;
                };
            }
            var content = '<div id="content"> '+name+'</div>'+
            '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
            '<div>103年彩券盈餘分配金: '+money2+'</div>'+
            '<div>103年起中頭獎次數: '+money3+'</div>'+
            '<div>彩券行: '+count1+' 家</div>'+
            '<div>社福機構: '+count2+' 家</div>'
            ;
            $('#county_detail').html(content);
            if ($('#county_detail').is(':hidden')) {
                    $('#county_detail').show();
            };    
        });
        map2_mouse_event_2 = map2.data.addListener('mouseout', function(event) {
            $('#county_detail').hide();
        });
        map3_mouse_event_1 = map3.data.addListener('mouseover', function(event) {
            var name = event.feature['G']['C_Name'];
            var city_id, money1, money2, money3, count1, count2, funds;
            if (yearshow == 103) {funds = fund_103;}
            else if (yearshow == 102) {funds = fund_102} 
            else if (yearshow == 101) {funds = fund_101}
            else {funds = fund_100};
            city_id = 21;
            for (var i = 21; i >= 0; i--) {
                if (funds[i]['city'] == city_id) {
                    money1 = funds[i]['money__sum'];
                };
                if (surp_103[i]['city'] == city_id) {
                    money2 = surp_103[i]['surplus__sum'];
                };
                if (prizes[i]) {
                    if (prizes[i]['city'] == city_id) {
                        money3 = prizes[i]['firstprize_times__sum'];
                    };
                }else{
                    money3 = 0;
                };
                if (store_count[i]) {
                    if (store_count[i]['city'] == city_id) {
                        count1 = store_count[i]['address__count'];
                    };
                }else{
                    count1 = 0;
                };
                if (org_count[i]) {
                    if (org_count[i]['city'] == city_id) {
                        count2 = org_count[i]['address__count'];
                    };
                }else{
                    count2 = 0;
                };
            }
            var content = '<div id="content"> '+name+'</div>'+
            '<div>社福機構獲得補助回饋金: '+money1+'</div>'+
            '<div>103年彩券盈餘分配金: '+money2+'</div>'+
            '<div>103年起中頭獎次數: '+money3+'</div>'+
            '<div>彩券行: '+count1+' 家</div>'+
            '<div>社福機構: '+count2+' 家</div>'
            ;
            $('#county_detail').html(content);
            if ($('#county_detail').is(':hidden')) {
                $('#county_detail').show();
            };
        });
        map3_mouse_event_2 = map3.data.addListener('mouseout', function(event) {
            $('#county_detail').hide();
        });
        chart_markers.map(function(obj){ 
            obj.setVisible(true);
            return obj;
        });
        store_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        organization_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        map1.data.setStyle(featureStyle);
        $('#map-canvas-2').show();
        $('#map-canvas-3').show();
        $('#blocker').show();
        $('#return').hide();
        $('#county_detail').hide();
        $('#store_detail').hide();
        $('#org_detail').hide();
    });
    for (var i = chart_markers.length - 1; i >= 0; i--) {
        google.maps.event.addListener(chart_markers[i], 'click', function() {
            var index = chart_markers.indexOf(this);
            var map1_sw = new google.maps.LatLng(county[index]['sw_latitude'], county[index]['sw_longitude']);
            var map1_ne = new google.maps.LatLng(county[index]['ne_latitude'], county[index]['ne_longitude']);
            var map1_bounds = new google.maps.LatLngBounds(map1_sw,map1_ne);
            map1.fitBounds(map1_bounds);
            chart_markers.map(function(obj){ 
                obj.setVisible(false);
                return obj;
            });
            store_markers.map(function(obj){ 
                obj.setVisible(true);
                return obj;
            });
            organization_markers.map(function(obj){ 
                obj.setVisible(true);
                return obj;
            });
            var styles = [{
                stylers: [{ visibility: "on" }]
            }];
            var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
            map1.mapTypes.set('map_style', styledMap);
            map1.setMapTypeId('map_style');
            for (var i = 0; i < map1_features.length; i++){
                map1.data.remove(map1_features[i]);
            };
            $('#map-canvas-2').hide();
            $('#map-canvas-3').hide();
            $('#blocker').hide();
            $('#return').show();
        });
        google.maps.event.addListener(chart_markers[i], 'mouseover', function() {

        });
        google.maps.event.addListener(chart_markers[i], 'mouseout', function() {

        });
    };

    var store_markers = [];
    for (var i = store.length - 1; i >= 0; i--) {
        store_markers[i] = new google.maps.Marker({
            map: map1,
            position: new google.maps.LatLng(store[i]['latitude'], store[i]['longitude']),
            visible: false
        });
        google.maps.event.addListener(store_markers[i], 'click', function() {
            var name = store[store_markers.indexOf(this)]['name'];
            var address = store[store_markers.indexOf(this)]['address'];
            var times = store[store_markers.indexOf(this)]['firstprize_times'];
            var content = '<div>店家名稱: '+name+'</div>'+
            '<div>地址: '+address+'</div>'+
            '<div>中頭獎次數: '+times+'</div>';
            $('#store_detail').html(content);
            if ($('#org_detail').is(':visible')) {
                $('#org_detail').hide();
            };
            if ($('#store_detail').is(':hidden')) {
                $('#store_detail').show();
            };
        });

    };
    var organization_markers = [];
    for (var i = organization.length - 1; i >= 0; i--) {
        var image = {
            url: '/static/img/heart-icon.png',
            // This marker is 20 pixels wide by 32 pixels tall.
            size: new google.maps.Size(20, 32)
            // The origin for this image is 0,0.
            // origin: new google.maps.Point(0,0),
            // The anchor for this image is the base of the flagpole at 0,32.
        };
        organization_markers[i] = new google.maps.Marker({
            map: map1,
            position: new google.maps.LatLng(organization[i]['latitude'], organization[i]['longitude']),
            icon: image,
            visible: false
        });
        google.maps.event.addListener(organization_markers[i], 'click', function() {
            var name = organization[organization_markers.indexOf(this)]['name'];
            var address = organization[organization_markers.indexOf(this)]['address'];
            var funds;
            if (yearshow == 103) {funds = fund_org_103;}
            else if (yearshow == 102) {funds = fund_102} 
            else if (yearshow == 101) {funds = fund_101}
            else {funds = fund_100};
            var money = "未申請";
            var applied = "";
            for (var i = funds.length - 1; i >= 0; i--) {
                if(funds[i]['org_name'] == name){
                    money = funds[i]['money'];
                    applied = funds[i]['content'];
                }
            };
            var content = '<div>機構名稱: '+name+'</div>'+
            '<div>獲得補助: '+address+'</div>'+
            '<div>獲得補助: '+money+'</div>'+
            '<div>申請內容: '+applied+'</div>'+
            '<div>詳細資訊</div>';
            $('#org_detail').html(content);
            if ($('#store_detail').is(':visible')) {
                $('#store_detail').hide();
            };
            if ($('#org_detail').is(':hidden')) {
                $('#org_detail').show();
            };
        });
    };
    google.maps.event.addListener(map1, 'click', function() {
        $('#store_detail').hide();
        $('#org_detail').hide();
    });
}
google.maps.event.addDomListener(window, 'load', initialize);

function dataVisual (year, chart_markers, fundshow, surpshow, prizeshow) {
    var fund_list
    if (year == 103) {fund_list = fund_103;}
    else if (year == 102) {fund_list = fund_102} 
    else if (year == 101) {fund_list = fund_101}
    else {fund_list = fund_100};
    var maxfund = 0;
    var maxsurp = 0;
    var maxprize = 0;
    for (var i = 21; i >= 0; i--) {
        var fund = fund_list[i]['money__sum'];
        if (fund > maxfund) {maxfund = fund;}
        var surp = surp_103[i]['surplus__sum'];
        if (surp > maxsurp) {maxsurp = surp;}
        var prize;
        if (prizes[i]) {
            prize = prizes[i]['firstprize_times__sum'];
        };
        if (prize > maxprize) {maxprize = prize;}
    };
    for (var i = 21; i >= 0; i--) {
        var city_id = fund_list[i]['city'];        
        var canvas = document.createElement('canvas');
        canvas.width=15;
        canvas.height=100;
        var context = canvas.getContext('2d');
        if (fundshow) {
            var height = Math.round(fund_list[i]['money__sum']*100/maxfund);
            context.fillStyle = "orange";
            context.fillRect(0,100 - height,5,height);
        };
        if (surpshow) {
            var height = Math.round(surp_103[i]['surplus__sum']*100/maxsurp);
            context.fillStyle = "brown";
            context.fillRect(5,100 - height,5,height);
        };
        if (prizeshow) {
            var height = 0;
            if (prizes[i]) {
                height = Math.round(prizes[i]['firstprize_times__sum']*100/maxprize);
            };
            context.fillStyle = "green";
            context.fillRect(10,100 - height,5,height);
        };
        chart_markers[city_id - 1].setIcon(canvas.toDataURL());
    };
}
