from django.shortcuts import render
from .forms import UserRegistrationForm, MemberFileForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Member


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
        register_form = UserRegistrationForm()
        file_form = MemberFileForm()
    template_name = 'user_app/register.html'
    context = {'register_form': register_form, 'file_form': file_form}
    return render(request, template_name, context)
