from django.db import models
from django.urls import reverse
from django.utils import timezone
from item_app.models import Project
from django.contrib.auth.models import User


# The Comment class defines the attributes corresponding to the project. This includes
# the comment itself and the date.
# @author Yassine Ibhir/David Pizzolongo
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']


# The Message class contains entities representing the user who sent the message,
# the user who received the message, the message description, the status of the message,
# as well as the date and time of the message.
# @author Yassine Ibhir/David Pizzolongo
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="msg_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="msg_receiver", on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    msg_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('message-room', kwargs={'pk': self.receiver.id})

    # orders by msg_date in decreasing order (most recent to oldest).
    class Meta:
        ordering = ['-msg_date']
