import requests

TOKEN = "8979638987:AAHZvZGyZk1S_dAh5VSTZu4xCI28hWOFMQ4"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

resposta = requests.get(url)

print(resposta.json())