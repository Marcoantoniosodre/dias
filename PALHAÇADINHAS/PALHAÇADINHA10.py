#Autor: Marco Antonio

import customtkinter as ctk
from PIL import Image
import random
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CalculadoraMaligna(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Média 😈")
        self.geometry("400x500")
        self.configure(fg_color="#0d0d0d")

        self.modo_maligno = False

        # Título
        self.label = ctk.CTkLabel(self, text="Calculadora de Média", font=("Arial", 20, "bold"), text_color="#ff0000")
        self.label.pack(pady=20)

        # Entradas
        self.entries = []
        for i in range(4):
            entry = ctk.CTkEntry(self, placeholder_text=f"Nota {i+1}", width=200)
            entry.pack(pady=5)
            self.entries.append(entry)

        # Botão calcular
        self.btn_calc = ctk.CTkButton(self, text="Calcular Média", command=self.calcular)
        self.btn_calc.pack(pady=15)

        # Resultado
        self.resultado = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.resultado.pack(pady=10)

        # Botão maligno
        self.btn_maligno = ctk.CTkButton(
            self,
            text="Ativar Modo Maligno 😈",
            fg_color="#8b0000",
            hover_color="#ff0000",
            command=self.toggle_maligno
        )
        self.btn_maligno.pack(pady=20)

    def calcular(self):
        try:
            notas = [float(e.get()) for e in self.entries if e.get() != ""]
            if not notas:
                self.resultado.configure(text="Digite pelo menos uma nota.")
                return

            media = sum(notas) / len(notas)

            if self.modo_maligno:
                media = self.media_maligna(media)
                self.resultado.configure(
                    text=f"Média MALIGNA: {media:.2f}",
                    text_color="#ff0000"
                )
            else:
                self.resultado.configure(
                    text=f"Média: {media:.2f}",
                    text_color="white"
                )

        except:
            self.resultado.configure(text="Erro nas entradas.")

    def media_maligna(self, media):
        # Aqui está a “maldade”:
        # distorce a média com uma curva injusta
        fator = random.uniform(0.5, 1.5)
        distorcao = (media ** 2) / 10
        resultado = (media * fator) - distorcao

        # chance de "punição extra"
        if random.random() < 0.3:
            resultado -= random.uniform(1, 3)

        return max(0, resultado)

    def toggle_maligno(self):
        self.modo_maligno = not self.modo_maligno

        if self.modo_maligno:
            self.btn_maligno.configure(text="Modo Maligno ATIVO", fg_color="#ff0000")
            self.jumpscare()
        else:
            self.btn_maligno.configure(text="Ativar Modo Maligno 😈", fg_color="#8b0000")

    def jumpscare(self):
        try:
            caminho = "MALIGNO.jpg"
            if not os.path.exists(caminho):
                print("Imagem não encontrada.")
                return

            img = Image.open(caminho)

            top = ctk.CTkToplevel(self)
            top.attributes("-fullscreen", True)
            top.configure(fg_color="black")

            largura = 1920
            altura = 1080

            img = img.resize((largura, altura))
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(largura, altura))

            label = ctk.CTkLabel(top, image=ctk_img, text="")
            label.pack(expand=True)

            # fecha sozinho depois de 1.5s
            self.after(3500, top.destroy)

        except Exception as e:
            print("Erro no jumpscare:", e)


if __name__ == "__main__":
    app = CalculadoraMaligna()
    app.mainloop()