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

def gw_manage(request):
    return render(request,"gw_manage.html")


def gwinfo_json(request):
    try:
        gateway_info = Gatewayinfo.objects.all()
    except Exception as e:
        gateway_info = []
        errmsg = "%s"%e
    if len(gateway_info) != 0:
        msg_dict = {"total":len(gateway_info)}
        msg_dict["rows"] = []
        for key in gateway_info:
            gw_id = key.gw_id
            gw_name = key.gw_name
            gw_cfg = key.gw_cfg
            port = key.port
            product = key.product
            gw_srv = key.gw_srv
            desc = key.desc
            msg_dict["rows"].append({"gw_id":gw_id,"gw_name":gw_name,"gw_cfg":gw_cfg,"gw_srv":gw_srv,"product":product,"port":port,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#新增网关
def gw_add(request):
    gw_id = request.POST.get('gw_id')
    gw_name = request.POST.get('gw_name')
    gw_cfg = request.POST.get('gw_cfg')
    port = request.POST.get('port')
    gw_srv = request.POST.get('gw_srv')
    product = request.POST.get('product')
    desc = request.POST.get('desc')
    msg_dict={}
    if gw_id:
        try:
            gateway_info = Gatewayinfo.objects.filter(gw_id=gw_id)
        except Exception,e:
            gateway_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(gateway_info) == 0:
            try:
                gateway_info = Gatewayinfo.objects.get(gw_id=gw_id)
            except:
                gateway_info = Gatewayinfo()
            gateway_info.gw_id = gw_id
            gateway_info.gw_name = gw_name
            gateway_info.gw_cfg = gw_cfg
            gateway_info.port = port
            gateway_info.gw_srv = gw_srv
            gateway_info.product = product
            gateway_info.desc = desc
            gateway_info.save()
            accmsg = u"网关 [ %s ] 添加成功!"%gw_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"网关 [ %s ] 已存在，不可重复添加!"%gw_id
            msg_dict['accmsg'] = errmsg
    else:
        errmsg = u"输入网关编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#修改网关信息
def gw_mod(request):
    gw_id = request.POST.get('gw_id')
    gw_name = request.POST.get('gw_name')
    gw_cfg = request.POST.get('gw_cfg')
    port = request.POST.get('port')
    gw_srv = request.POST.get('gw_srv')
    product = request.POST.get('product')
    desc = request.POST.get('desc')
    msg_dict={}
    if gw_id:
        try:
            gateway_info = Gatewayinfo.objects.filter(gw_id=gw_id).update(gw_name=gw_name,gw_cfg=gw_cfg,port=port,gw_srv=gw_srv,product=product,desc=desc)
            accmsg = u"网关 [ %s ] 信息修改成功!"%gw_id
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            gateway_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入网关编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#删除策略
def gw_del(request):
    delinfo = request.POST.get('delinfo')
    gwidlist = delinfo.split("#")
    del gwidlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for gw_id in gwidlist:
        try:
            gw_name = Gatewayinfo.objects.filter(gw_id=gw_id)[0].gw_name
            gw_id = Gatewayinfo.objects.filter(gw_id=gw_id)[0].gw_id
            Gatewayinfo.objects.filter(gw_id=gw_id).delete()
            msg_dict["accmsg"] += "%s "%gw_name 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
