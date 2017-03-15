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
#from ansible_api_views import *

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

def data_send(request):
    return render(request,"data_send.html")

def data_send_json(request):
    try:
        data_send_info = Data_send.objects.all()
    except Exception,e:
        data_send_info = []
        errmsg = "%s"%e
    if len(data_send_info) != 0:
        msg_dict = {"total":len(data_send_info)}
        msg_dict["rows"] = []
        for key in data_send_info:
            id = key.id
            d_name = key.d_name
            o_srv = key.o_srv
            o_dir = key.o_dir
            p_srv = key.p_srv
            p_dir = key.p_dir
            msg_dict["rows"].append({"id":id,"d_name":d_name,"o_srv":o_srv,"o_dir":o_dir,"p_srv":p_srv,"p_dir":p_dir})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def data_send_add(request):
    d_name = request.GET.get('d_name')
    o_srv = request.GET.get('o_srv')
    o_dir = request.GET.get('o_dir')
    p_srv = request.GET.get('p_srv')
    p_dir = request.GET.get('p_dir')
    msg_dict = {}
    try:
        u1 = Data_send(d_name=d_name,o_srv=o_srv,o_dir=o_dir,p_srv=p_srv,p_dir=p_dir)
        u1.save()
    except Exception,e:
        errmsg = "%s"%e
        msg_dict['errmsg'] = errmsg
        accmsg = u"新产品 [ %s ] 添加成功!"%pid
        msg_dict['accmsg'] = accmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

    try:
        pass
    except Exception as e:
        raise e
    finally:
        pass