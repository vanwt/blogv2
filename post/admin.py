from django.contrib import admin
from .models import Post, PostCategory
import markdown


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "is_top", "desc", "read_num", "create_time"]
    fields = (
        ("title", "desc"), "url", "category", "tags", "md_content")
    list_filter = ("title",)
    search_fields = ("title",)
    list_editable = ["desc"]
    filter_horizontal = ["tags"]

    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        obj.html_content = markdown.markdown(obj.md_content)
        return super().save_model(request, obj, form, change)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "create_time"]

    def __str__(self):
        return self.title
