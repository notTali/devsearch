from django.shortcuts import render
from .models import Project
# Create your views here.
def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {"project":project, 'tags':tags}
    return render(request, 'project/project.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, 'project/projects.html', context)