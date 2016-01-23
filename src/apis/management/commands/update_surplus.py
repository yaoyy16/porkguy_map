from django.core.management.base import BaseCommand
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from apis.models import Surplus, City


class Command(BaseCommand):
    help = 'update surplus table'

    def handle(self, *args, **options):
        location = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣', '桃園市', '新竹縣',
                    '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣',
                    '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']
        with open('./docs/surplus.txt') as f:
            data = f.readlines()
        lines = []
        for line in data:
            lines.append(line.replace("\n", "").replace(
                ",", "").replace("\t", ""))

        k = 0
        for i in range(7, 13):
            for j in range(0, 22):
                city = City.objects.get(name=location[j])
                Surplus.objects.create(
                    year=101,
                    month=i,
                    city=city,
                    surplus=lines[k]
                )
                print(101, i, lines[k], location[j])
                k += 1

        for i in range(1, 13):
            for j in range(0, 22):
                city = City.objects.get(name=location[j])
                Surplus.objects.create(
                    year=102,
                    month=i,
                    city=city,
                    surplus=lines[k]
                )
                print(102, i, lines[k], location[j])
                k += 1

        # def convert(filename):
        #     import pdb;pdb.set_trace()
        #     fp = open(filename, 'rb')
        #     parser = PDFParser(fp)
        #     doc = PDFDocument()
        #     parser.set_document(doc)
        #     doc.set_parser(parser)
        #     doc.initialize('')
        #     rsrcmgr = PDFResourceManager()
        #     laparams = LAParams()
        #     device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        #     interpreter = PDFPageInterpreter(rsrcmgr, device)
        #     content = ""
        #     # Process each page contained in the document.
        #     for page in doc.get_pages():
        #         interpreter.process_page(page)
        #         layout = device.get_result()
        #         for lt_obj in layout:
        #             if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
        #                 content += lt_obj.get_text()
        #     return content

        # location = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣','桃園市','新竹縣',
        # '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣',
        # '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣']

        # 　add 100 1~12  & 101 1~6
        # for i in range(7,13) :
        #     content = convert('./docs/surplus/101'+str(i)+'.pdf')
        #     print(content)
            # str1 = content.replace(",", "").split("公益彩券盈餘分配")
            # str2 = str1[-1].split("\n")[1:23]
            # money = []
            # for n in str2 :
            #     money.append(int(n))
            # for j in range(0, 22) :
            #     print(money[j])
            #     city = City.objects.get(name=location[j])
            #     Surplus.objects.create(
            #         year = 101,
            #         month = i,
            #         city = city,
            #         surplus = money[j]
            #     )
