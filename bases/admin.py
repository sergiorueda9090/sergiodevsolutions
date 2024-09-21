from django.contrib import admin
from .models        import HomePage

# Register your models here.
# Registrar DetailPage en el admin
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'slug')  # Muestra columnas en la lista de objetos


# Registrar los modelos
admin.site.register(HomePage, HomePageAdmin)