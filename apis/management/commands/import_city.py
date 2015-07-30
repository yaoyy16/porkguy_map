from django.core.management.base import BaseCommand
from apis.models import City

class Command(BaseCommand):
    help = 'create city table'

    def handle(self, *args, **options):
        city_name = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣', '桃園縣', '新竹縣', '苗栗縣', '彰化縣', '南投縣',
        			 '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣', '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣',
        			 '全國性']
        for i in range(0, len(city_name)):
        	city = city_name[i]
	        print(city)
	        City.objects.create(
	            city_id = i,
				name = city,
				longitude = 0,
				latitude = 0
	        )
