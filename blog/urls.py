from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static as st
from django.views import static
from django.conf.urls import url
from django.views.generic import TemplateView
from blog import settings
from content.views import IndexView

urlpatterns = [
    path('blog/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path('uploader/', include('ckeditor_uploader.urls')),
    path("note/", include("note.urls")),
    path("post/", include("post.urls")),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]

urlpatterns += st(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += serve(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
