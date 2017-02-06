# coding:utf-8
from django.db import models

# Create your models here.

class Serverinfo(models.Model):                                                                                              
    srvnum = models.CharField(verbose_name='服务器编号',max_length=10)
    ip = models.GenericIPAddressField(verbose_name="IP",max_length=50,unique=True)                                           
    user = models.CharField(verbose_name='用户名',max_length=10)                                                             
    passwd = models.CharField(verbose_name='密码',max_length=50)                                                            
    port = models.IntegerField(verbose_name='SSH端口')                                                                          
    desc = models.CharField(verbose_name="业务描述",max_length=100)                                                          
    def __unicode__(self):                                                                                                   
        return self.ip   

class Productinfo(models.Model):
    product_num = models.IntegerField(verbose_name='产品编号',unique=True)
    product_name = models.CharField(verbose_name='产品名称',max_length=32)
    product_admin = models.CharField(verbose_name='产品管理人',max_length=32)
    product_desc = models.CharField(verbose_name='产品描述',max_length=32)
    def __unicode__(self):
        return self.product_num

class Strategyinfo(models.Model):
    strategy_id = models.IntegerField(verbose_name='策略编号',max_length=11)
    strategy_name = models.CharField(verbose_name='策略名称',max_length=32)
    strategy_product = models.CharField(verbose_name='所属产品',max_length=32)
    strategy_desc = models.CharField(verbose_name='策略介绍',max_length=32)
    total_account = models.IntegerField(verbose_name='总账号',max_length=20)
    sub_account = models.IntegerField(verbose_name='子账号',max_length=20)
    def __unicode__(self):
        return self.strategy_id
        