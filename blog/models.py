from django.db import models

# Create your models here.
from django.utils import timezone
class messageMail(models.Model):
    name = models.CharField("用户名", max_length=30, default="没留名的小坏蛋")
    message = models.CharField("留言内容", max_length=1024, default="刘明")
    email = models.CharField("联系邮箱", max_length=50, null=True)
    isOpen = models.BooleanField("是否公开", default=False)
    date = models.DateTimeField("留言时间", default=timezone.now)