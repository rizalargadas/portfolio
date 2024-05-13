from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'project/projects.html', {'projects': projects, 'page_obj': page_obj})


@login_required
def add_project(request):
    print("POST: ", request.POST)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project was added successfully.")
            return redirect('projects')
        else:
            messages.error(request, "Invalid input.")
    else:
        form = ProjectForm()
    return render(request, 'project/add_project.html', {'form': form})
