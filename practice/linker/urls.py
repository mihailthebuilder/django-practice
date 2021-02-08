from django.urls import path
from . import views

app_name = "linker"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add_message/", views.add_message, name="add_message"),
    path(
        "message/<int:message_id>/add_comment/", views.add_comment, name="add_comment"
    ),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("message/<int:pk>/", views.MessageView.as_view(), name="message_detail"),
]
