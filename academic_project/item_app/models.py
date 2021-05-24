from django.core.validators import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# This method validates that the user rating is a positive decimal number and it is not greater than 5 (maximum).
# @author David Pizzolongo
def checkRating(rating):
    if rating < 0:
        raise ValidationError("Rating can only be a positive number.")
    if rating > 5:
        raise ValidationError("Rating cannot exceed 5 stars.")

# The Project model contains projects published by a member.
# Its entities include the member's name, project name, type, keyword_list and status, as well as
# other optional fields.
# @author Yassine Ibhir/David Pizzolongo
class Project(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Member')
    avg_rating = models.DecimalField(default=0, decimal_places=1, max_digits=2, validators=[checkRating])
    likes = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=40)
    project_type = models.CharField(max_length=35)
    keyword_list = models.CharField(max_length=30)
    description = models.TextField(max_length=60, blank=True)
    url = models.URLField(blank=True)
    status = models.CharField(max_length=15, help_text="Ex: Started, In Progress or Completed")
    post_date = models.DateTimeField(default=timezone.now)
    snapshot = models.ImageField(upload_to='project_images', default='project_default_pic.png')

    def __str__(self):
        # returns the project's name as its identifier
        return self.name
