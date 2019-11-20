"""
获取全局使用的数据/tags/白名单访问量
"""
from content.models import Tags, WhiteList
from note.models import Note


def base_data(request):
    tag_list = Tags.objects.only("title").all()
    ip = request.META.get("REMOTE_ADDR")
    log = WhiteList.objects.filter(ip=ip).first()
    if not log:
        log = WhiteList(ip=ip, access=1)
        log.save()
    else:
        log.access += 1
        log.save()
    count = WhiteList.objects.count()

    notes = Note.objects.order_by("-create_time").only("id", "title").all()[:4]
    return {
        "tags": tag_list,
        "see": count,
        "new_notes": notes
    }
