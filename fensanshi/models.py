from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nid=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=32,null=True,unique=True)
    create_time=models.DateTimeField(auto_now_add=True)
    team=models.CharField(max_length=32)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

