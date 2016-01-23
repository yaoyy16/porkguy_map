from django.contrib import admin
from apis.models import City
from apis.models import FundGet
from apis.models import Surplus
from apis.models import Lottery_store
from apis.models import Organization

# # # Register your models here.
admin.site.register(City)
admin.site.register(FundGet)
admin.site.register(Surplus)
admin.site.register(Lottery_store)
admin.site.register(Organization)
