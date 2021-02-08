from django.http import HttpResponse, HttpResponseRedirect
from .models import Message, Comment
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404

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


def add_message(request):
    message = Message(
        message_title=request.POST["message_title"],
        text_content=request.POST["message_text"],
    )
    message.save()
    return HttpResponseRedirect(reverse("linker:index"))


def add_comment(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    comment = Comment(text_content=request.POST["comment"], message=message)
    comment.save()
    return HttpResponseRedirect(reverse("linker:message_detail", args=(message.id,)))


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")


def page_not_found_view(request, exception=None):
    return HttpResponse("Wrong page.", status=404)
