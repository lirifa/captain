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

def master_acct(request):
    return render(request,"master_acct.html")

def master_acct_json(request):
    try:
        master_acct_info = Master_acct.objects.all()
    except Exception,e:
        master_acct_info = []
        errmsg = "%s"%e
    if len(master_acct_info) != 0:
        msg_dict = {"total":len(master_acct_info)}
        msg_dict["rows"] = []
        num = 1
        for key in master_acct_info:
            id = num
            acc_num = key.acc_num
            acc_name = key.acc_name
            trdacct = key.trdacct
            equity = str(key.equity)
            buy_margin = str(key.buy_margin)
            sell_margin = str(key.sell_margin)
            margin_locked = str(key.margin_locked)
            fund_avaril = str(key.fund_avaril)
            num += 1
            msg_dict["rows"].append({
                "id":id,
                "acc_num":acc_num,
                "acc_name":acc_name,
                "trdacct":trdacct,
                "equity":equity,
                "buy_margin":buy_margin,
                "sell_margin":sell_margin,
                "margin_locked":margin_locked,
                "fund_avaril":fund_avaril
                })
    else:
        msg_dict = {"total":0,"rows":[]}
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#-------------新增总账号------------------
def master_acct_add(request):
    acc_num = request.GET.get('acc_num')
    acc_name = request.GET.get('acc_name')
    trdacct = request.GET.get('trdacct')
    equity = request.GET.get('equity')
    fund_avaril = request.GET.get('fund_avaril')
    margin_locked = request.GET.get('margin_locked')
    buy_margin = request.GET.get('buy_margin')
    sell_margin = request.GET.get('sell_margin')
    msg_dict = {}
    if acc_num:
        try:
            master_acct_info = Master_acct.objects.filter(acc_num=acc_num)
        except Exception, e:
            master_acct_info = []
            errmsg = "%s"%e 
            msg_dict['errmsg'] = errmsg
        if len(master_acct_info) == 0:
            try:
                master_acct_info = Master_acct.objects.get(acc_num=acc_num)
            except:
                master_acct_info = Master_acct()
            master_acct_info.acc_num = acc_num
            master_acct_info.acc_name = acc_name
            master_acct_info.trdacct = trdacct
            master_acct_info.equity = equity
            master_acct_info.buy_margin = buy_margin
            master_acct_info.sell_margin = sell_margin
            master_acct_info.margin_locked = margin_locked
            master_acct_info.fund_avaril= fund_avaril
            master_acct_info.save()
            accmsg = u"总账号 [ %s ] 添加成功!"%acc_name
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"总账号 [ %s ] 已存在，不可重复添加!"%acc_num
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入总账号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#--------------修改总账号------------------
def master_acct_mod(request):
    acc_num = request.GET.get('acc_num')
    acc_name = request.GET.get('acc_name')
    trdacct = request.GET.get('trdacct')
    equity = request.GET.get('equity')
    fund_avaril = request.GET.get('fund_avaril')
    margin_locked = request.GET.get('margin_locked')
    buy_margin = request.GET.get('buy_margin')
    sell_margin = request.GET.get('sell_margin')
    msg_dict = {}
    if acc_num:
        try:
            Master_acct.objects.filter(acc_num=acc_num).update(acc_name=acc_name,trdacct=trdacct,equity=equity,fund_avaril=fund_avaril,margin_locked=margin_locked,buy_margin=buy_margin,sell_margin=sell_margin)
            accmsg = u"总账号 [ %s ] 信息修改成功!"%acc_num
            msg_dict['accmsg'] = accmsg
        except Exception, e:
            master_acct_info = []
            errmsg = "%s"%e
            msg_dict['errmsg'] = errmsg
    else:
        errmsg = u"输入总账号为空!"
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

#--------------删除总账号---------------
def master_acct_del(request):
    delinfo = request.GET.get('delinfo')
    idlist = delinfo.split("#")
    del idlist[0]
    msg_dict = {"accmsg":"","errmsg":""}
    for acc_num in idlist:
        try:
            acc_num = Master_acct.objects.filter(acc_num=acc_num)[0].acc_num
            Master_acct.objects.filter(acc_num=acc_num).delete()
            msg_dict["accmsg"] += "<p>%s</p>"%acc_num
        except Exception,e:
            errmsg = "%s"%e
            msg_dict["errmsg"] = errmsg
    print msg_dict
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

def masteracc_combobox_json(request):
    try:
        master_info = Master_acct.objects.all()
    except Exception,e:
        master_info = []
        errmsg = "%s"%e
    msg_dict = []
    if len(master_info) !=0:
        for key in master_info:
            acc_num = key.acc_num
            acc_name = key.acc_name
            msg_dict.append({"acc_num":acc_num,"acc_name":acc_name})
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')

def master_acct_fund_change(request):
    change_fund = decimal.Decimal(request.POST.get('fund_change'))
    change_acct = request.POST.get('change_acct')
    change_desc = request.POST.get('change_desc')
    msg_dict = {}
    try:
        #修改总账号客户权益、可用资金
        acc_num = Master_acct.objects.filter(acc_num=change_acct)[0].acc_num
        equity_ex = Master_acct.objects.filter(acc_num=change_acct)[0].equity
        equity_ed = equity_ex+ change_fund
        fund_avaril_ex = Master_acct.objects.filter(acc_num=change_acct)[0].fund_avaril
        fund_avaril_ed = fund_avaril_ex + change_fund
        Master_acct.objects.filter(acc_num=change_acct).update(equity=equity_ed,fund_avaril=fund_avaril_ed)
        accmsg = u"账号 [ %s ] 资金修改成功!"%acc_num
        msg_dict['accmsg'] = accmsg

        #出入金记录日志
        try:
            Fund_change_log.objects.create(acct_type='master_acct',acct_id=change_acct,change_fund=change_fund,desc=change_desc)
        except Exception as e:
            raise e
    except Exception,e:
        errmsg = "%s"%e
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict),content_type='application/json')