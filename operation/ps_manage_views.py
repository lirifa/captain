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

def ps_manage(request):
    return render(request,"ps_manage.html")

def psinfo_json(request):
    try:
        priceserver_info = Priceserverinfo.objects.all()
    except Exception as e:
        priceserver_info = []
        errmsg = "%s"%e
    if len(priceserver_info) != 0:
        msg_dict = {"total":len(priceserver_info)}
        msg_dict["rows"] = []
        for key in priceserver_info:
            ps_id = key.ps_id
            ps_name = key.ps_name
            ps_cfg = key.ps_cfg
            port = key.port
            ps_srv = key.ps_srv
            desc = key.desc
            msg_dict["rows"].append({"ps_id":ps_id,"ps_name":ps_name,"ps_cfg":ps_cfg,"port":port,"ps_srv":ps_srv,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#新增行情
def ps_add(request):
    ps_id = request.POST.get('ps_id')
    ps_name = request.POST.get('ps_name')
    ps_cfg = request.POST.get('ps_cfg')
    port = request.POST.get('port')
    ps_srv = request.POST.get('ps_srv')
    desc = request.POST.get('desc')
    msg_dict={}
    if ps_id:
        try:
            priceserver_info = Priceserverinfo.objects.filter(ps_id=ps_id)
        except Exception,e:
            priceserver_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(priceserver_info) == 0:
            try:
                priceserver_info = Priceserverinfo.objects.get(ps_id=ps_id)
            except:
                priceserver_info = Priceserverinfo()
            priceserver_info.ps_id = ps_id
            priceserver_info.ps_name = ps_name
            priceserver_info.ps_cfg = ps_cfg
            priceserver_info.port = port
            priceserver_info.ps_srv = ps_srv
            priceserver_info.desc = desc
            priceserver_info.save()
            accmsg = u"行情 [ %s ] 添加成功!"%ps_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"行情 [ %s ] 已存在，不可重复添加!"%ps_name
            msg_dict['accmsg'] = errmsg
    else:
        errmsg = u"输入行情编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#修改行情信息
def ps_mod(request):
    ps_id = request.POST.get('ps_id')
    ps_name = request.POST.get('ps_name')
    ps_cfg = request.POST.get('ps_cfg')
    port = request.POST.get('port')
    ps_srv = request.POST.get('ps_srv')
    desc = request.POST.get('desc')
    msg_dict={}
    if ps_id:
        try:
            priceserver_info = Priceserverinfo.objects.filter(ps_id=ps_id).update(ps_name=ps_name,ps_cfg=ps_cfg,port=port,ps_srv=ps_srv,desc=desc)
            accmsg = u"行情 [ %s ] 修改成功!"%ps_id
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            priceserver_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入行情编号为空"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#删除行情
def ps_del(request):
    delinfo = request.POST.get('delinfo')
    psidlist = delinfo.split("#")
    del psidlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for ps_id in psidlist:
        try:
            ps_name = Priceserverinfo.objects.filter(ps_id=ps_id)[0].ps_name
            ps_id = Priceserverinfo.objects.filter(ps_id=ps_id)[0].ps_id
            Priceserverinfo.objects.filter(ps_id=ps_id).delete()
            msg_dict["accmsg"] += "%s "%ps_name 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#行情数据查看
def ps_watch(request):
    ser_srv = request.POST.get('srv')
    ps_cfg = request.POST.get('cfg')
    ps_port = request.POST.get('port')
    Ukey = request.POST.get('Ukey')
    sleeptime = request.POST.get('sleeptime')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if ser_srv:
        server = Serverinfo.objects.filter(srvnum=ser_srv)[0]
        ip = server.ip
        port = server.port
        user = server.user
    #接口调用
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
