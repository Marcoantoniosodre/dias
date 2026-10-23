#Autor: Marco Antonio
#criação da calculadora de media de alunos beeeeeem maligna 

import customtkinter as ctk
import random


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela = ctk.CTk()
janela.title("Calculadora de média maléfica")
janela.geometry("500x600")


nomeA= ctk.CTkEntry(janela, placeholder_text='Nome do aluno 1',)



janela.mainloop()