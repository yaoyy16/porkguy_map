from django.core.management.base import BaseCommand
from apis.models import FundGet, City


class Command(BaseCommand):
    help = 'add project name to fundget table'

    def handle(self, *args, **options):
        import glob
        import xlrd

        wb = xlrd.open_workbook('./docs/fundget/100.xls')
        sh_namelist = wb.sheet_names()
        for i in range(0, len(sh_namelist)):
          sh = wb.sheet_by_index(i)
          for r in range(5,sh.nrows-1):
              FundGet.objects.filter(index=sh.cell(r,0).value).update(project=sh.cell(r,2).value)
              print(r)

        file101 = glob.glob("./docs/fundget/101*.xls")
        for j in range(0,len(file101)) :
            file101[j] = file101[j].replace("./docs/fundget\\", "")
            wb = xlrd.open_workbook('./docs/fundget/'+file101[j])
            sh = wb.sheet_by_index(0) 
            for r in range(5,sh.nrows-1):
                FundGet.objects.filter(index=sh.cell(r,0).value).update(project=sh.cell(r,2).value)
                print(r)

        wb = xlrd.open_workbook('./docs/fundget/102.xls')
        sh_namelist = wb.sheet_names()
        for i in range(0, len(sh_namelist)):
            sh = wb.sheet_by_index(i)
            for r in range(5,sh.nrows-1):
                FundGet.objects.filter(index=sh.cell(r,0).value).update(project=sh.cell(r,2).value)
                print(r)

        file103 = glob.glob("./docs/fundget/103*.xls")
        for j in range(0,len(file103)) :
            file103[j] = file103[j].replace("./docs/fundget\\", "")
            wb = xlrd.open_workbook('./docs/fundget/'+file103[j])
            sh = wb.sheet_by_index(0) 
            for r in range(5,sh.nrows-1):
                FundGet.objects.filter(index=sh.cell(r,0).value).update(project=sh.cell(r,2).value)
                print(r)