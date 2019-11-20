from django.urls import path
from .views import *

urlpatterns = [
    path("<int:id>/", NoteView.as_view()),
    path("category/", NodeCateGoryView.as_view()),
    path("category/<int:id>/", NodeCateGoryView.as_view())

]
