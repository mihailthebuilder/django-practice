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


class MessageView(generic.DetailView):
    template_name = "linker/message_detail.html"
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = context["message"].comment_set.all()
        context["comments_num"] = len(context["comments"])
        return context


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")


def page_not_found_view(request, exception=None):
    return HttpResponse("Wrong page.", status=404)
