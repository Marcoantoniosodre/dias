#Autor: Marco Antonio
#Projeto: padrao visual

#=============== IMPORTAÇÕES ===============
import os
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from pytubefix import YouTube
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#=============== CONFIGURAÇÕES ===============
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("900x700")
janela.title("Multi ferramentas V1.0")
janela.grid_columnconfigure(0, weight=0)
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)

# ── HEADER ──────────────────────────────────────────────────────────────
fmreader = ctk.CTkFrame(janela, fg_color="#111111", border_width=1, border_color="white", height=80)
fmreader.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
fmreader.grid_propagate(False)
fmreader.grid_columnconfigure(0, weight=1)

titulo = ctk.CTkLabel(fmreader, text="✦ Multi Ferramentas V1.0 ✦", font=("Arial", 22, "bold"), text_color="white")
titulo.grid(row=0, column=0, pady=(10, 2))

subtitulo = ctk.CTkLabel(
    fmreader,
    text="Pequeno por enquanto, grande em breve. Sua caixa de ferramentas digital está só começando 🚀",
    font=("Verdana", 11),
    text_color="#AAAAAA"
)
subtitulo.grid(row=1, column=0, pady=(0, 8))

# ── SIDEBAR ──────────────────────────────────────────────────────────────
side = ctk.CTkFrame(janela, width=170, fg_color="#111111", border_width=1, border_color="white")
side.grid(row=1, column=0, sticky="ns", padx=(10, 0), pady=10)
side.grid_propagate(False)

# ── FRAME DE CONTEÚDO ────────────────────────────────────────────────────
frame = ctk.CTkFrame(janela, fg_color="#1a1a1a", border_width=1, border_color="white")
frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

#=============== VARIÁVEL DE TEMA ===============
tema_var     = ctk.StringVar(value="escuro")
bg_label_ref = [None]

#=============== SISTEMA DE TEMAS ===============
TEMAS = {
    "escuro": {
        "appearance": "dark",
        "janela_bg":  "#0d0d0d",
        "header_bg":  "#111111",
        "frame_bg":   "#1a1a1a",
        "side_bg":    "#111111",
        "btn_fg":     "darkblue",
        "btn_hover":  "blue",
        "border":     "white",
        "text":       "white",
        "sub_text":   "#AAAAAA",
    },
    "claro": {
        "appearance": "light",
        "janela_bg":  "#FFFFFF",
        "header_bg":  "#BFBFBF",
        "frame_bg":   "#BFBFBF",
        "side_bg":    "#BFBFBF",
        "btn_fg":     "#2255cc",
        "btn_hover":  "#3366ff",
        "border":     "#000000",
        "text":       "#111111",
        "sub_text":   "#000000",
    },
    "vermelho": {
        "appearance": "dark",
        "janela_bg":  "#0a0000",
        "header_bg":  "#1a0000",
        "frame_bg":   "#110000",
        "side_bg":    "#1a0000",
        "btn_fg":     "#8b0000",
        "btn_hover":  "#cc0000",
        "border":     "#cc0000",
        "text":       "#ff6666",
        "sub_text":   "#aa3333",
    },
}

def t():
    """Atalho para pegar o dicionário do tema atual."""
    return TEMAS[tema_var.get()]

def aplicar_tema(nome):
    tk = TEMAS[nome]

    if bg_label_ref[0]:
        bg_label_ref[0].destroy()
        bg_label_ref[0] = None

    ctk.set_appearance_mode(tk["appearance"])
    janela.configure(fg_color=tk["janela_bg"])
    frame.configure(fg_color=tk["frame_bg"], border_color=tk["border"])
    side.configure(fg_color=tk["side_bg"], border_color=tk["border"])
    fmreader.configure(fg_color=tk["header_bg"], border_color=tk["border"])
    titulo.configure(text_color=tk["text"])
    subtitulo.configure(text_color=tk["sub_text"])

    for widget in side.winfo_children():
        if isinstance(widget, ctk.CTkButton):
            widget.configure(fg_color=tk["btn_fg"], hover_color=tk["btn_hover"])

    if nome == "vermelho":
        caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TIGRE_MALIGNO.jpg")
        if os.path.exists(caminho):
            try:
                w = frame.winfo_width()  or 700
                h = frame.winfo_height() or 600
                img  = Image.open(caminho).resize((w, h))
                foto = ImageTk.PhotoImage(img)
                bg   = ctk.CTkLabel(frame, image=foto, text="")
                bg.image = foto
                bg.place(x=0, y=0, relwidth=1, relheight=1)
                bg_label_ref[0] = bg
            except Exception:
                pass

def on_tema_change():
    aplicar_tema(tema_var.get())

#=============== FUNÇÕES AUXILIARES ===============
def clear():
    if bg_label_ref[0]:
        bg_label_ref[0].destroy()
        bg_label_ref[0] = None
    for widget in frame.winfo_children():
        widget.destroy()

def make_titulo(texto):
    return ctk.CTkLabel(frame, text=texto, font=("Arial", 22, "bold"), text_color=t()["text"])

def make_entry(placeholder):
    return ctk.CTkEntry(frame, placeholder_text=placeholder, width=400, height=30, font=("Arial", 14))

def make_resultado():
    return ctk.CTkLabel(frame, text="Resultado:", text_color=t()["text"])

def make_botao(texto, comando):
    return ctk.CTkButton(frame, text=texto, fg_color=t()["btn_fg"], hover_color=t()["btn_hover"],
                         command=comando, width=400, height=30, font=("Arial", 14))

#=============== BOTAO FLUTUANTE ===============
def efeito_botao(botao, cor_normal):
    botao.bind("<ButtonPress-1>",   lambda e: botao.configure(fg_color="#550000"))
    botao.bind("<ButtonRelease-1>", lambda e: botao.configure(fg_color=cor_normal))

#=============== FUNÇÕES DE IMC ===============
def abrir_IMC():
    clear()
    make_titulo("Calculadora de IMC").pack(pady=10)

    altura = make_entry("Digite sua altura, ex: 1.75")
    altura.pack(pady=10)

    peso = make_entry("Digite seu peso, ex: 70.5")
    peso.pack(pady=10)

    label_resultado = make_resultado()
    label_resultado.pack(pady=10)

    barra = ctk.CTkProgressBar(frame, width=400)
    barra.pack(pady=10)
    barra.set(0)

    def calcular_imc():
        try:
            imc = float(peso.get()) / (float(altura.get()) ** 2)
            label_resultado.configure(text=f"Seu IMC é: {imc:.2f}")
            if imc < 18.5:
                label_resultado.configure(text_color="orange")
            elif imc < 25:
                label_resultado.configure(text_color="lightgreen")
            elif imc < 30:
                label_resultado.configure(text_color="yellow")
            else:
                label_resultado.configure(text_color="red")
            barra.set(min(imc / 40, 1.0))
        except ValueError:
            label_resultado.configure(text="Digite valores válidos!", text_color="red")

    make_botao("Calcular IMC", calcular_imc).pack(pady=10)

#=============== FUNÇÕES DE TABUADA ===============
def mutiplicacao():
    clear()
    make_titulo("Tabuada").pack(pady=10)

    numero = make_entry("Digite o numero da tabuada que deseja:")
    numero.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calculo():
        try:
            num = int(numero.get())
            res = "".join(f"{num} x {i} = {num * i}\n" for i in range(1, 11))
            resultado.configure(text=res, text_color=t()["text"])
        except ValueError:
            resultado.configure(text="Digite um número válido!", text_color="red")

    make_botao("Calcular Tabuada", calculo).pack(pady=10)

#=============== FUNÇÕES DE CPF ===============
def abrir_CPF():
    clear()
    make_titulo("Buscador de CPF").pack(pady=10)

    cpf = make_entry("Digite o seu CPF, ex: 13430481700")
    cpf.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def buscar_cpf():
        try:
            url = f'https://api.cpfhub.io/cpf/{cpf.get()}'
            res = requests.get(url, headers={'x-api-key': 'SUA CHAVE DE API AQUI'})
            d = res.json()['data']
            resultado.configure(
                text=f"CPF: {d.get('cpf','N/A')}\nNome: {d.get('name','N/A')}\nNasc.: {d.get('birthDate','N/A')}\nSexo: {d.get('gender','N/A')}",
                text_color=t()["text"]
            )
        except Exception:
            resultado.configure(text="Erro ao buscar CPF!", text_color="red")

    make_botao("Buscar CPF", buscar_cpf).pack(pady=10)

#=============== FUNÇÕES DE CNPJ ===============
def abrir_CNPJ():
    clear()
    make_titulo("Buscador de CNPJ").pack(pady=10)

    cnpj = make_entry("Digite o número do CNPJ, ex: 12345678000195")
    cnpj.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def buscar_cnpj():
        try:
            res = requests.get(f'https://api.opencnpj.org/{cnpj.get()}?dataset=receita').json()
            resultado.configure(
                text=f"CNPJ: {res['cnpj']}\nRazão Social: {res['razao_social']}\nFantasia: {res['nome_fantasia']}\nSituação: {res['situacao_cadastral']}",
                text_color=t()["text"]
            )
        except Exception:
            resultado.configure(text="Erro ao buscar CNPJ!", text_color="red")

    make_botao("Buscar CNPJ", buscar_cnpj).pack(pady=10)

#=============== FUNÇÕES DE FATORIAL ===============
def abrir_fatorial():
    clear()
    make_titulo("Calculadora de Fatorial").pack(pady=10)

    numero = make_entry("Digite um número para calcular o fatorial:")
    numero.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calcular_fatorial():
        try:
            num = int(numero.get())
            if num < 0:
                resultado.configure(text="Fatorial não definido para negativos!", text_color="red")
                return
            fat = 1
            for i in range(1, num + 1):
                fat *= i
            resultado.configure(text=f"O fatorial de {num} é: {fat}", text_color=t()["text"])
        except ValueError:
            resultado.configure(text="Digite um número válido!", text_color="red")

    make_botao("Calcular Fatorial", calcular_fatorial).pack(pady=10)

#=============== FUNÇÕES DE POTÊNCIA ===============
def abrir_potencia():
    clear()
    make_titulo("Calculadora de Potência").pack(pady=10)

    base = make_entry("Digite a base:")
    base.pack(pady=10)

    expoente = make_entry("Digite o expoente:")
    expoente.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calcular_potencia():
        try:
            b, e = float(base.get()), float(expoente.get())
            resultado.configure(text=f"{b} elevado a {e} é: {b ** e}", text_color=t()["text"])
        except ValueError:
            resultado.configure(text="Digite valores válidos!", text_color="red")

    make_botao("Calcular Potência", calcular_potencia).pack(pady=10)

#=============== FUNÇÕES DE RAIZ QUADRADA ===============
def abrir_raiz():
    clear()
    make_titulo("Calculadora de Raiz Quadrada").pack(pady=10)

    numero = make_entry("Digite um número para calcular a raiz quadrada:")
    numero.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calcular_raiz():
        try:
            num = float(numero.get())
            if num < 0:
                resultado.configure(text="Raiz não definida para negativos!", text_color="red")
                return
            resultado.configure(text=f"A raiz quadrada de {num} é: {num**0.5:.2f}", text_color=t()["text"])
        except ValueError:
            resultado.configure(text="Digite um número válido!", text_color="red")

    make_botao("Calcular Raiz Quadrada", calcular_raiz).pack(pady=10)

#=============== FUNÇÕES DE ÁREA ===============
def abrir_area():
    clear()
    make_titulo("Calculadora de Área").pack(pady=10)

    numero  = make_entry("Base:")
    numero.pack(pady=10)

    numero2 = make_entry("Altura:")
    numero2.pack(pady=10)

    raio = make_entry("Raio (apenas para círculo):")
    raio.pack(pady=10)

    escolhas = ctk.CTkComboBox(frame, values=["Área do Triângulo", "Área do Retângulo", "Área do Círculo"],
                               width=400, height=30, font=("Arial", 14))
    escolhas.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calcular_area():
        try:
            escolha = escolhas.get()
            if escolha == "Área do Triângulo":
                area = (float(numero.get()) * float(numero2.get())) / 2
            elif escolha == "Área do Retângulo":
                area = float(numero.get()) * float(numero2.get())
            elif escolha == "Área do Círculo":
                area = 3.14159 * float(raio.get()) ** 2
            else:
                resultado.configure(text="Escolha uma opção válida!", text_color="red")
                return
            resultado.configure(text=f"A área é: {area:.2f}", text_color=t()["text"])
        except ValueError:
            resultado.configure(text="Digite um número válido!", text_color="red")

    make_botao("Calcular Área", calcular_area).pack(pady=10)

#=============== FUNÇÕES DE CEP ===============
def abrir_CEP():
    clear()
    make_titulo("Buscar CEP").pack(pady=10)

    entrada_cep = make_entry("Digite o CEP, ex: 01001000")
    entrada_cep.pack(pady=10)

    resultado_cep = make_resultado()
    resultado_cep.pack(pady=10)

    def buscar_cep():
        try:
            data = requests.get(f"https://viacep.com.br/ws/{entrada_cep.get()}/json/").json()
            if "erro" not in data:
                resultado_cep.configure(
                    text=f"CEP: {data['cep']}\nLogradouro: {data['logradouro']}\nBairro: {data['bairro']}\nCidade: {data['localidade']}\nEstado: {data['uf']}",
                    text_color=t()["text"]
                )
            else:
                resultado_cep.configure(text="CEP não encontrado", text_color="red")
        except Exception:
            resultado_cep.configure(text="Erro na busca!", text_color="red")

    make_botao("Buscar CEP", buscar_cep).pack(pady=10)

#=============== FUNÇÕES DE JUROS ===============
def abrir_juros():
    clear()
    make_titulo("Calculadora de Juros simples e compostos").pack(pady=10)

    principal = make_entry("Valor principal (R$)")
    principal.pack(pady=10)

    taxa = make_entry("Taxa de juros (% ao período)")
    taxa.pack(pady=10)

    periodo = make_entry("Número de períodos")
    periodo.pack(pady=10)

    tipo = ctk.CTkComboBox(frame, values=["Juros Simples", "Juros Compostos"], width=400, height=30, font=("Arial", 14))
    tipo.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def calcular_juros():
        try:
            valor, tx, n = float(principal.get()), float(taxa.get()) / 100, float(periodo.get())
            if valor <= 0 or tx <= 0 or n <= 0:
                resultado.configure(text="Digite valores maiores que zero!", text_color="red")
                return
            juros = valor * tx * n if tipo.get() == "Juros Simples" else valor * (1 + tx) ** n - valor
            resultado.configure(
                text=f"Principal: R${valor:.2f}\nJuros: R${juros:.2f}\nTotal: R${valor+juros:.2f}",
                text_color=t()["text"]
            )
        except ValueError:
            resultado.configure(text="Digite apenas números válidos!", text_color="red")

    make_botao("Calcular", calcular_juros).pack(pady=10)

#=============== FUNÇÕES DE YOUTUBE ===============
def abrir_youtube():
    clear()
    make_titulo("Baixar Vídeo do YouTube").pack(pady=10)

    link = make_entry("Digite o link do YouTube:")
    link.pack(pady=10)

    resultado = make_resultado()
    resultado.pack(pady=10)

    def baixar():
        try:
            YouTube(link.get()).streams.first().download()
            resultado.configure(text='Download concluído!', text_color="lightgreen")
        except Exception:
            resultado.configure(text="Erro ao baixar vídeo!", text_color="red")

    make_botao("Baixar Vídeo", baixar).pack(pady=10)

#=============== FUNÇÕES DE PLANILHAS ===============
def abrir_planilhas():
    clear()
    make_titulo("Leitor de Planilhas").pack(pady=10)

    planilha = make_entry("Digite o caminho da planilha Excel:")
    planilha.pack(pady=10)

    resultado_label = ctk.CTkLabel(frame, text="", text_color=t()["text"])
    resultado_label.pack(pady=10)

    def analisar():
        try:
            df = pd.read_excel(planilha.get())
            agrupado = df.groupby(['ID_Produto', 'Nome_Produto'])['Quantidade_Vendida'].sum()
            texto = "Resultado:\n\n" + "".join(
                f"ID: {id_p} | Produto: {nome_p} | Qtd: {qtd}\n"
                for (id_p, nome_p), qtd in agrupado.items()
            )
            resultado_label.configure(text=texto, text_color=t()["text"])
        except Exception as e:
            resultado_label.configure(text=f"Erro!\n{e}", text_color="red")

    make_botao("Analisar Planilha", analisar).pack(pady=10)

#=============== RASPAGEM DE DADOS ===============
def abrir_raspagem():
    clear()
    make_titulo("Raspagem de Dados").pack(pady=10)

    entry_raspagem = make_entry("Digite o link do produto aqui:")
    entry_raspagem.pack(pady=10)

    def executar_raspagem():
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            url = entry_raspagem.get()
            driver.get(url)
            inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
            decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
            resultado = f"O preço do produto é: {inteiro},{decimal}"
            ctk.CTkLabel(frame, text=resultado, font=("Arial", 16), text_color=t()["text"]).pack(pady=10)
            driver.quit()
            time.sleep(9)
        except Exception as e:
            ctk.CTkLabel(frame, text=f"Erro ao raspar dados!\n{e}", font=("Arial", 14), text_color="red").pack(pady=10)

    make_botao("Raspar Preço", executar_raspagem).pack(pady=10)

#=============== FUNÇÃO DA TECNOLOGIA SOU EU ===============
def abrir_tecnologia():
    clear()
    make_titulo("Tecnologia Sou Eu").pack(pady=10)

    frame_borda = ctk.CTkFrame(frame, border_width=1, border_color=t()["border"], width=600, height=200)
    frame_borda.pack(pady=20)
    frame_borda.pack_propagate(False)

    ctk.CTkLabel(
        frame_borda,
        text=(
            "A tecnologia é uma extensão da nossa criatividade e capacidade de transformar o mundo.\n"
            "Sou eu, você, nós - todos nós somos a tecnologia em ação, moldando o futuro com cada\n"
            "inovação e ideia brilhante que surge. Juntos, somos a força por trás do progresso\n"
            "e da evolução tecnológica."
        ),
        font=("Arial", 14),
        text_color=t()["text"],
        justify="center",
        wraplength=560
    ).pack(expand=True, padx=10, pady=10)

    def abrir_imagem():
        clear()
        caminho_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tecnologia.jpg")
        if os.path.exists(caminho_img):
            try:
                w = frame.winfo_width() or 700
                h = frame.winfo_height() or 600
                img  = Image.open(caminho_img).resize((w, h))
                foto = ImageTk.PhotoImage(img)
                bg   = ctk.CTkLabel(frame, image=foto, text="")
                bg.image = foto
                bg.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception:
                pass

    make_botao("Ver Imagem", abrir_imagem).pack(pady=10)

#=============== FUNÇÃO DE TEMAS ===============
def abrir_temas():
    clear()

    ctk.CTkLabel(
        frame,
        text="🎨 Configurações de Tema",
        font=("Arial", 20, "bold"),
        text_color=t()["text"]
    ).pack(pady=30)

    opcoes = [
        ("escuro",   "🌙  Modo Escuro",      "#222222", "#444444", "white"),
        ("claro",    "☀️  Modo Claro",        "#cccccc", "#aaaaaa", "#111111"),
        ("vermelho", "🔴  Vermelho Maligno",  "#8b0000", "#cc0000", "white"),
    ]

    for valor, label, fg, hover, text_color in opcoes:
        ctk.CTkRadioButton(
            frame,
            text=label,
            variable=tema_var,
            value=valor,
            font=("Arial", 15, "bold"),
            text_color=text_color,
            fg_color=fg,
            hover_color=hover,
            command=on_tema_change,
            width=300,
            height=40,
        ).pack(pady=12)

    caminho_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TIGRE_MALIGNO.jpg")
    if not os.path.exists(caminho_img):
        ctk.CTkLabel(
            frame,
            text="💡 Coloque 'TIGRE_MALIGNO.jpg' na mesma pasta\npara ativar o fundo no tema vermelho.",
            font=("Arial", 11),
            text_color=t()["sub_text"],
            justify="center"
        ).pack(pady=20)

#=============== BOTÕES LATERAIS ===============
selections = [
    ("Calculadora de IMC",   abrir_IMC),
    ("Busca de CPF",         abrir_CPF),
    ("Busca de CNPJ",        abrir_CNPJ),
    ("Calc. de Fatoriais",   abrir_fatorial),
    ("Calc. de Tabuada",     mutiplicacao),
    ("Calc. de Potências",   abrir_potencia),
    ("Calc. de Raízes",      abrir_raiz),
    ("Calc. de Área",        abrir_area),
    ("Busca de CEP",         abrir_CEP),
    ("Calc. de Juros",       abrir_juros),
    ("YouTube Installer",    abrir_youtube),
    ("Analise de Planilhas", abrir_planilhas),
    ("Raspagem de Dados",    abrir_raspagem),
    ("Tecnologia Sou Eu",    abrir_tecnologia),
    ("🎨 Temas",             abrir_temas),
]

for item, cmd in selections:
    btn = ctk.CTkButton(
        side, text=item,
        fg_color="darkblue", hover_color="blue",
        command=cmd
    )
    btn.pack(pady=6, padx=10, fill="x")
    efeito_botao(btn, "darkblue")

janela.mainloop()