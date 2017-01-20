# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productinfo',
            fields=[
                ('product_num', models.IntegerField(max_length=16, serialize=False, primary_key=True, db_column=b'product_num')),
                ('product_name', models.CharField(max_length=32, db_column=b'product_name', blank=True)),
                ('product_admin', models.CharField(max_length=32, db_column=b'product_admin', blank=True)),
                ('product_des', models.CharField(max_length=32, db_column=b'product_des', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Serverinfo',
        ),
    ]
