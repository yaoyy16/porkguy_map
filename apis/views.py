import django_filters

from rest_framework import viewsets

from .models import FundGet, Lottery_store
from .serializers import FundGetSerializer, LotteryStoreSerializer


class FundGetFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name="city__name")
    org_name = django_filters.CharFilter(
        name="org_name", lookup_type="contains")

    class Meta:
        model = FundGet
        fields = ['city', 'year', 'org_name']


class FundGetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundGet.objects.all()
    serializer_class = FundGetSerializer
    filter_class = FundGetFilter


class LotteryStoreFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name="city__name")
    name = django_filters.CharFilter(name="name", lookup_type="contains")
    min_first_prize = django_filters.NumberFilter(
        name="firstprize_times", lookup_type='gte')

    class Meta:
        model = Lottery_store

        fields = ['city', 'name', 'min_first_prize']


class LotteryStoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lottery_store.objects.all()
    serializer_class = LotteryStoreSerializer
    filter_class = LotteryStoreFilter
