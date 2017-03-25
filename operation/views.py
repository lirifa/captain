#coding:utf-8
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
from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from operation.models import *
from operation.user_manage_views import *
from operation.serverinfo_views import *
from operation.productinfo_views import *
from operation.acct_views import *
from operation.master_acct_views import *
from operation.sub_acct_views import *
from operation.clear_views import *
from operation.feerate_manage_views import *
from operation.service_views import *
from operation.gw_manage_views import *
from operation.ss_manage_views import *
from operation.ps_manage_views import *
from operation.position_manage_views import *
from operation.data_send_views import *

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

def login(request):
    return render(request,"login.html")

# def index(request):
#     return render(request,"index.html")

def checklogin(request):
    username = request.POST.get("username")
    passwd = request.POST.get("password")
    msg_dict = {}
    print username,passwd
    if username:
        try:
            user = User.objects.filter(username=username)
        except Exception,e:
            user = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
        if len(user) != 0:
            passwd_db = User.objects.filter(username=username)[0].passwd
            if passwd == passwd_db:
                accmsg = "Hello %s,welcome to captain!"%username
                msg_dict['accmsg']=accmsg
                response =  HttpResponseRedirect("/index/")
                response.set_cookie('username',username,3600)
                print response
                return response
            else:
                errmsg = "Sorry, wrong password, please login again!"
                msg_dict['errmsg'] = errmsg
                return HttpResponse(json.dumps(msg_dict), content_type='application/json')
        else:
            errmsg = "User doesn't exist!"
            msg_dict['errmsg'] = errmsg
        return HttpResponse(json.dumps(msg_dict), content_type='application/json')
    else:
        errmsg = "Username is empty!"
        msg_dict['errmsg'] = errms
        return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

def dashboard(request):
    return render(request,"dashboard.html")

def supervisor(request):
    return render(request,"supervisor.html")

def configure(request):
    return render(request,"configure.html")

#404页面
def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response('500.html')