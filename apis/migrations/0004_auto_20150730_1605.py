# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20150730_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='index',
            new_name='city_id',
        ),
    ]
