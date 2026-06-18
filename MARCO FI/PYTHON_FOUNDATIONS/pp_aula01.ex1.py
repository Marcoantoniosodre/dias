#Autor: Marco antonio


import requests

url= ' https://economia.awesomeapi.com.br/last/USD-BRL'
resposta = requests.get(url)
dados = resposta.json()

valor_dolar = dados['USDBRL']['bid']
print(f'cotação do dolar: {valor_dolar}')