import django_filters

from rest_framework import viewsets

from .models import FundGet, Lottery_store, Surplus
from .serializers import (FundGetSerializer,
                          LotteryStoreSerializer,
                          SurplusSerializer)


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
    first_prize = django_filters.NumberFilter(name="firstprize_times")

    class Meta:
        model = Lottery_store
        fields = ['city', 'name', 'first_prize']


class LotteryStoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lottery_store.objects.all()
    serializer_class = LotteryStoreSerializer
    filter_class = LotteryStoreFilter


class SurplusFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name="city__name")
    min_surplus = django_filters.NumberFilter(
        name="surplus", lookup_type='gte')

    class Meta:
        model = Surplus
        fields = ['city', 'year', 'month', 'min_surplus']


class SurplusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Surplus.objects.all()
    serializer_class = SurplusSerializer
    filter_class = SurplusFilter
