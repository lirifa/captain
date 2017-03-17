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

def ss_manage(request):
    return render(request,'ss_manage.html')

def ssinfo_json(request):
    try:
        strategy_info = Strategyinfo.objects.all()
    except Exception as e:
        strategy_info = []
        errmsg = "%s"%e
    if len(strategy_info) != 0:
        msg_dict = {"total":len(strategy_info)}
        msg_dict["rows"] = []
        for key in strategy_info:
            ss_id = key.ss_id
            ss_name = key.ss_name
            ss_cfg = key.ss_cfg
            port = key.port
            ss_srv = key.ss_srv
            product = key.product
            desc = key.desc
            master_acc = key.master_acc
            sub_acc = key.sub_acc
            msg_dict["rows"].append({"ss_id":ss_id,"ss_name":ss_name,"ss_cfg":ss_cfg,"port":port,"ss_srv":ss_srv,"product":product,"master_acc":master_acc,"sub_acc":sub_acc,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#新增策略
def ss_add(request):
    ss_id = request.GET.get('ss_id')
    ss_name = request.GET.get('ss_name')
    ss_cfg = request.GET.get('ss_cfg')
    port = request.GET.get('port')
    ss_srv = request.GET.get('ss_srv')
    product = request.GET.get('product')
    master_acc = request.GET.get('master_acc')
    sub_acc = request.GET.get('sub_acc')
    desc = request.GET.get('desc')
    msg_dict={}
    if ss_id:
        try:
            strategy_info = Strategyinfo.objects.filter(ss_id=ss_id)
        except Exception,e:
            strategy_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(strategy_info) == 0:
            try:
                strategy_info = Strategyinfo.objects.get(ss_id=ss_id)
            except:
                strategy_info = Strategyinfo()
            strategy_info.ss_id = ss_id
            strategy_info.ss_name = ss_name
            strategy_info.ss_cfg = ss_cfg
            strategy_info.port = port
            strategy_info.ss_srv = ss_srv
            strategy_info.product = product
            strategy_info.master_acc = master_acc
            strategy_info.sub_acc = sub_acc
            strategy_info.desc = desc
            strategy_info.save()
            accmsg = u"策略 [ %s ] 添加成功!"%ss_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"策略 [ %s ] 已存在，不可重复添加!"%ss_name
            msg_dict['accmsg'] = errmsg
    else:
        errmsg = u"输入策略编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#修改策略信息
def ss_mod(request):
    ss_id = request.POST.get('ss_id')
    ss_name = request.POST.get('ss_name')
    ss_cfg = request.POST.get('ss_cfg')
    port = request.POST.get('port')
    ss_srv = request.POST.get('ss_srv')
    product = request.POST.get('product')
    master_acc = request.POST.get('master_acc')
    sub_acc = request.POST.get('sub_acc')
    desc = request.POST.get('desc')
    msg_dict={}
    if ss_id:
        try:
            strategy_info = Strategyinfo.objects.filter(ss_id=ss_id).update(ss_name=ss_name,ss_cfg=ss_cfg,port=port,ss_srv=ss_srv,product=product,master_acc=master_acc,sub_acc=sub_acc,desc=desc)
            accmsg = u"策略 [ %s ] 修改成功!"%ss_id
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            strategy_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入策略编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#删除策略
def ss_del(request):
    delinfo = request.GET.get('delinfo')
    ssidlist = delinfo.split("#")
    del ssidlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for ss_id in ssidlist:
        try:
            ss_name = Strategyinfo.objects.filter(ss_id=ss_id)[0].ss_name
            ss_id = Strategyinfo.objects.filter(ss_id=ss_id)[0].ss_id
            Strategyinfo.objects.filter(ss_id=ss_id).delete()
            msg_dict["accmsg"] += "%s "%ss_name 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#combobox产品列表
def serverinfo_combobox_json(request):
    try:
        server_info = Serverinfo.objects.all()
    except Exception, e:
        server_info = []
        errmsg = "%s"%e
    msg_dict = []
    if len(server_info) != 0:
        for key in server_info:
            srvnum = key.srvnum
            ip = key.ip
            msg_dict.append({"srvnum":srvnum,"ip":ip})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

