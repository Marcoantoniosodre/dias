#Autor: Marco Antonio

import customtkinter as ctk
from PIL import Image, ImageTk
import random
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("AURA TECH")
janela.geometry("400x500")
janela.configure(fg_color="#0d0d0d")


bg_image = ctk.CTkImage(Image.open('Auratech.jpg'), size=(400, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

janela.iconbitmap('Auratech.ico')


titulo = ctk.CTkLabel(janela, text= "AURA TECH", text_color= "purple", width= 200, height= 20)
titulo.pack(pady=20)

subt = ctk.CTkLabel(janela, text= "Precisando de uma solução rapida? ", text_color= "white", width= 300, height= 20)
subt.pack(pady=20)
problema = ctk.CTkEntry(janela, placeholder_text= "Digite seu problema aqui: ", width= 225, height= 30, font= ("Arial", 14))
problema.pack(pady=20)
botao = ctk.CTkButton(janela, text= "Enviar", fg_color= "green", hover_color= "blue")
botao.pack(pady=20)

janela.mainloop()