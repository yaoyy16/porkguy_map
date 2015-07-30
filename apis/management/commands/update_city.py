# coding=UTF-8
import json
import requests
from django.core.management.base import BaseCommand
from apis.models import City

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        # locations = ["台北市", "高雄市"]
        locations = City.objects.exclude(name='全國性').values('name') 
        for loca in locations:
            city = City.objects.get(name = loca['name'])
            if city.center_latitude == 0:
                print(city.name)
                url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % loca['name']
                r = requests.get(url).json()["results"][0]["geometry"]
                lat1, lng1 = r["location"]["lat"], r["location"]["lng"]
                lat2, lng2 = r["bounds"]['northeast']["lat"], r["bounds"]['northeast']["lng"]
                lat3, lng3 = r["bounds"]['southwest']["lat"], r["bounds"]['southwest']["lng"]
                city.center_latitude = lat1
                city.center_longitude = lng1
                city.ne_latitude = lat2 
                city.ne_longitude = lng2
                city.sw_latitude = lat3
                city.sw_longitude = lng3
                city.save()