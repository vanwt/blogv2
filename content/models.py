from django.db import models


# Create your models here.
class Tags(models.Model):
    title = models.CharField(verbose_name="标签名", max_length=128, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", blank=True)

    class Meta:
        db_table = "blog_tag"
        verbose_name = "标签表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Site(models.Model):
    head_background_color = models.CharField(verbose_name="头部背景色", null=True, blank=True, max_length=32)
    content_background_color = models.CharField(verbose_name="头部内容色", null=True, blank=True, max_length=32)
    bottom_background_color = models.CharField(verbose_name="底部内容色", null=True, blank=True, max_length=32)
    head_color = models.CharField(verbose_name="头部字体颜色", null=True, blank=True, max_length=32)
    content_color = models.CharField(verbose_name="内容字体颜色", null=True, blank=True, max_length=32)

    class Meta:
        db_table = "blog_site"
        verbose_name = "设置"
        verbose_name_plural = verbose_name


class WhiteList(models.Model):
    ip = models.GenericIPAddressField(verbose_name="访问ip", editable=True, db_index=True)
    is_ban = models.BooleanField(verbose_name="Ban", default=False, blank=True)
    access = models.IntegerField(verbose_name="访问次数", default=False, blank=True)
    last_time = models.DateField(auto_now=True, verbose_name="最后访问时间", blank=True)

    class Meta:
        db_table = "white_list"
        verbose_name = "名单"
        verbose_name_plural = verbose_name
