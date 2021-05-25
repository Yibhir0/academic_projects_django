# from datetime import timezone
#
# from django.contrib.admin.models import LogEntry
# from django.db import models
# from django.core.validators import RegexValidator
# from django.contrib.auth.models import User, Group
# from item_app.models import Project
# from django.contrib.auth.models import Permission, User
# from django.contrib.contenttypes.models import ContentType
#
# # Permissions and Authorization
# def add_groups():
#     list_groups = ['members', 'admin_gp', 'admin_user_gp', 'admin_Item_gp']
#     for group in list_groups:
#         groupObj = Group.objects.get_or_create(name = group)
#         set_permissions(groupObj, group)
#
# def set_permissions(groupObj, group_name):
#     content_type = ContentType.objects.get_for_model(Project)
#     if group_name == "members":
#         permission = Permission.objects.create(codename='can_add_project',
#                                                name='Can add project',
#                                                content_type=content_type)
#         permission = Permission.objects.create(codename='can_delete_project',
#                                                name='Can add project',
#                                                content_type=content_type)
#         groupObj.permissions.add(permission)
#
# def add_to_group(userid):
#     msg = "User successfulled added to group"
#     admin = Administration()
#     admin.set_values()
#     logs = LogEntry.objects.log_action(user_id=us)objects.all()
#     for l in logs:
#     # perform action
#
# # @author David Pizzolongo
# class LogEntry(models.Model):
#     log_msg = models.TextField(max_length=150, editable=False, default=self.__msg)
#     date = models.DateTimeField(editable=False, default=timezone.now)
#
#
