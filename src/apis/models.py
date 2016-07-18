# -*- encoding=utf8 -*-
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=10)
    center_longitude = models.FloatField()
    center_latitude = models.FloatField()
    ne_longitude = models.FloatField()
    ne_latitude = models.FloatField()
    sw_longitude = models.FloatField()
    sw_latitude = models.FloatField()

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=15)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name


class FundGet(models.Model):
    index = models.CharField(max_length=15, primary_key=True)
    year = models.IntegerField()
    city = models.ForeignKey(City)
    organization = models.ForeignKey(Organization, null=True)
    org_name = models.CharField(max_length=30)
    money = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    project = models.CharField(max_length=100, blank=True, default='')
    result = models.TextField(default=u"未公佈", blank=True)

    def __str__(self):
        return u'[{org_name}] {year}: {money}'.format(
            org_name=self.org_name,
            year=self.year,
            money=self.money
        )


class Surplus(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    city = models.ForeignKey(City)
    surplus = models.IntegerField(default=0)

    def __str__(self):
        return u'[{city}] {year}: {surplus}'.format(
            city=self.city,
            year=self.year,
            surplus=self.surplus
        )


class Lottery_store(models.Model):
    name = models.CharField(max_length=15)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=50)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    firstprize_times = models.IntegerField(default=0)

    def __str__(self):
        return self.name
