#Autor: Marco Antonio
import requests


cnpj = float(input('Digite o CNPJ da empresa: '))
url = f'https://api.opencnpj.org/{cnpj}'
res= requests.get(url)
busca = res.json()

dados = res.json()

print(f'CNPJ: {dados["cnpj"]}')
print(f'razao social: {dados["razao_social"]}')
print(f'nome fantasia: {dados["nome_fantasia"]}')
print(f'situação cadastral: {dados["situacao_cadastral"]}')
