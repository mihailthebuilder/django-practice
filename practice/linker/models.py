from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    message_title = models.CharField(max_length=100)
    message_text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def save(self, *args, **kwargs):
        """on save, update timestamp"""
        if not self.id:
            self.created = timezone.now()
        return super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return self.pub_date.strftime("%d/%m/%Y") + "|| " + self.message_title
