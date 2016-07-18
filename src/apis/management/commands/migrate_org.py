from django.core.management.base import BaseCommand
from apis.models import Organization, FundGet


class Command(BaseCommand):
    help = 'Add Organization object into FundGet'

    def handle(self, *args, **options):
        funds = FundGet.objects.all()
        print(funds.count())
        for fund in funds:
            orgs = Organization.objects.filter(name=fund.org_name)
            if orgs.count() > 0:
                fund.organization = orgs[0]
                fund.save()
            else:
                print(fund.org_name)
