from urllib import request

from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# ADD COMMENTS
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    # create form with these fields
    fields = ['username', 'email', 'first_name', 'last_name']
    # template that will receive the form and display it
    template_name = 'administration_app/user_form.html'

    # url to go to when user is not authenticated(login)
    login_url = '/user_app/user_login/'

    # name space of the path
    redirect_field_name = 'user-login'

    # go to user-list when successfully updated a user
    success_url = reverse_lazy('users-list')

    def test_func(self):
        try:
            self.request.user.groups.get(name="members")
            return False

        except ObjectDoesNotExist:
            return True

    # passing context to use inside the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['legend'] = 'Update User'
        context['btn'] = 'Save User'
        return context


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User

    # template that will receive the form and display it
    template_name = 'administration_app/user_confirm_delete.html'

    # go to users-list when successfully deleted a project
    success_url = '/admin_app/users_list/'

    def test_func(self):
        try:
            self.request.user.groups.get(name="members")

            return False

        except ObjectDoesNotExist:
            return True


class GetAllUsersList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'administration_app/users_list.html'
    context_object_name = 'users_list'
    paginate_by = 8

    def test_func(self):
        try:
            self.request.user.groups.get(name="members")
            return False

        except ObjectDoesNotExist:
            return True

    # The get_queryset() method returns the list of created users.
    def get_queryset(self):
        return setGroupNameToUsers(User.objects.all())

    # The following method adds the tab title and the total number of tasks to the list of user tasks.
    def get_context_data(self, **kwargs):
        users_tab_context = super().get_context_data(**kwargs)
        users_tab_context['tab_title'] = 'List Users'
        return users_tab_context


def setGroupNameToUsers(users):
    for u in users:
        groups = Group.objects.filter(user=u)
        if len(groups) > 0:
            group = groups[0].name
            u.group = group

    return users;
