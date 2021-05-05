from django.http import Http404
from django.shortcuts import render
from .models import Project, Comment

from django.views import generic


# Create your views here.

# render the home page
def home(request):
    return render(request, 'item_app/index.html')


class ProjectListView(generic.ListView):
    template_name = 'item_app/all_projects.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'item_app/project_detail.html'
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
