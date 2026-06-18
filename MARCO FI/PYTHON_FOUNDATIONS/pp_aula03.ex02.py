#Autor: Marco Antonio
#Uso de API para um buscador de CPF

import requests

cpf = '50874450802'  # Substitua pelo CPF que deseja consultar
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
    'x-api-key': 'sua_chave_de_api_aqui',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
