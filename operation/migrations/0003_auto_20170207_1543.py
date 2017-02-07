# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20170207_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='serverinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='strategyinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='pid',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='srvnum',
            field=models.CharField(max_length=10, serialize=False, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True),
        ),
        migrations.AlterField(
            model_name='strategyinfo',
            name='sid',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True),
        ),
    ]
