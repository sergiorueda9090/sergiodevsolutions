from django.urls import path
from blogdetails.views import DetailPageListView, BlogDetails

app_name = 'blogdetails'

urlpatterns = [
    path('',              DetailPageListView.as_view(),   name='detailpage_list'),
    path('<slug:slug>/',  BlogDetails,          name="blogdetails"),
]