# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20150731_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city_id',
        ),
    ]
