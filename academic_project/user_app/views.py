from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetDoneView, PasswordResetCompleteView)

from django.shortcuts import render
from .forms import UserRegistrationForm, MemberFileForm, MemberUpdateForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# validates and registers user
# @author Yassine Ibhir
def register(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        file_form = MemberFileForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            new_customer = User.objects.get(username=username)

            if file_form.is_valid():
                profile_image = file_form.cleaned_data.get('profile_picture')
                customer_profile = Member.objects.create(profile_picture=profile_image, user=new_customer)
            else:
                customer_profile = Member.objects.create(user=new_customer)

            customer_profile.save()
            messages.success(request, 'Congratulations {0}, You are registered'.format(username))

            members_group = Group.objects.get(name='members')
            members_group.user_set.add(new_customer)
            return redirect('user-login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:

        register_form = UserRegistrationForm()
        file_form = MemberFileForm()
    template_name = 'user_app/register.html'
    context = {'register_form': register_form, 'file_form': file_form}
    return render(request, template_name, context)


# Inherits from LoginView and SuccessMessageMixin
# to login a user and provide a message
# @author Yassine Ibhir
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'user_app/login.html'
    success_message = 'You are logged in, Welcome.'


# Inherits from LogoutView and overrides dispatch to add a message
# when user is logged out
# @author Yassine Ibhir
class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, 'You are logged out, GoodBye.')
        return response


# using PasswordResetDone View we will create our own class
# to override dispatch method to add a message.
# @author Yassine Ibhir
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user_app/password_reset_done.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, 'Check your email and follow the instructions to reset your password.')
        return response


# using PasswordResetCompleteView we will create our own class
# that displays a message to the user.
# @author Yassine Ibhir
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user_app/password_reset_complete.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, 'You have successfully reset you password')
        return response


#  member's profile view
# @author Yassine Ibhir
@login_required(login_url='/user_app/user_login/')
def viewProfile(request):
    template_name = 'user_app/profile.html'
    context = {'user': request.user}
    return render(request, template_name, context)


# Update member profile
# @author Yassine Ibhir
@login_required(login_url='/user_app/user_login/')
def updateProfile(request):
    if request.method == 'POST':
        update_form = MemberUpdateForm(request.POST, instance=request.user)
        file_form = MemberFileForm(request.POST, request.FILES, instance=request.user.member)

        if update_form.is_valid():
            update_form.save()
            if file_form.is_valid():
                file_form.save()
            messages.success(request, 'You successfully updated your profile')
            return redirect('user-profile')
        else:
            messages.error(request, "Invalid information.Try again")

    else:
        update_form = MemberUpdateForm(instance=request.user)
        file_form = MemberFileForm(instance=request.user.member)

    template_name = 'user_app/update_profile.html'
    context = {'update_form': update_form, 'file_form': file_form}
    return render(request, template_name, context)
