#Autor: Marco antonio


import requests

latitude= float(input(' Digite a sua latitude: '))
longitude= float(input( ' Digite a sua longitude: '))
url= f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

resposta = requests.get(url)
dados= resposta.json()

print(f'A temperatura atual é de {dados["current"]["temperature_2m"]} graus Celsius')
