from django.contrib import admin
from .models import DetailPage, BenefitsPage, ServicesPage

# Registrar DetailPage en el admin
class DetailPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'titleBenefits')  # Muestra columnas en la lista de objetos

# Registrar BenefitsPage en el admin
class BenefitsPageAdmin(admin.ModelAdmin):
    list_display = ('description', 'detail_page')  # Muestra la descripción y la relación con DetailPage

# Registrar ServicesPage en el admin
class ServicesPageAdmin(admin.ModelAdmin):
    list_display = ('description', 'detail_page')  # Muestra la descripción y la relación con DetailPage

# Registrar los modelos
admin.site.register(DetailPage, DetailPageAdmin)
admin.site.register(BenefitsPage, BenefitsPageAdmin)
admin.site.register(ServicesPage, ServicesPageAdmin)