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
            id_db = key.id
            srvnum = key.srvnum
            ip = key.ip
            user = key.user
            passwd = key.passwd
            port = key.port
            desc = key.desc
            num += 1
            msg_dict["rows"].append({"id":id,"id_db":id_db,"srvnum":srvnum,"ip":ip,"user":user,"passwd":passwd,"port":port,"desc":desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def serverinfo_add(request):
    srvnum = request.GET.get('srvnum')
    ip = request.GET.get('ip')
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    port = request.GET.get('port')
    desc = request.GET.get('desc')
    msg_dict = {}
    if ip:
        try:
            server_info = Serverinfo.objects.filter(ip=ip)
        except Exception,e:
            server_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(server_info) == 0:
            try:
                server_info = Serverinfo.objects.get(ip=ip)
            except:
                server_info = Serverinfo()
            server_info.srvnum = srvnum
            server_info.ip = ip
            server_info.user = user
            server_info.passwd = passwd
            server_info.port = port
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

def serverinfo_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for dbid in idlist:
        try:
            ip = Serverinfo.objects.filter(id=dbid)[0].ip
            Serverinfo.objects.filter(id=dbid).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%ip 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
