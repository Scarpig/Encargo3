"""vuelo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin 
from django.urls import path 
from django.urls import include 
from django.conf.urls.static import static
from django.conf import settings 
from destinos.views import ListacotizacionVista,cotizacionCreate,cotizacionDelete,cotizacionUpdate
urlpatterns = [ 
    path ('admin/', admin.site.urls), 
    # path ('destinos/', include('destinos.urls')), 
    path ('cotizaciones/create', cotizacionCreate.as_view(), name='create_cotizacion'), 
    path ('cotizacion/<pk>/update', cotizacionUpdate.as_view()), 
    path ('cotizacion/<pk>/delete', cotizacionDelete.as_view()),
    path('',include('destinos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
