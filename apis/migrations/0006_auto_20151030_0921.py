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
            field=models.ForeignKey(to='apis.Organization', null=True),
        ),
        migrations.AlterField(
            model_name='fundget',
            name='project',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='fundget',
            name='result',
            field=models.TextField(default='\u672a\u516c\u4f48', blank=True),
        ),
    ]
