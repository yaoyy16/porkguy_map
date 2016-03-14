from django.core.management.base import BaseCommand
import json
import requests
from apis.models import City


class Command(BaseCommand):
    help = 'create city table'

    def handle(self, *args, **options):
        city = City.objects.get(name='桃園縣')
        city.name = '桃園市'
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % city.name
        r = requests.get(url).json()["results"][0]["geometry"]
        lat1, lng1 = r["location"]["lat"], r["location"]["lng"]
        lat2, lng2 = r["bounds"]['northeast'][
            "lat"
        ], r["bounds"]['northeast']["lng"]
        lat3, lng3 = r["bounds"]['southwest'][
            "lat"
        ], r["bounds"]['southwest']["lng"]
        city.center_latitude = lat1
        city.center_longitude = lng1
        city.ne_latitude = lat2
        city.ne_longitude = lng2
        city.sw_latitude = lat3
        city.sw_longitude = lng3
        city.save()
