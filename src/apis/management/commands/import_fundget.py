# -- coding: utf-8 --
from django.core.management.base import BaseCommand
from apis.models import FundGet, City


class Command(BaseCommand):
    help = 'create fundget table'

    def handle(self, *args, **options):
        import glob
        import xlrd

        # create data of year 100
        wb = xlrd.open_workbook('./docs/fundget/100.xls')
        sh_namelist = wb.sheet_names()

        for i in range(0, len(sh_namelist)):
            location = sh_namelist[i]
            if location == "臺北縣":
                location = "新北市"
            elif location == "高雄縣":
                location = "高雄市"
            elif location == "臺南縣":
                location = "臺南市"
            elif location == "臺中縣":
                location = "臺中市"
            elif location == "桃園縣":
                location = "桃園市"

            print(location)
            sh = wb.sheet_by_index(i)
            city = City.objects.get(name=location)
            for r in range(5, sh.nrows - 1):
                FundGet.objects.create(
                    index=sh.cell(r, 0).value,
                    year=100,
                    city=city,
                    org_name=sh.cell(r, 1).value,
                    money=sh.cell(r, 8).value,
                    content=sh.cell(r, 10).value
                )

        # create data of year 101
        file101 = glob.glob("./docs/fundget/101*.xls")
        for j in range(0, len(file101)):
            file101[j] = file101[j].replace("./docs/fundget\\", "")
            wb = xlrd.open_workbook('./docs/fundget/' + file101[j])
            sh = wb.sheet_by_index(0)
            location = file101[j].replace("101", "").replace(".xls", "")
            if location == "桃園縣":
                location = "桃園市"
            city = City.objects.get(name=location)
            print(location)
            for r in range(5, sh.nrows - 1):
                FundGet.objects.create(
                    index=sh.cell(r, 0).value,
                    year=101,
                    city=city,
                    org_name=sh.cell(r, 1).value,
                    money=sh.cell(r, 7).value,
                    content=sh.cell(r, 9).value
                )

        # create data of year 102
        wb = xlrd.open_workbook('./docs/fundget/102.xls')
        sh_namelist = wb.sheet_names()

        for i in range(0, len(sh_namelist)):
            location = sh_namelist[i]
            if location == "桃園縣":
                location = "桃園市"
            print(location)
            sh = wb.sheet_by_index(i)
            city = City.objects.get(name=location)
            for r in range(5, sh.nrows - 1):
                FundGet.objects.create(
                    index=sh.cell(r, 0).value,
                    year=102,
                    city=city,
                    org_name=sh.cell(r, 1).value,
                    money=sh.cell(r, 7).value,
                    content=sh.cell(r, 9).value
                )

        # create data of year 103
        file103 = glob.glob("./docs/fundget/103*.xls")
        for j in range(0, len(file103)):
            file103[j] = file103[j].replace("./docs/fundget\\", "")
            wb = xlrd.open_workbook('./docs/fundget/' + file103[j])
            sh = wb.sheet_by_index(0)
            location = file103[j].replace("103", "").replace(".xls", "")
            if location == "桃園縣":
                location = "桃園市"
            city = City.objects.get(name=location)
            print(location)
            for r in range(5, sh.nrows - 1):
                FundGet.objects.create(
                    index=sh.cell(r, 0).value,
                    year=103,
                    city=city,
                    org_name=sh.cell(r, 1).value,
                    money=sh.cell(r, 5).value,
                    content=sh.cell(r, 7).value
                )
