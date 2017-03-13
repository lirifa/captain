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
from operation.serverinfo_views import *
from operation.productinfo_views import *
from operation.strategyinfo_views import *
from operation.acct_views import *
from operation.master_acct_views import *
from operation.sub_acct_views import *
from operation.clear_views import *
from operation.feerate_manage_views import *
from operation.service_views import *
from operation.supervisor_views import *
from operation.position_manage_views import *
from operation.data_send_views import *

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def checklogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    msg_dict = {}
    if username == "hiki" and password == "redhat":
        accmsg = "Hello hiki,welcome to captain!"
        msg_dict['accmsg'] = accmsg
    else:
        errmsg = "Hello hiki,authentication fails!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

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