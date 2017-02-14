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

def productinfo(request):
    return render(request,'productinfo.html')

def productinfo_json(request):
    try:
        product_info = Productinfo.objects.all()
    except Exception,e:
        product_info = []
        errmsg = "%s"%e 
    if len(product_info) != 0:
        msg_dict = {"total":len(product_info)}
        msg_dict["rows"] = []
        num = 1
        for key in product_info:
            id = num
            pid = key.pid
            pname = key.pname
            admin = key.admin
            desc = key.desc
            num += 1
            msg_dict["rows"].append({"id":id,"pid":pid,"pname":pname,"admin":admin,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#--------------------------增加产品-------------------#
def productinfo_add(request):
    pid = request.GET.get('pid')
    pname = request.GET.get('pname')
    admin = request.GET.get('admin')
    desc = request.GET.get('desc')
    msg_dict = {}
    if pid:
        try:
            product_info = Productinfo.objects.filter(pid=pid)
        except Exception,e:
            product_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
        if len(product_info) == 0:
            try:
                product_info = Productinfo.objects.get(pid=pid)
            except:
                product_info = Productinfo()
            product_info.pid = pid
            product_info.pname = pname
            product_info.admin = admin
            product_info.desc = desc
            product_info.save()
            accmsg = u"新产品 [ %s ] 添加成功!"%pid
            msg_dict['accmsg'] = accmsg
    else:
        errmsg = u"输入产品编号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-------------------修改产品信息--------------------#
def productinfo_mod(request):
    pid = request.GET.get('pid')
    pname = request.GET.get('pname')
    admin = request.GET.get('admin')
    desc = request.GET.get('desc')
    msg_dict = {}
    if pid:
        try:
            product_info = Productinfo.objects.filter(pid=pid).update(pname=pname,admin=admin,desc=desc)
            accmsg = u"产品 [ %s ] 修改成功!"%pid
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            product_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入产品编号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-------------------删除产品------------------------#
def productinfo_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for pid in idlist:
        try:
            pname = Productinfo.objects.filter(pid=pid)[0].pname
            pid = Productinfo.objects.filter(pid=pid)[0].pid
            Productinfo.objects.filter(pid=pid).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%pname
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
