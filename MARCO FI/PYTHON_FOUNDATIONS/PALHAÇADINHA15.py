# Autor: Marco Antonio
# Projeto: Calculadora Visual (versão corrigida e comentada)

import customtkinter as ctk
from tkinter import messagebox
from math import pi

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Calculadora")
janela.geometry("400x600")
janela.resizable(False, False)


janela.grid_columnconfigure((0, 1, 2, 3), weight=1)


frame_titulo = ctk.CTkFrame(janela, corner_radius=10)
frame_titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

label_titulo = ctk.CTkLabel(
    frame_titulo,
    text="Calculadora",
    font=ctk.CTkFont(size=24, weight="bold")
)
label_titulo.pack(pady=20)

frame_resultado = ctk.CTkFrame(janela, corner_radius=10)
frame_resultado.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

label_resultado = ctk.CTkLabel(
    frame_resultado,
    text="0",
    font=ctk.CTkFont(size=24, weight="bold")
)
label_resultado.pack(pady=20)

frame_botoes = ctk.CTkFrame(janela, corner_radius=10)
frame_botoes.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# 6 linhas e 4 colunas dentro do frame de botões
frame_botoes.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
frame_botoes.grid_columnconfigure((0, 1, 2, 3), weight=1)

def adicionar_numero(numero):
    """
    Acrescenta um caractere (dígito ou operador) ao display.
    Se o display mostrar '0', substitui em vez de concatenar,
    evitando resultados como '05'.
    """
    texto_atual = label_resultado.cget("text")
    if texto_atual == "0" or texto_atual == "Erro":
        label_resultado.configure(text=numero)
    else:
        label_resultado.configure(text=texto_atual + numero)


def calcular_resultado():
    """
    Lê a expressão do display e avalia com eval().
    Em caso de divisão por zero ou expressão inválida,
    exibe 'Erro' no display.
    """
    expressao = label_resultado.cget("text")
    try:
        resultado = eval(expressao)
        label_resultado.configure(text=str(resultado))
    except ZeroDivisionError:
        label_resultado.configure(text="Divisão por 0")
    except Exception:
        label_resultado.configure(text="Erro")


def limpar():
    """Reinicia o display para o valor inicial '0'."""
    label_resultado.configure(text="0")


def apagar_ultimo():
    """
    Remove o último caractere digitado (backspace).
    Se restar string vazia, volta para '0'.
    """
    texto_atual = label_resultado.cget("text")
    novo_texto = texto_atual[:-1]
    if novo_texto == "" or novo_texto == "-":
        novo_texto = "0"
    label_resultado.configure(text=novo_texto)


FONTE = ctk.CTkFont(size=24, weight="bold")

ctk.CTkButton(frame_botoes, text="7", font=FONTE,
              command=lambda: adicionar_numero("7")).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="8", font=FONTE,
              command=lambda: adicionar_numero("8")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="9", font=FONTE,
              command=lambda: adicionar_numero("9")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="÷", font=FONTE,
              command=lambda: adicionar_numero("/")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="4", font=FONTE,
              command=lambda: adicionar_numero("4")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="5", font=FONTE,
              command=lambda: adicionar_numero("5")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="6", font=FONTE,
              command=lambda: adicionar_numero("6")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="×", font=FONTE,
              command=lambda: adicionar_numero("*")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="1", font=FONTE,
              command=lambda: adicionar_numero("1")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="2", font=FONTE,
              command=lambda: adicionar_numero("2")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="3", font=FONTE,
              command=lambda: adicionar_numero("3")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="−", font=FONTE,
              command=lambda: adicionar_numero("-")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="C", font=FONTE,
              fg_color="#c0392b", hover_color="#e74c3c",
              command=limpar).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="0", font=FONTE,
              command=lambda: adicionar_numero("0")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="⌫", font=FONTE,
              command=apagar_ultimo).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="+", font=FONTE,
              command=lambda: adicionar_numero("+")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text=".", font=FONTE,
              command=lambda: adicionar_numero(".")).grid(row=4, column=0, columnspan=2,
                                                         padx=5, pady=5, sticky="nsew")

ctk.CTkButton(frame_botoes, text="=", font=FONTE,
              fg_color="#27ae60", hover_color="#2ecc71",
              command=calcular_resultado).grid(row=4, column=2, columnspan=2,
                                              padx=5, pady=5, sticky="nsew")

janela.mainloop()