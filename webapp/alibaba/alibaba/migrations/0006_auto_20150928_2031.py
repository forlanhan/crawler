# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alibaba', '0005_auto_20150928_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='city',
            field=models.IntegerField(default=0, verbose_name='\u57ce\u5e02'),
        ),
    ]