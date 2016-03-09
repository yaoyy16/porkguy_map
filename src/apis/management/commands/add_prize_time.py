from django.core.management.base import BaseCommand
from apis.models import Lottery_store, City
from django.db.models import F


class Command(BaseCommand):
    help = 'add first prize time to Lottery_store'

    def handle(self, *args, **options):
        import re

        ####　add first prize times of 今彩539 ####
        # with open('./docs/firstprize/firstprize539.txt', encoding = 'utf8') as f:
        #     data = f.readlines()
        # i = 23
        # for line in data :
        #     s = line.split(" ")
        #     s[2] = s[2].replace("台", "臺")
        #     if len(Lottery_store.objects.filter(address=s[2])) > 0 :
        #         Lottery_store.objects.filter(address=s[2]).update(firstprize_times=F('firstprize_times') + 1)
        #         print("find")
        #     else :
        #         store_city = s[2][0:3]
        #         city = City.objects.get(name=store_city)
        #         Lottery_store.objects.create(
        #             name = s[1],
        #             city = city,
        #             address = s[2],
        #             firstprize_times = 1,
        #         )
        #         print("add store")
        #     i += 1
        #     print(i)

        ####　add first prize times of 威力彩 ####
        # with open('./docs/firstprize/firstprize_power.txt', encoding = 'utf8') as f:
        #     data = f.readlines()
        # for line in data :
        #     string = line.split("   ")
        #     address = string[4].replace("台","臺")

        #     strs = re.findall(r'\d+', string[4])
        #     for s in strs :
        #         n = int(s)
        #         newint = str(n)
        #         address = address.replace(s, newint)

        #     if len(Lottery_store.objects.filter(address=address)) > 0 :
        #         Lottery_store.objects.filter(address=address).update(firstprize_times=F('firstprize_times') + 1)
        #         print("find")
        #     else :
        #         store_city = address[0:3]
        #         city = City.objects.get(name=store_city)
        #         Lottery_store.objects.create(
        #             name = string[3],
        #             city = city,
        #             address = address,
        #             firstprize_times = 1,
        #         )
        #         print("add store")

        #### add first prize times of 大樂透 ####
        with open(
            './docs/firstprize/firstprize_big.txt',
            encoding='utf8'
        ) as f:
            data = f.readlines()
        for line in data:
            string = line.split("   ")
            address = string[1].replace("台", "臺").replace("\n", "")
            strs = re.findall(r'\d+', string[1])
            for s in strs:
                n = int(s)
                newint = str(n)
                address = address.replace(s, newint)
            address = address.replace("一樓", "").replace("1樓", "")

            if len(Lottery_store.objects.filter(address=address)) > 0:
                Lottery_store.objects.filter(address=address).update(
                    firstprize_times=F('firstprize_times') + 1
                )
                print("find")
            else:
                store_city = address[0:3]
                city = City.objects.get(name=store_city)
                Lottery_store.objects.create(
                    name=string[0],
                    city=city,
                    address=address,
                    firstprize_times=1,
                )
                print("add store")
