from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VueloViewSet, AerolineaViewSet

router = DefaultRouter()
router.register(r'vuelos', VueloViewSet)
router.register(r'aerolineas', AerolineaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
