# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_fundget_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundget',
            name='organization',
            field=models.ForeignKey(null=True, to='apis.Organization'),
        ),
        migrations.AlterField(
            model_name='fundget',
            name='project',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fundget',
            name='result',
            field=models.TextField(default='未公佈', blank=True),
        ),
    ]
