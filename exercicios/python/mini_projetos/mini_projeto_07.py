#Autor: Marco Antonio

import customtkinter as ctk
import requests
from PIL import Image, ImageTk
from pathlib import Path


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title('Busca de CEP')
janela.geometry('500x600')

assets_dir = Path(__file__).resolve().parents[3] / "assets" / "images"
bg_image = ctk.CTkImage(Image.open(assets_dir / "TIGRE_MALIGNO.jpg"), size=(500, 600))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

def calcular():
    cep = entrada_cep.get()
    url= f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    dados = resposta.json()
    label_endereco.configure(text=dados['logradouro'])
    label_bairro.configure(text=dados['bairro'])
    label_cidade.configure(text=dados['localidade'])
    label_estado.configure(text=dados['uf'])


    entrada_cep.delete(0, ctk.END)

entrada_cep = ctk.CTkEntry(janela, width=200)
entrada_cep.place(x=50, y=10)

botao = ctk.CTkButton(janela, text='Buscar', command=calcular, fg_color= 'red', hover_color="#7B0000")
botao.place(x=260, y=10)
label_endereco = ctk.CTkLabel(janela, text='Endereço: ', width=80, height=20)
label_endereco.place(x=10, y=50)

label_bairro = ctk.CTkLabel(janela, text='Bairro: ', width=80, height=20)
label_bairro.place(x=10, y=80)

label_cidade = ctk.CTkLabel(janela, text='Cidade: ', width=80, height=20)
label_cidade.place(x=10, y=110)

label_estado = ctk.CTkLabel(janela, text='Estado: ', width=80, height=20)
label_estado.place(x=10, y=140)

label= ctk.CTkLabel(janela, text='dados ', width=200, height=20)




janela.mainloop()
