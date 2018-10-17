from django.db import models

# Create your models here.


class PraiseUser(models.Model):
    """
    有赞用户表：有赞渠道进入系统用户信息表，外键关联系统用户表
    """
    nickname = models.CharField(max_length=32, null=True, blank=True, verbose_name="用户昵称")
    mobile = models.CharField(max_length=24, null=True, blank=True, verbose_name="用户电话")
    sex = models.IntegerField(null=True, blank=True, verbose_name="性别")
    birthday = models.CharField(max_length=24, null=True, blank=True, verbose_name="生日")
    country = models.CharField(max_length=32, null=True, blank=True, verbose_name="国家")
    province = models.CharField(max_length=32, null=True, blank=True, verbose_name="省份")
    city = models.CharField(max_length=32, null=True, blank=True, verbose_name="城市")
    points = models.IntegerField(null=True, blank=True, verbose_name="积分")
    contact_address = models.CharField(max_length=256, null=True, blank=True, verbose_name="详细地址")
    is_member = models.BooleanField(default=False, verbose_name="是否为有赞会员")
    trade_count = models.IntegerField(default=0, verbose_name="订单数")
    yz_uid = models.IntegerField(null=True, blank=True, verbose_name="有赞id")

    class Meta:
        verbose_name = '有赞用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.mobile


class students(models.Model):
    nickname = models.CharField(max_length=32, null=True, blank=True, verbose_name="用户昵称")
    mobile = models.CharField(max_length=24, null=True, blank=True, verbose_name="用户电话")
    sex = models.IntegerField(null=True, blank=True, verbose_name="性别")