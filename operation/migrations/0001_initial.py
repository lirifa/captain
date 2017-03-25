# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acct',
            fields=[
                ('trdacct', models.CharField(max_length=32, serialize=False, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x8f\xb7', primary_key=True)),
                ('acc_name', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x90\x8d')),
                ('bid', models.IntegerField(verbose_name=b'\xe7\xbb\x8f\xe7\xba\xaa\xe5\x95\x86id')),
                ('pid', models.IntegerField(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81id')),
                ('equity', models.DecimalField(max_length=128, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe6\x9d\x83\xe7\x9b\x8a', max_digits=17, decimal_places=2)),
                ('margin_locked', models.DecimalField(verbose_name=b'\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('fund_avaril', models.DecimalField(verbose_name=b'\xe5\x8f\xaf\xe4\xbb\xa5\xe8\xb5\x84\xe9\x87\x91', max_digits=17, decimal_places=2)),
                ('risk_degree', models.CharField(max_length=11, verbose_name=b'\xe9\xa3\x8e\xe9\x99\xa9\xe5\xba\xa6')),
            ],
            options={
                'db_table': 'acct',
            },
        ),
        migrations.CreateModel(
            name='Acct_hold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trd_date', models.CharField(max_length=8, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5\xe6\x9c\x9f')),
                ('trdacct', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe9\x87\x91\xe8\xb4\xa6\xe6\x88\xb7\xe5\x8f\xb7')),
                ('instrument', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x88\xe7\xba\xa6\xe5\x90\x8d')),
                ('variety', models.CharField(max_length=32, verbose_name=b'\xe5\x93\x81\xe7\xa7\x8d\xe5\x90\x8d')),
                ('long_pos', models.IntegerField(verbose_name=b'\xe4\xb9\xb0\xe6\x8c\x81\xe4\xbb\x93')),
                ('avg_buy_price', models.DecimalField(verbose_name=b'\xe4\xb9\xb0\xe5\x9d\x87\xe4\xbb\xb7', max_digits=17, decimal_places=3)),
                ('short_pos', models.IntegerField(verbose_name=b'\xe5\x8d\x96\xe6\x8c\x81\xe4\xbb\x93')),
                ('avg_sell_price', models.DecimalField(verbose_name=b'\xe5\x8d\x96\xe5\x9d\x87\xe4\xbb\xb7', max_digits=17, decimal_places=3)),
                ('pos_pl', models.DecimalField(verbose_name=b'\xe6\x8c\x81\xe4\xbb\x93\xe8\xae\xa2\xe5\xb8\x82\xe7\x9b\x88\xe4\xba\x8f', max_digits=17, decimal_places=2)),
                ('margin_occupied', models.DecimalField(verbose_name=b'\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('sh_mark', models.CharField(max_length=1, verbose_name=b'\xe6\x8a\x95\xe4\xbf\x9d\xe6\xa0\x87\xe8\xaf\x86')),
            ],
            options={
                'db_table': 'acct_hold',
            },
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('bid', models.IntegerField(serialize=False, verbose_name=b'\xe7\xbb\x8f\xe7\xba\xaa\xe5\x95\x86ID', primary_key=True)),
                ('bname', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x8f\xe7\xba\xaa\xe5\x95\x86\xe7\xae\x80\xe7\xa7\xb0')),
                ('blname', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x8f\xe7\xba\xaa\xe5\x95\x86\xe5\x85\xa8\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'broker',
            },
        ),
        migrations.CreateModel(
            name='Data_send',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe4\xb8\xbb\xe9\x94\xaeid', primary_key=True)),
                ('d_name', models.CharField(max_length=32, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe5\x90\x8d')),
                ('o_srv', models.CharField(max_length=32, verbose_name=b'\xe6\xba\x90\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('o_dir', models.CharField(max_length=32, verbose_name=b'\xe6\xba\x90\xe7\x9b\xae\xe5\xbd\x95\xe5\x9c\xb0\xe5\x9d\x80')),
                ('p_srv', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\xae\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('p_dir', models.CharField(max_length=32, verbose_name=b'\xe7\x9b\xae\xe7\x9a\x84\xe7\x9b\xae\xe5\xbd\x95\xe5\x9c\xb0\xe5\x9d\x80')),
                ('update_tm', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'data_send',
            },
        ),
        migrations.CreateModel(
            name='Fund_change_log',
            fields=[
                ('log_id', models.AutoField(serialize=False, primary_key=True)),
                ('acct_type', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe7\xb1\xbb\xe5\x88\xab')),
                ('acct_id', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7id')),
                ('change_fund', models.DecimalField(verbose_name=b'\xe5\x87\xba\xe5\x85\xa5\xe9\x87\x91\xe9\x87\x91\xe9\xa2\x9d', max_digits=17, decimal_places=2)),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('log_tm', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\x9d\xe5\xad\x98\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'db_table': 'fund_change_log',
            },
        ),
        migrations.CreateModel(
            name='Gatewayinfo',
            fields=[
                ('gw_id', models.CharField(max_length=32, serialize=False, verbose_name=b'gateway id', primary_key=True)),
                ('gw_name', models.CharField(max_length=32, verbose_name=b'gateway\xe5\x90\x8d\xe7\xa7\xb0')),
                ('gw_cfg', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\x85\x8d\xe7\xbd\xae\xe5\x90\x8d')),
                ('port', models.IntegerField(verbose_name=b'gw\xe7\xab\xaf\xe5\x8f\xa3')),
                ('gw_srv', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\xbb\xe6\x9c\xba')),
                ('product', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\xa7\xe5\x93\x81')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'gatewayinfo',
            },
        ),
        migrations.CreateModel(
            name='Master_acct',
            fields=[
                ('acc_num', models.CharField(max_length=32, serialize=False, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x8f\xb7', primary_key=True)),
                ('acc_name', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x90\x8d')),
                ('trdacct', models.CharField(max_length=32, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe8\xb5\x84\xe9\x87\x91\xe8\xb4\xa6\xe6\x88\xb7')),
                ('equity', models.DecimalField(verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe6\x9d\x83\xe7\x9b\x8a', max_digits=17, decimal_places=2)),
                ('buy_margin', models.DecimalField(verbose_name=b'\xe4\xb9\xb0\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('sell_margin', models.DecimalField(verbose_name=b'\xe5\x8d\x96\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('margin_locked', models.DecimalField(verbose_name=b'\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('fund_avaril', models.DecimalField(verbose_name=b'\xe5\x8f\xaf\xe7\x94\xa8\xe8\xb5\x84\xe9\x87\x91', max_digits=17, decimal_places=2)),
            ],
            options={
                'db_table': 'master_acct',
            },
        ),
        migrations.CreateModel(
            name='Priceserverinfo',
            fields=[
                ('ps_id', models.CharField(max_length=32, serialize=False, verbose_name=b'PS id', primary_key=True)),
                ('ps_name', models.CharField(max_length=32, verbose_name=b'PS\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ps_cfg', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\x85\x8d\xe7\xbd\xae\xe5\x90\x8d')),
                ('port', models.IntegerField(verbose_name=b'ps\xe7\xab\xaf\xe5\x8f\xa3')),
                ('ps_srv', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\xbb\xe6\x9c\xba')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'priceserverinfo',
            },
        ),
        migrations.CreateModel(
            name='Productinfo',
            fields=[
                ('pid', models.IntegerField(serialize=False, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('pname', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('admin', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'productinfo',
            },
        ),
        migrations.CreateModel(
            name='Serverinfo',
            fields=[
                ('srvnum', models.CharField(max_length=10, serialize=False, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'IP')),
                ('user', models.CharField(max_length=10, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x94\xa8\xe6\x88\xb7')),
                ('passwd', models.CharField(max_length=50, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe5\xaf\x86\xe7\xa0\x81')),
                ('port', models.IntegerField(verbose_name=b'SSH\xe7\xab\xaf\xe5\x8f\xa3')),
                ('productadmin', models.CharField(max_length=32, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba')),
                ('desc', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'serverinfo',
            },
        ),
        migrations.CreateModel(
            name='Serviceinfo',
            fields=[
                ('ser_id', models.AutoField(serialize=False, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1id', primary_key=True)),
                ('ser_name', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ser_att', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xb1\x9e\xe6\x80\xa7')),
                ('ser_cfg', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\x85\x8d\xe7\xbd\xae\xe5\x90\x8d')),
                ('ser_port', models.IntegerField(verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('ser_stat', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81')),
                ('port_stat', models.CharField(max_length=32, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe7\x8a\xb6\xe6\x80\x81')),
                ('ser_srv', models.CharField(max_length=10, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\xbb\xe6\x9c\xba')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'serviceinfo',
            },
        ),
        migrations.CreateModel(
            name='Strategyinfo',
            fields=[
                ('ss_id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('ss_name', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ss_cfg', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\x85\x8d\xe7\xbd\xae\xe5\x90\x8d')),
                ('ss_srv', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xb8\xbb\xe6\x9c\xba')),
                ('product', models.CharField(max_length=32, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\xa7\xe5\x93\x81')),
                ('master_acc', models.CharField(max_length=32, verbose_name=b'\xe6\x80\xbb\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('sub_acc', models.CharField(max_length=32, verbose_name=b'\xe5\xad\x90\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('port', models.IntegerField(verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\xab\xaf\xe5\x8f\xa3')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe4\xbb\x8b\xe7\xbb\x8d')),
            ],
            options={
                'db_table': 'strategyinfo',
            },
        ),
        migrations.CreateModel(
            name='Sub_acct',
            fields=[
                ('acc_num', models.CharField(max_length=32, serialize=False, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x8f\xb7', primary_key=True)),
                ('acc_name', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x90\x8d')),
                ('master_acct', models.CharField(max_length=32, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x80\xbb\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('equity', models.DecimalField(verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe6\x9d\x83\xe7\x9b\x8a', max_digits=17, decimal_places=2)),
                ('fund_avaril', models.DecimalField(verbose_name=b'\xe5\x8f\xaf\xe7\x94\xa8\xe8\xb5\x84\xe9\x87\x91', max_digits=17, decimal_places=2)),
                ('margin_locked', models.DecimalField(verbose_name=b'\xe6\x80\xbb\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('buy_margin', models.DecimalField(verbose_name=b'\xe4\xb9\xb0\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
                ('sell_margin', models.DecimalField(verbose_name=b'\xe5\x8d\x96\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91\xe5\x8d\xa0\xe7\x94\xa8', max_digits=17, decimal_places=2)),
            ],
            options={
                'db_table': 'sub_acct',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', primary_key=True)),
                ('passwd', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('tel', models.CharField(max_length=50, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('email', models.CharField(max_length=50, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80')),
                ('permission', models.CharField(max_length=1, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe7\xad\x89\xe7\xba\xa7')),
                ('desc', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AlterUniqueTogether(
            name='acct_hold',
            unique_together=set([('trd_date', 'trdacct', 'instrument')]),
        ),
    ]
