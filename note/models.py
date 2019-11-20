from django.db import models
from content.models import Tags
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题", blank=True, db_index=True)
    desc = models.CharField(max_length=256, verbose_name="总结", blank=True, null=True)
    read_num = models.IntegerField(verbose_name="阅读量", default=0)
    md_content = RichTextUploadingField(verbose_name="内容", blank=True, config_name="my_config")
    html_content = models.TextField(verbose_name="markdown", null=True, blank=True)

    is_hide = models.BooleanField("是否隐藏", default=False, blank=True)
    is_top = models.BooleanField("是否置顶", default=False, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    tags = models.ManyToManyField(Tags, related_name="notes", db_constraint=False, blank=True)
    category = models.ForeignKey("note.NoteCategory", related_name="notes", db_constraint=False, null=True,
                                 blank=True, on_delete=models.SET_NULL)

    objects = models.Manager

    class Meta:
        db_table = "note"
        verbose_name = "笔记"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NoteCategory(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, verbose_name="分类名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", blank=True)

    class Meta:
        db_table = "note_category"
        verbose_name = "笔记分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
