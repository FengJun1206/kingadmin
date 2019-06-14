from django.db import models
from django.contrib.auth.models import User, AbstractUser   # 导入 AbstractUser 类


class UserProfile(AbstractUser):
    username = models.CharField(max_length=64, verbose_name='用户名', unique=True)
    phone = models.CharField(max_length=11, verbose_name='手机号码', null=True, blank=True)
    addr = models.CharField(max_length=128, verbose_name='家庭地址', null=True , blank=True)
    user = models.ManyToManyField("Role", blank=True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return '%s：%s' % (self.username, self.user.all()[0].name, )


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, verbose_name='角色名字', unique=True)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.name

