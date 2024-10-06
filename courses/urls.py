from django.urls import path
from . import views

urlpatterns = [
    path('<slug:course_slug>', views.course_detail,                     name='course'),
    path('<slug:course_slug>/<slug:step_slug>/', views.course_detail,   name='course'),
]