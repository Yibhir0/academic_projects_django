from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.contrib import messages as django_messages


# Lists all users and add an attribute as number of
# unread messages sent to the current user. This will be used a notice.
# @author Yassine Ibhir
class UserMessageListView(LoginRequiredMixin, ListView):
    Model = User
    template_name = 'message_app/user_list_message.html'
    context_object_name = 'users_list'

    # we get all users except the login one.
    def get_queryset(self):
        login_user = self.request.user
        users = User.objects.exclude(id__exact=login_user.id)
        # call helper method to add the number of unread msgs.
        users_with_msgs_num = appendNumberOfMsgs(users, login_user)
        return users_with_msgs_num


# This methods access the Message model
# to get the numbers of unread messages
# and then appends it to the list and returns it
# @author Yassine Ibhir
def appendNumberOfMsgs(users, login_user):
    users_with_num_messages = []
    for u in users:
        # we get all messages between login_user and the receiver
        users_messages = Message.objects.filter(Q(receiver=login_user, sender=u))
        # we count the number of unread messages
        num_of_unread_msg = users_messages.filter(is_read=False).count()
        # we add the attribute if it's not 0
        if num_of_unread_msg > 0:
            u.un_read = num_of_unread_msg
            users_with_num_messages = [u] + users_with_num_messages
        # no need to add zero
        else:
            users_with_num_messages = users_with_num_messages + [u]

    return users_with_num_messages


# @ Yassine Ibhir
# this function returns a json response containing
# the number of unread messages for the logged in user.
def getUnreadMsgs(request):
    users_messages = Message.objects.filter(Q(receiver=request.user))
    # we count the number of unread messages
    num_of_unread_msg = users_messages.filter(is_read=False).count()

    context = {"unread_msgs": num_of_unread_msg}

    return JsonResponse(context, safe=False)


# Yassine Ibhir
# This method handles the communication between
#  the logged in member and all registered members
#  any chats between 2 users will have a room and
#  that room will be identified by the id of the
#  member that the logged in user will chat with.

@login_required
def UserToUserMessageRoom(request, pk):
    # we get the user the logged in-member wants to chat with
    alternate_user = get_object_or_404(User, pk=pk)
    # we get all messages that the current member
    # receives from the user attached to the room
    users_messages = Message.objects.filter(
        Q(receiver=request.user, sender=alternate_user)
    )
    # since the user enters the room, we set is_read = true
    users_messages.update(is_read=True)
    # we unified the messages from both sides
    users_messages = users_messages.union(Message.objects.filter(Q(receiver=alternate_user, sender=request.user)))
    # descending order
    users_messages = users_messages.order_by('-msg_date')
    # handles the message send button
    if request.method == 'POST':
        # using the message form
        message_form = MessageForm(request.POST)
        # if everything is good, we add the message to the model
        # and redirect to the contact/messages page with a success django message
        if message_form.is_valid():
            message = message_form.cleaned_data.get('message')
            newMessage = Message.objects.create(sender=request.user, receiver=alternate_user, message=message)
            django_messages.success(request,
                                    'Message sent to {0} '.format
                                    (alternate_user.first_name + ' ' + alternate_user.last_name))

        else:
            django_messages.error(request,
                                  'Could not send message to  {0} '.format
                                  (alternate_user.first_name + ' ' + alternate_user.last_name))

        return redirect(newMessage.get_absolute_url())
    # no post request
    else:
        message_form = MessageForm()
    # renders all users messages with the form
    # and the user attached to the room
    template_name = "message_app/message_room.html"
    context = {"msgs": users_messages, "alternate_user": alternate_user, "message_form": message_form}
    return render(request, template_name, context)
