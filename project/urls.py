from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add_project/', views.add_project, name='add_project'),
]
