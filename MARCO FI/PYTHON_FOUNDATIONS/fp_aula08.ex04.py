#Autor: Marco antonio


import requests


resposta = requests.get('url')
dados = resposta.json()

print(f'O valor do dolar é {dados["USDBRL"]["bid"]}')

dolar= float(input( ' Digite o valor do dolar: '))
url= f'http://economia.awesomeapi.com.br/json/last/USD-BRL'
