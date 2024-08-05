from rest_framework import serializers
from .models import Cabeceraventas, Detalleventas
from clientesApp.models import Cliente
from productosApp.models import Producto
from ventasApp.models import Cabeceraventas, Detalleventas

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'valorventa', 'porcentajeiva']
        
class DetalleVentaSerializer(serializers.ModelSerializer):
    productocodigo  = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = Detalleventas
        fields = ['productocodigo', 'valorproducto', 'iva']

class CabeceraVentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True, write_only=True)  # Incluir detalles en la respuesta
    cliente = serializers.CharField()    
    class Meta:
        model = Cabeceraventas
        fields = ['consecutivo','fecha', 'cliente', 'totalventa', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        cliente_cedula = validated_data.pop('cliente')
        
        print("cliente_cedula", cliente_cedula)
        
        try:
            cliente = Cliente.objects.get(cedula=cliente_cedula)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError({"cliente": "Cliente no encontrado."})
        
        
        cabecera = Cabeceraventas.objects.create(cliente=Cliente.objects.get(cedula=cliente), **validated_data)
        
        # Crear los detalles asociados con la cabecera
        for detalle_data in detalles_data:
            
             print("Datos detalle_data:", detalle_data['productocodigo'])
            
             producto_instance = detalle_data['productocodigo']
             print("Datos producto_instance:", producto_instance)
             
             Detalleventas.objects.create(
                ventaconsecutivo=cabecera,
                productocodigo=producto_instance,
                valorproducto=detalle_data['valorproducto'],
                iva=detalle_data['iva']
            )
                
        return cabecera