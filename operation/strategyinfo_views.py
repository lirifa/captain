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

def strategyinfo(request):
    return render(request,'strategyinfo.html')

def strategyinfo_json(request):
	try:
		strategy_info = Strategyinfo.objects.all()

	except Exception as e:
		strategy_info = []
		errmsg = "%s"%e
	if len(strategy_info) != 0:
        msg_dict = {"total":len(strategy_info)}
        msg_dict["rows"] = []
        num = 1
        for key in product_info:
            id = num
            strategy_id = key.strategy_id
            strategy_name = key.product_name
            strategy_product = key.to_product
            strategy_desc = key.product_desc
            total_account = key.total_account
            sub_account = key.sub_account
            num += 1
            msg_dict["rows"].append({"id":id,"strategy_id":strategy_id,"strategy_name":strategy_name,"strategy_product":strategy_product,"strategy_desc":strategy_desc,"total_account":total_account,"sub_account":sub_account})	
	else:
		msg_dict = {"total":0,"rows":[]}
	return HttpResponse(json.dumps(msg_dict), content_type='application/json')