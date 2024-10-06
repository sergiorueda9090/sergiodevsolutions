from django.shortcuts import render
from django.views     import generic
from .models          import HomePage
from courses.models   import Course
from django.core.serializers import serialize

# Create your views here.
def Home(request):
    pages = HomePage.objects.all()
    courses = Course.objects.all()

    return render(request, 'home.html', {"pages":pages, "courses":courses})

    
