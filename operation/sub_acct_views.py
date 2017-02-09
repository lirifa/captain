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

def sub_acct(request):
    return render(request,"sub_acct.html")

def sub_acct_json(request):
    try:
        sub_acct_info = Sub_acct.objects.all()
    except Exception as e:
        sub_acct_info = []
        errmsg = "%s"%e
    if len(sub_acct_info) !=0:
        msg_dict = {"total":len(sub_acct_info)}
        msg_dict["rows"] = []
        num = 1
        for key in sub_acct_info:
            id = num
            acc_num = key.acc_num
            acc_name = key.acc_name
            master_acct = key.master_acct
            equity = key.equity
            fund_avaril = key.fund_avaril
            margin_locked = key.margin_locked
            buy_margin = key.buy_margin
            sell_margin = key.sell_margin
            num += 1
            msg_dict["rows"].append({"id":id,"acc_num":acc_num,"acc_name":acc_name,"master_acct":master_acct,"equity":equity,"fund_avaril":fund_avaril,"margin_locked":margin_locked,"buy_margin":buy_margin,"sell_margin":sell_margin})
        else:
            msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
