#Autor: Marco Antonio
#Projeto: padrao visual: média de alunos 

import customtkinter as ctk
import requests

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Média de alunos')
        self.geometry('400x300')

        self.e1 = ctk.CTkEntry(self, placeholder_text=' Digite a nota do aluno aqui: ', text_color="#000000", width=200, height=30, font=('Arial', 14))
        self.e1.pack(pady=5)

        self.e2 = ctk.CTkEntry(self, placeholder_text=' Digite a nota do aluno aqui: ', text_color="#000000", width=200, height=30, font=('Arial', 14))
        self.e2.pack(pady=5)

        self.e3 = ctk.CTkEntry(self, placeholder_text=' Digite a nota do aluno aqui: ', text_color="#000000", width=200, height=30, font=('Arial', 14))
        self.e3.pack(pady=5)

        self.e4 = ctk.CTkEntry(self, placeholder_text=' Digite aqui a nota do aluno: ', text_color="#040404", width=200, height=30, font=('Arial', 15))
        self.e4.pack(pady=5)

        self.resultado = ctk.CTkLabel(self, text='')
        self.resultado.pack(pady=10)

        botao = ctk.CTkButton(self, text='Calcular',fg_color='blue', hover_color='dark red', command=self.conta)
        botao.pack(pady=10)
        

    def conta(self):
        b1 = float(self.e1.get())
        b2 = float(self.e2.get())
        b3 = float(self.e3.get())
        b4 = float(self.e4.get())

        media = (b1 + b2 + b3 + b4) / 4

        self.resultado.configure(text=f'A média é: {media:.2f}')
        if media >= 6:
            self.resultado.configure(text=f' A média é: {media:.2f} \n Aluno aprovado', text_color='green')
        else:
            self.resultado.configure(text=f' A média é: {media:.2f} \n Aluno reprovado', text_color= 'red')
app = App()
app.mainloop()