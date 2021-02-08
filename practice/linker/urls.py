from django.urls import path
from . import views

app_name = "linker"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("message/<int:message_id>", views.message_detail, name="message_detail"),
]
