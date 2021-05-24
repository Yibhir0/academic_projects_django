from django.urls import path

from . import views

# The message_app urls include references to a message list html page and a message room page.
# @author Yassine Ibhir
urlpatterns = [
    path('users_msgs_list/', views.UserMessageListView.as_view(), name='user-msgs'),
    path('message_room/<int:pk>/', views.UserToUserMessageRoom, name='message-room'),

    path('messages_num/', views.getUnreadMsgs, name='messages-num'),

]