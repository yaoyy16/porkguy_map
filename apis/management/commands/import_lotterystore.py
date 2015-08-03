from django.core.management.base import BaseCommand
from apis.models import Lottery_store, City

class Command(BaseCommand):
    help = 'create surplus table'

    def handle(self, *args, **options):
        with open('./docs/lotterystore.txt', encoding = 'utf8') as f:
            data = f.readlines()    
        str1 = "運動彩券"
        for store in data :
            if store.find(str1):
                store = store.split("\t")
                store_name = store[0].replace("台灣彩券(","").replace(")","")
                store_address = store[1].replace("\n","").replace("台","臺")
                store_city = store_address[0:3]
                print(store_address , store_city)
                city = City.objects.get(name=store_city)

                Lottery_store.objects.create(
                    name = store_name,
                    city = city,
                    address = store_address
                )
