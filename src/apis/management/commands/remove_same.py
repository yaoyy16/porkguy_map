from django.core.management.base import BaseCommand
from apis.models import Lottery_store, City


class Command(BaseCommand):
    help = 'remove duplicate store in table'

    def handle(self, *args, **options):
    	i = 0
    	for store in Lottery_store.objects.all():
    		for pre_store in Lottery_store.objects.filter(id__lt=store.id):
    			if store.address == pre_store.address:
                    # i += 1
                    # print(i)

                    print(store.address)
    				store.delete()
