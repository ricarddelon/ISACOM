"""ISA_COM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import serve
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.authentication.urls')),
    path('', include('apps.home.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('compras/', include('apps.ventas_compras.compras.urls')),
    path('ventas/', include('apps.ventas_compras.ventas.urls')),
    path('almacenes/', include('apps.almacen.urls')),
    path('finanzas/', include('apps.finanzas.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
