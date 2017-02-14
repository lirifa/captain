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
    master_acc = models.CharField(verbose_name='总账号',max_length=32)
    sub_acc = models.CharField(verbose_name='子账号',max_length=32)
    port = models.IntegerField(verbose_name='策略端口')
    desc = models.CharField(verbose_name='策略介绍',max_length=32)
    def __unicode__(self):
        return self.sid
    class Meta:
        db_table = 'strategyinfo'

#资金账户信息表
class Acct(models.Model):
    trdacct = models.CharField(verbose_name='账户号',max_length=32,primary_key=True)
    acc_name = models.CharField(verbose_name='账户名',max_length=32)
    bid = models.IntegerField(verbose_name='经纪商id')
    pid = models.IntegerField(verbose_name='产品id')
    equity = models.DecimalField(verbose_name='客户权益',max_length=128,max_digits=17,decimal_places=2)
    margin_locked = models.DecimalField(verbose_name='保证金占用',max_digits=17,decimal_places=2)
    fund_avaril = models.DecimalField(verbose_name='可以资金',max_digits=17,decimal_places=2)
    risk_degree = models.CharField(verbose_name='风险度',max_length=11)
    def __unicode__(self):
        return self.trdacct
    class Meta:
        db_table = 'acct'

#总账号信息表
class Master_acct(models.Model):
    acc_num = models.CharField(verbose_name='账户号',max_length=32,primary_key=True)
    acc_name = models.CharField(verbose_name='账户名',max_length=32)
    trdacct = models.CharField(verbose_name='关联资金账户',max_length=32)
    equity = models.DecimalField(verbose_name='客户权益',max_digits=17,decimal_places=2)
    buy_margin = models.DecimalField(verbose_name='买保证金占用',max_digits=17,decimal_places=2)
    sell_margin = models.DecimalField(verbose_name='卖保证金占用',max_digits=17,decimal_places=2)
    margin_locked = models.DecimalField(verbose_name='保证金占用',max_digits=17,decimal_places=2)
    fund_avaril = models.DecimalField(verbose_name='可用资金',max_digits=17,decimal_places=2)
    def __unicode__(self):
        return self.acc_num
    class Meta:
        db_table = 'master_acct'

#子账号信息表
class Sub_acct(models.Model):
    acc_num = models.CharField(verbose_name='账户号',max_length=32,primary_key=True)
    acc_name = models.CharField(verbose_name='账户名',max_length=32)
    master_acct = models.CharField(verbose_name='关联总账号',max_length=32)
    equity = models.DecimalField(verbose_name='客户权益',max_digits=17,decimal_places=2)
    fund_avaril = models.DecimalField(verbose_name='可用资金',max_digits=17,decimal_places=2)
    margin_locked = models.DecimalField(verbose_name='总保证金占用',max_digits=17,decimal_places=2)
    buy_margin = models.DecimalField(verbose_name='买保证金占用',max_digits=17,decimal_places=2)
    sell_margin = models.DecimalField(verbose_name='卖保证金占用',max_digits=17,decimal_places=2)
    def __unicode__(self):
        return self.acc_num
    class Meta:
        db_table = 'sub_acct'

#经纪商信息表
class Broker(models.Model):
    bid = models.IntegerField(verbose_name='经纪商ID',primary_key=True)
    bname = models.CharField(verbose_name='经纪商简称',max_length=32)
    blname = models.CharField(verbose_name='经纪商全称',max_length=32)
    def __unicode__(self):
        return self.bid
    class Meta:
        db_table = 'broker'



