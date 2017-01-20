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
        product_info = productinfo.objects.all()
    except Exception,e:
        product_info = []
        errmsg = "%s"%e
    if len(product_info) != 0:
        msg_dict = {"total":len(product_info)}
        msg_dict["rows"] = []
        num = 1
        for key in product_info:
            id = num
            product_num = key.product_num
            product_name = key.product_name
            product_admin = key.product_admin
            product_desc = key.product_desc
            num += 1
            msg_dict["rows"].append({"id":id,"product_num":product_num,"product_name":product_name,"product_admin":product_admin,"product_desc":product_desc})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def productinfo_add(request):
    product_num = request.GET.get('product_num')
    product_name = request.GET.get('product_name')
    product_admin = request.GET.get('product_admin')
    product_desc = request.GET.get('product_desc')
    msg_dict = {}
    if product_num:
        try:
            product_info = productinfo.objects.filter(product_num=product_num)
        except Exception,e:
            product_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(product_info) == 0:
            try:
                product_info = productinfo.objects.get(productinfo=product_num)
            except:
                product_info = productinfo()
            product_info.product_num = product_num
            product_info.product_name = product_name
            product_info.product_admin = product_admin
            product_info.desc = product_desc
            product_info.save()
            accmsg = u"新产品 [ %s ] 添加成功!"%ip
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"产品 [ %s ] 已存在，不可重复添加!"%ip
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入产品编号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')    

def productinfo_del(request):
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
