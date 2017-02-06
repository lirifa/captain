# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_serverinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='product_num',
            field=models.IntegerField(serialize=False, primary_key=True, db_column=b'product_num'),
        ),
    ]
