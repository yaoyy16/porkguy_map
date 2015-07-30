from django.db import models

# Create your models here.
class City(models.Model):
	city_id = models.IntegerField()
	name = models.CharField(max_length=10)
	longitude = models.FloatField()
	latitude = models.FloatField()

class FundGet(models.Model):
	index = models.CharField(max_length=15, primary_key=True)
	year = models.IntegerField()
	city = models.ForeignKey(City)
	org_name = models.CharField(max_length=30)
	money = models.IntegerField(default=0)
	content = models.TextField(blank=True)

class Surplus(models.Model):
	year = models.IntegerField()
	month = models.IntegerField()
	city = models.ForeignKey(City)
	surplus = models.IntegerField(default=0)

class Lottery_store(models.Model):
	name = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	address = models.CharField(max_length=50)
	longitude = models.FloatField()
	latitude = models.FloatField()
	firstprize_times = models.IntegerField(default=0)

class Organization(models.Model):
	name = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	address = models.CharField(max_length=50)
	longitude = models.FloatField()
	latitude = models.FloatField()
