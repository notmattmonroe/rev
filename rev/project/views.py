import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from .models import *

class ProjectIndexView(generic.ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projectindex'
    queryset = Project.objects.order_by('-date')[:10]


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name  = 'project'