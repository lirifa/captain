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
#import ansible_api_views

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

def serviceinfo(request):
    return render(request,"service_manage.html")

def serviceinfo_json(request):
    ser_srv = request.POST.get('ser_srv')
    if ser_srv == 'all':
        try:
            service_info = Serviceinfo.objects.all()
        except Exception,e:
            service_info = []
            errmsg = "%s"%e
        if len(service_info) != 0:
            msg_dict = {"total":len(service_info)}
            msg_dict["rows"] = []
            for key in service_info:
                ser_id = key.ser_id
                ser_name = key.ser_name
                ser_cfg = key.ser_cfg
                ser_port = key.ser_port
                ser_srv = key.ser_srv
                desc = key.desc
                msg_dict["rows"].append({"ser_id":ser_id,"ser_name":ser_name,"ser_cfg":ser_cfg,"ser_port":ser_port,"ser_srv":ser_srv,"desc":desc})
        else:
            msg_dict = {"total":0,"rows":[]}
    else:
        try:
            service_info = Serviceinfo.objects.filter(ser_srv=ser_srv)
        except Exception,e:
            service_info = []
            errmsg = "%s"%e
        if len(service_info) != 0:
            msg_dict = {"total":len(service_info)}
            msg_dict["rows"] = []
            for key in service_info:
                ser_id = key.ser_id
                ser_name = key.ser_name
                ser_cfg = key.ser_cfg
                ser_port = key.ser_port
                ser_srv = key.ser_srv
                desc = key.desc
                msg_dict["rows"].append({"ser_id":ser_id,"ser_name":ser_name,"ser_cfg":ser_cfg,"ser_port":ser_port,"ser_srv":ser_srv,"desc":desc})
        else:
            msg_dict = {"total":0,"rows":[]}

    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def service_add(request):
    ser_id = request.GET.get('ser_id')
    ser_name = request.GET.get('ser_name')
    ser_cfg = request.GET.get('ser_cfg')
    ser_port = request.GET.get('ser_port')
    ser_srv = request.GET.get('ser_srv')
    desc = request.GET.get('desc')
    msg_dict = {}
    if ser_id:
        try:
            service_info=Serviceinfo.objects.filter(ser_id=ser_id)
        except Exception, e:
            service_info=[]
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
        if len(service_info) == 0:
            try:
                service_info = Serviceinfo.objects.get(ser_id=ser_id)
            except :
                service_info = Serviceinfo()
            service_info.ser_id = ser_id
            service_info.ser_name = ser_name
            service_info.ser_cfg = ser_cfg
            service_info.ser_port = ser_port
            service_info.ser_srv = ser_srv
            service_info.desc = desc
            service_info.save()
            accmsg = u'服务程序[ %s ] 添加成功！'%ser_name
            msg_dict['accmsg']=accmsg
        else:
            errmsg = u"输入服务程序编号为空"
            msg_dict["errmsg"] = errmsg
        return HttpResponse(json.dumps(msg_dict),content_type='application/json')

def service_mod(request):
    ser_id = request.GET.get('ser_id')
    ser_name = request.GET.get('ser_name')
    ser_cfg = request.GET.get('ser_cfg')
    ser_port = request.GET.get('ser_port')
    ser_srv = request.GET.get('ser_srv')
    desc = request.GET.get('desc')
    msg_dict = {}
    if ser_id:
        try:
            service_info = Serviceinfo.objects.filter(ser_id=ser_id).update(ser_name=ser_name,ser_cfg=ser_cfg,ser_port=ser_port,ser_srv=ser_srv,desc=desc)
            accmsg = u"服务 [ %s ] 信息修改成功!"%ser_id
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            service_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入服务id为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def service_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    print idlist
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for ser_id in idlist:
        try:
            ser_id = Serviceinfo.objects.filter(ser_id=ser_id)[0].ser_id
            Serviceinfo.objects.filter(ser_id=ser_id).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%ser_id 
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def check_stat(request):
    ser_cfg = request.POST.get('ser_cfg')
    ser_port = request.POST.get('ser_port')
    ser_srv = request.POST.get('ser_srv')
    server = Serverinfo.objects.filter(srvnum=ser_srv)[0]
    ip = server.ip
    print ip
    user = server.user
    port = server.port
    #theUser = AnsibleWork(ip,port,user,"script","./check_services.py %s:%s#"%(ser_cfg,ser_port))
    #service_status = theUser.workrun()
    sevice_status=('172.27.13.179', 'ss-HjhyComMulti,UP,DOWN\r\n',)
    all_info = sevice_status[1].split("\r\n")[0].split(",")
    cfg_name = all_info[0]
    process_statu = all_info[1]
    port_statu = all_info[2]
    msg_dict = {}
    msg_dict["cfg_name"] = cfg_name
    msg_dict["ser_stat"] = process_statu
    msg_dict["port_stat"] = port_statu
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')

def ser_check_stat(request):
    srvnum = request.POST.get('srvnum')
    msg_dict = {}
    if srvnum == 'all':
        try:
            server_info = Serverinfo.objects.all()
            msg_dict["rows"] = []
            for server in server_info:
                server = Serverinfo.objects.filter(srvnum=server)[0]
                ip = server.ip
                user = server.user
                port = server.port
                service_info = Serviceinfo.objects.filter(ser_srv=server)
                for i in range(len(service_info)):
                    print i
                    ser_id =  service_info[i].ser_id
                    ser_cfg = service_info[i].ser_cfg
                    ser_port = service_info[i].ser_port
                    #theUser = AnsibleWork(ip,port,user,"script","./check_services.py %s:%s#"%(ser_cfg,ser_port))
                    #service_status=theUser.workrun()
                    service_status=('172.27.13.179', 'ss-HjhyComMulti,UP,DOWN\r\n',)
                    all_info = service_status[1].split("\r\n")[0].split(",")
                    cfg_name = all_info[0]
                    process_statu = all_info[1]
                    port_statu = all_info[2]
                    msg_dict["rows"].append({"ser_id":ser_id,"ser_stat":process_statu,"port_stat":port_statu})
        except Exception,e:
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        try:
            server = Serverinfo.objects.filter(srvnum=srvnum)[0]
            ip = server.ip
            user = server.user
            port = server.port
            service_info = Serviceinfo.objects.filter(ser_srv=srvnum)
            msg_dict["rows"] = []
            for i in range(len(service_info)):
                ser_id = service_info[i].ser_id
                ser_cfg = service_info[i].ser_cfg
                ser_port = service_info[i].ser_port
                #theUser = AnsibleWork(ip,port,user,"script","./check_services.py %s:%s#"%(ser_cfg,ser_port))
                #service_status = theUser.workrun()
                service_status=('172.27.13.179', 'ss-HjhyComMulti,UP,DOWN\r\n',)
                all_info = service_status[1].split("\r\n")[0].split(",")
                cfg_name = all_info[0]
                process_statu = all_info[1]
                port_statu = all_info[2]
                msg_dict["rows"].append({"ser_id":ser_id,"ser_stat":process_statu,"port_stat":port_statu})
        except Exception,e:
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg

    return HttpResponse(json.dumps(msg_dict),content_type='application/json')
