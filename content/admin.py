from django.contrib import admin
from content.models import Tags, WhiteList, Site


# Register your models here.
@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "create_time"]

    def __str__(self):
        return self.title


@admin.register(WhiteList)
class WhiteListAdmin(admin.ModelAdmin):
    list_display = ["ip", "access", "last_time"]

    def __str__(self):
        return self.ip


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ["head_background_color", "content_background_color", "bottom_background_color", "head_color",
                    "content_color"]

    def __str__(self):
        return self.ip
