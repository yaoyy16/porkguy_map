# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('apis', '0004_merge'), ]

    operations = [
        migrations.AddField(
            model_name='fundget',
            name='result',
            field=models.TextField(default='未公佈',
                                   null=True,
                                   blank=True),
        ),
    ]
