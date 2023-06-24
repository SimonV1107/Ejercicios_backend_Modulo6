from rest_framework import status
from rest_framework.test import APITestCase
from .models import Jugador
from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token
from equipos.models import Equipo


# Create your tests here.


class JuagadorGetTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.jugador1 = Jugador.objects.create(nombre='Jose Luis Gaya', edad='28', nacionalidad='España', posicion='Defensa', equipo='Valencia FC')
        
    def test_jugador_get(self):
        url = f'/jugadores/{self.jugador1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jugador_get_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/jugadores/{self.jugador1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class jugadorCreationTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)

    def test_jugador_creation(self):
        url = '/jugadores/create'
        data = {'nombre': 'Ansu Fati', 'edad': 20, 'nacionalidad': 'España', 'posicion': 'delantero', 'equipo': 'FCBarcelona'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_jugador_creation_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = '/jugadores/create'
        data = {'nombre': 'Ansu Fati', 'edad': 20, 'nacionalidad': 'España', 'posicion': 'delantero', 'equipo': 'FCBarcelona'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class jugadorDeleteTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.jugador1 = Jugador.objects.create(nombre='Jose Luis Gaya', edad='28', nacionalidad='España', posicion='Defensa', equipo='Valencia FC')

    def test_jugador_delete(self):
        url = f'/jugadores/delete/{self.jugador1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_jugador_delete_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/jugadores/delete/{self.jugador1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)   

class jugadorUpdateTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.jugador1 = Jugador.objects.create(nombre='Jose Luis Gaya', edad='28', nacionalidad='España', posicion='Defensa', equipo='Valencia FC')

    def test_jugador_update(self):
        url = f'/jugadores/update/{self.jugador1.id}'
        data = {'nombre': 'Ansu Fati', 'edad': 20, 'nacionalidad': 'España', 'posicion': 'delantero', 'equipo': 'FCBarcelona'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jugador_update_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/jugadores/update/{self.jugador1.id}'
        data = {'nombre': 'Ansu Fati', 'edad': 20, 'nacionalidad': 'España', 'posicion': 'delantero', 'equipo': 'FCBarcelona'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        
class JugadorApi_viewTestCase:
    def setUp(self):
            self.user = DjangoUser.objects.create_superuser(username='test', password='test')
            self.token = Token.objects.create(user = self.user)
            self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
            self.equipo1 = Equipo.objects.create(nombre='Real Sociedad', ciudad='San Sebastián', ligas=2, champions=0)

    def test_jugador_api_view(self):
        url = f'/jugadores/{self.equipo1.nombre}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jugador_api_view_no_authoritation(self):
        self.client.force_authenticate(user=None)
        url = f'/jugadores/{self.equipo1.nombre}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

