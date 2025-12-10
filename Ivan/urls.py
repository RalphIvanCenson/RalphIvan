from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('projects/', views.projects_list, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills_view, name='skills'),
]
