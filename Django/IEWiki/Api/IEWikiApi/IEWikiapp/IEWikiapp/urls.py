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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from IEWikiapp01.endpoints import  juego_1, juego_2, juego_3, juego_4, pregunta_1, pregunta_2, pregunta_3, jugador, equipos, jugadores, jugadores_por_equipo, vecinos, presidentes, superheroes, user, sessions, like, favoritos, votar_equipo




urlpatterns = [
    path('admin/', admin.site.urls),

    path ('juego-1/<precio>/', juego_1 ,name='juego'),
    path('juego-2/<int:id>/<precio>', juego_2, name='juego'),
    path('juego-3/<precio>/', juego_3, name='juego'),
    path('juego-4/<int:id>/', juego_4, name='juego'),
    path ('pregunta-1/', pregunta_1),
    path ('pregunta-2/<personaje>/', pregunta_2),
    path ('pregunta-3/', pregunta_3),
    path ('jugadores/', jugadores),
    path ('jugadores/<id>/', jugador),
    path ('equipos/', equipos),
    path ('equipo/<int:equipo_id>/jugadores', jugadores_por_equipo),
    path ('equipo/<int:equipo_id>/upvote', votar_equipo),
    path ('vecinos/', vecinos),
    path ('presidentes/', presidentes),
    path ('superheroes/', superheroes),
    path ('user/', user),
    path ('login/', sessions),
    path ('like/', like),
    path ('favoritos/', favoritos)




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
