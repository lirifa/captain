# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
    ]
