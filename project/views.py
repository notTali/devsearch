from django.shortcuts import render

# Create your views here.
def project(request, pk):
    return render(request, 'project/project.html')

def projects(request):
    return render(request, 'project/projects.html')