from django.core.validators import ValidationError
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# This method validates that the user rating is a positive decimal number and it is not greater than 5 (maximum).
# @author David Pizzolongo
def checkRating(rating):
    if rating < 0:
        raise ValidationError("Rating can only be a positive number.")
    elif rating > 5:
        raise ValidationError("Rating cannot exceed 5 stars.")

# The Project model contains projects published by a member.
# Its entities include the member's name, project name, type, keyword_list and status, as well as
# other optional fields.
# @author Yassine Ibhir/David Pizzolongo
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

    # could we use get_absolute_url???

# The Comment class holds the foreign key entities from the Project and User models,
# and a comment field that holds the user's message. The __str__ method
# displays the member's name.
# @author David Pizzolongo
class Comment(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    member_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # returns the member's name
        return str(self.member_name)
