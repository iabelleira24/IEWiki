from enum import unique

from django.db import models

class Equipo(models.Model):
    nombreE = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    entrenador2 = models.CharField(max_length=100, null=True)
    imagen = models.CharField(max_length=500)


    def __str__(self):
        return self.nombreE

class Jugador(models.Model):
    nombreJ = models.CharField(max_length=100)
    posicionJ = models.CharField(max_length=50)
    supertecnicaJ = models.CharField(max_length=100)
    equipoJ = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    imagenJ = models.CharField(max_length=500)


    def __str__(self):
        return self.nombreJ

class Videojuego(models.Model):

    class PlataformaChoices(models.TextChoices):
        NDS = 'NDS', 'Nintendo DS'
        N3DS = 'N3DS', 'Nintendo 3DS'
        WII = 'WII', 'Nintendo Wii'

    nombreVideojuego = models.CharField(max_length=200)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    plataforma = models.CharField(
        max_length=5,
        choices=PlataformaChoices.choices,

    )

    def __str__(self):
        return self.nombreVideojuego




class VideojuegoEquipo(models.Model):

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)

    def __str__(self):
        return "equipo" + str(self.equipo) + "videojuego" + str(self.videojuego)





class User(models.Model):

    username = models.CharField(max_length=50, unique= True)
    password = models.CharField(max_length=130)
    tokenSessions =  models.CharField(max_length=64, blank=True, null=True)




    def __str__(self):
        return str(self.username)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'jugador')


class Supertecnica (models.Model):

    nombre = models.CharField (max_length=50)
    descripcion = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre



