from django.shortcuts import render
from rest_framework import viewsets
from .models import Cabeceraventas, Detalleventas
from .serializers import CabeceraVentaSerializer, DetalleVentaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status



# Create your views here.
class VentaViewSet(viewsets.ModelViewSet):
    queryset = Cabeceraventas.objects.all().prefetch_related('detalles', 'detalles__productocodigo')
    serializer_class = CabeceraVentaSerializer

    @action(detail=False, methods=['post'])
    def create_venta(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Usar el método create del serializador para crear la venta
            cabecera = serializer.save()
            # Devolver una respuesta adecuada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Devolver un error si los datos no son válidos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DetalleVentaViewSet(viewsets.ViewSet):
    def list(self, request):
        consecutivo = request.query_params.get('consecutivo')
        if not consecutivo:
            return Response({"detail": "Consecutivo no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            detalles = Detalleventas.objects.filter(ventaconsecutivo__consecutivo=consecutivo)
        except Cabeceraventas.DoesNotExist:
            return Response({"detail": "Venta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetalleVentaSerializer(detalles, many=True)
        return Response(serializer.data)