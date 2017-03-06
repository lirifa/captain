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

def sub_acct(request):
    return render(request,"sub_acct.html")

def sub_acct_json(request):
    try:
        sub_acct_info = Sub_acct.objects.all()
    except Exception, e:
        sub_acct_info = []
        errmsg = "%s"%e
    if len(sub_acct_info) !=0:
        msg_dict = {"total":len(sub_acct_info)}
        msg_dict["rows"] = []
        num = 1
        for key in sub_acct_info:
            id = num
            acc_num = key.acc_num
            acc_name = key.acc_name
            master_acct = key.master_acct
            equity = str(key.equity)
            fund_avaril = str(key.fund_avaril)
            margin_locked = str(key.margin_locked)
            buy_margin = str(key.buy_margin)
            sell_margin = str(key.sell_margin)
            num += 1
            msg_dict["rows"].append({"id":id,"acc_num":acc_num,"acc_name":acc_name,"master_acct":master_acct,"equity":equity,"fund_avaril":fund_avaril,"margin_locked":margin_locked,"buy_margin":buy_margin,"sell_margin":sell_margin})
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#--------------新增子账号------------------
def sub_acct_add(request):
    acc_num = request.GET.get('acc_num')
    acc_name = request.GET.get('acc_name')
    master_acct = request.GET.get('master_acct')
    equity = request.GET.get('equity')
    buy_margin = request.GET.get('buy_margin')
    sell_margin = request.GET.get('sell_margin')
    margin_locked = request.GET.get('margin_locked')
    fund_avaril = request.GET.get('fund_avaril')
    msg_dict = {}
    if acc_num:
        try:
            sub_acct_info = Sub_acct.objects.filter(acc_num=acc_num)
        except Exception, e:
            sub_acct_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(sub_acct_info) == 0 :
            try:
                sub_acct_info = Sub_acct.objects.get(acc_num=acc_num)
            except:
                sub_acct_info = Sub_acct()
            sub_acct_info.acc_num = acc_num
            sub_acct_info.acc_name = acc_name
            sub_acct_info.master_acct = master_acct
            sub_acct_info.equity = equity
            sub_acct_info.fund_avaril= fund_avaril
            sub_acct_info.margin_locked = margin_locked
            sub_acct_info.buy_margin = buy_margin
            sub_acct_info.sell_margin = sell_margin
            sub_acct_info.save()
            accmsg = u"子账号 [ %s ] 添加成功!"%acc_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"子账号 [ %s ] 已存在，不可重复添加!"%acc_num
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入子账号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#----------------修改子账号信息---------------------------
def sub_acct_mod(request):
    acc_num = request.GET.get('acc_num')
    acc_name = request.GET.get('acc_name')
    master_acct = request.GET.get('master_acct')
    equity = request.GET.get('equity')
    fund_avaril = request.GET.get('fund_avaril')
    margin_locked = request.GET.get('margin_locked')
    buy_margin = request.GET.get('buy_margin')
    sell_margin = request.GET.get('sell_margin')
    msg_dict = {}
    if acc_num:
        try:
            Sub_acct.objects.filter(acc_num=acc_num).update(acc_name=acc_name,master_acct=master_acct,equity=equity,fund_avaril=fund_avaril,margin_locked=margin_locked,buy_margin=buy_margin,sell_margin=sell_margin)
            accmsg = u"子账号 [ %s ] 信息修改成功!"%acc_num
            msg_dict['accmsg'] = accmsg
        except Exception, e:
            sub_acct_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入子账号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-----------------------删除子账号---------------------------------
def sub_acct_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for acc_num in idlist:
        try:
            acc_num = Sub_acct.objects.filter(acc_num=acc_num)[0].acc_num
            Sub_acct.objects.filter(acc_num=acc_num).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%acc_num
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def subacc_combobox_json(request,*param1):
    master_acct = request.GET.get('param1')
    print master_acct
    if master_acct:
        try:
            sub_info = Sub_acct.objects.filter(master_acct=master_acct)
        except Exception,e:
            sub_info = []
            errmsg = "%s"%e
        if len(sub_info) !=0:
            msg_dict = []
            for key in sub_info:
                acc_num = key.acc_num
                acc_name = key.acc_name
                msg_dict.append({"acc_num":acc_num,"acc_name":acc_name})
    else:
        try:
            sub_info = Sub_acct.objects.all()
        except Exception,e:
            sub_info = []
            errmsg = "%s"%e
        if len(sub_info) !=0:
            msg_dict = []
            for key in sub_info:
                acc_num = key.acc_num
                acc_name = key.acc_name
                msg_dict.append({"acc_num":acc_num,"acc_name":acc_name})
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def sub_acct_fund_change(request):
    change_fund = decimal.Decimal(request.POST.get('fund_change'))
    change_acct = request.POST.get('change_acct')
    change_desc = request.POST.get('change_desc')
    msg_dict = {}
    try:
        #修改子账号客户权益、可用资金
        acc_num = Sub_acct.objects.filter(acc_num=change_acct)[0].acc_num
        equity_ex = Sub_acct.objects.filter(acc_num=change_acct)[0].equity
        equity_ed = equity_ex+ change_fund
        fund_avaril_ex = Sub_acct.objects.filter(acc_num=change_acct)[0].fund_avaril
        fund_avaril_ed = fund_avaril_ex + change_fund
        Sub_acct.objects.filter(acc_num=change_acct).update(equity=equity_ed,fund_avaril=fund_avaril_ed)
        accmsg = u"账号 [ %s ] 资金修改成功!"%acc_num
        msg_dict['accmsg'] = accmsg

        #出入金记录日志
        try:
            Fund_change_log.objects.create(acct_type='sub_acct',acct_id=change_acct,change_fund=change_fund,desc=change_desc)
        except Exception as e:
            raise e
    except Exception,e:
        errmsg = "%s"%e
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')