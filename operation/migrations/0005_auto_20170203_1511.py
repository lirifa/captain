# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20170120_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='product_des',
        ),
        migrations.AddField(
            model_name='productinfo',
            name='product_desc',
            field=models.CharField(max_length=32, db_column=b'product_desc', blank=True),
        ),
    ]
