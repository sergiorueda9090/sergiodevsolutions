from django.shortcuts import render
from django.views     import generic
from .models          import HomePage

from django.core.serializers import serialize

# Create your views here.
def Home(request):
    pages = HomePage.objects.all()
    json_data = serialize('json', pages)
    print(json_data)
    return render(request, 'home.html', {"pages":pages})

    
