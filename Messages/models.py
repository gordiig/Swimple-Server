from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    text = models.CharField(max_length=10000, null=False)
    user_from = models.ForeignKey(User, related_name='from_user', on_delete=models.DO_NOTHING)
    user_to = models.ForeignKey(User, related_name='to_user', on_delete=models.DO_NOTHING)
    when_sended = models.DateTimeField(null=False, auto_now_add=True)
    is_read = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'Message_{self.id}'
