# coding=UTF-8
from django.shortcuts import render
from apis.models import FundGet
from apis.models import City
from apis.models import Surplus
from django.db.models import Count
from django.db.models import Sum
import json
def PageWithJquery( request ):
    return render( 'home.html')
# Create your views here.
def index(request):
    fund_list_103 = FundGet.objects.filter(year=103).exclude(city=23).values('city').annotate(Sum('money'))
    fund_list_103 = json.dumps([v for v in fund_list_103.values('city', 'money__sum')])
    fund_list_102 = FundGet.objects.filter(year=102).exclude(city=23).values('city').annotate(Sum('money'))
    fund_list_102 = json.dumps([v for v in fund_list_102.values('city', 'money__sum')])
    surp_list_103 = Surplus.objects.filter(year=103).values('city').annotate(Sum('surplus'))
    surp_list_103 = json.dumps([v for v in surp_list_103.values('city', 'surplus__sum')])
    location_list = City.objects.exclude(name='全國性')
    location_list = json.dumps([v for v in location_list.values('name', 'center_longitude', 'center_latitude', 'ne_longitude', 'ne_latitude', 'sw_longitude', 'sw_latitude')])
    return render(request, "index.html", {'fund_list_103': fund_list_103, 'fund_list_102': fund_list_102,'surp_list_103': surp_list_103, 'location_list': location_list})