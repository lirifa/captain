# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_auto_20170203_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategyinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strategy_id', models.IntegerField(max_length=11, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\xbc\x96\xe5\x8f\xb7')),
                ('strategy_name', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe5\x90\x8d\xe7\xa7\xb0')),
                ('strategy_product', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\xa7\xe5\x93\x81')),
                ('strategy_desc', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('total_account', models.IntegerField(max_length=20, verbose_name=b'\xe6\x80\xbb\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('sub_account', models.IntegerField(max_length=20, verbose_name=b'\xe5\xad\x90\xe8\xb4\xa6\xe5\x8f\xb7')),
            ],
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_num',
            field=models.IntegerField(unique=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
