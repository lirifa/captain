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

def acct(request):
    return render(request,"acct.html")

def comboxpid_json(request):
    try:
        product_info = Productinfo.bojects.all()
    except Exception,e:
        acct_info = []
        errmsg = "%s"%e
    if len(product_info) !=0:
        msg_dict = {"total":len(acct_info)}
        msg_dict["rows"] = []
        for key in product_info:
            pid = key.pid
            pname = key.pname
            msg_dict["rows"].append({"pid":pid,"pname":pname})
    else:
        msg_dict = {"total":0,"rows":0}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


def acct_json(request):
    try:
        acct_info = Acct.objects.all()
    except Exception,e:
        acct_info = []
        errmsg = "%s"%e
    if len(acct_info) !=0:
        msg_dict = {"total":len(acct_info)}
        msg_dict["rows"] = []
        num = 1
        for key in acct_info:
            id = num
            trdacct = key.trdacct
            acc_name = key.acc_name
            bid = key.bid
            pid = key.pid
            equity = str(key.equity)
            margin_locked = str(key.margin_locked)
            fund_avaril = str(key.fund_avaril)
            risk_degree = key.risk_degree
            num += 1
            msg_dict["rows"].append({"id":id,"trdacct":trdacct,"acc_name":acc_name,"bid":bid,"pid":pid,"equity":equity,"margin_locked":margin_locked,"fund_avaril":fund_avaril,"risk_degree":risk_degree})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#新增资金账户
def acct_add(request):
    trdacct = request.GET.get('trdacct')
    acc_name = request.GET.get('acc_name')
    bid = request.GET.get('bid')
    pid = request.GET.get('pid')
    equity = request.GET.get('equity')
    margin_locked = request.GET.get('margin_locked')
    fund_avaril = request.GET.get('fund_avaril')
    risk_degree = request.GET.get('risk_degree')
    msg_dict = {}
    if trdacct:
        try:
            acct_info = Acct.objects.filter(trdacct=trdacct)
        except Exception,e:
            acct_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(acct_info) == 0:
            try:
                acct_info = Acct.objects.get(trdacct=trdacct)
            except:
                acct_info = Acct()
            print acct_info
            acct_info.trdacct = trdacct
            acct_info.acc_name = acc_name
            acct_info.bid = bid
            acct_info.pid = pid
            acct_info.equity = equity
            acct_info.margin_locked = margin_locked
            acct_info.fund_avaril = fund_avaril
            acct_info.risk_degree = risk_degree
            acct_info.save()
            accmsg = u"资金账户 [ %s ] 添加成功!"%acc_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"资金账户 [ %s ] 已存在，不可重复添加!"%acc_name
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入资金账户号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#修改资金账户信息
def acct_mod(request):
    trdacct = request.GET.get('trdacct')
    acc_name = request.GET.get('acc_name')
    bid = request.GET.get('bid')
    pid = request.GET.get('pid')
    equity = request.GET.get('equity')
    margin_locked = request.GET.get('margin_locked')
    fund_avaril = request.GET.get('fund_avaril')
    risk_degree = request.GET.get('risk_degree')
    msg_dict = {}
    if trdacct:
        try:
            acct_info = Acct.objects.filter(trdacct=trdacct).update(acc_name=acc_name,bid=bid,pid=pid,equity=equity,margin_locked=margin_locked,fund_avaril=fund_avaril,risk_degree=risk_degree)
            accmsg = u"资金账户 [ %s ] 信息修改成功!"%trdacct
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            acct_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
            print errmsg
    else:
        errmsg = u"输入资金账户号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#删除资金账户
def acct_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for trdacct in idlist:
        try:
            trdacct = Acct.objects.filter(trdacct=trdacct)[0].trdacct
            Acct.objects.filter(trdacct=trdacct).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%trdacct 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def product_combobox_json(request):
    try:
        product_info = Productinfo.objects.all()
    except Exception,e:
        product_info = []
        errmsg = "%s"%e 
    if len(product_info) != 0:
        msg_dict = []
        for key in product_info:
            pid = key.pid
            pname = key.pname
            msg_dict.append({"pid":pid,"pname":pname})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def broker_combobox_json(request):
    try:
        broker_info = Broker.objects.all()
    except Exception,e:
        broker_info = []
        errmsg = "%s"%e
    if len(broker_info) !=0:
        msg_dict = []
        for key in broker_info:
            bid = key.bid
            bname = key.bname
            msg_dict.append({"bid":bid,"bname":bname})
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')

def acct_combobox_json(request):
    try:
        acct_info = Acct.objects.all()
    except Exception,e:
        acct_info = []
        errmsg = "%s"%e
    if len(acct_info) !=0:
        msg_dict = []
        for key in acct_info:
            trdacct = key.trdacct
            acc_name = key.acc_name
            msg_dict.append({"trdacct":trdacct,"acc_name":acc_name})
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')