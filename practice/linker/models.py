from django.db import models

# Create your models here.
class Message(models.Model):
    message_title = models.CharField(max_length=100)
    message_text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.pub_date.strftime("%d/%m/%Y") + "|| " + self.message_title
