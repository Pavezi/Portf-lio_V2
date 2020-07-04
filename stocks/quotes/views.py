from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'

home = ProjectListView.as_view()