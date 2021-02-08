from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects':projects})

def detail_portfolio(request, portfolio_id):
    project = get_object_or_404(Project, id=portfolio_id)
    return render(request, 'detail_portfolio.html', {'project':project})