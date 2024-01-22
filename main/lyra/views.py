from django.shortcuts import render
from .models import Project

def home(request):

    projects = Project.objects.all()

    context = {
        "projects": projects,
    }

    return render(request, "lyra/home.html", context)

def show_data(request):
    pass

def generate_data(start, end):
    pass
