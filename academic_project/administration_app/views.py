from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render
from .models import Member

from django.views import generic


# Create your views here.

# render the home page
def home(request):
    return render(request, 'administration_app/index.html')


class MemberLoginListView(generic.ListView):
    template_name = 'administration_app/admin_login.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        return Member.objects.all()

