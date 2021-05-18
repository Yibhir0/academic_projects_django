from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# The Message model contains entities for the sender, the recipient, the message
# and the current datetime, which cannot be edited by the user sending the message.
# @author David Pizzolongo
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="server")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient")
    message = models.CharField(max_length=300)
    date = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        # returns the sender's name
        return "Message from " + str(self.sender)

# for showing messages, find user.username, set it to user and then do
# goodMessages = Message.objects.exclude(sender=user).filter(recipient=user)