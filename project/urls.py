from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('<str:pk>/', views.project, name='project'),
    path('<str:pk>/delete/', views.delete_project, name='delete'),
    path('<str:pk>/edit/', views.edit_project, name='edit'),
]
