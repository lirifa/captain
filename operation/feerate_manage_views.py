#!/usr/bin/python
# coding:utf-8
import os
import sys
import time
import json

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

def feerate_manage(request):
    return render(request,"feerate_manage.html")

def feerate_json(request):
    try:
        print "yes"
        feerate_info = Feerate.objects.all()
    except Exception,e:
        feerate_info = []
        errmsg = "%s"%e
    if len(feerate_info) != 0:
        print "yes2"
        msg_dict = {"total":len(feerate_info)}
        msg_dict["rows"] = []
        for key in feerate_info:
            bid = str(key.bid)
            exchange_id = key.exchange_id
            contract_id = key.contract_id
            biz_type = key.biz_type
            feerate_by_amt = str(key.feerate_by_amt)
            feerate_by_qty = str(key.feerate_by_qty)
            msg_dict["rows"].append({
                "bid":bid,
                "exchange_id":exchange_id,
                "contract_id":contract_id,
                "biz_type":biz_type,
                "feerate_by_amt":feerate_by_amt,
                "feerate_by_qty":feerate_by_qty
                })
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')