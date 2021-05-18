from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import UpdateLikesForm, UpdateRatingForm
from .models import Project

from django.views.generic import ListView, DetailView


# Create your views here.

# render the home paged
def home(request):
    return render(request, 'item_app/index.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'item_app/project_list.html'
    context_object_name = 'project_list'
    paginate_by = 4

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'item_app/project_detail.html'


class searchProjectKeyWord(ListView):
    model = Project
    template_name = 'item_app/project_list.html'
    context_object_name = 'project_list'
    paginate_by = 4

    def get_queryset(self):
        keyword_text = self.request.GET.get('qry-search')
        projects = Project.objects.filter(keyword_list__icontains=keyword_text)
        print(projects)
        if len(projects) > 0:
            return projects
        else:
            return Project.objects.all()

def updateLikes(request):
    if request.method == "POST":
        update_create_form = UpdateLikesForm(request.POST)
        if update_create_form.is_valid():
            project_id = update_create_form.cleaned_data['id']
            new_likes = update_create_form.cleaned_data['likes']

            updated_post = Project.objects.filter(id=project_id).update(likes=new_likes)
            success_msg = "Successfully updated likes on project " + project_id + "!"
            messages.success(success_msg)
            return redirect('update_likes/<int:pk>')
    # user not logged in
    return redirect('user_login')

def updateRating(request):
    if request.method == "POST":
        update_create_form = UpdateRatingForm(request.POST)
        if update_create_form.is_valid():
            project_id = update_create_form.cleaned_data['id']
            new_rating = update_create_form.cleaned_data['avg_rating']

            updated_post = Project.objects.filter(id=project_id).update(avg_rating=new_rating)
            success_msg = "Successfully updated rating on project " + project_id + ", author will be happy!"
            messages.success(success_msg)
            return redirect('update_rating/<int:pk>')
    # user not logged in or registered
    return redirect('user_login')

# def projects_list(request):
#     all_projects = Project.objects.all()
#     context = {'projects_list': all_projects}
#     return render(request, 'item_app/all_projects.html', context)
#
#
# def project_detail(request, id):
#     try:
#         project = Project.objects.get(pk=id)
#     except Project.DoesNotExist:
#         raise Http404("Project does not exist")
#     return render(request, 'item_app/project_detail.html', {'project': project})
