# Autor: Marco Antonio
# Projeto: padrao visual:

#Instalar o pacote do customtkinter 
# pip install customtkinter 

#importação da biblioteca 
import customtkinter as ctk
from datetime import datetime
from PIL import Image
# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("600x500")
janela.title("Calculadora PRO de IMC")

bg_image = ctk.CTkImage(Image.open('finados.jpg'), size=(600, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)



# ================= FUNÇÕES =================

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "orange"
    elif imc < 25:
        return "Peso normal", "green"
    elif imc < 30:
        return "Sobrepeso", "yellow"
    else:
        return "Obesidade", "red"

def calcular_imc():
    try:
        altura_valor = float(altura.get().replace(',', '.'))
        peso_valor = float(peso.get().replace(',', '.'))

        if altura_valor <= 0 or peso_valor <= 0:
            mostrar_erro("Valores devem ser positivos!")
            return

        imc = peso_valor / (altura_valor ** 2)
        classificacao, cor = classificar_imc(imc)

        resultado.configure(
            text=f"IMC: {imc:.2f}\n{classificacao}",
            text_color=cor
        )

        atualizar_barra(imc)
        salvar_historico(imc, classificacao)

    except:
        mostrar_erro("Digite valores válidos!")

def mostrar_erro(msg):
    resultado.configure(text=msg, text_color="red")
    barra.set(0)

def atualizar_barra(imc):
    # Normaliza IMC para barra (0 a 40)
    progresso = min(imc / 40, 1)
    barra.set(progresso)

def limpar():
    altura.delete(0, 'end')
    peso.delete(0, 'end')
    resultado.configure(text="")
    barra.set(0)

def salvar_historico(imc, classificacao):
    horario = datetime.now().strftime("%H:%M:%S")
    historico.insert("0.0", f"[{horario}] IMC {imc:.2f} - {classificacao}\n")

# ================= UI =================

# Tabs
tabview = ctk.CTkTabview(janela)
tabview.pack(expand=True, fill="both", padx=10, pady=10)

tab_calc = tabview.add("Calculadora")
tab_hist = tabview.add("Histórico")

# ====== ABA CALCULADORA ======

titulo = ctk.CTkLabel(tab_calc, text="Calculadora de IMC", font=("Arial", 22, "bold"))
titulo.pack(pady=10)

altura = ctk.CTkEntry(tab_calc, placeholder_text="Altura (ex: 1.75)")
altura.pack(pady=10)

peso = ctk.CTkEntry(tab_calc, placeholder_text="Peso (kg)")
peso.pack(pady=10)

botao_calcular = ctk.CTkButton(tab_calc, text="Calcular", command=calcular_imc)
botao_calcular.pack(pady=10)

botao_limpar = ctk.CTkButton(tab_calc, text="Limpar", command=limpar, fg_color="gray")
botao_limpar.pack(pady=5)

# Barra de progresso
barra = ctk.CTkProgressBar(tab_calc, width=300)
barra.pack(pady=15)
barra.set(0)

resultado = ctk.CTkLabel(tab_calc, text="", font=("Arial", 16, "bold"))
resultado.pack(pady=10)

# ====== ABA HISTÓRICO ======

historico = ctk.CTkTextbox(tab_hist)
historico.pack(expand=True, fill="both", padx=10, pady=10)

# Atalho Enter
janela.bind("<Return>", lambda event: calcular_imc())

janela.mainloop()