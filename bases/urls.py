from django.urls import path
from . import views

app_name = 'bases'

urlpatterns = [
    path('', views.Home, name="home"),
]