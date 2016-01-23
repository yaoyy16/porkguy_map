# coding=UTF-8
import json
import requests
from django.core.management.base import BaseCommand
from apis.models import Lottery_store


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        import time

        stores = Lottery_store.objects.all()
        i = 0
        for store in stores:
            if store.latitude == 0:
                # print(store.name)
                url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % store.address
                r = requests.get(url).json()["results"][0]["geometry"]
                lat, lng = r["location"]["lat"], r["location"]["lng"]
                print(lat, lng)
                store.latitude = lat
                store.longitude = lng
                store.save()
                i += 1
                if i == 10:
                    time.sleep(5)
                    i = 0
