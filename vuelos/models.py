from django.db import models

class Aerolinea(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    codigo_vuelo = models.CharField(max_length=10)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE, related_name='vuelos')

    def __str__(self):
        return self.codigo_vuelo
