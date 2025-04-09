"""
URL configuration for IEWikiapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from IEWikiapp01.endpoints import json_1, json_2, json_3, json_4, json_5, json_6, juego_1, juego_2, juego_3, juego_4, pregunta_1, pregunta_2, pregunta_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json-1/', json_1),
    path('json-2/', json_2),
    path('json-3/', json_3),
    path('json-4/', json_4),
    path('json-5/', json_5),
    path('json-6/', json_6),
    path ('juego-1/<precio>/', juego_1 ,name='juego'),
    path('juego-2/<int:id>/<precio>', juego_2, name='juego'),
    path('juego-3/<precio>/', juego_3, name='juego'),
    path('juego-4/<int:id>/', juego_4, name='juego'),
    path ('pregunta-1/', pregunta_1),
    path ('pregunta-2/<personaje>/', pregunta_2),
    path ('pregunta-3/', pregunta_3),


]
