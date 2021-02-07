from django.db import models
from django.utils import timezone

# Create your models here.
class CommonTextModel(models.Model):
    text_content = models.TextField()
    pub_date = models.DateTimeField("date published", blank=True)
    votes = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        """on save, update timestamp"""
        self.pub_date = timezone.now()
        return super(CommonTextModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Message(CommonTextModel):
    message_title = models.CharField(max_length=100)

    def __str__(self):
        return self.pub_date.strftime("%d/%m/%Y") + " || " + self.message_title


class Comment(CommonTextModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        str_self_text = self.text_content
        if len(str_self_text) > 40:
            str_self_text = str_self_text[:40] + "..."

        return self.pub_date.strftime("%d/%m/%Y") + " || " + str_self_text