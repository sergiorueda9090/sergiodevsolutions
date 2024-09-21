import html
from django.shortcuts import render, get_object_or_404
from django.views     import generic
from .models          import DetailPage, BenefitsPage

# Create your views here.
def BlogDetails(request, slug):
    # Obtener la página de detalles usando el slug
    detail_page = get_object_or_404(DetailPage, slug=slug)

    # Decodificar las entidades HTML en la descripción
    benefits = detail_page.benefits.all()
    for benefit in benefits:
        benefit.description = html.unescape(benefit.description)

    # Decodificar las entidades HTML en la descripción
    services = detail_page.services.all()
    for services in services:
        services.description = html.unescape(services.description)

    context = {
        'detail_page': detail_page,
        'benefits': benefits,
        'services': services
    }
    
    return render(request, 'blogdetail.html', context)

class DetailPageListView(generic.ListView):
    model = DetailPage
    template_name = 'detailpage_list.html'
    context_object_name = 'detail_pages'


