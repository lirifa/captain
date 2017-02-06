# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20170203_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=11, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_admin',
            field=models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_desc',
            field=models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_name',
            field=models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product_num',
            field=models.IntegerField(unique=True, max_length=10, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
