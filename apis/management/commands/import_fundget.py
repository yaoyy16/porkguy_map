# -- coding: utf-8 --
from django.core.management.base import BaseCommand
from apis.models import FundGet


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        fundgets = FundGet.objects.all()
        print(fundgets)
