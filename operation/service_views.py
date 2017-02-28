#!/usr/bin/python
# coding:utf-8
import os
import sys
import time
import json
import socket
import logging
import hashlib
import datetime
import paramiko
import threading
import decimal

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
cur_dir = cur_file_dir() + '/'
pro_dir = os.path.abspath(os.path.join(os.path.dirname(cur_dir),os.path.pardir))
sys.path.append(pro_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "captain.settings")

import django
if django.VERSION >= (1, 7):
    django.setup()
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from operation.models import *

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

def serviceinfo(request):
    return render(request,"service_manage.html")

def serviceinfo_json(request):
    try:
        service_info = Serviceinfo.objects.all()
    except Exception,e:
        service_info = []
        errmsg = "%s"%e
    if len(service_info) != 0:
        msg_dict = {"total":len(service_info)}
        msg_dict["rows"] = []
        for key in service_info:
            ser_id = key.ser_id
            ser_name = key.ser_name
            ser_cfg = key.ser_cfg
            ser_port = key.ser_port
            ser_srv = key.ser_srv
            desc = key.desc
            msg_dict["rows"].append({"service_id":ser_id,"service_name":ser_name,"service_cfg":ser_cfg,"service_port":ser_port,"service_srv":ser_srv,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')