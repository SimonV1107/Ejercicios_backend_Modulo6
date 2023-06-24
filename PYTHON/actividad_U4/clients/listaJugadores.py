import requests
from getpass import getpass

endpoint ='http://localhost:8000/auth/'
username = input('Usuario: ')
password = getpass('Contraseña: ')


token_res = requests.post(endpoint, json={'username': username, 'password': password})


if token_res.status_code==200:

    token = token_res.json()['token']
    headers = {
        "Authorization": f'Token {token}'
    }
    endpoint2 ='http://localhost:8000/jugadores/create'

    response = requests.get(endpoint2, headers=headers)
    
    print(response.json())