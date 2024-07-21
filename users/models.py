# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

#  CustomUser model
class CustomUser(AbstractUser):
    pass  

###########################



class Interest(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_interests', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)



#########################3


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
