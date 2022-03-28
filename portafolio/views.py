from django.shortcuts import render
from .models import Project #importar modelos 

# Create your views here.
def home(request):
    proyectos = Project.objects.all()

    return render(request, 'home.html',{'proyectos':proyectos})
