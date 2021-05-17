from django.http import Http404
from django.shortcuts import render
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
