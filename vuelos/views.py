from rest_framework import viewsets, filters
from .models import Vuelo, Aerolinea
from .serializers import VueloSerializer, AerolineaSerializer

class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo_vuelo', 'origen', 'destino']
