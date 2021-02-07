from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the homepage.")


def contact(request):
    return HttpResponse("Contact me here.")


def about(request):
    return HttpResponse("Find out more about me.")
