from django.shortcuts import render, Http404
from django.views.generic import View
from .models import Post, PostCategory


# Create your views here.
class PostView(View):
    def get(self, request, **kwargs):
        url = self.kwargs.get("url", None)
        post = Post.objects.filter(url=url).first()

        if post:
            content = {
                "html": post.html_content,
            }
            post.read_num += 1
            post.save()
            return render(request, "post.html", content)

        raise Http404


class PostCateGoryView(View):
    def get(self, request, **kwargs):
        id = self.kwargs.get("id", None)
        cg = PostCategory.objects.filter(id=id).first()
        if cg:
            posts = Post.objects.only("url", "title", "create_time").filter(category=cg)
            p_c = PostCategory.objects.only("id", "title").all()
            content = {
                "posts": posts,
                "postCategory": p_c,
            }
        else:
            posts = Post.objects.only("url", "title", "create_time").all()
            p_c = PostCategory.objects.only("id", "title").all()
            content = {
                "posts": posts,
                "postCategory": p_c,
            }
        return render(request, "post_category.html", content)
