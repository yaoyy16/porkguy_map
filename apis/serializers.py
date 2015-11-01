# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import FundGet


class FundGetSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = FundGet
        fields = (
            'year', 'city',
            'org_name', 'money',
            'content', 'project',
            'result',)
