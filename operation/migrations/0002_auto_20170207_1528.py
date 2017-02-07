# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productinfo',
            table='productinfo',
        ),
        migrations.AlterModelTable(
            name='serverinfo',
            table='serverinfo',
        ),
        migrations.AlterModelTable(
            name='strategyinfo',
            table='strategyinfo',
        ),
    ]
