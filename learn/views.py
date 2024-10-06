import html
from django.shortcuts import render
from .models  import Lear
# Create your views here.
def Learn(request):
    steps = Lear.objects.all()
    for step in steps:
        step.description = html.unescape(step.description)
    context = {"steps":steps}
    return render(request, 'django.html', context)