#Autor: Marco Antonio
#Bot do Telegram 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# Acesso do Telegram
TOKEN = "8757985347:AAHoIMLInktOTV03zgWVQtwJ5Q1jYLruSWc"
CHAT_ID = "8838918666"

# URLs dos produtos
produtos = [
    {
        "url" : "https://www.amazon.com.br/Echo-Dot-4%C2%AA-gera%C3%A7%C3%A3o-Cor-Azul/dp/B09B8QFYZ2",
        "valor_desejado" : 450
    },
    {
        "url" : "https://www.amazon.com.br/Insta360-desempenho-aprimorado-atualizadas-substitu%C3%ADveis/dp/B0F3P4G8SY",
        "valor_desejado" : 3200
    }
]

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Loop que percorre toda a lista de URLs e trata o valor desejado
for produto in produtos:
    driver.get(produto["url"])
    
    # Aguarda carregamento da página
    time.sleep(5)

    inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    # retirar caracteres
    inteiro = inteiro.replace(".","").replace(",","")

    # concatenar as variáveis
    preco = float(f"{inteiro}.{decimal}")

    # Análise da condição do preço
    if preco <= produto["valor_desejado"]:

        mensagem = (
            f"Pode comprar, o preço está bom!!!\n"
            f"O preço do produto é: {preco:.2f}\n"
            f"{produto['url']}"
        )

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
               "chat_id" : CHAT_ID,
               "text" : mensagem
            }
        )
        print('Pesquisa realizada e Mensagem enviada!')

driver.quit()