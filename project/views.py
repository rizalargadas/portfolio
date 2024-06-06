from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project, Tag
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    query = request.GET.get('q', '')
    if query:
        projects = projects.filter(Q(tags__name__icontains=query))

    paginator = Paginator(projects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(f'query: {query}')
    print(f'tags: {tags}')
    context = {
        'projects': projects,
        'page_obj': page_obj,
        'tags': tags,
        'query': query
    }
    return render(request, 'project/projects.html', context)


def project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project.html', {'project': project})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project edited successfully.')
            return redirect(reverse('project', args=[pk]))
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project/edit_project.html', {'form': form})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('projects')


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
