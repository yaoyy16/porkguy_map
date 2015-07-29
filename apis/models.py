from django.db import models

# Create your models here.
class FundGet(models.Model):
	index = models.CharField(max_length=15, primary_key=True)
	year = models.IntegerField()
	location = models.CharField(max_length=10)
	org_name = models.CharField(max_length=30)
	money = models.IntegerField()
	content = models.TextField(blank=True)