from rest_framework import serializers
from .models import Vuelo, Aerolinea

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = '__all__'

class VueloSerializer(serializers.ModelSerializer):
    aerolinea_nombre = serializers.CharField(source='aerolinea.nombre', read_only=True)

    class Meta:
        model = Vuelo
        fields = ['id', 'codigo_vuelo', 'origen', 'destino', 'aerolinea', 'aerolinea_nombre']
