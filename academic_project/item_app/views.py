from urllib import request
from django.contrib import messages
from django.shortcuts import render
from .models import Project
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Yassine Ibhir
# render the home page
def home(request):
    return render(request, 'item_app/index.html')


# Yassine Ibhir
# Class based view that handles the Project list using pagination.
# Note that we don't need to override the get_queryset since
# ListView returns all the objects in the model but we are doing it
# to sort by date in desc order.

class ProjectListView(ListView):
    model = Project
    template_name = 'item_app/project_list.html'
    context_object_name = 'project_list'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.all().order_by('-post_date')


# Yassine Ibhir
# Class based view that handles the view of one project.
# all we need to do is pass the primary key with the url when user
# clicks the project and the rest is handled by Django DetailView class.

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'item_app/project_detail.html'


# Yassine Ibhir
# Class based View  searches based on the filter and
# the texts the user enters.

class searchProjectKeyWord(ListView):
    model = Project
    template_name = 'item_app/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):

        keyword_text = self.request.GET.get('qry-search', '')
        option_text = self.request.GET.get('options', 'keyword')
        projects = Project.objects.all()
        if len(keyword_text) == 0:
            messages.error(self.request, 'Provide a text to search for')
            return projects
        if option_text == 'keyword':
            projects = projects.filter(keyword_list__icontains=keyword_text).order_by('-post_date')
        elif option_text == 'name':
            projects = projects.filter(name__icontains=keyword_text).order_by('-post_date')
        # owner's name
        else:
            projects = projects.filter(member__username__icontains=keyword_text).order_by('-post_date')

        if len(projects) > 0:
            messages.success(self.request, 'Found {0}, matching'.format(len(projects)))
            return projects
        else:
            messages.warning(self.request, 'Search did not match any text {0}'.format(keyword_text))
            return projects


# Yassine Ibhir
# Class based View  searches and renders projects of the logged in user

class searchMemberProjectKeyWord(ListView):
    model = Project
    template_name = 'item_app/memberProject_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):

        keyword_text = self.request.GET.get('qry-search')
        option_text = self.request.GET.get('options')
        login_member = self.request.user
        projects = Project.objects.filter(member=login_member).order_by('-post_date')

        if len(keyword_text) == 0:
            messages.error(self.request, 'Provide a text to search for')
            return projects
        if option_text == 'keyword':
            projects = projects.filter(keyword_list__icontains=keyword_text).order_by('-post_date')
        else:
            projects = projects.filter(name__icontains=keyword_text).order_by('-post_date')

        if len(projects) > 0:
            messages.success(self.request, 'Found {0}, matches'.format(len(projects)))
        else:
            messages.warning(self.request, 'Search did not match any text {0}'.format(keyword_text))
        return projects


# Yassine Ibhir
# Class based view that handles the authenticated-user's
# Project list using pagination.

class ProjectMemberListView(ListView):
    model = Project
    template_name = 'item_app/memberProject_list.html'
    context_object_name = 'project_list'
    paginate_by = 6

    def get_queryset(self):
        login_member = self.request.user
        member_projects = Project.objects.filter(member=login_member).order_by('-post_date')
        return member_projects


# Yassine Ibhir

# saves and provides form for adding Project (CreateView)
# it requires login and redirects to project-list or
# login pages based on user authentication(LoginRequiredMixin).
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    # create form with these fields
    fields = ['name', 'project_type', 'keyword_list',
              'description', 'url', 'status', 'snapshot']
    # template that will receive the form and display it
    template_name = 'item_app/project_form.html'

    # url to go to when user is not authenticated(login)
    login_url = '/user_app/user_login/'

    # name space of the path
    redirect_field_name = 'user-login'

    # go to member project-list when successfully added a project
    success_url = reverse_lazy('memberProject-list')

    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)  # our form will contain the authenticated user

    # passing context to use inside the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['legend'] = 'Create Project'
        context['btn'] = 'Add Project'
        return context


# Yassine Ibhir
# saves and provides form for updating Project
# it requires login and also verifies that the user
# is the one who created the post before updating. This is all done by
# the base classes that we inherit from.

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    # create form with these fields
    fields = ['name', 'project_type', 'keyword_list',
              'description', 'url', 'status', 'snapshot']
    # template that will receive the form and display it
    template_name = 'item_app/project_form.html'

    # url to go to when user is not authenticated(login)
    login_url = '/user_app/user_login/'

    # name space of the path
    redirect_field_name = 'user-login'

    # go to member project-list when successfully updated a project
    success_url = reverse_lazy('memberProject-list')

    # we override this function to check if the roject will be updated by the right user
    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)  # our form will contain the authenticated user

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.member

    # passing context to use inside the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['legend'] = 'Update Project'
        context['btn'] = 'Save Project'
        return context


# Yassine Ibhir
# deletes project
# it requires login and also verifies that the user
# is the one who created the post before deleting.

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project

    # template that will receive the form and display it
    template_name = 'item_app/project_confirm_delete.html'

    # go to member project-list when successfully deleted a project
    success_url = reverse_lazy('memberProject-list')

    # we override this function to check if the project will be deleted by the right user
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.member

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
