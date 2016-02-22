from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        import urllib
        import urllib.parse
        import requests
        import time
        import re
        from bs4 import BeautifulSoup

        #### get first prize store html ####

        # url = "http://www.taiwanlottery.com.tw/Lotto/se/store.aspx?TYPE=539"
        # data = "__EVENTTARGET=StoreControl1%24GridView1&__EVENTARGUMENT=Page%2432&__VIEWSTATE=%2FwEPDwUKMjA3NDYwOTIxMw9kFgICAQ9kFgICAw9kFggCAQ8QZBAVBAnlqIHlipvlvakJ5aSn5qiC6YCPCeWkp%2Bemj%2BW9qQnku4rlvak1MzkVBAnlqIHlipvlvakJ5aSn5qiC6YCPCeWkp%2Bemj%2BW9qQnku4rlvak1MzkUKwMEZ2dnZ2RkAgUPEGQQFRcDQWxsCeWPsOWMl%2BW4ggnpq5jpm4TluIIJ5paw5YyX5biCCeWunOiYree4ownmoYPlnJLluIIJ5paw56u557ijCeiLl%2Bagl%2Be4ownlvbDljJbnuKMJ5Y2X5oqV57ijCembsuael%2Be4ownlmInnvqnnuKMJ5bGP5p2x57ijCeWPsOadsee4ownoirHok67nuKMJ5r6O5rmW57ijCeWfuumahuW4ggnmlrDnq7nluIIJ5Y%2Bw5Lit5biCCeWYiee%2BqeW4ggnlj7DljZfluIIJ6YeR6ZaA57ijCemAo%2Baxn%2Be4oxUXA0FsbAnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl%2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl%2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj%2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea%2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y%2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ%2FnuKMUKwMXZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIJDxYCHgRUZXh0ZWQCCw88KwARAgAPFgYeC18hRGF0YUJvdW5kZx4LXyFJdGVtQ291bnQC%2FQQeF0ZpcnN0RGlzcGxheWVkUGFnZUluZGV4AhZkARAWABYAFgAWAmYPZBYqAgEPZBYKZg8PFgIfAAUCMzdkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMjJkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yNWRkAgMPZBYCAgEPDxYCHwAFD%2BmHkeWIqemmrOWVhuihjGRkAgQPZBYCAgEPDxYCHwAFMOaWsOWMl%2BW4guS4iemHjeWNgOS4reato%2BWMl%2Bi3r%2B%2B8ku%2B8lu%2B8meiZn%2B%2B8keaok2RkAgIPZBYKZg8PFgIfAAUCMzZkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMjFkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yNGRkAgMPZBYCAgEPDxYCHwAFD%2BiMguWvjOW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFM%2BWPsOWMl%2BW4guWNl%2Ba4r%2BWNgOiIiOiPr%2Bi3r%2B%2B8k%2B%2B8kOW3t%2B%2B8ke%2B8l%2BiZn%2B%2B8keaok2RkAgMPZBYKZg8PFgIfAAUCMzVkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMjBkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yM2RkAgMPZBYCAgEPDxYCHwAFD%2Bi2hee0muaKleazqOermWRkAgQPZBYCAgEPDxYCHwAFJOaWsOWMl%2BW4guS4ieWzveWNgOWkp%2BWQjOi3r%2B%2B8mO%2B8luiZn2RkAgQPZBYKZg8PFgIfAAUCMzRkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMjBkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yM2RkAgMPZBYCAgEPDxYCHwAFD%2BWMl%2BiyoeelnuWVhuihjGRkAgQPZBYCAgEPDxYCHwAFPOahg%2BWckuW4guWkp%2BWckuWNgOWMl%2Ba4r%2BadkeWkp%2BingOi3r%2B%2B8le%2B8ku%2B8lu%2B8je%2B8kuiZn%2B%2B8keaok2RkAgUPZBYKZg8PFgIfAAUCMzNkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMjBkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yM2RkAgMPZBYCAgEPDxYCHwAFFeWFg%2BWGoOmbu%2BiFpuW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFOeW9sOWMlue4o%2BWflOW%2Fg%2BmEiee%2BqeawkeadkeWToem5v%2BS6jOaute%2B8le%2B8ku%2B8mOiZn%2B%2B8keaok2RkAgYPZBYKZg8PFgIfAAUCMzJkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTlkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yMmRkAgMPZBYCAgEPDxYCHwAFD%2BWwmueZvOW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFM%2BWPsOWMl%2BW4guS4reWxseWNgOWMl%2BWuiei3r%2B%2B8le%2B8ke%2B8lOS5i%2B%2B8keiZn%2B%2B8keaok2RkAgcPZBYKZg8PFgIfAAUCMzFkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTlkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yMmRkAgMPZBYCAgEPDxYCHwAFD%2BiBluWEhOW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFLeWPsOWNl%2BW4guWuieW5s%2BWNgOaWh%2BW5s%2Bi3r%2B%2B8k%2B%2B8lu%2B8l%2BiZn%2B%2B8keaok2RkAggPZBYKZg8PFgIfAAUCMzBkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMThkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yMWRkAgMPZBYCAgEPDxYCHwAFD%2BaYk%2BWvjOaKleazqOermWRkAgQPZBYCAgEPDxYCHwAFLeaWsOWMl%2BW4guaWsOW6l%2BWNgOawkeaXj%2Bi3r%2B%2B8ku%2B8ku%2B8keiZn%2B%2B8keaok2RkAgkPZBYKZg8PFgIfAAUCMjlkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTdkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8yMGRkAgMPZBYCAgEPDxYCHwAFD%2Be%2BjummmeW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFPOaWsOWMl%2BW4guWcn%2BWfjuWNgOS4reWkrui3r%2BS6jOaute%2B8ku%2B8l%2B%2B8mOW3t%2B%2B8ke%2B8kuiZn%2B%2B8keaok2RkAgoPZBYKZg8PFgIfAAUCMjhkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTZkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xOGRkAgMPZBYCAgEPDxYCHwAFDOaXuuaXuuWVhuihjGRkAgQPZBYCAgEPDxYCHwAFLeWunOiYree4o%2BWGrOWxsemEiee%2BqeaIkOi3r%2BS4ieaute%2B8k%2B%2B8l%2B%2B8kuiZn2RkAgsPZBYKZg8PFgIfAAUCMjdkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTZkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xOGRkAgMPZBYCAgEPDxYCHwAFD%2BmHkemghuaogumAj%2BermWRkAgQPZBYCAgEPDxYCHwAFP%2Bahg%2BWckuW4guaWsOWxi%2BWNgOa4heiPr%2BadkeS4reWxseadsei3r%2BS4gOaute%2B8ke%2B8mO%2B8keiZn%2B%2B8keaok2RkAgwPZBYKZg8PFgIfAAUCMjZkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTZkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xOGRkAgMPZBYCAgEPDxYCHwAFEumHkemBi%2BmHkeW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFM%2Bahg%2BWckuW4guS4reWjouWNgOS4reWOn%2BmHjOiIiOi%2Bsui3r%2B%2B8mO%2B8keiZn%2B%2B8keaok2RkAg0PZBYKZg8PFgIfAAUCMjVkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTZkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xOGRkAgMPZBYCAgEPDxYCHwAFD%2Ba6quW0keW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFM%2BaWsOWMl%2BW4guadv%2Bapi%2BWNgOa6quW0keS6jOihl%2B%2B8ke%2B8ke%2B8kuW3t%2B%2B8ku%2B8kuiZn2RkAg4PZBYKZg8PFgIfAAUCMjRkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTVkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xN2RkAgMPZBYCAgEPDxYCHwAFEuWPrOiyoeWIqeW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFJ%2BWPsOWMl%2BW4guiQrOiPr%2BWNgOW7o%2BW3nuihl%2B%2B8ke%2B8mO%2B8meiZn2RkAg8PZBYKZg8PFgIfAAUCMjNkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTRkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNmRkAgMPZBYCAgEPDxYCHwAFDOeFp%2BmBlOWVhuihjGRkAgQPZBYCAgEPDxYCHwAFLeaWsOerueW4guWMl%2BWNgOS4reiIiOmHjOWMl%2BmWgOihl%2BS6lOiZn%2BS4gOaok2RkAhAPZBYKZg8PFgIfAAUCMjJkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTRkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNmRkAgMPZBYCAgEPDxYCHwAFEuWFq%2BS9sOWEhOW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFMOWPsOWMl%2BW4guS4reWxseWNgOael%2BajruWMl%2Bi3r%2B%2B8ke%2B8k%2B%2B8lOiZn%2B%2B8keaok2RkAhEPZBYKZg8PFgIfAAUCMjFkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTNkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNWRkAgMPZBYCAgEPDxYCHwAFEuWEhOmjm%2BS%2BhuW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFMOahg%2BWckuW4guWkp%2Ba6quWNgOiIiOWSjOmHjOS4reWxsei3r%2B%2B8keiZn%2B%2B8keaok2RkAhIPZBYKZg8PFgIfAAUCMjBkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTNkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNWRkAgMPZBYCAgEPDxYCHwAFD%2BaWsOWvtuS8gealreekvmRkAgQPZBYCAgEPDxYCHwAFJOWxj%2Badsee4o%2BWxj%2BadseW4guW%2BqeiIiOWMl%2Bi3r%2B%2B8luiZn2RkAhMPZBYKZg8PFgIfAAUCMTlkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTJkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNGRkAgMPZBYCAgEPDxYCHwAFEuWQiemWi%2BmBi%2BW9qeWIuOihjGRkAgQPZBYCAgEPDxYCHwAFJOmrmOmbhOW4gumzs%2BWxseWNgOWkp%2BaYjui3r%2B%2B8lO%2B8mOiZn2RkAhQPZBYKZg8PFgIfAAUCMThkZAIBD2QWAgIBDw8WAh8ABQkxMDMwMDAwMTJkZAICD2QWAgIBDw8WAh8ABQgxMDMvMS8xNGRkAgMPZBYCAgEPDxYCHwAFD%2BmHkeS%2BhuWvjOWVhuihjGRkAgQPZBYCAgEPDxYCHwAFKuWPsOWNl%2BW4guWNl%2BWNgOaWh%2BWNl%2Bi3r%2B%2B8ke%2B8ku%2B8kOiZn%2B%2B8keaok2RkAhUPDxYCHgdWaXNpYmxlaGRkGAEFF1N0b3JlQ29udHJvbDEkR3JpZFZpZXcxDzwrAAwCAgIeCAIgZOMa%2FNJ1JpOwS9c56mQFcbrAHBkWby56HU%2FDs2oyOKll&__EVENTVALIDATION=%2FwEWKAKO%2B4C6AgKgvrfGDwKEmLm2DwKKtMedCAKBxJ%2FBCgKaldbRBgLFw9iGCQLI5vvpCAKg8aCHDQKIsvvpCAL3xu3xDQLF1ZeICQKTgt2WBAK80YaDCwLTz4HbCgK8sI3XCwLRuIb%2FCwL6uZ28BALEzb36CwLTtr36CwKS0OLnDQKFroGNCwLO7qeFDQKIsrOnCgLI5sPGDwL%2F6fPyCgLI5vvrCAKyu%2FrsDgKgtaa9CwKSpLqTBQKq6fvZBwK1gNnyCQLkvLazCwLP15WkDQK%2BkvLkDgKZpdCZAQK4zc2NDQKD5LOnBwKQm7vkAwKq6ffZB%2FiGN3DRfsQNrxZlPHtriA786vznE6%2BsO8sSbzvcnBIN&StoreControl1%24DropDownList1=%E4%BB%8A%E5%BD%A9539&StoreControl1%24TextBox1=&StoreControl1%24DropDownList5=All"
        # data = urllib.parse.parse_qs(data)

        # for i in range(1,33) :
        #     event_arg = "Page${}".format(i)
        #     data['__EVENTARGUMENT'] = event_arg
        #     print(data['__EVENTARGUMENT'])
        #     req = requests.post(url, data)
        #     htmlfile = open("./docs/firstprize/"+str(i)+".html", "wb")
        #     htmlfile.write(req.content)
        #     htmlfile.close()
        #     time.sleep(3)

        #### read html file ###

        text_file = open("./docs/firstprize/firstprize539.txt", "wb")
        for i in range(1, 33):
            data = open("./docs/firstprize/" + str(i) +
                        ".html", 'r', encoding="utf-8").read()
            soup = BeautifulSoup(data, 'html.parser')
            prizes1 = soup.findAll("tr", {"class": "table_level_1"})
            prizes2 = soup.findAll("tr", {"class": "table_level_2"})

            for prize in prizes1:
                line = prize.find("td").get_text() + " "
                details = prize.findAll("span")
                line += details[2].get_text()
                line += " "
                strs = re.findall(r'\d+', details[3].get_text())
                address = details[3].get_text()
                for s in strs:
                    n = int(s)
                    newint = str(n)
                    address = address.replace(s, newint)
                address = address.replace("一樓", "").replace("1樓", "")
                line += address
                line += "\n"
                text_file.write(bytes(line, 'utf-8'))

            for prize in prizes2:
                line = prize.find("td").get_text() + " "
                details = prize.findAll("span")
                line += details[2].get_text()
                line += " "
                strs = re.findall(r'\d+', details[3].get_text())
                address = details[3].get_text()
                for s in strs:
                    n = int(s)
                    newint = str(n)
                    address = address.replace(s, newint)
                address = address.replace("一樓", "").replace("1樓", "")
                line += address
                line += "\n"
                text_file.write(bytes(line, 'utf-8'))

            print(i, "is done")
        text_file.close()
