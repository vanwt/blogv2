from django.urls import path
from .views import PostCateGoryView, PostView

urlpatterns = [
    path("category/", PostCateGoryView.as_view()),
    path("<str:url>/", PostView.as_view()),
    path("category/<int:id>/", PostCateGoryView.as_view()),
]
