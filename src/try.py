import csv


def csv_from_excel(fileName):
    wb = xlrd.open_workbook(fileName)
    sh = wb.sheet_by_index(0)
    your_csv_file = open(fileName.replace(".xls", ".csv"), 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sh.nrows):
        wr.writerow(
            [
                unicode(entry).encode("utf-8") for entry in sh.row_values(
                    rownum)
            ]
        )
    your_csv_file.close()
    with open(fileName.replace(".xls", ".csv"), 'rb') as f:
        data = csv.reader(f, delimiter=' ', quotechar='|')
    return data

# 103公益彩券回饋金計畫審核結果
# 各縣市在不同檔案中
# 0 編號
# 1 社福機構
# 5 審查結果
# 7 核定內容
import xlrd
wb = xlrd.open_workbook('103(縣市).xls')
sh = wb.sheet_by_index(0)
for r in range(5, sh.nrows):
    for c in [0, 1]:
        print sh.cell(r, c).value.encode(encoding="cp950",
                                         errors="ignore"), "|",
    print sh.cell(r, 5).value, "|"
    print sh.cell(r, 7).value.encode(encoding="cp950", errors="ignore"), "|",
    print r

# 102 公益彩券回饋金計畫審核結果
# 所有縣市的在不同分頁(sheet)裡
wb = xlrd.open_workbook('102年回饋金補助審核結果.xls')
sh = wb.sheet_by_index(2)  # 分頁index
for r in range(5, sh.nrows):
    for c in [0, 1]:
        print sh.cell(r, c).value.encode(encoding="cp950",
                                         errors="ignore"), "|",
    print sh.cell(r, 7).value, "|"
    print sh.cell(r, 9).value.encode(encoding="cp950", errors="ignore"), "|",
    print r

# 101 公益彩券回饋金計畫審核結果
# 各縣市在不同檔案中
# 0 編號
# 1 社福機構
# 7 審查結果
# 9 核定內容
wb = xlrd.open_workbook('101苗栗縣.xls')
sh = wb.sheet_by_index(0)
for r in range(5, sh.nrows):
    for c in [0, 1]:
        print sh.cell(r, c).value.encode(encoding="cp950",
                                         errors="ignore"), "|",
    print sh.cell(r, 7).value, "|"
    print sh.cell(r, 9).value.encode(encoding="cp950", errors="ignore"), "|",
    print r

# 100 公益彩券回饋金計畫審核結果
# 所有縣市的在不同分頁(sheet)裡
# 0 編號
# 1 社福機構
# 8 審查結果
# 10 核定內容
wb = xlrd.open_workbook('100年回饋金補助審核結果.xls')
sh = wb.sheet_by_index(2)  # 分頁index
for r in range(5, sh.nrows):
    for c in [0, 1]:
        print sh.cell(r, c).value.encode(encoding="cp950",
                                         errors="ignore"), "|",
    print sh.cell(r, 8).value, "|"
    print sh.cell(r, 10).value.encode(encoding="cp950", errors="ignore"), "|",
    print r

# create data
from apis.models import FundGet
import xlrd

wb = xlrd.open_workbook('./fundget/102.xls')
sh_namelist = wb.sheet_names()

for i in range(0, len(sh_namelist)):
    location = sh_namelist[i].encode(encoding="utf-8", errors="ignore")
    sh = wb.sheet_by_index(i)
    for r in range(5, sh.nrows - 1):

        FundGet.objects.create(
            index=sh.cell(r, 0).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            year=103,
            location=location,
            org_name=sh.cell(r, 1).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            money=sh.cell(r, 7).value,
            content=sh.cell(r, 9).value.encode(
                encoding="utf-8",
                errors="ignore"
            )
        )

# creat data for 101 & 103
import glob
file101 = glob.glob("./fundget/103*.xls")

for j in range(0, len(file101)):
    file101[j] = file101[j].replace("./fundget\\", "")
    wb = xlrd.open_workbook('./fundget/' + file101[j])

    sh = wb.sheet_by_index(0)
    location = file101[j].replace("101", "").replace(".xls", "")
    print location
    location = location.decode(encoding="cp950", errors="ignore")
    location = location.encode(encoding="utf-8", errors="ignore")
    for r in range(5, sh.nrows - 1):
        FundGet.objects.create(
            index=sh.cell(r, 0).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            year=101,
            location=location,
            org_name=sh.cell(r, 1).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            money=sh.cell(r, 7).value,
            content=sh.cell(r, 9).value.encode(
                encoding="utf-8",
                errors="ignore"
            )
        )

file103 = glob.glob("./fundget/103*.xls")

for j in range(0, len(file101)):
    file103[j] = file103[j].replace("./fundget\\", "")
    wb = xlrd.open_workbook('./fundget/' + file103[j])

    sh = wb.sheet_by_index(0)
    location = file103[j].replace("103", "").replace(".xls", "")
    print location
    location = location.decode(encoding="cp950", errors="ignore")
    location = location.encode(encoding="utf-8", errors="ignore")
    for r in range(5, sh.nrows - 1):
        FundGet.objects.create(
            index=sh.cell(r, 0).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            year=103,
            location=location,
            org_name=sh.cell(r, 1).value.encode(
                encoding="utf-8",
                errors="ignore"
            ),
            money=sh.cell(r, 5).value,
            content=sh.cell(r, 7).value.encode(
                encoding="utf-8",
                errors="ignore"
            )
        )

FundGet.objects.filter(year=101).delete()
FundGet.objects.filter(location).delete()
# update(location='捷運大安站')

# 公益彩券盈餘分配
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from apis.models import Surplus


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


location = [
    '臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣', '桃園縣', '新竹縣', '苗栗縣', '彰化縣',
    '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣', '基隆市', '新竹市', '嘉義市',
    '金門縣', '連江縣', 'fm06'
]

for i in range(1, 13):
    content = convert('./surplus/103' + str(i) + '.pdf')
    str1 = content.replace(",", "").split("(G+H+I)\n\n")
    str2 = str1[1].split("\n\n")[0].split("\n")
    print i
    money = []
    for n in str2:
        money.append(int(n))
    for j in range(0, len(location)):
        place = location[j].decode(encoding="utf-8", errors="ignore")
        print place
        Surplus.objects.create(
            year=103,
            month=i,
            location=place,
            surplus=money[j]
        )

import urllib
import urlparse
import requests
url = "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx"
data = '__EVENTTARGET=DropDownList1&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCBQ8QZA8WAWYWARAFEuiri"%"2BWFiOmBuOaTh"%"2Be4o"%"2BW4ggUBMGdkZAIJDxYCHgRUZXh0ZWRkd"%"2BTuIrQ"%"2FF8WUr6a"%"2FseU20Sjr4NH"%"2FLgXmxkH7MtCnbaQ"%"3D&__EVENTVALIDATION="%"2FwEWGwLUqtGAAwKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKOi6WLBgKM54rGBsIHFqCV0TzwENfeTcuCJaINSvb6OFvVtTwP1JeOQ4X"%"2B&DropDownList1=1&DropDownList2=0'
data = urlparse.parse_qs(data)
req = requests.post(url, data)

htmlfile = open("5.html", "w")
htmlfile.write(req.content)
htmlfile.close()
