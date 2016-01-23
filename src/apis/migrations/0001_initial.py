# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, verbose_name='ID', serialize=False)),
                ('city_id', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('center_longitude', models.FloatField()),
                ('center_latitude', models.FloatField()),
                ('ne_longitude', models.FloatField()),
                ('ne_latitude', models.FloatField()),
                ('sw_longitude', models.FloatField()),
                ('sw_latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FundGet',
            fields=[
                ('index', models.CharField(
                    primary_key=True, serialize=False, max_length=15)),
                ('year', models.IntegerField()),
                ('org_name', models.CharField(max_length=30)),
                ('money', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True)),
                ('city', models.ForeignKey(to='apis.City')),
            ],
        ),
        migrations.CreateModel(
            name='Lottery_store',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('firstprize_times', models.IntegerField(default=0)),
                ('city', models.ForeignKey(to='apis.City')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('city', models.ForeignKey(to='apis.City')),
            ],
        ),
        migrations.CreateModel(
            name='Surplus',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, verbose_name='ID', serialize=False)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('surplus', models.IntegerField(default=0)),
                ('city', models.ForeignKey(to='apis.City')),
            ],
        ),
    ]
