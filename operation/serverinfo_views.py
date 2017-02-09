#!/usr/bin/python
# coding:utf-8
# Serverinfoor: hiki
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

def serverinfo(request):
    return render(request,'serverinfo.html')

def serverinfo_json(request):
    try:
        server_info = Serverinfo.objects.all()
    except Exception,e:
        server_info = []
        errmsg = "%s"%e
    if len(server_info) != 0:
        msg_dict = {"total":len(server_info)}
        msg_dict["rows"] = []
        num = 1
        for key in server_info:
            id = num
            srvnum = key.srvnum
            ip = key.ip
            user = key.user
            passwd = key.passwd
            port = key.port
            productadmin = key.productadmin
            desc = key.desc
            num += 1
            msg_dict["rows"].append({"id":id,"srvnum":srvnum,"ip":ip,"user":user,"passwd":passwd,"port":port,"productadmin":productadmin,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#---------------------添加主机---------------
def serverinfo_add(request):
    srvnum = request.GET.get('srvnum')
    ip = request.GET.get('ip')
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    port = request.GET.get('port')
    productadmin = request.GET.get('productadmin')
    desc = request.GET.get('desc')
    msg_dict = {}
    if srvnum:
        try:
            server_info = Serverinfo.objects.filter(srvnum=srvnum)
        except Exception,e:
            server_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(server_info) == 0:
            try:
                server_info = Serverinfo.objects.get(srvnum=srvnum)
            except:
                server_info = Serverinfo()
            server_info.srvnum = srvnum
            server_info.ip = ip
            server_info.user = user
            server_info.passwd = passwd
            server_info.port = port
            server_info.productadmin = productadmin
            server_info.desc = desc
            server_info.save()
            accmsg = u"服务器 [ %s ] 添加成功!"%ip
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"服务器 [ %s ] 已存在，不可重复添加!"%ip
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入IP为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-------------------修改主机信息--------------------#
def serverinfo_mod(request):
    srvnum = request.GET.get('srvnum')
    ip = request.GET.get('ip')
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    port = request.GET.get('port')
    productadmin = request.GET.get('productadmin')
    desc = request.GET.get('desc')
    msg_dict = {}
    if srvnum:
        try:
            server_info = Serverinfo.objects.filter(srvnum=srvnum).update(ip=ip,user=user,passwd=passwd,port=port,productadmin=productadmin,desc=desc)
            accmsg = u"服务器 [ %s ] 修改成功!"%ip
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            server_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-----------------删除主机-------------------------#
def serverinfo_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for srvnum in idlist:
        try:
            srvnum = Serverinfo.objects.filter(srvnum=srvnum)[0].srvnum
            Serverinfo.objects.filter(srvnum=srvnum).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%srvnum 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
