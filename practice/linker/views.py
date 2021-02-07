from django.http import HttpResponse
from .models import Message, Comment
from django.shortcuts import render

# Create your views here.
def index(request):

    messages = Message.objects.all()
    comments = Comment.objects.all()

    message_list = list(
        map(
            lambda message: {
                "message_title": message.message_title,
                "formatted_date": message.formatted_date,
                "votes": message.votes,
                "comments_num": len(comments.filter(message=message)),
            },
            messages,
        )
    )

    context = {"message_list": message_list}
    return render(request, "linker/index.html", context)


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")


def page_not_found_view(request, exception=None):
    return HttpResponse("Wrong page.", status=404)
