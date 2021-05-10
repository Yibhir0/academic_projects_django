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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
