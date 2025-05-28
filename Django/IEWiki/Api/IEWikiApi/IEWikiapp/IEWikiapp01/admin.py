from django.contrib import admin
from .models import Jugador, Equipo, Videojuego, VideojuegoEquipo, User
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Videojuego)
admin.site.register(VideojuegoEquipo)
admin.site.register(User)

