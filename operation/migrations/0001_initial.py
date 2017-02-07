# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.IntegerField(unique=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7')),
                ('pname', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('admin', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Serverinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('srvnum', models.CharField(max_length=10, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xbc\x96\xe5\x8f\xb7')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'IP')),
                ('user', models.CharField(max_length=10, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('passwd', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('port', models.IntegerField(verbose_name=b'SSH\xe7\xab\xaf\xe5\x8f\xa3')),
                ('desc', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Strategyinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.IntegerField(verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\xbc\x96\xe5\x8f\xb7')),
                ('sname', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe5\x90\x8d\xe7\xa7\xb0')),
                ('product', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\xa7\xe5\x93\x81')),
                ('master_acc', models.IntegerField(verbose_name=b'\xe6\x80\xbb\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('sub_acc', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe4\xbb\x8b\xe7\xbb\x8d')),
            ],
        ),
    ]
