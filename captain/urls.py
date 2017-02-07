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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from operation.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'operation.views.login', name='login'),
    url(r'^login/$', 'operation.views.login', name='login'),
    url(r'^checklogin/$', 'operation.views.checklogin', name='checklogin'),
    url(r'^index/$', 'operation.views.index', name='index'),
    url(r'^dashboard/$', 'operation.views.dashboard', name='dashboard'),

    url(r'^serverinfo/$', 'operation.views.serverinfo', name='serverinfo'),
    url(r'^serverinfo_json/$', 'operation.views.serverinfo_json', name='serverinfo_json'),
    url(r'^serverinfo_add/$', 'operation.views.serverinfo_add', name='serverinfo_add'),
    url(r'^serverinfo_del/$', 'operation.views.serverinfo_del', name='serverinfo_del'),

    url(r'^productinfo/$','operation.views.productinfo',name='productinfo'),
    url(r'^productinfo_json/$', 'operation.views.productinfo_json', name='productinfo_json'),
    url(r'^productinfo_add/$', 'operation.views.productinfo_add', name='productinfo_add'), 
    url(r'^productinfo_del/$', 'operation.views.productinfo_del', name='productinfo_del'),

    url(r'^strategyinfo/$','operation.views.strategyinfo',name='strategyinfo'),
]
