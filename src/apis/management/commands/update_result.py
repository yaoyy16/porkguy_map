from django.core.management.base import BaseCommand
from apis.models import FundGet, City


class Command(BaseCommand):
    help = 'update result of project in fundget table'

    def handle(self, *args, **options):
        import glob
        import xlrd

        wb = xlrd.open_workbook('./docs/result/100.xls')
        sh = wb.sheet_by_index(0)
        for r in range(5, sh.nrows - 2):
            FundGet.objects.filter(index=sh.cell(r, 1).value).update(
                result=sh.cell(r, 9).value)
            print(sh.cell(r, 1).value)
            print(sh.cell(r, 9).value)
            print(r)

        wb = xlrd.open_workbook('./docs/result/101.xls')
        sh = wb.sheet_by_index(0)
        for r in range(5, sh.nrows - 2):
            try:
                a = FundGet.objects.get(index=sh.cell(r, 1).value)
                a.result = sh.cell(r, 10).value
                a.save()
                print(r)
            except Exception as e:
                print(e)

        wb = xlrd.open_workbook('./docs/result/102.xlsx')
        sh = wb.sheet_by_index(0)
        for r in range(5, sh.nrows - 2):
            try:
                a = FundGet.objects.get(index=sh.cell(r, 1).value)
                a.result = sh.cell(r, 10).value
                a.save()
                print(r)
            except Exception as e:
                print(e)
