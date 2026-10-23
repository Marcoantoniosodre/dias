# Autor: Marco Antonio
# Projeto: padrao visual:

#Instalar o pacote do customtkinter 
# pip install customtkinter 

#importação da biblioteca 
import customtkinter as ctk
from PIL import Image
from pathlib import Path
#configurações da janela
ctk.set_appearance_mode('dark')
# temas: 'dark', 'light' e 'system' (sistema operacional)
ctk.set_default_color_theme('blue') 

janela= ctk.CTk()
janela.geometry('400x500')
janela.title(' Calculadora de IMC.DoughV2') 

assets_dir = Path(__file__).resolve().parents[3] / "assets" / "images"
bg_image = ctk.CTkImage(Image.open(assets_dir / "finados.jpg"), size=(400, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)





#definição de funções 
def calcular_imc():
    altura_valor= float(altura.get().replace(',', '.'))
    peso_valor= float(peso.get().replace(',', '.'))
    imc= peso_valor/(altura_valor*altura_valor)
    resultado.configure(text=f' o seu imc é de: {imc:.2f}')
    if imc < 18.5:
        resultado.configure(text=f' o seu imc é de: {imc:.2f} \n Classificação: Abaixo do peso', text_color='orange')       
    elif imc < 25:
        resultado.configure(text=f' o seu imc é de: {imc:.2f} \n Classificação: Peso normal', text_color='green')
    elif imc < 30:
        resultado.configure(text=f' o seu imc é de: {imc:.2f} \n Classificação: Sobrepeso', text_color='yellow')
    else:
        resultado.configure(text=f' o seu imc é de: {imc:.2f} \n Classificação: Obesidade', text_color='red')
        print('obesidade, cuidado!')

#criação de elementos da janela
altura= ctk.CTkEntry(janela, placeholder_text='sua altura aqui, ex: 1.75', width=200, height=30, font=('Arial', 14))
altura.pack(pady=20)
peso= ctk.CTkEntry(janela, placeholder_text='seu peso aqui, ex: 70.5', width=200, height=30, font=('Arial', 14))
peso.pack(pady=20)
botao_calcular= ctk.CTkButton(janela, text= ' calcular imc', command=calcular_imc)
botao_calcular.pack(pady=20)
resultado= ctk.CTkLabel(janela, text= ' resultado')
resultado.pack(pady=20)
botao_calcular.configure(fg_color='red', hover_color='purple', text_color='lightblue', font=('Arial', 14, 'bold'))
altura.configure(fg_color='black', text_color='lightblue', font=('Arial', 14))
peso.configure(fg_color='black', text_color='lightblue', font=('Arial', 14))
resultado.configure(text_color='white', font=('Arial', 14, 'bold')) 

janela.mainloop()