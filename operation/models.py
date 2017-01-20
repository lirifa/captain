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

# class productinfo(models.Model):                                                                                              
#     srvnum = models.CharField(verbose_name='服务器编号',max_length=10)
#     ip = models.GenericIPAddressField(verbose_name="IP",max_length=50,unique=True)                                           
#     user = models.CharField(verbose_name='用户名',max_length=10)                                                             
#     passwd = models.CharField(verbose_name='密码',max_length=50)                                                            
#     port = models.IntegerField(verbose_name='SSH端口')                                                                          
#     desc = models.CharField(verbose_name="业务描述",max_length=100)                                                          
#     def __unicode__(self):                                                                                                   
#         return self.ip   
# #def Freekeyinfo(models.Model):
class productinfo(models.Model):
    class productinfo:
        db_table = 'productinfo'
    product_num = models.IntegerField(max_length=16,db_column='product_num',primary_key=True)
    product_name = models.CharField(max_length=32,db_column='product_name',blank=True)
    product_admin = models.CharField(max_length=32,db_column='product_admin',blank=True)
    product_des = models.CharField(max_length=32,db_column='product_des',blank=True)
    def __unicode__(self):
        return self.product_num
