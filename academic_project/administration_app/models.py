from django.db import models
from django.core.validators import RegexValidator

# The Member class sets the attributes for fullname, profession, group, status (inaccessible to normal user),
# profile_pic and achievement_list.
# @author David Pizzolongo
class Member(models.Model):
    # Member.project = models.ForeignKeyField(Project)
    fullname = models.CharField(
        max_length=35,
        help_text="Enter your name: ",
        # validator used when the admin or a privileged group adds a new member
        validators=[
            RegexValidator(
                regex="^[A-Za-z\\s]+$",
                message="Invalid name, must only contain letters and spaces.",
            ),
        ])
    profession = models.CharField(max_length=25, help_text="Enter your job: ", blank=True)
    # group = models.CharField(max_length=40, default="members")
    status = models.CharField(editable=False, max_length=15, default="Active", help_text="Enter current status (reserved to admin): ")
    profile_pic = models.ImageField(upload_to='member_images', default='member_default_pic.png')
    achievement_list = models.TextField(max_length=100, help_text="Enter academic achievements: ", blank=True)

    def __str__(self):
        # id is unique
        return "Member " + str(self.id)