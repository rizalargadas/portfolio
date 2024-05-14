from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'overview', 'description', 'project_image',
                  'tags', 'live_link', 'source_link', 'is_featured']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
