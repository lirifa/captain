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

def user_manage(request):
    return render(request,'user_manage.html')

#返回用户列表信息
def userinfo_json(request):
    msg_dict = {}
    try:
        user_info = User.objects.all()
    except Exception,e:
        user_info = []
        errmsg = "%s"%e
        msg_dict['errmsg'] = errmsg
    if len(user_info) != 0:
        msg_dict = {"total":len(user_info)}
        msg_dict["rows"] = []
        for key in user_info:
            username = key.username
            passwd = key.passwd
            tel = key.tel
            email = key.email
            permission = key.permission
            desc = key.desc
            msg_dict["rows"].append({"username":username,"passwd":passwd,"tel":tel,"email":email,"permission":permission,"desc":desc})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#------------------新增用户------------------#
def user_add(request):
    username = request.POST.get('username')
    passwd = request.POST.get('passwd')
    tel = request.POST.get('tel')
    email = request.POST.get('email')
    permission = request.POST.get('permission')
    desc = request.POST.get('desc')
    print username,passwd,tel,email,permission,desc
    msg_dict={}
    if username:
        try:
            user = User.objects.filter(username=username)
            print user
        except Exception,e:
            user = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(user) == 0:
            try:
                user = User.objects.get(username=username)
            except:
                user = User()
            user.username = username
            user.passwd = passwd
            user.tel = tel
            user.email = email
            user.permission = permission
            user.desc = desc
            user.save()
            accmsg = u"用户 [ %s ] 添加成功!"%username
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"用户名 [ %s ] 已存在，请选择其他用户名!"%username
            msg_dict['accmsg'] = errmsg
    else:
        errmsg = u"输入用户名为空！"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#-------------------修改用户信息--------------------#
def user_mod(request):
    username = request.POST.get('username')
    passwd = request.POST.get('passwd')
    tel = request.POST.get('tel')
    email = request.POST.get('email')
    permission = request.POST.get('permission')
    desc = request.POST.get('desc')
    msg_dict = {}
    if username:
        try:
            user = User.objects.filter(username=username).update(passwd=passwd,tel=tel,email=email,permission=permission,desc=desc)
            accmsg = u"用户 [ %s ] 信息修改成功!"%username
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            user = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-----------------删除主机-------------------------#
def user_del(request):
    delinfo = request.POST.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for username in idlist:
        try:
            user = User.objects.filter(username=username)[0].username
            User.objects.filter(username=username).delete()
            msg_dict["accmsg"] += "%s"%user 
        except Exception,e:
            errmsg = "%s"%e
            print errmsg
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')