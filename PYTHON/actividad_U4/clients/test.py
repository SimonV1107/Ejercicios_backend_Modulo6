import requests

endpoint ='http://localhost:8000/jugadores/delete/1'

endpoint_add ='http://localhost:8000/jugadores/create'

# endpoint ='http://localhost:8000/jugadores/FCBarcelona'


json={
    'nombre': 'Borja Iglesias',
    'edad': 25,
    'nacionalidad': 'España',
    'posicion': 'delantero',
    'equipo': 'Betis'
}

response = requests.delete(endpoint)

print(response.json())