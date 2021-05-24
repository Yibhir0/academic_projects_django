from django.contrib import admin

from .models import Comment, Message
admin.site.register(Comment)
admin.site.register(Message)