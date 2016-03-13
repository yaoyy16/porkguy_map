from django.core.management.base import BaseCommand
from apis.models import Organization, City


class Command(BaseCommand):
    help = 'create Organization table'

    def handle(self, *args, **options):
        import re

        with open('./docs/org.txt', encoding='utf8') as f:
            data = f.readlines()
        i = 1
        for line in data:
            print(i)
            space = re.findall(r'\s+', line)
            line = line.split(space[0])
            if len(line) == 1:
                continue
            if line[1][0].isdigit():
                num = re.findall(r'\d+', line[1])
                zip_code = num[0]
                address = line[1].replace(zip_code, "").replace("台", "臺")
            else:
                address = line[1].replace("台", "臺")
            address = address.split("、")[0]
            org_city = address[0:3]
            if org_city == "臺北縣":
                org_city = "新北市"
            elif org_city == "高雄縣":
                org_city = "高雄市"
            elif org_city == "臺南縣":
                org_city = "臺南市"
            elif org_city == "臺中縣":
                org_city = "臺中市"
            elif org_city == "桃園縣":
                org_city = "桃園市"
            city = City.objects.get(name=org_city)
            # print(line[0], "| ", address)
            i += 1
            Organization.objects.create(
                name=line[0],
                city=city,
                address=address,
                longitude=0,
                latitude=0
            )
