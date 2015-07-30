from django.core.management.base import BaseCommand
from pyPdf import PdfFileReader
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from cStringIO import StringIO
from apis.models import Surplus, City

class Command(BaseCommand):
    help = 'create surplus table'
    with open('./docs/surplus/1031.pdf') as f:
...    doc = slate.PDF(f)

    # def convert(fname, pages=None):
    #     if not pages:
    #         pagenums = set()
    #     else:
    #         pagenums = set(pages)
    #     output = StringIO()
    #     manager = PDFResourceManager()
    #     converter = TextConverter(manager, output, laparams=LAParams())
    #     interpreter = PDFPageInterpreter(manager, converter)
    #     infile = file(fname, 'rb')
    #     for page in PDFPage.get_pages(infile, pagenums):
    #         interpreter.process_page(page)
    #     infile.close()
    #     converter.close()
    #     text = output.getvalue()
    #     output.close
    #     return text 

    def handle(self, *args, **options):
        location = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣','桃園縣','新竹縣',
        '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣',
        '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']

        content = PdfFileReader("./docs/surplus/1031.pdf")
        print(content)

        # for i in range(1,13) :
        #     if i == 12 :
        #         content = convert('./docs/surplus/103'+str(12)+'.pdf')
        #         str1 = content.replace(",", "").split("(J+G+H+I)\n\n")
        #         str2 = str1[1].split("\n\n")[3].split("\n")
        #         print(i)
        #         money = []
        #         for n in str2 :
        #             money.append(int(n))
        #         for j in range(0, len(location)) :
        #             place = location[j]
        #             print(place)
        #             city = City.objects.get(name=place) 
        #             Surplus.objects.create(
        #                 year = 103,
        #                 month = i,
        #                 city = city,
        #                 surplus = money[j]
        #             )
        #     else :
        #         content = convert('./docs/surplus/103'+str(i)+'.pdf')
        #         str1 = content.replace(",", "").split("(G+H+I)\n\n")
        #         str2 = str1[1].split("\n\n")[0].split("\n")
        #         print(i)
        #         money = []
        #         for n in str2 :
        #             money.append(int(n))
        #         for j in range(0, len(location)) :
        #             place = location[j]
        #             print(place)
        #             city = City.objects.get(name=place) 
        #             Surplus.objects.create(
        #                 year = 103,
        #                 month = i,
        #                 city = city,
        #                 surplus = money[j]
        #             )