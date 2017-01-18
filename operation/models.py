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

class productinfo(models.Model):                                                                                              
    srvnum = models.CharField(verbose_name='服务器编号',max_length=10)
    ip = models.GenericIPAddressField(verbose_name="IP",max_length=50,unique=True)                                           
    user = models.CharField(verbose_name='用户名',max_length=10)                                                             
    passwd = models.CharField(verbose_name='密码',max_length=50)                                                            
    port = models.IntegerField(verbose_name='SSH端口')                                                                          
    desc = models.CharField(verbose_name="业务描述",max_length=100)                                                          
    def __unicode__(self):                                                                                                   
        return self.ip   
#def Freekeyinfo(models.Model):
