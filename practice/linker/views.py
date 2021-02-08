from django.http import HttpResponse
from .models import Message, Comment
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "linker/index.html"
    context_object_name = "message_list"

    def get_queryset(self):
        return list(
            map(
                lambda message: {
                    "id": message.id,
                    "message_title": message.message_title,
                    "formatted_date": message.formatted_date,
                    "votes": message.votes,
                    "comments_num": len(message.comment_set.all()),
                },
                Message.objects.all(),
            )
        )


def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    comments = Comment.objects.all().filter(message=message)

    context = {
        "message": message,
        "comments": comments,
        "comments_num": len(comments),
    }

    return render(request, "linker/message_detail.html", context)


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")


def page_not_found_view(request, exception=None):
    return HttpResponse("Wrong page.", status=404)
