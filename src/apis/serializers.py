# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import FundGet, Organization, Lottery_store, Surplus


class OrganizationSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Organization


class FundGetSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    organization = OrganizationSerializer()

    class Meta:
        model = FundGet
        fields = (
            'year', 'city', 'org_name',
            'organization', 'money',
            'content', 'project',
            'result',)


class LotteryStoreSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    first_prize_count = serializers.IntegerField(source='firstprize_times')

    class Meta:
        model = Lottery_store
        fields = (
            'name', 'city', 'address',
            'longitude', 'latitude',
            'first_prize_count')


class SurplusSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Surplus
        fields = ('year', 'month', 'city', 'surplus')
