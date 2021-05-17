from django.core.validators import ValidationError
from django.db import models
from django.utils import timezone


# This method validates that the user rating is a positive decimal number and it is not greater than 5 (maximum).
# @author David Pizzolongo
def checkRating(rating):
    if rating < 0:
        raise ValidationError("Rating can only be a positive number.")
    if rating > 5:
        raise ValidationError("Rating cannot exceed 5 stars.")

# def getDefaultRating(likes):
#     default_rating = 0
#     likesNum = int(likes)
#
#     if likesNum >= 8:
#         default_rating = 5
#     elif likesNum >= 6:
#         default_rating = 4
#     elif likesNum >= 4:
#         default_rating = 3
#     elif likesNum >= 2:
#         default_rating = 2
#     elif likesNum == 1:
#         default_rating = 1
#
#     return default_rating

# The Project class contains projects published by one or many members.
# Its entities include the project name, type, keyword_list and status, as well as
# other optional fields.
# @author Yassine Ibhir/David Pizzolongo
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(default=0, decimal_places=1, max_digits=2, validators=[checkRating])
    name = models.CharField(max_length=40)
    project_type = models.CharField(max_length=35)
    keyword_list = models.CharField(max_length=70)
    description = models.TextField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    status = models.CharField(max_length=15, help_text="Ex: Started, In Progress or Completed")
    post_date = models.DateTimeField(default=timezone.now)
    snapshot = models.ImageField(upload_to='project_images', default='project_default_pic.png')

    def __str__(self):
        # returns the project id assigned automatically
        return "Project " + str(self.id)
