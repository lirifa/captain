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
import subprocess
#from ansible_api_views import *

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

#加载服务信息列表
def serviceinfo_json(request):
    ser_srv = request.POST.get('ser_srv')
    msg_dict = {}
    if ser_srv == 'all':
        try:
            service_info = Serviceinfo.objects.all()
        except Exception,e:
            service_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
        if len(service_info) != 0:
            msg_dict = {"total":len(service_info)}
            msg_dict["rows"] = []
            for key in service_info:
                ser_id = key.ser_id
                ser_name = key.ser_name
                ser_att = key.ser_att
                ser_cfg = key.ser_cfg
                ser_port = key.ser_port
                ser_srv = key.ser_srv
                desc = key.desc
                msg_dict["rows"].append({"ser_id":ser_id,"ser_name":ser_name,"ser_att":ser_att,"ser_cfg":ser_cfg,"ser_port":ser_port,"ser_srv":ser_srv,"desc":desc})
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
                ser_att = key.ser_att
                ser_cfg = key.ser_cfg
                ser_port = key.ser_port
                ser_srv = key.ser_srv
                desc = key.desc
                msg_dict["rows"].append({"ser_id":ser_id,"ser_name":ser_name,"ser_att":ser_att,"ser_cfg":ser_cfg,"ser_port":ser_port,"ser_srv":ser_srv,"desc":desc})
        else:
            msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#x新增服务
def service_add(request):
    # ser_id = request.GET.get('ser_id')
    ser_name = request.GET.get('ser_name')
    ser_att = request.GET.get('ser_att')
    ser_cfg = request.GET.get('ser_cfg')
    ser_port = request.GET.get('ser_port')
    ser_srv = request.GET.get('ser_srv')
    desc = request.GET.get('desc')
    msg_dict = {}
    if ser_name:
        try:
            service_info=Serviceinfo.objects.filter(ser_name=ser_name)
        except Exception, e:
            service_info=[]
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
        if len(service_info) == 0:
            try:
                service_info = Serviceinfo.objects.get(ser_name=ser_name)
            except :
                service_info = Serviceinfo()
            # service_info.ser_id = ser_id
            service_info.ser_name = ser_name
            service_info.ser_att = ser_att
            service_info.ser_cfg = ser_cfg
            service_info.ser_port = ser_port
            service_info.ser_srv = ser_srv
            service_info.desc = desc
            service_info.save()
            accmsg = u'服务程序[ %s ] 添加成功！'%ser_name
            msg_dict['accmsg']=accmsg
        else:
            errmsg = u"输入服务名称为空！"
            msg_dict["errmsg"] = errmsg
        return HttpResponse(json.dumps(msg_dict),content_type='application/json')

#修改服务信息
def service_mod(request):
    ser_id = request.GET.get('ser_id')
    ser_name = request.GET.get('ser_name')
    ser_att = request.GET.get('ser_att')
    ser_cfg = request.GET.get('ser_cfg')
    ser_port = request.GET.get('ser_port')
    ser_srv = request.GET.get('ser_srv')
    desc = request.GET.get('desc')
    msg_dict = {}
    if ser_id:
        try:
            service_info = Serviceinfo.objects.filter(ser_id=ser_id).update(ser_name=ser_name,ser_att=ser_att,ser_cfg=ser_cfg,ser_port=ser_port,ser_srv=ser_srv,desc=desc)
            accmsg = u"服务 [ %s ] 信息修改成功!"%ser_cfg
            msg_dict['accmsg'] = accmsg
        except Exception,e:
            service_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入服务id为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#删除某个服务
def service_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for ser_id in idlist:
        try:
            ser_id = Serviceinfo.objects.filter(ser_id=ser_id)[0].ser_id
            ser_cfg = Serviceinfo.objects.filter(ser_id=ser_id)[0].ser_cfg
            Serviceinfo.objects.filter(ser_id=ser_id).delete()
            msg_dict["accmsg"] += "%s "%ser_cfg
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#策略combobox
def add_combobox_json(request):
    ser_att = request.GET.get('ser_att')
    ser_srv = request.GET.get('ser_srv')
    msg_dict=[]
    if ser_srv:
        if ser_att == 'SS':
            try:
                combobox_info = Strategyinfo.objects.filter(ss_srv=ser_srv)
            except Exception,e:
                combobox_info = []
                errmsg = "%s"%e
            if len(combobox_info) != 0:
                for key in combobox_info:
                    id = key.ss_id
                    cfg = key.ss_cfg
                    port = key.port
                    ser = key.ss_srv
                    msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
        elif ser_att == 'PS':
            try:
                combobox_info = Priceserverinfo.objects.filter(ps_srv=ser_srv)
            except Exception,e:
                combobox_info = []
                errmsg = "%s"%e
            if len(combobox_info) != 0:
                for key in combobox_info:
                    id = key.ps_id
                    cfg = key.ps_cfg
                    port = key.port
                    ser = key.ps_srv
                    msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
        elif ser_att == 'GW' or ser_att == 'SS2ISON':
            try:
                combobox_info = Gatewayinfo.objects.filter(gw_srv=ser_srv)
            except Exception,e:
                combobox_info = []
                errmsg = "%s"%e
            if len(combobox_info) != 0:
                for key in combobox_info:
                    id = key.gw_id
                    cfg = key.gw_cfg
                    port = key.port
                    ser = key.gw_srv
                    msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
        else:
            id = '请先选择服务属性'
            cfg = '请先选择服务属性'
            port = '请先选择服务属性'
            ser = '请先选择服务属性'
            msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
    else:
        id = '请先选择所属主机'
        cfg = '请先选择所属主机'
        port = '请先选择所属主机'
        ser = '请先选择所属主机'
        msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def combobox_port_json(request):
    ser_att = request.GET.get('ser_att')
    ser_srv = request.GET.get('ser_srv')
    ser_cfg = request.GET.get('ser_cfg')
    msg_dict=[]
    if ser_att == 'SS':
        try:
            combobox_info = Strategyinfo.objects.filter(ss_srv=ser_srv,ss_cfg=ser_cfg)
        except Exception,e:
            combobox_info = []
            errmsg = "%s"%e
        if len(combobox_info) != 0:
            for key in combobox_info:
                id = key.ss_id
                cfg = key.ss_cfg
                port = key.port
                ser = key.ss_srv
                msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
    elif ser_att == 'PS' or ser_att =='PP':
        try:
            combobox_info = Priceserverinfo.objects.filter(ps_srv=ser_srv,ps_cfg=ser_cfg)
        except Exception,e:
            combobox_info = []
            errmsg = "%s"%e
        if len(combobox_info) != 0:
            for key in combobox_info:
                id = key.ps_id
                cfg = key.ps_cfg
                port = key.port
                ser = key.ps_srv
                msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
    elif ser_att == 'GW':
        try:
            combobox_info = Gatewayinfo.objects.filter(gw_srv=ser_srv,gw_cfg=ser_cfg)
        except Exception,e:
            combobox_info = []
            errmsg = "%s"%e
        if len(combobox_info) != 0:
            for key in combobox_info:
                id = key.gw_id
                cfg = key.gw_cfg
                port = key.port
                ser = key.gw_srv
                msg_dict.append({"id":id,"cfg":cfg,"port":port,"ser":ser})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#查看服务及端口的函数状态
def get_stat(request):
    ser_srv = request.POST.get('srvnum')
    msg_dict = {}
    if ser_srv == 'all':
        try:
            service_info = Serviceinfo.objects.all()
        except Exception,e:
            service_info = []
            errmsg = "%s"%e
        if len(service_info) != 0:
            msg_dict["rows"] = []
            for key in service_info:
                ser_id = key.ser_id
                ser_stat = key.ser_stat
                port_stat = key.port_stat
                msg_dict["rows"].append({"ser_id":ser_id,"ser_stat":ser_stat,"port_stat":port_stat})
        else:
            msg_dict = {"total":0,"rows":[]}
    else:
        try:
            service_info = Serviceinfo.objects.filter(ser_srv=ser_srv)
        except Exception,e:
            service_info = []
            errmsg = "%s"%e
        if len(service_info) != 0:
            msg_dict["rows"] = []
            for key in service_info:
                ser_id = key.ser_id
                ser_stat = key.ser_stat
                port_stat = key.port_stat
                msg_dict["rows"].append({"ser_id":ser_id,"ser_stat":ser_stat,"port_stat":port_stat})
        else:
            msg_dict = {"total":0,"rows":[]}
    msg_dict["monitor_statu"] = []
    statu = subprocess.Popen("ps -ef | grep auto_services_views | grep -v grep | wc -l", stdout=subprocess.PIPE, shell=True)
    result = statu.communicate()[0].split("\n")[0]
    if str(result) != "0":
        monitor_statu = "UP"
    else:
        monitor_statu = "DOWN"
    msg_dict["monitor_statu"].append(monitor_statu) 
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#启动监控程序
def monitor_run(request):
    action = request.POST.get('action')
    msg_dict ={}
    if action == 'run':
        msg_dict["monitor_statu"] = []
        #启动命令
        result = os.system("nohup python %s/operation/auto_services_views.py > /dev/null 2>&1 &"%os.getcwd())
        statu = subprocess.Popen("ps -ef | grep auto_services_views | grep -v grep | wc -l", stdout=subprocess.PIPE, shell=True)
        result = statu.communicate()[0].split("\n")[0]
        if result != "0":
            monitor_statu = "UP"
        else:
            monitor_statu = "DOWN"
        msg_dict["monitor_statu"].append(monitor_statu)
    else:
        msg_dict['errmsg'] = "前台发过来的不是run囧"
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#停止监控程序
def monitor_stop(request):
    action = request.POST.get('action')
    msg_dict={}
    if action == 'stop':
        msg_dict["monitor_statu"] = []
        #停止命令
        stop = subprocess.Popen("kill -9 `ps -ef | grep auto_services_views | grep -v grep | awk '{print $2}'`", stdout=subprocess.PIPE, shell=True)
        statu = subprocess.Popen("ps -ef | grep auto_services_views | grep -v grep | wc -l", stdout=subprocess.PIPE, shell=True)
        result = statu.communicate()[0].split("\n")[0]
        if result != "0":
            monitor_statu = "UP"
        else:
            monitor_statu = "DOWN"
        msg_dict["monitor_statu"].append(monitor_statu)
    else:
        msg_dict['errmsg'] = "前台发过来的不是stop"
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

##############################################################################################
#单个服务启动
def service_start(request):
    ser_att=request.POST.get('ser_att')
    ser_srv=request.POST.get('ser_srv')
    ser_cfg=request.POST.get('ser_cfg')
    ser_port=request.POST.get('ser_port')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if ser_srv:
        server = Serverinfo.objects.filter(srvnum=ser_srv)[0]
        ip = server.ip
        port = server.port
        user = server.user
        #theUser = AnsibleWork(ip,port,user,"script","%s/operation/control_services.py %s"%(os.getcwd(),check_args))
    msg_dict[""]
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#单个服务停止
def service_stop(request):
    ser_att=request.POST.get('ser_att')
    ser_srv=request.POST.get('ser_srv')
    ser_cfg=request.POST.get('ser_cfg')
    ser_port=request.POST.get('ser_port')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if ser_srv:
        server = Serverinfo.objects.filter(srvnum=ser_srv)[0]
        ip = server.ip
        port = server.port
        user = server.user
        # theUser = AnsibleWork(ip,port,user,"script","%s/operation/check_services.py %s"%(os.getcwd(),check_args))
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#单个服务重启
def service_restart(request):
    ser_att=request.POST.get('ser_att')
    ser_srv=request.POST.get('ser_srv')
    ser_cfg=request.POST.get('ser_cfg')
    ser_port=request.POST.get('ser_port')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if ser_srv:
        server = Serverinfo.objects.filter(srvnum=ser_srv)[0]
        ip = server.ip
        port = server.port
        user = server.user
        # theUser = AnsibleWork(ip,port,user,"script","%s/operation/check_services.py %s"%(os.getcwd(),check_args))
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#启动所有服务器上全部服务或者启动某个服务器上的所有的服务
def services_start(request):
    srvnum = request.POST.get('srvnum')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if srvnum =='all':
        pass
    else:
        server = Serverinfo.objects.filter(srvnum=srvnum)[0]
        ip = server.ip
        port = server.port
        user = server.user
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


#停止所有服务器上全部服务或者停止某个服务器上的所有的服务
def services_stop(request):
    srvnum = request.POST.get('srvnum')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if srvnum == 'all':
        pass
    else:
        server = Serverinfo.objects.filter(srvnum=srvnum)[0]
        ip = server.ip
        port = server.port
        user = server.user
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#重启所有服务器上全部服务或者重启某个服务器上的所有的服务
def services_restart(request):
    srvnum = request.POST.get('srvnum')
    msg_dict = {'hello':"后端功能还没OK囧"}
    if srvnum == 'all':
        pass
    else:
        server = Serverinfo.objects.filter(srvnum=srvnum)[0]
        ip = server.ip
        port = server.port
        user = server.user
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')
