from django.http import HttpResponse
from .models import Message, Comment
from django.shortcuts import render

# Create your views here.
def index(request):
    message_list = Message.objects.all()

    context = {"message_list": message_list}
    return render(request, "linker/index.html", context)


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")


def page_not_found_view(request, exception=None):
    return HttpResponse("Wrong page.", status=404)
