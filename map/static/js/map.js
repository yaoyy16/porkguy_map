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
        center: {lat: 23.73763123744288, lng: 119.52077989062502},
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
    
    mapOptions_detail = {
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

    map1 = new google.maps.Map(document.getElementById('map-canvas-1'), mapOptions1);
    map2 = new google.maps.Map(document.getElementById('map-canvas-2'), mapOptions2);
    map3 = new google.maps.Map(document.getElementById('map-canvas-3'), mapOptions3);
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
    map_detailed = false;
    var yearshow = document.getElementById('demo-category').value;
    var fundshow = document.getElementById('profit-distribut').checked;
    var surpshow = document.getElementById('charity').checked;
    var prizeshow = document.getElementById('prize').checked;

    document.getElementById('demo-category').addEventListener('change', function() {
        yearshow = document.getElementById('demo-category').value;
        dataVisual(yearshow, fundshow, surpshow, prizeshow);
    });

    $('input').on('click', function(){
        if(this.id == 'profit-distribut'){ 
            fundshow = this.checked;
            $('#year').show();
        };
        if(this.id == 'charity'){ 
            surpshow = this.checked;
            $('#year').hide();
        };
        if(this.id == 'prize'){ 
            prizeshow = this.checked;
            $('#year').hide();
        };
        dataVisual(yearshow, fundshow, surpshow, prizeshow);
    });
    countyData = {};
    for (var i = county.length - 1; i >= 0; i--) {
        // (function (i){
        //     $.getJSON("static/json/county"+i+".json", function(data){
        //     geoJsonObject = topojson.feature(data, data.objects["1031225_big5"]);
        //     console.log(i, , geoJsonObject['features'][0]["properties"]["C_Name"], county[i-1]['name']);

        //     });
        // })(i);
        var id =  county[i]['id'];
        var money1, money2, money3, money4, money5, times, count1, count2;
        for (var j = 21; j >= 0; j--) {
            if (fund_103[j]['city'] == id) {
                money1 = fund_103[j]['money__sum'];
            };
            if (fund_102[j]['city'] == id) {
                money2 = fund_102[j]['money__sum'];
            };
            if (fund_101[j]['city'] == id) {
                money3 = fund_101[j]['money__sum'];
            };
            if (fund_100[j]['city'] == id) {
                money4 = fund_100[j]['money__sum'];
            };
            if (surp_103[j]['city'] == id) {
                money5 = surp_103[j]['surplus__sum'];
            };
            if (prizes[j]) {
                if (prizes[j]['city'] == id) {
                    times = prizes[j]['firstprize_times__sum'];
                };
            }else{
                times = 0;
            };
            if (store_count[j]) {
                if (store_count[j]['city'] == id) {
                    count1 = store_count[j]['address__count'];
                };
            }else{
                count1 = 0;
            };
            if (org_count[j]) {
                if (org_count[j]['city'] == id) {
                    count2 = org_count[j]['address__count'];
                };
            }else{
                count2 = 0;
            };
        }
        countyData[id] = {
            "name":county[i]['name'],
            "location":{
                "lat":county[i]['center_latitude'],
                "lng":county[i]['center_longitude']
            },
            "bounds":{
                "ne":{
                    "lat":county[i]['ne_latitude'],
                    "lng":county[i]['ne_longitude']
                },
                "sw":{
                    "lat":county[i]['sw_latitude'],
                    "lng":county[i]['sw_longitude']
                }
            },
            "money":{
                "fund":{
                    103:money1,
                    102:money2,
                    101:money3,
                    100:money4
                },
                "surp":money5
            },
            "count":{
                "prize":times,
                "stores":count1,
                "charity":count2
            },
            "area": {
                "shape": new google.maps.Data()                
            }
        };
    };
    for (var i = 22; i >= 1; i--) {
        importdata(i);
        dataVisual(yearshow, fundshow, surpshow, prizeshow);
        addevent(i);
    };
    
    document.getElementById('return').addEventListener('click', function() {
        var styles = [{
            stylers: [{ visibility: "off" }]
        }];
        var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
        map1.setOptions(mapOptions1);
        map1.mapTypes.set('map_style', styledMap);
        map1.setMapTypeId('map_style');
        map1.setZoom(8);
        map1.setCenter({lat: 24.167622, lng: 119.391408});
        map_detailed = false;
        $('#return').hide();
        $('#county_detail').hide();
        $('#store_detail').hide();
        $('#org_detail').hide();
        
        for (var i = 22; i >= 1; i--) {
            if (i == 22) {
                countyData[i]['area']['shape'].setMap(map2);
            }else if (i == 21) {
                countyData[i]['area']['shape'].setMap(map3);
            } else{
                countyData[i]['area']['shape'].setMap(map1);
            };
        };
        
        store_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        organization_markers.map(function(obj){ 
            obj.setVisible(false);
            return obj;
        });
        $('#map-canvas-2').show();
        $('#map-canvas-3').show();
        $('#blocker').show();
    });

    store_markers = [];
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
    organization_markers = [];
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

function importdata (id) {
    $.getJSON("static/json/county"+id+".json", function(data){
        geoJsonObject = topojson.feature(data, data.objects["1031225_big5"]);
        countyData[id]['area']['shape'].addGeoJson(geoJsonObject);
        if (id == 22) {
            countyData[id]['area']['shape'].setMap(map2);
            // countyData[id]['area']['shape'].setStyle({
            //     fillColor: '#158c28',
            //     fillOpacity: 0.5,
            //     strokeColor: '#ffe24d',
            //     strokeWeight: 0
            // });
        }else if (id == 21) {
            countyData[id]['area']['shape'].setMap(map3);
            // countyData[id]['area']['shape'].setStyle({
            //     fillColor: '#158c28',
            //     fillOpacity: 0.5,
            //     strokeColor: '#ffe24d',
            //     strokeWeight: 0
            // });
        }else {
            countyData[id]['area']['shape'].setMap(map1);
            if (id == 17) {
                // countyData[id]['area']['shape'].setStyle({
                //     fillColor: '#158c28',
                //     fillOpacity: 0.5,
                //     strokeColor: '#ffe24d',
                //     strokeWeight: 0
                // });
            }else{
                // countyData[id]['area']['shape'].setStyle({
                //     fillColor: '#158c28',
                //     fillOpacity: 1,
                //     strokeColor: '#ffe24d',
                //     strokeWeight: 3
                // });
            };
        };
    });
}

function addevent (id) {
    var map = countyData[id]['area']["shape"].getMap();
    countyData[id]['area']["event"] = {
        "mouseover":
            google.maps.event.addListener(countyData[id]['area']["shape"], 'mouseover', function(event) {
                var content = '<div id="content"> '+countyData[id]['name']+'</div>'+
                '<div>社福機構獲得補助回饋金: '+countyData[id]['money']['fund']['103']+'</div>'+
                '<div>103年彩券盈餘分配金: '+countyData[id]['money']['surp']+'</div>'+
                '<div>103年起中頭獎次數: '+countyData[id]['count']['prize']+'</div>'+
                '<div>彩券行: '+countyData[id]['count']['stores']+' 家</div>'+
                '<div>社福機構: '+countyData[id]['count']['charity']+' 家</div>';
                $('#county_detail').html(content);
                if ($('#county_detail').is(':hidden')) {
                       $('#county_detail').show();
                };
            }),
        "mouseout":
            google.maps.event.addListener(countyData[id]['area']["shape"], 'mouseout', function(event) {
                if (!map_detailed) {
                    $('#county_detail').hide();
                };
            }),
        "click":
            google.maps.event.addListener(countyData[id]['area']["shape"], 'click', function(event) {
                $('#map-canvas-2').hide();
                $('#map-canvas-3').hide();
                $('#blocker').hide();
                var map1_sw = new google.maps.LatLng(countyData[id]['bounds']['sw']['lat'], countyData[id]['bounds']['sw']['lng']);
                var map1_ne = new google.maps.LatLng(countyData[id]['bounds']['ne']['lat'], countyData[id]['bounds']['ne']['lng']);
                var map1_bounds = new google.maps.LatLngBounds(map1_sw,map1_ne);;
                map1.fitBounds(map1_bounds);
                map_detailed = true;
                store_markers.map(function(obj){ 
                    obj.setVisible(true);
                    return obj;
                });
                organization_markers.map(function(obj){ 
                    obj.setVisible(true);
                    return obj;
                });
                var detail_style = [{
                    "featureType":"administrative",
                    "elementType":"geometry",
                    "stylers":[{
                        "visibility":"off"
                    }]
                },{
                    "featureType":"landscape.man_made",
                        "stylers":[{
                        "visibility":"simplified"},
                        {"color":"#ffe24d"
                    }]
                },{
                    "featureType":"road",
                    "stylers":[{
                        "visibility":"simplified"},
                        {"color":"#158c28"
                    }]
                },{
                    "featureType":"landscape.natural",
                    "stylers":[{
                        "visibility":"simplified"},
                        {"color":"#37b34a"
                    }]
                },{
                    "featureType":"water",
                    "stylers":[{
                        "color":"#ffe24d"
                        }]
                },{
                    "featureType":"poi",
                    "stylers":[{
                        "visibility":"simplified"
                    },{
                        "color":"#8bc53f"
                    }]
                },{
                    "elementType":"labels.text.stroke",
                    "stylers":[{
                        "color":"#808080"
                    },{
                        "gamma":9.91
                    },{
                        "visibility":"off"
                    }]
                },{
                    "elementType":"labels.text.fill",
                    "stylers":[{
                        "color":"#ffffff"
                    },{
                        "lightness":100
                    },{
                        "visibility":"on"
                    }]
                },{
                    "elementType":"labels.icon",
                    "stylers":[{
                        "visibility":"off"
                    }]
                }]
                var styledMap = new google.maps.StyledMapType(detail_style, {name: "Styled Map"});
                map1.setOptions(mapOptions_detail);
                map1.mapTypes.set('map_style', styledMap);
                map1.setMapTypeId('map_style');
                for (var i = 1; i < 23; i++){
                    countyData[i]['area']["shape"].setMap(null);
                };
                $('#return').show();
                $('#county_detail').show();
            })
    }
}

function dataVisual (year, fundshow, surpshow, prizeshow) {
    var maxdata = 0;
    var mindata = 9999999999999999999;
    for (var i = 22; i >= 1; i--) {
        if (fundshow) {
            if (year == 103) {
                if (countyData[i]['money']['fund'][103] > maxdata) {
                    maxdata = countyData[i]['money']['fund'][103];
                } else if (countyData[i]['money']['fund'][103] < mindata) {
                    mindata = countyData[i]['money']['fund'][103];
                };
            }else if (year == 102) {
                if (countyData[i]['money']['fund'][102] > maxdata) {
                    maxdata = countyData[i]['money']['fund'][102];
                } else if (countyData[i]['money']['fund'][102] < mindata) {
                    mindata = countyData[i]['money']['fund'][102];
                };
            }else if (year == 101) {
                if (countyData[i]['money']['fund'][101] > maxdata) {
                    maxdata = countyData[i]['money']['fund'][101];
                } else if (countyData[i]['money']['fund'][101] < mindata) {
                    mindata = countyData[i]['money']['fund'][101];
                };
            }else {
                if (countyData[i]['money']['fund'][100] > maxdata) {
                    maxdata = countyData[i]['money']['fund'][100];
                } else if (countyData[i]['money']['fund'][100] < mindata) {
                    mindata = countyData[i]['money']['fund'][100];
                };
            };
        }else if (surpshow) {
            if (countyData[i]['money']['surp'] > maxdata) {
                maxdata = countyData[i]['money']['surp'];
            } else if (countyData[i]['money']['surp'] < mindata) {
                mindata = countyData[i]['money']['surp'];
            };
        }else if (prizeshow) {
            if (countyData[i]['count']['prize'] > maxdata) {
                maxdata = countyData[i]['count']['prize'];
            } else if (countyData[i]['count']['prize'] < mindata) {
                mindata = countyData[i]['count']['prize'];
            };
        };
    }
    for (var i = 22; i >= 1; i--) {
        var opacity;
        if (fundshow) {
            if (year == 103) {
                opacity = range (countyData[i]['money']['fund'][103], maxdata, mindata);
            }else if (year == 102) {
                opacity = range (countyData[i]['money']['fund'][102], maxdata, mindata);
            }else if (year == 101) {
                opacity = range (countyData[i]['money']['fund'][101], maxdata, mindata);
            }else {
                opacity = range (countyData[i]['money']['fund'][100], maxdata, mindata);
            };
        }else if (surpshow) {
            opacity = range (countyData[i]['money']['surp'], maxdata, mindata);
        }else if (prizeshow) {
            opacity = range (countyData[i]['money']['prize'], maxdata, mindata);
        };
        console.log(opacity);
        if (i == 22 || i == 21 || i == 17) {
            countyData[i]['area']['shape'].setStyle({
                fillColor: '#158c28',
                fillOpacity: opacity,
                strokeColor: '#ffe24d',
                strokeWeight: 0
            });
        }else{
            countyData[i]['area']['shape'].setStyle({
                fillColor: '#158c28',
                fillOpacity: opacity,
                strokeColor: '#ffe24d',
                strokeWeight: 3
            });
        };
    }
}

function range (data, max, min) {
    var range = (max - min)/4;
    var range1 = min + range;
    var range2 = range1 + range;
    var range3 = range2 + range;
    if (data == min){
        return 0.1
    }else if(data<range1){
        return 0.2
    }else if(data<range2){
        return 0.4
    }else if(data<range3){
        return 0.6
    }else if(data<max){
        return 0.8
    }else{
        return 2
    };
}