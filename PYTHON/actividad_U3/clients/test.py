import requests

endpoint ='http://localhost:8000/jugadores/1'

endpoint_add ='http://localhost:8000/jugadores/create'

endpoint ='http://localhost:8000/jugadores/FCBarcelona'


json={
    'nombre': 'Pedri',
    'edad': 22,
    'nacionalidad': 'España',
    'posicion': 'mediocampista',
    'equipo': 'FCBarcelona'
}

response = requests.get(endpoint)

print(response.json())