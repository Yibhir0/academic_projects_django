from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Yassine Ibhir
# Member model which inherits all the field from the User class
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='member_images', default='member_default_pic.png', null=True,
                                        blank=True)

