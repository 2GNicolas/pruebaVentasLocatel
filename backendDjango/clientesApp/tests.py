from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from productosApp.models import Cliente

class ClienteAPITestCase(APITestCase):
    
    # Se crea un cliente
    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(
            cedula='1234567890',
            nombre='John Doe',
            direccion='123 Main St',
            telefono='555-5555',
            email='john.doe@example.com'
        )
        cls.list_url = reverse('cliente-list')
        cls.detail_url = reverse('cliente-detail', kwargs={'pk': cls.cliente.cedula})

    # se listan los clientes
    def test_listar_clientes(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['cedula'], self.cliente.cedula)

    # se crea un nuevo cliente
    def test_crear_cliente(self):
        data = {
            'cedula': '0987654321',
            'nombre': 'Jane Smith',
            'direccion': '456 Elm St',
            'telefono': '555-1234',
            'email': 'jane.smith@example.com'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)
        self.assertEqual(Cliente.objects.get(cedula=data['cedula']).nombre, 'Jane Smith')

    # Se verifica que se pueda obtener la cedula del cliente
    def test_cedula_cliente(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cedula'], self.cliente.cedula)

    # se actualiza el cliente
    def test_actualizar_cliente(self):
        data = {
            'nombre': 'John Updated',
            'direccion': '789 New St',
            'telefono': '555-6789',
            'email': 'john.updated@example.com'
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nombre, 'John Updated')

    # Se elimina el cliente
    def test_eliminar_cliente(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
