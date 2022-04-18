from django.shortcuts import render
from django.http import HttpResponse as hr
from .models import Project

def about(request) :
    projects = Project.objects.all()
    return render(request,'blog/about.html',{'projects':projects})


