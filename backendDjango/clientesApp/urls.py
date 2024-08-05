from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
