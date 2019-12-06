from django.urls import path 
from . import views 

urlpatterns = [ 
    path('',views.index,name='index'),
    path('carrete/',views.carrete,name='carrete'),
    path('register/',views.register,name='register'),
    path('cotizacion/',views.ListacotizacionVista,name='cotizacion'),
    path('login_view/',views.login_view, name='login_view'),
    path('logout_view/',views.logout_view, name='logout_view'),
]

urlpatterns+= [ 
    path('cotizacion/create',views.cotizacionCreate.as_view(),name='cotizacion_create'), 
    path('cotizacion/<pk>/update',views.cotizacionUpdate.as_view(),name='cotizacion_update'),
    path('cotizacion/<pk>/delete',views.cotizacionDelete.as_view(),name='cotizacion_delete'),


]

