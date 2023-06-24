from rest_framework import status
from rest_framework.test import APITestCase
from .models import Equipo
from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token
# Create your tests here.


class EquipoGetTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.equipo1 = Equipo.objects.create(nombre='Real Sociedad', ciudad='San Sebastián', ligas=2, champions=0)
        
    def test_equipo_get(self):
        url = f'/equipos/{self.equipo1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_equipo_get_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/equipos/{self.equipo1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EquipoCreationTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)

    def test_equipo_creation(self):
        url = '/equipos/create'
        data = {'nombre': 'Real Sociedad', 'ciudad': 'San Sebastian', 'ligas': 2, 'champions': 0 }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_equipo_creation_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = '/equipos/create'
        data = {'nombre': 'Real Sociedad', 'ciudad': 'San Sebastián', 'ligas': 2, 'champions': 0 }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EquipoDeleteTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.equipo1 = Equipo.objects.create(nombre='Real Sociedad', ciudad='San Sebastián', ligas=2, champions=0)

    def test_Equipo_delete(self):
        url = f'/equipos/delete/{self.equipo1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_Equipo_delete_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/equipos/delete/{self.equipo1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)   
        

class EquipoUpdateTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.equipo1 = Equipo.objects.create(nombre='Real Sociedad', ciudad='San Sebastián', ligas=2, champions=0)

    def test_Equipo_update(self):
        url = f'/equipos/update/{self.equipo1.id}'
        data = {'nombre': 'Real Sociedad', 'ciudad': 'San Sebastian', 'ligas': 2, 'champions': 0 }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Equipo_update_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/equipos/update/{self.equipo1.id}'
        data = {'nombre': 'Real Sociedad', 'ciudad': 'San Sebastian', 'ligas': 2, 'champions': 0 }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    
