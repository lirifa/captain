# coding:utf-8
from django.db import models


# Create your models here.
#用户信息表
class User(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=50,primary_key=True )
    passwd = models.CharField(verbose_name='用户密码',max_length=50)
    tel = models.CharField(verbose_name='联系电话',max_length=50)
    email = models.CharField(verbose_name='邮箱地址',max_length=50)
    permission = models.CharField('权限等级',max_length=1)
    desc = models.CharField('备注',max_length=32)
    def __unicode__(self):
        return self.username
    class Meta:
        db_table = 'userinfo'

#主机信息表
class Serverinfo(models.Model):
    srvnum = models.CharField(verbose_name='服务器编号',max_length=10,primary_key=True)
    ip = models.GenericIPAddressField(verbose_name="IP",max_length=50,unique=True)
    user = models.CharField(verbose_name='主机用户',max_length=10)
    passwd = models.CharField(verbose_name='登录密码',max_length=50)
    port = models.IntegerField(verbose_name='SSH端口')
    productadmin = models.CharField(verbose_name='产品管理人',max_length=32) 
    desc = models.CharField(verbose_name="业务描述",max_length=100)
    def __unicode__(self):
        return self.srvnum
    class Meta:
        db_table = 'serverinfo'

#服务信息表
class Serviceinfo(models.Model):
    ser_id = models.IntegerField('服务id',primary_key=True)
    ser_name = models.CharField('服务名称',max_length=32)
    ser_att = models.CharField('服务属性',max_length=32)
    ser_cfg = models.CharField('对应配置名',max_length=32)
    ser_port =  models.IntegerField('端口')
    ser_stat = models.CharField('服务状态',max_length=32)
    port_stat = models.CharField('端口状态',max_length=32)
    ser_srv = models.CharField('所属主机',max_length=10)
    desc = models.CharField('备注',max_length=32)
    def __unicode__(self):
        return self.service_id
    class Meta:
        db_table = 'serviceinfo'

#数据分发配置表
class Data_send(models.Model):
    id = models.AutoField('主键id',primary_key=True)
    d_name = models.CharField('配置名',max_length=32)
    o_srv = models.CharField('源服务器',max_length=32)
    o_dir = models.CharField('源目录地址',max_length=32)
    p_srv = models.CharField('目的服务器',max_length=32)
    p_dir = models.CharField('目的目录地址',max_length=32)
    update_tm = models.DateTimeField('更新时间',auto_now=True)
    def __unicode__(self):
        return self.id
    class Meta:
        db_table = 'data_send'

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
    ss_id = models.IntegerField(verbose_name='策略编号',primary_key=True)
    ss_name = models.CharField(verbose_name='策略名称',max_length=32)
    ss_cfg = models.CharField(verbose_name='对应配置名',max_length=32)
    ss_srv = models.CharField('对应主机',max_length=32)
    product = models.CharField(verbose_name='所属产品',max_length=32)
    master_acc = models.CharField(verbose_name='总账号',max_length=32)
    sub_acc = models.CharField(verbose_name='子账号',max_length=32)
    port = models.IntegerField(verbose_name='策略端口')
    desc = models.CharField(verbose_name='策略介绍',max_length=32)
    def __unicode__(self):
        return self.sid
    class Meta:
        db_table = 'strategyinfo'

#PriceServer信息表
class Priceserverinfo(models.Model):
    ps_id = models.CharField('PS id',max_length=32,primary_key=True)
    ps_name = models.CharField('PS名称',max_length=32)
    ps_cfg = models.CharField('对应配置名',max_length=32)
    port = models.IntegerField('ps端口')
    ps_srv = models.CharField('所属主机',max_length=32)
    desc = models.CharField('备注',max_length=32)
    def __unicode__(self):
        return self.ps_id
    class Meta:
        db_table = 'priceserverinfo'

#Gateway信息表
class Gatewayinfo(models.Model):
    gw_id = models.CharField('gateway id',max_length=32,primary_key=True)
    gw_name = models.CharField('gateway名称',max_length=32)
    gw_cfg = models.CharField('对应配置名',max_length=32)
    port = models.IntegerField('gw端口')
    gw_srv = models.CharField('所属主机',max_length=32)
    product = models.CharField('所属产品',max_length=32)
    desc = models.CharField('备注',max_length=32)
    def __unicode__(self):
        return self.gw_id
    class Meta:
        db_table = 'gatewayinfo'

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

#出入金记录表
class Fund_change_log(models.Model):
    log_id = models.AutoField(primary_key=True)
    acct_type = models.CharField(verbose_name='账户类别',max_length=32)
    acct_id = models.CharField(verbose_name='账户id',max_length=32)
    change_fund = models.DecimalField(verbose_name='出入金金额',max_digits=17,decimal_places=2)
    desc = models.CharField(verbose_name='备注',max_length=32)
    log_tm = models.DateTimeField(verbose_name='保存日期',auto_now=True)
    def __unicode__(self):
        return self.log_id
    class Meta:
        db_table = 'fund_change_log'

#资金账户持仓表
class Acct_hold(models.Model):
    trd_date = models.CharField(verbose_name='交易日期',max_length=8)
    trdacct = models.CharField(verbose_name='资金账户号',max_length=32)
    instrument = models.CharField(verbose_name='合约名',max_length=32)
    variety = models.CharField(verbose_name='品种名',max_length=32)
    long_pos = models.IntegerField(verbose_name='买持仓')
    avg_buy_price = models.DecimalField(verbose_name='买均价',max_digits=17,decimal_places=3)
    short_pos = models.IntegerField(verbose_name='卖持仓')
    avg_sell_price = models.DecimalField(verbose_name='卖均价',max_digits=17,decimal_places=3)
    pos_pl = models.DecimalField(verbose_name='持仓订市盈亏',max_digits=17,decimal_places=2)
    margin_occupied = models.DecimalField(verbose_name='保证金占用',max_digits=17,decimal_places=2)
    sh_mark = models.CharField(verbose_name='投保标识',max_length=1)
    class Meta:
        db_table = 'acct_hold'
        unique_together = ("trd_date","trdacct","instrument")
    def __unicode__(self):
        return '%s,%s,%s'%(self.trd_date,self.trdacct,self.instrument)

#手续费率信息表
class Feerate(object):
    bid = models.IntegerField(verbose_name='券商id')
    exchange_id = models.CharField(verbose_name='交易所',max_length=32)
    contract_id = models.CharField(verbose_name='合约标识',max_length=32)
    biz_type = models.CharField(verbose_name='开平标志',max_length=1)
    feerate_by_amt = models.DecimalField(verbose_name='百分比',max_digits=17,decimal_places=8)
    feerate_by_qty = models.DecimalField(verbose_name='按手数',max_digits=17,decimal_places=8)
    def __unicode__(self):
        return '%d,%s,%s,%s'%(self.bid,self.exchange_id,self.contract_id,self.biz_type)
    class Meta:
        db_table = 'feerate'
        unique_together = ("bid","exchange_id","contract_id","biz_type")
