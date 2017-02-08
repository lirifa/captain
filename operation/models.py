# coding:utf-8
from django.db import models

# Create your models here.
#主机信息表
class Serverinfo(models.Model):
    srvnum = models.CharField(verbose_name='服务器编号',max_length=10,primary_key=True)
    ip = models.GenericIPAddressField(verbose_name="IP",max_length=50,unique=True)
    user = models.CharField(verbose_name='用户名',max_length=10)
    passwd = models.CharField(verbose_name='密码',max_length=50)
    port = models.IntegerField(verbose_name='SSH端口')
    productadmin = models.CharField(verbose_name='产品管理人',max_length=32) 
    desc = models.CharField(verbose_name="业务描述",max_length=100)
    def __unicode__(self):
        return self.ip
    class Meta:
        db_table = 'serverinfo'

#产品信息表
class Productinfo(models.Model):
    pid = models.IntegerField(verbose_name='产品编号',primary_key=True)
    pname = models.CharField(verbose_name='产品名称',max_length=32)
    admin = models.CharField(verbose_name='产品管理人',max_length=32)
    desc = models.CharField(verbose_name='产品描述',max_length=32)
    def __unicode__(self):
        return self.pid
    class Meta:
        db_table = 'productinfo'

#策略信息表
class Strategyinfo(models.Model):
    sid = models.IntegerField(verbose_name='策略编号',primary_key=True)
    sname = models.CharField(verbose_name='策略名称',max_length=32)
    scfg = models.CharField(verbose_name='对应配置名',max_length=32)
    product = models.CharField(verbose_name='所属产品',max_length=32)
    master_acc = models.IntegerField(verbose_name='总账号')
    sub_acc = models.IntegerField(verbose_name='子账号')
    port = models.IntegerField(verbose_name='策略端口')
    desc = models.CharField(verbose_name='策略介绍',max_length=32)
    def __unicode__(self):
        return self.sid
    class Meta:
        db_table = 'strategyinfo'

#资金账户信息表
#class Accout:
#    pass


#总账号信息表
#class Master_acc(object):
#    acc_num = models.IntegerField(verbose_name='账户号',primary_key=True)
#    acc_name = models.CharField(verbose_name='账户名',max_length=32)
#    b_acc = models.IntegerField(verbose_name='关联资金账户')
#    acc_fund = models.IntegerField(verbose_name='初始资金')
#    interests = models.IntegerField(verbose_name='客户权益')
#    fund_bln = models.
#
#子账号信息表

