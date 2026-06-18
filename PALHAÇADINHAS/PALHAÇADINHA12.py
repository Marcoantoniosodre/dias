#Autor: Marco Antonio
#Projeto: Visual buscador de CNPJ e CPF

import requests
import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Busca de CNPJ e CPF")
janela.geometry("700x400")

bg_image = ctk.CTkImage(Image.open('finados.jpg'), size=(700, 400))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

box = ctk.CTkComboBox(janela, values=["CNPJ", "CPF"])
box.pack(pady=20)
box.configure(width=200, height=30, font=("Arial", 14), fg_color="black", text_color="lightblue")
caixa = box.get() 
escolha = ctk.CTkEntry(janela, placeholder_text="Digite o número aqui", width=200, height=30, font=("Arial", 14))
escolha.pack(pady=20)
botao = ctk.CTkButton(janela, text= "Buscar", fg_color="red", hover_color="#7B0000")
botao.pack(pady=20)
label1= ctk.CTkLabel(janela, text="")
label1.pack(pady=10)
label2= ctk.CTkLabel(janela, text="")
label2.pack(pady=10)
label3= ctk.CTkLabel(janela, text="")
label3.pack(pady=10)
label4= ctk.CTkLabel(janela, text="")
label4.pack(pady=10)

def CNPJ():
    cnpj = escolha.get()
    url = f'https://api.opencnpj.org/{cnpj}?dataset=receita'
    res = requests.get(url)
    dados = res.json()
    label1.configure(text=f"CNPJ: {dados['cnpj']}")
    label2.configure(text=f"Razão Social: {dados['razao_social']}")
    label3.configure(text=f"Nome Fantasia: {dados['nome_fantasia']}")
    label4.configure(text=f"Situação Cadastral: {dados['situacao_cadastral']}")

def CPF():
    cpf = escolha.get()
    url = f'https://api.cpfhub.io/cpf/{cpf}'
    token = '15fb9829763702195c4dd71892817a0dc6f864dd49da2ca26c22c4c4fd721bed'
    headers = {'x-api-key': token}
    res = requests.get(url, headers=headers)
    dados = res.json()
    label1.configure(text=f"CPF: {dados['data'].get('cpf', 'N/A')}")
    label2.configure(text=f"Nome: {dados['data'].get('name', 'N/A')}")
    label3.configure(text=f"Data de Nascimento: {dados['data'].get('birthDate', 'N/A')}")
    label4.configure(text=f"Sexo: {dados['data'].get('gender', 'N/A')}")


botao.configure(command=lambda: CNPJ() if box.get() == "CNPJ" else CPF())

janela.mainloop()
