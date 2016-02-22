import json
import requests
from django.core.management.base import BaseCommand
from apis.models import Organization


class Command(BaseCommand):
    help = 'update latitude and longitude of organization'

    def handle(self, *args, **options):
        import time

        orgs = Organization.objects.all()
        i = 1
        for org in orgs:
            if org.latitude == 0:
                print(i)
                url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % org.address
                r = requests.get(url).json()["results"][0]["geometry"]
                lat, lng = r["location"]["lat"], r["location"]["lng"]
                org.latitude = lat
                org.longitude = lng
                org.save()
                if i % 10 == 0:
                    time.sleep(5)
            i += 1
