from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .forms import UserRegistrationForm, MemberFileForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Member


# Yassine Ibhir
# validate and register user
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
            messages.success(request, 'Gongratulations {0}, You are registered'.format(username))
            return redirect('user-login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:

        register_form = UserRegistrationForm()
        file_form = MemberFileForm()
    template_name = 'user_app/register.html'
    context = {'register_form': register_form, 'file_form': file_form}
    return render(request, template_name, context)


# Yassine Ibhir
# Inherits from LoginView and SuccessMessageMixin
# to login a user and provide a message
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'user_app/login.html'
    success_message = 'You are logged in, Welcome.'


# Yassine Ibhir
# Inherits from LogoutView and overides dispatch to add a message when user is logged out
# to logout a user and provide a message
class UserLogoutView(LogoutView):
    template_name = 'user_app/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, 'You are logged out, GoodBye.')
        return response
