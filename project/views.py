from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

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


def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(projects)
    context = {'form':form}
    return render(request, 'project/add-project.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(projects)
    context = {'form':form}
    return render(request, 'project/add-project.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    if request.method == "POST":
        project.delete()
        return redirect(projects)
    return render(request, 'project/delete-project.html', context)