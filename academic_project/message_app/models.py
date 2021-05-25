from django.db import models
from django.utils import timezone
from item_app.models import Project
from django.contrib.auth.models import User


# Create your models here.
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


# This class represents the Message model
# and its attributes
# @author Yassine Ibhir
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="msg_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="msg_receiver", on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    msg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-msg_date']
