from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VentaViewSet, DetalleVentaViewSet

router = DefaultRouter()
router.register(r'ventas', VentaViewSet)
router.register(r'detalleventas', DetalleVentaViewSet, basename='detalleventas')

urlpatterns = [
    path('', include(router.urls)),
]
