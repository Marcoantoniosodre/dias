#Autor: Marco antonio


import requests


cep = input('Digite o seu cep: ')
url = f'https://viacep.com.br/ws/{cep}/json/'
resposta = requests.get(url)
dados= resposta.json()


print(f" Logradouro: {dados['logradouro']}")
print(f' Bairro: {dados['bairro']}')
print(f' Cidade: {dados['localidade']}')
print(f' Estado: {dados['uf']}')