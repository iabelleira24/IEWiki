from django.contrib import admin
from .models import Jugador, Equipo, Videojuego, VideojuegoEquipo
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Videojuego)
admin.site.register(VideojuegoEquipo)
