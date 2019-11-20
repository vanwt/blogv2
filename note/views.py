from django.shortcuts import render, Http404
from django.views.generic import View
from .models import Note, NoteCategory


# Create your views here.


class NoteView(View):
    def get(self, request, **kwargs):
        id = self.kwargs.get("id", None)
        note = Note.objects.filter(id=id).first()

        if note:
            content = {
                "html": note.html_content,
            }
            note.read_num += 1
            note.save()
            return render(request, "note.html", content)

        raise Http404


class NodeCateGoryView(View):
    def get(self, request, **kwargs):
        id = self.kwargs.get("id", None)
        cg = NoteCategory.objects.filter(id=id).first()
        if cg:
            notes = Note.objects.only("id", "title", "create_time").filter(category=cg)
            n_c = NoteCategory.objects.only("id", "title").all()
            content = {
                "notes": notes,
                "nodeCategory": n_c,
            }
        else:
            notes = Note.objects.only("id", "title", "create_time").all()
            n_c = NoteCategory.objects.only("id", "title").all()
            content = {
                "notes": notes,
                "nodeCategory": n_c,
            }
        return render(request, "node_category.html", content)
