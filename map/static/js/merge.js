/*
 * merge.js
 * Copyright (C) 2015 george <george@george-ThinkPad-T420>
 *
 * Distributed under terms of the MIT license.
 */

function value2latlng(value){
    value = value.toString(2);
    value = value.split('');
    var lat = [], lng = [];
    
    for(var idx=0;idx<value.length;idx++){
        if(idx%2){
            lat.push(value[idx]);
        }else{
            lng.push(value[idx]);
        }
    }
    lat = parseInt(lat.join(''), 2)/10 / Math.pow(2,17);
    lng = parseInt(lng.join(''), 2)/10 / Math.pow(2,17);
    return [lat, lng];
}

function latlng2value(lat,lng){
    lat = Math.floor(lat * Math.pow(2, 17)*10).toString(2);
    lng = Math.floor(lng * Math.pow(2, 17)*10).toString(2);
    lat = parseInt(lat.split('').join('0') +"0", 2);
    lng = parseInt(lng.split('').join('0'), 2);
    var value = (lat + lng);
    return value.toString(4);
}



function __merge(data){
    var keys = Object.keys(data);
    var tmp = {};
    for(var idx=0;idx<keys.length;idx++){
        var key = keys[idx];
        var merge_key = key.slice(0,-1);
        var tmp_data = tmp[merge_key] || [];      
        tmp_data.push({"key": key, "value": data[key]});
        tmp[merge_key] = tmp_data;
    }    
    var tmp_keys = Object.keys(tmp);
    var merged_latlng = {};
    var un_merged_latlng = {};
    for(var idx=0;idx<tmp_keys.length;idx++){
        var tmp_key = tmp_keys[idx];
        if(tmp[tmp_key].length >= 4){
            var tmp_values = tmp[tmp_key].map(function(d){return d['value']})
            merged_latlng[tmp_key] = [].concat.apply([], tmp_values);
        }else{
            tmp[tmp_key].map(function(d){
                un_merged_latlng[d['key']] = d['value'];
            })
        }
    }
    return [merged_latlng, un_merged_latlng]

}

function latlng_merge(latlngs, zoom){
    zoom = zoom || 21;
    var delta_zoom = zoom - 21 -3; // 8pixel merge
    data = {};
    // first merge
    for(var idx=0; idx<latlngs.length; idx++){
        var latlng = latlngs[idx];
        var key = latlng2value(latlng['latitude'], latlng['longitude']);
        key = key.slice(0, delta_zoom);
        var latlng_pool = data[key] || [];
        latlng_pool.push(latlng);
        data[key] = latlng_pool;
    }
    
    result = {};
    for(var level=0;level <= 5; level ++){
        var info = __merge(data);
        var merged = info[0];
        var un_merged = info[1];
        var keys = Object.keys(un_merged);
        for(var idx=0; idx<keys.length; idx++){
            result[keys[idx]] = un_merged[keys[idx]];
        }
        data = merged;
        if(!Object.keys(merged).length)
            break;
    }
    
    var keys = Object.keys(result);
    
    for(var idx=0;idx<keys.length;idx++){
        var info = {};
        var key = keys[idx];
        info['data'] = result[key];
        info['min_lat'] = info['data'][0].latitude;
        info['max_lat'] = info['data'][0].latitude;
        info['min_lng'] = info['data'][0].longitude;
        info['max_lng'] = info['data'][0].longitude;
        for(var d_idx=0;d_idx<info['data'].length;d_idx++){
            if(info['data'][d_idx].latitude < info['min_lat'])
                info['min_lat'] = info['data'][d_idx].latitude;

            if(info['data'][d_idx].longitude < info['min_lng'])
                info['min_lng'] = info['data'][d_idx].longitude;

            if(info['data'][d_idx].latitude > info['max_lat'])
                info['max_lat'] = info['data'][d_idx].latitude;

            if(info['data'][d_idx].longitude > info['max_lng'])
                info['max_lng'] = info['data'][d_idx].longitude;
        }
        result[key] = info;
    }


    return result;
}





