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
    url(r'^accounts/', include('users.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),
    # url(r'^$', 'operation.views.login', name='login'),
    # url(r'^login/$', 'operation.views.login', name='login'),
    url(r'^checklogin/$', 'operation.views.checklogin', name='checklogin'),
    url(r'^index/$', 'operation.views.index', name='index'),
    url(r'^dashboard/$', 'operation.views.dashboard', name='dashboard'),

    url(r'^user_manage/$','operation.views.user_manage',name='user_manage'),
    url(r'^userinfo_json/$','operation.views.userinfo_json',name='userinfo_json'),
    url(r'^user_add/$','operation.views.user_add',name='user_add'),
    url(r'^user_mod/$','operation.views.user_mod',name='user_mod'),
    url(r'^user_del/$','operation.views.user_del',name='user_del'),

    url(r'^serverinfo/$', 'operation.views.serverinfo', name='serverinfo'),
    url(r'^serverinfo_json/$', 'operation.views.serverinfo_json', name='serverinfo_json'),
    url(r'^serverinfo_add/$', 'operation.views.serverinfo_add', name='serverinfo_add'),
    url(r'^serverinfo_mod/$', 'operation.views.serverinfo_mod', name='serverinfo_mod'),
    url(r'^serverinfo_del/$', 'operation.views.serverinfo_del', name='serverinfo_del'),

    url(r'^serviceinfo/$','operation.views.serviceinfo',name='serciceinfo'),
    url(r'^serviceinfo_json/$','operation.views.serviceinfo_json',name='serciceinfo_json'),
    url(r'^service_add/$','operation.views.service_add',name='service_add'),
    url(r'^service_mod/$','operation.views.service_mod',name='service_mod'),
    url(r'^service_del/$','operation.views.service_del',name='service_del'),
    url(r'^service_start/$','operation.views.service_start',name='service_start'),
    url(r'^service_stop/$','operation.views.service_stop',name='service_stop'),
    url(r'^service_restart/$','operation.views.service_restart',name='service_restart'),
    url(r'^services_start/$','operation.views.services_start',name='services_start'),
    url(r'^services_stop/$','operation.views.services_stop',name='services_stop'),
    url(r'^services_restart/$','operation.views.services_restart',name='services_restart'),
    url(r'^monitor_run/$','operation.views.monitor_run',name='monitor_run'),
    url(r'^monitor_stop/$','operation.views.monitor_stop',name='monitor_stop'),

    #url(r'^check_stat/$','operation.views.check_stat',name='check_stat'),
    #url(r'^ser_check_stat/$','operation.views.ser_check_stat',name='ser_check_stat'),

    url(r'^get_stat/$','operation.views.get_stat',name='get_stat'),
    url(r'^add_combobox_json/$','operation.views.add_combobox_json',name='add_combobox_json'),
    url(r'^combobox_port_json/$','operation.views.combobox_port_json',name='combobox_port_json'),

    url(r'^ss_manage/$','operation.views.ss_manage',name='ss_manage'),
    url(r'^ssinfo_json/$', 'operation.views.ssinfo_json', name='strategyinfo_json'),
    url(r'^ss_add/$', 'operation.views.ss_add', name='strategy_add'),
    url(r'^ss_mod/$', 'operation.views.ss_mod', name='strategy_mod'),
    url(r'^ss_del/$', 'operation.views.ss_del', name='strategy_del'),
    url(r'^serverinfo_combobox_json/$','operation.views.serverinfo_combobox_json',name='serverinfo_combobox_json'),
    url(r'^subacc_combobox_json/$','operation.views.subacc_combobox_json',name='subacc_combobox_json'),

    url(r'^ps_manage/$','operation.views.ps_manage',name='ps_manage'),
    url(r'^psinfo_json/$', 'operation.views.psinfo_json', name='priceserverinfo_json'),
    url(r'^ps_add/$', 'operation.views.ps_add', name='priceserver_add'),
    url(r'^ps_mod/$', 'operation.views.ps_mod', name='priceserver_mod'),
    url(r'^ps_del/$', 'operation.views.ps_del', name='priceserver_del'),
    url(r'^ps_watch/$', 'operation.views.ps_watch', name='priceserver_watch'),

    url(r'^gw_manage/$','operation.views.gw_manage',name='gw_manage'),
    url(r'^gwinfo_json/$', 'operation.views.gwinfo_json', name='gatewyinfo_json'),
    url(r'^gw_add/$', 'operation.views.gw_add', name='gw_add'),
    url(r'^gw_mod/$', 'operation.views.gw_mod', name='gw_mod'),
    url(r'^gw_del/$', 'operation.views.gw_del', name='gw_del'),

    url(r'^data_send/$','operation.views.data_send',name='data_send'),
    url(r'^data_send_json/$','operation.views.data_send_json',name='data_send_json'),
    url(r'^productinfo/$','operation.views.productinfo',name='productinfo'),
    url(r'^productinfo_json/$', 'operation.views.productinfo_json', name='productinfo_json'),
    url(r'^productinfo_add/$', 'operation.views.productinfo_add', name='productinfo_add'),
    url(r'^productinfo_mod/$', 'operation.views.productinfo_mod', name='productinfo_mod'),
    url(r'^productinfo_del/$', 'operation.views.productinfo_del', name='productinfo_del'),



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
    # url(r'^subacc_combobox_json/$','operation.views.subacc_combobox_json',name='subacc_combobox_json'),
    url(r'^sub_acct_fund_change/$','operation.views.sub_acct_fund_change',name='sub_acct_fund_change'),

    url(r'^clear/$','operation.views.clear',name='clear'),
    url(r'^gatewayinfo_json/$','operation.views.gatewayinfo_json',name='gatewayinfo_json'),
    url(r'^feerate_manage/$','operation.views.feerate_manage',name='feerate_manage'),
    url(r'^feerate_json/$','operation.views.feerate_json',name='feerate_json'),

    url(r'^position/$','operation.views.position',name='position'),
]
