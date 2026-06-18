#Autor: Marco Antonio
#Projeto: padrao visual:

import customtkinter as ctk
from PIL import Image, ImageTk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("800x500")
janela.title("Calculadora PRO")
janela.grid_columnconfigure(1, weight= 0)
janela.grid_rowconfigure(0, weight= 1)

side = ctk.CTkFrame(janela, width= 150, height= 300, fg_color= "black")
side.grid(row= 0, column= 0, sticky= "ns")
selections = [
    "Calculadora de IMC",
    "Busca de CPF",
    "Busca de CNPJ",
    "Calculadora de Fatorias",
    "Calculadora de Tabuada",
    "Calculadora de Potências",
    "Calculadora de Raízes",
    "Calculadora de Área",  

]
for item in selections:
    botao = ctk.CTkButton(side, text= item, fg_color= "darkblue", hover_color= "blue")
    botao.pack(pady= 10, padx= 10, fill= "x")


janela.mainloop()