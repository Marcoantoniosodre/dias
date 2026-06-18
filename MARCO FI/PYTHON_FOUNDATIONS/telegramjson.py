# Autor: Marco Antonio
# Bot do Telegram - Monitor de Preços Amazon
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import json

with open("telegram.json", "r") as arquivo:
    config = json.load(arquivo)

TOKEN = config["token"]
CHAT_ID = config["chat_id"]

PRODUTOS = [
    {
        "nome": "Bola Adidas League",
        "url": "https://www.amazon.com.br/dp/B0DLHL9WM5",
        "preco_alvo": 320.00,
    },
    {
        "nome": "Controle DualShock PS4",
        "url": "https://www.amazon.com.br/dp/B07FN1MZBH",
        "preco_alvo": 250.00,
    },
    {
        "nome": "Estação de Carregamento PS4",
        "url": "https://www.amazon.com.br/dp/B075YBBQMM",
        "preco_alvo": 123.00,
    },
    {
        "nome": "Controle Bluetooth Ergonômico",
        "url": "https://www.amazon.com.br/dp/B0H2445D4F",
        "preco_alvo": 50.00,
    },
    {
        "nome": "Bonsai Permanente Vaso Branco",
        "url": "https://www.amazon.com.br/dp/B0F279DTY5",
        "preco_alvo": 40.00,
    },
]

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

for produto in PRODUTOS:
    try:
        print(f"🔍 Verificando: {produto['nome']}...")
        driver.get(produto["url"])
        time.sleep(5)

        inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
        decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

        inteiro = inteiro.replace(".", "").replace(",", "")
        preco = float(f"{inteiro}.{decimal}")

        if preco >= produto["preco_alvo"]:
            status = "⚠️ ACIMA DO IDEAL"
            emoji_preco = "📈"
        else:
            status = "✅ BOA OPORTUNIDADE!"
            emoji_preco = "📉"

        mensagem = (
            f"🛍️ *ALERTA DE PREÇO!*\n\n"
            f"📦 {produto['nome']}\n"
            f"{emoji_preco} Preço atual: R$ {preco:.2f}\n"
            f"🎯 Preço alvo: R$ {produto['preco_alvo']:.2f}\n"
            f"📊 Status: {status}\n\n"
            f"🔗 [Ver na Amazon]({produto['url']})\n\n"
            f"🤖 _PriceBot - monitorando pra você!_"
        )

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": mensagem,
                "parse_mode": "Markdown",
            },
        )
        print(f"✅ Mensagem enviada: {produto['nome']} - R$ {preco:.2f}")

    except Exception as e:
        print(f"❌ Erro ao verificar {produto['nome']}: {e}")

driver.quit()
print("🏁 Verificação concluída!")