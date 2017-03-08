"""captain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url,handler404,handler500
from django.contrib import admin
from operation.views import *

admin.autodiscover()

handler404="operation.views.page_not_found"
handler500="operation.views.page_not_found"

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),
    url(r'^$', 'operation.views.login', name='login'),
    url(r'^login/$', 'operation.views.login', name='login'),
    url(r'^checklogin/$', 'operation.views.checklogin', name='checklogin'),
    url(r'^index/$', 'operation.views.index', name='index'),
    url(r'^dashboard/$', 'operation.views.dashboard', name='dashboard'),

    url(r'^serverinfo/$', 'operation.views.serverinfo', name='serverinfo'),
    url(r'^serverinfo_json/$', 'operation.views.serverinfo_json', name='serverinfo_json'),
    url(r'^serverinfo_add/$', 'operation.views.serverinfo_add', name='serverinfo_add'),
    url(r'^serverinfo_mod/$', 'operation.views.serverinfo_mod', name='serverinfo_mod'),
    url(r'^serverinfo_del/$', 'operation.views.serverinfo_del', name='serverinfo_del'),

    url(r'^serviceinfo/$','operation.views.serviceinfo',name='serciceinfo'),
    url(r'^serviceinfo_json/$','operation.views.serviceinfo_json',name='serciceinfo_json'),
    url(r'^service_add/$','operation.views.service_add',name='sercice_add'),
    url(r'^service_mod/$','operation.views.service_mod',name='sercice_mod'),
    url(r'^service_del/$','operation.views.service_del',name='sercice_del'),
    url(r'^check_stat/$','operation.views.check_stat',name='check_stat'),
    url(r'^ser_check_stat/$','operation.views.ser_check_stat',name='ser_check_stat'),
    url(r'^strategyinfo_combobox_json/$','operation.views.strategyinfo_combobox_json',name='strategyinfo_combobox_json'),

    url(r'^supervisor/$','operation.views.supervisor',name='supervisor'),

    url(r'^productinfo/$','operation.views.productinfo',name='productinfo'),
    url(r'^productinfo_json/$', 'operation.views.productinfo_json', name='productinfo_json'),
    url(r'^productinfo_add/$', 'operation.views.productinfo_add', name='productinfo_add'),
    url(r'^productinfo_mod/$', 'operation.views.productinfo_mod', name='productinfo_mod'),
    url(r'^productinfo_del/$', 'operation.views.productinfo_del', name='productinfo_del'),

    url(r'^strategyinfo/$','operation.views.strategyinfo',name='strategyinfo'),
    url(r'^strategyinfo_json/$', 'operation.views.strategyinfo_json', name='strategyinfo_json'),
    url(r'^strategyinfo_add/$', 'operation.views.strategyinfo_add', name='strategyinfo_add'),
    url(r'^strategyinfo_mod/$', 'operation.views.strategyinfo_mod', name='strategyinfo_mod'),
    url(r'^strategyinfo_del/$', 'operation.views.strategyinfo_del', name='strategyinfo_del'),
    url(r'^serverinfo_combobox_json/$','operation.views.serverinfo_combobox_json',name='serverinfo_combobox_json'),

    url(r'^configure/$','operation.views.configure',name='configure'),

    url(r'^acct/$','operation.views.acct',name='acct'),
    url(r'^acct_json/$','operation.views.acct_json',name='acct_json'),
    url(r'^acct_add/$', 'operation.views.acct_add', name='acct_add'),
    url(r'^acct_mod/$', 'operation.views.acct_mod', name='acct_mod'),
    url(r'^acct_del/$', 'operation.views.acct_del', name='acct_del'),
    url(r'^acct_combobox_json/$','operation.views.acct_combobox_json',name='acct_combobox_json'),
    url(r'^product_combobox_json/$','operation.views.product_combobox_json',name='product_combobox_json'),
    url(r'^broker_combobox_json/$','operation.views.broker_combobox_json',name='broker_combobox_json'),
    url(r'^acct_fund_change/$','operation.views.acct_fund_change',name='acct_fund_change'),


    url(r'^master_acct/$','operation.views.master_acct',name='master_acct'),
    url(r'^master_acct_json/$','operation.views.master_acct_json',name='master_acct_json'),
    url(r'^master_acct_add/$','operation.views.master_acct_add',name='master_acct_add'),
    url(r'^master_acct_mod/$','operation.views.master_acct_mod',name='master_acct_mod'),
    url(r'^master_acct_del/$','operation.views.master_acct_del',name='master_acct_del'),
    url(r'^masteracc_combobox_json/$','operation.views.masteracc_combobox_json',name='masteracc_combobox_json'),
    url(r'^master_acct_fund_change/$','operation.views.master_acct_fund_change',name='master_acct_fund_change'),

    url(r'^sub_acct/$','operation.views.sub_acct',name='sub_acct'),
    url(r'^sub_acct_json/$','operation.views.sub_acct_json',name='sub_acct_json'),
    url(r'^sub_acct_add/$','operation.views.sub_acct_add',name='sub_acct_add'),
    url(r'^sub_acct_mod/$','operation.views.sub_acct_mod',name='sub_acct_mod'),
    url(r'^sub_acct_del/$','operation.views.sub_acct_del',name='sub_acct_del'),
    url(r'^strategyinfo/subacc_combobox_json/(.*)$','operation.views.subacc_combobox_json',name='subacc_combobox_json'),
    url(r'^subacc_combobox_json/$','operation.views.subacc_combobox_json',name='subacc_combobox_json'),
    url(r'^sub_acct_fund_change/$','operation.views.sub_acct_fund_change',name='sub_acct_fund_change'),

    url(r'^clear/$','operation.views.clear',name='clear'),
    url(r'^feerate_manage/$','operation.views.feerate_manage',name='feerate_manage'),
    url(r'^feerate_json/$','operation.views.feerate_json',name='feerate_json'),

]
