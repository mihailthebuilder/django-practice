from django.db import models
from django.utils import timezone

# Create your models here.
class CommonTextModel(models.Model):
    text_content = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    votes = models.SmallIntegerField(default=0)

    def formatted_date(self):
        return self.pub_date.strftime("%d/%m/%Y | %H:%M")

    class Meta:
        abstract = True


class Message(CommonTextModel):
    message_title = models.CharField(max_length=100)

    def __str__(self):
        return self.formatted_date() + " || " + self.message_title


class Comment(CommonTextModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        str_self_text = self.text_content
        if len(str_self_text) > 40:
            str_self_text = str_self_text[:40] + "..."

        return self.formatted_date() + " || " + str_self_text