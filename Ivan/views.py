from django.shortcuts import render
from .models import Project, Skill, About

def portfolio_home(request):
    """Display portfolio home page with featured projects"""
    projects = Project.objects.all()
    skills = Skill.objects.all()
    about = About.objects.first()
    
    context = {
        'projects': projects,
        'skills': skills,
        'about': about,
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, pk):
    """Display detailed view of a single project"""
    project = Project.objects.get(pk=pk)
    related_projects = Project.objects.exclude(pk=pk)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)


def projects_list(request):
    """Display all projects"""
    projects = Project.objects.all()
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category:
        projects = projects.filter(technologies__icontains=category)
    
    context = {
        'projects': projects,
        'category': category,
    }
    return render(request, 'portfolio/projects_list.html', context)


def skills_view(request):
    """Display all skills organized by category"""
    skills = Skill.objects.all()
    categories = Skill.objects.values_list('category', flat=True).distinct()
    
    context = {
        'skills': skills,
        'categories': categories,
    }
    return render(request, 'portfolio/skills.html', context)
