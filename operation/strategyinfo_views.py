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

def strategyinfo(request):
    return render(request,'strategyinfo.html')

def strategyinfo_json(request):
    try:
        strategy_info = Strategyinfo.objects.all()
    except Exception as e:
        strategy_info = []
        errmsg = "%s"%e
    if len(strategy_info) != 0:
        msg_dict = {"total":len(strategy_info)}
        msg_dict["rows"] = []
        num = 1
        for key in strategy_info:
            id = num
            sid = key.sid
            sname = key.sname
            scfg = key.scfg
            port = key.port
            ssrv = key.ssrv
            product = Productinfo.objects.filter(pid=key.product)[0].pname
            desc = key.desc
            master_acc = key.master_acc
            sub_acc = key.sub_acc
            num += 1
            msg_dict["rows"].append({"id":id,"sid":sid,"sname":sname,"scfg":scfg,"port":port,"ssrv":ssrv,"product":product,"master_acc":master_acc,"sub_acc":sub_acc,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#新增策略
def strategyinfo_add(request):
    sid = request.GET.get('sid')
    sname = request.GET.get('sname')
    scfg = request.GET.get('scfg')
    port = request.GET.get('port')
    ssrv = request.GET.get('ssrv')
    product = request.GET.get('product')
    master_acc = request.GET.get('master_acc')
    sub_acc = request.GET.get('sub_acc')
    desc = request.GET.get('desc')
    msg_dict={}
    if sid:
        try:
            strategy_info = Strategyinfo.objects.filter(sid=sid)
        except Exception,e:
            strategy_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(strategy_info) == 0:
            try:
                strategy_info = Strategyinfo.objects.get(sid=sid)
            except:
                strategy_info = Strategyinfo()
            strategy_info.sid = sid
            strategy_info.sname = sname
            strategy_info.scfg = scfg
            strategy_info.port = port
            strategy_info.ssrv = ssrv
            strategy_info.product = product
            strategy_info.master_acc = master_acc
            strategy_info.sub_acc = sub_acc
            strategy_info.desc = desc
            strategy_info.save()
            accmsg = u"策略 [ %s ] 添加成功!"%sname
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"策略 [ %s ] 已存在，不可重复添加!"%sname
            msg_dict['accmsg'] = errmsg
    else:
        errmsg = u"输入策略编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#修改策略信息
def strategyinfo_mod(request):
    sid = request.GET.get('sid')
    sname = request.GET.get('sname')
    scfg = request.GET.get('scfg')
    port = request.GET.get('port')
    ssrv = request.GET.get('ssrv')
    product = request.GET.get('product')
    master_acc = request.GET.get('master_acc')
    sub_acc = request.GET.get('sub_acc')
    desc = request.GET.get('desc')
    msg_dict={}
    if sid:
        try:
            ssrv = Productinfo.objects.filter(pname=ssrv)[0].pid
            strategy_info = Strategyinfo.objects.filter(sid=sid).update(sname=sname,scfg=scfg,port=port,ssrv=ssrv,product=product,master_acc=master_acc,sub_acc=sub_acc,desc=desc)
            accmsg = u"策略 [ %s ] 修改成功!"%sname
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
def strategyinfo_del(request):
    delinfo = request.GET.get('delinfo')
    sidlist = delinfo.split("#")
    del sidlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for sid in sidlist:
        try:
            sname = Strategyinfo.objects.filter(sid=sid)[0].sname
            sid = Strategyinfo.objects.filter(sid=sid)[0].sid
            Strategyinfo.objects.filter(sid=sid).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%sname 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#combobox产品列表
def serverinfo_combobox_json(request):
    try:
        server_info = Serverinfo.objects.all()
    except Exception, e:
        server_info = []
        errmsg = "%s"%e
    if len(server_info) != 0:
        msg_dict = []
        for key in server_info:
            srvnum = key.srvnum
            ip = key.ip
            msg_dict.append({"srvnum":srvnum,"ip":ip})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

