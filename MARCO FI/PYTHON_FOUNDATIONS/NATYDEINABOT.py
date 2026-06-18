#Autor: Marco Antonio
#Bot do Telegram 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# Acesso do Telegram
TOKEN = "8979638987:AAHZvZGyZk1S_dAh5VSTZu4xCI28hWOFMQ4"
CHAT_ID = "8924203491"

# URLs dos produtos
produtos = [
    {
        "url" : "https://www.amazon.com.br/Futebol-Campe%C3%B5es-Champions-Original-Raccer/dp/B0FQFTVTXF/",
        "valor_desejado" : 130
    },
    {
        "url" : "https://www.amazon.com.br/Controle-Nintendo-Bluetooth-Movimento-Confort%C3%A1vel/dp/B0G1LYBYFY/ref=pd_rhf_dp_s_ci_mcx_mr__d_sccl_2_4/147-5658657-1142712",
        "valor_desejado" : 250
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