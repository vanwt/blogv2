from django.shortcuts import render
from django.views.generic import View
from post.models import PostCategory, Post
from note.models import Note, NoteCategory


# Create your views here.
class IndexView(View):
    def get(self, request, **kwargs):
        n_c = NoteCategory.objects.only("id", "title").all()
        p_c = PostCategory.objects.only("id", "title").all()

        posts = Post.objects.only("title", "create_time", "url").all()
        notes = Note.objects.only("id", "title", "create_time").all()

        content = {
            "nodeCategory": n_c,
            "postCategory": p_c,
            "posts": posts,
            "notes": notes
        }
        return render(request, "index.html", content)
