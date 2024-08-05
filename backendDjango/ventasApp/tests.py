from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from productosApp.models import Cabeceraventas, Detalleventas, Cliente, Producto

class VentaAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        
        # Se crean un cliente, un producto, una venta y un detalle de venta.
        cls.cliente = Cliente.objects.create(
            cedula='1234567890',
            nombre='John Doe',
            direccion='123 Main St',
            telefono='555-5555',
            email='john.doe@example.com'
        )
        cls.producto = Producto.objects.create(
            codigo='P001',
            nombre='Producto Test',
            descripcion='Descripción del producto',
            precio=100
        )
        cls.venta = Cabeceraventas.objects.create(
            fecha='2024-08-04T12:00:00Z',
            cliente=cls.cliente,
            totalventa=500
        )
        cls.detalle = Detalleventas.objects.create(
            ventaconsecutivo=cls.venta,
            productocodigo=cls.producto,
            valorproducto=100,
            iva=19
        )
        cls.list_url = reverse('venta-list')
        cls.detail_url = reverse('venta-detail', kwargs={'pk': cls.venta.consecutivo})
        
    
    # Verifica que la lista de ventas se devuelve correctamente y que la venta creada
    # está en la lista.
    def test_listar_ventas(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['consecutivo'], self.venta.consecutivo)

    # Verifica que se puede crear una nueva venta con detalles asociados. También
    # verifica que la venta y los detalles se han creado correctamente en la base de datos.
    def test_crear_venta(self):
        data = {
            'fecha': '2024-08-05T14:00:00Z',
            'cliente': self.cliente.cedula,
            'totalventa': 300,
            'detalles_write': [
                {
                    'productocodigo': self.producto.codigo,
                    'valorproducto': 150,
                    'iva': 19
                }
            ]
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cabeceraventas.objects.count(), 2)
        self.assertEqual(Cabeceraventas.objects.latest('consecutivo').totalventa, 300)
        self.assertEqual(Detalleventas.objects.count(), 2)

    # Verifica que se puede recuperar la información de una venta usando su consecutivo.
    def test_consecutivo_venta(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['consecutivo'], self.venta.consecutivo)

    # Verifica que se puede actualizar la información de una venta. En este caso,
    # se actualiza el total de la venta.
    def test_actualizar_venta(self):
        data = {
            'totalventa': 600
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.venta.refresh_from_db()
        self.assertEqual(self.venta.totalventa, 600)

    # Verifica que se puede eliminar una venta y que la venta ya no está presente
    # en la base de datos.
    def test_eliminar_venta(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cabeceraventas.objects.count(), 0)
