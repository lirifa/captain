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

def clear(request):
    return render(request,"clear.html")


def gatewayinfo_json(request):
    try:
        gateway_info = Gatewayinfo.objects.all()
    except Exception as e:
        gateway_info = []
        errmsg = "%s"%e
    if len(gateway_info) != 0:
        msg_dict = {"total":len(gateway_info)}
        msg_dict["rows"] = []
        num = 1
        for key in gateway_info:
            id = num
            gw_id = key.gw_id
            gw_name = key.gw_name
            gw_cfg = key.gw_cfg
            port = key.port
            gw_srv = key.gw_srv
            desc = key.desc
            num += 1
            msg_dict["rows"].append({"id":id,"gw_id":gw_id,"gw_name":gw_name,"gw_cfg":gw_cfg,"port":port,"gw_srv":gw_srv,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

