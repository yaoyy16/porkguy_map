from django.core.management.base import BaseCommand
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from apis.models import Surplus, City

class Command(BaseCommand):
    help = 'create surplus table'

    def handle(self, *args, **options):

        location = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣','桃園縣','新竹縣',
        '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣',
        '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']

        fp = open("./docs/surplus/1031.pdf", 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    print(lt_obj.get_text())

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