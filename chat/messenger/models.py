from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    room_id = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)
 

#new_dialog = type('Message', (models.Model,), {'__module__': 'messenger.models'})
