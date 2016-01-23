# coding=UTF-8
from django.shortcuts import render
from apis.models import FundGet
from apis.models import City
from apis.models import Surplus
from apis.models import Lottery_store
from apis.models import Organization
from django.db.models import Count
from django.db.models import Sum
import json


def PageWithJquery(request):
    return render('home.html')
# Create your views here.


def showmap(request):
    fund_list_103 = FundGet.objects.filter(year=103).exclude(
        city=23).values('city').annotate(Sum('money'))
    fund_list_103 = json.dumps(
        [v for v in fund_list_103.values('city', 'money__sum')])
    fund_org_103 = FundGet.objects.filter(year=103).exclude(city=23)
    fund_org_103 = json.dumps(
        [v for v in fund_org_103.values('org_name', 'money', 'content')])
    fund_list_102 = FundGet.objects.filter(year=102).exclude(
        city=23).values('city').annotate(Sum('money'))
    fund_list_102 = json.dumps(
        [v for v in fund_list_102.values('city', 'money__sum')])
    fund_org_102 = FundGet.objects.filter(year=102).exclude(city=23)
    fund_org_102 = json.dumps(
        [v for v in fund_org_102.values('org_name', 'money', 'content')])
    fund_list_101 = FundGet.objects.filter(year=101).exclude(
        city=23).values('city').annotate(Sum('money'))
    fund_list_101 = json.dumps(
        [v for v in fund_list_101.values('city', 'money__sum')])
    fund_org_101 = FundGet.objects.filter(year=101).exclude(city=23)
    fund_org_101 = json.dumps(
        [v for v in fund_org_101.values('org_name', 'money', 'content')])
    fund_list_100 = FundGet.objects.filter(year=100).exclude(
        city=23).values('city').annotate(Sum('money'))
    fund_list_100 = json.dumps(
        [v for v in fund_list_100.values('city', 'money__sum')])
    fund_org_100 = FundGet.objects.filter(year=100).exclude(city=23)
    fund_org_100 = json.dumps(
        [v for v in fund_org_100.values('org_name', 'money', 'content')])
    surp_list_103 = Surplus.objects.filter(
        year=103).values('city').annotate(Sum('surplus'))
    surp_list_103 = json.dumps(
        [v for v in surp_list_103.values('city', 'surplus__sum')])
    surp_list_102 = Surplus.objects.filter(
        year=102).values('city').annotate(Sum('surplus'))
    surp_list_102 = json.dumps(
        [v for v in surp_list_102.values('city', 'surplus__sum')])
    surp_list_101 = Surplus.objects.filter(
        year=101).values('city').annotate(Sum('surplus'))
    surp_list_101 = json.dumps(
        [v for v in surp_list_101.values('city', 'surplus__sum')])
    surp_list_100 = Surplus.objects.filter(
        year=100).values('city').annotate(Sum('surplus'))
    surp_list_100 = json.dumps(
        [v for v in surp_list_100.values('city', 'surplus__sum')])
    prize_list = Lottery_store.objects.all().values(
        'city').annotate(Sum('firstprize_times'))
    prize_list = json.dumps(
        [v for v in prize_list.values('city', 'firstprize_times__sum')])
    store_list = Lottery_store.objects.all()
    store_list = json.dumps([v for v in store_list.values(
        'name', 'city', 'address', 'latitude', 'longitude', 'firstprize_times')])
    store_count_list = Lottery_store.objects.all().values(
        'city').annotate(Count('address'))
    store_count_list = json.dumps(
        [v for v in store_count_list.values('city', 'address__count')])
    organization_list = Organization.objects.all()
    organization_list = json.dumps([v for v in organization_list.values(
        'id', 'name', 'city', 'address', 'latitude', 'longitude')])
    organization_count_list = Organization.objects.all().values(
        'city').annotate(Count('address'))
    organization_count_list = json.dumps(
        [v for v in organization_count_list.values('city', 'address__count')])
    location_list = City.objects.exclude(name='全國性')
    location_list = json.dumps([v for v in location_list.values(
        'id', 'name', 'center_longitude', 'center_latitude', 'ne_longitude', 'ne_latitude', 'sw_longitude', 'sw_latitude')])
    return render(request, "map.html",
                  {'fund_list_103': fund_list_103,
                   'fund_list_102': fund_list_102,
                   'fund_list_101': fund_list_101,
                   'fund_list_100': fund_list_100,
                   'fund_org_103': fund_org_103,
                   'fund_org_102': fund_org_102,
                   'fund_org_101': fund_org_101,
                   'fund_org_100': fund_org_100,
                   'surp_list_103': surp_list_103,
                   'surp_list_102': surp_list_102,
                   'surp_list_101': surp_list_101,
                   'surp_list_100': surp_list_100,
                   'prize_list': prize_list,
                   'store_list': store_list,
                   'organization_list': organization_list,
                   'store_count_list': store_count_list,
                   'organization_count_list': organization_count_list,
                   'location_list': location_list})
