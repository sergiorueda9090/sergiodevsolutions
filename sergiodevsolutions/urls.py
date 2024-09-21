"""
URL configuration for sergiodevsolutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('',            include(('bases.urls',       'bases'),          namespace='bases')),
    path('blogdetails/',include(('blogdetails.urls', 'blogdetails'),    namespace='blogdetails')),
    path('ecommerce',   include(('blogdetails.urls', 'ecommerce'),      namespace='ecommerce')),
    path('corporativa', include(('blogdetails.urls', 'corporativa'),    namespace='corporativa')),
    path('aws',         include(('blogdetails.urls', 'aws'),            namespace='aws')),
    path('software',    include(('blogdetails.urls', 'aws'),            namespace='software')),
    path('api',         include(('blogdetails.urls', 'api'),            namespace='api')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
