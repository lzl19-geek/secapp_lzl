# Create your models here.
from django.db import models  # 引入django.db.models模块
class CreateUpdate(models.Model):  # 创建抽象数据模型，同样要继承于models.Model
    # 创建时间，使用models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间，使用models.DateTimeField
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:  # 元数据，除了字段以外的所有属性
        # 设置model为抽象类。指定该表不应该在数据库中创建
        abstract = True

class Person(CreateUpdate):  # 继承CreateUpdate基类，相当于创建一个表格：firstapp
    first_name = models.CharField(max_length=30)  #相当于创建的一个字段：
    last_name = models.CharField(max_length=30)

class Order(CreateUpdate):  # 继承CreateUpdate基类
    order_id = models.CharField(max_length=30, db_index=True)
    order_desc = models.CharField(max_length=120)

class mylogin(CreateUpdate):  # 继承CreateUpdate基类
    Username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class mylogout(CreateUpdate):  # 继承CreateUpdate基类
    logoutime = models.DateTimeField(auto_now=True)