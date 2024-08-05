from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto

class ProductoAPITestCase(APITestCase):
    
    @classmethod
    def setUp(self):
        
        # se crea un producto de prueba
        self.producto = Producto.objects.create(
            codigo='PROD001',
            nombre='Producto A',
            valorventa=1000,
            isiva=True,
            porcentajeiva=19
        )
        self.productos_url = reverse('producto-list')  # URL para listar productos
        self.producto_url = reverse('producto-detail', args=[self.producto.codigo])  # URL para detalles de un producto

    # se crea un nuevo dato de producto
    def test_crear_producto(self):
        new_producto_data = {
            'codigo': 'PROD002',
            'nombre': 'Producto B',
            'valorventa': 2000,
            'isiva': False,
            'porcentajeiva': 0
        }
        response = self.client.post(self.productos_url, new_producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 2)  # Verifica que el número total de productos ha aumentado
        self.assertEqual(Producto.objects.get(codigo='PROD002').nombre, 'Producto B')

    # probamos que podamos obtener un producto
    def test_obtener_producto(self):
        response = self.client.get(self.producto_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.producto.nombre)
        self.assertEqual(response.data['valorventa'], self.producto.valorventa)

    # actualizamos un prodcuto
    def test_actualizar_producto(self):
        updated_data = {
            'nombre': 'Producto A Actualizado',
            'valorventa': 1500,
            'isiva': False,
            'porcentajeiva': 0
        }
        response = self.client.patch(self.producto_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, updated_data['nombre'])
        self.assertEqual(self.producto.valorventa, updated_data['valorventa'])

    # eliminamos un producto
    def test_eliminar_producto(self):
        response = self.client.delete(self.producto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Producto.objects.filter(codigo=self.producto.codigo).exists())
