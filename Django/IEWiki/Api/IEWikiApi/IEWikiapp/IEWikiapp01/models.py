from django.db import models

class Equipo(models.Model):
    nombreE = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreE

class Jugador(models.Model):
    nombreJ = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    supertecnica = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

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