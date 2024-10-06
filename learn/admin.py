from django.contrib import admin
from .models import Lear

# Register your models here.
class LearnPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'command')
    

admin.site.register(Lear, LearnPageAdmin)