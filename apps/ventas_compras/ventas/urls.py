from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas, name='ventas'),
    path('registro-ventas/', views.ventas_registro, name='ventas_registro'),
    path('nuevo-registro/', views.registro, name='registro'),
    path('detalles/<int:id>', views.detalles, name='detalles'),
    path('comisiones/', views.comisiones, name='comisiones'),
    path('comisiones-registro/', views.comisiones_registro, name='comisiones_registro'),
]