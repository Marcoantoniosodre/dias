# Autor: Marco Antonio
# Projeto: Multi Ferramentas V1.0 — Visual redesenhado

import os
from pathlib import Path
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
import pandas as pd
import matplotlib.pyplot as plt

ASSETS_DIR = Path(__file__).resolve().parents[3] / "assets" / "images"

# ─── CONFIGURAÇÕES ───────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("980x680")
janela.title("Multi Ferramentas V1.0")
janela.configure(fg_color="#0D1117")
janela.grid_columnconfigure(0, weight=0)
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)

# ─── HEADER ──────────────────────────────────────────────────────────
header = ctk.CTkFrame(
    janela, fg_color="#161B22",
    border_width=1, border_color="#21262D", height=72
)
header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=12, pady=(12, 0))
header.grid_propagate(False)
header.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(
    header, text="⚙  Multi Ferramentas V1.0",
    font=("Segoe UI", 20, "bold"), text_color="#E6EDF3"
).grid(row=0, column=0, pady=(10, 2))

ctk.CTkLabel(
    header,
    text="Pequeno por enquanto, grande em breve. Sua caixa de ferramentas digital está só começando 🚀",
    font=("Segoe UI", 11), text_color="#8B949E"
).grid(row=1, column=0, pady=(0, 8))

# ─── SIDEBAR ─────────────────────────────────────────────────────────
side = ctk.CTkScrollableFrame(
    janela, width=175,
    fg_color="#161B22",
    border_width=1, border_color="#21262D",
    scrollbar_button_color="#21262D",
    scrollbar_button_hover_color="#2D5F8A"
)
side.grid(row=1, column=0, sticky="ns", padx=(12, 0), pady=12)

# ─── FRAME DE CONTEÚDO ───────────────────────────────────────────────
frame = ctk.CTkFrame(
    janela, fg_color="#161B22",
    border_width=1, border_color="#21262D"
)
frame.grid(row=1, column=1, sticky="nsew", padx=12, pady=12)

# ─── TEMA ────────────────────────────────────────────────────────────
tema_var     = ctk.StringVar(value="escuro")
bg_label_ref = [None]

TEMAS = {
    "escuro": {
        "appearance": "dark",
        "janela_bg": "#0D1117", "header_bg": "#161B22",
        "frame_bg":  "#161B22", "side_bg":   "#161B22",
        "btn_fg":    "#1C4E80", "btn_hover": "#2563A8",
        "border":    "#21262D", "text":      "#E6EDF3", "sub_text": "#8B949E",
    },
    "claro": {
        "appearance": "light",
        "janela_bg": "#F0F2F5", "header_bg": "#FFFFFF",
        "frame_bg":  "#FFFFFF", "side_bg":   "#F6F8FA",
        "btn_fg":    "#1C4E80", "btn_hover": "#2563A8",
        "border":    "#D0D7DE", "text":      "#1F2328", "sub_text": "#636C76",
    },
    "vermelho": {
        "appearance": "dark",
        "janela_bg": "#0A0000", "header_bg": "#1A0000",
        "frame_bg":  "#110000", "side_bg":   "#1A0000",
        "btn_fg":    "#8B0000", "btn_hover": "#CC0000",
        "border":    "#CC0000", "text":      "#FF6666", "sub_text": "#AA3333",
    },
}

def aplicar_tema(nome):
    t = TEMAS[nome]
    if bg_label_ref[0]:
        bg_label_ref[0].destroy()
        bg_label_ref[0] = None
    ctk.set_appearance_mode(t["appearance"])
    janela.configure(fg_color=t["janela_bg"])
    frame.configure(fg_color=t["frame_bg"], border_color=t["border"])
    side.configure(fg_color=t["side_bg"], border_color=t["border"])
    header.configure(fg_color=t["header_bg"], border_color=t["border"])
    for w in side.winfo_children():
        if isinstance(w, ctk.CTkButton):
            w.configure(fg_color=t["btn_fg"], hover_color=t["btn_hover"])
    if nome == "vermelho":
        caminho = ASSETS_DIR / "TIGRE_MALIGNO.jpg"
        if os.path.exists(caminho):
            try:
                ww = frame.winfo_width()  or 700
                hh = frame.winfo_height() or 600
                img  = Image.open(caminho).resize((ww, hh))
                foto = ImageTk.PhotoImage(img)
                bg   = ctk.CTkLabel(frame, image=foto, text="")
                bg.image = foto
                bg.place(x=0, y=0, relwidth=1, relheight=1)
                bg_label_ref[0] = bg
            except Exception:
                pass

def on_tema_change():
    aplicar_tema(tema_var.get())

# ─── HELPERS ─────────────────────────────────────────────────────────
def clear():
    if bg_label_ref[0]:
        bg_label_ref[0].destroy()
        bg_label_ref[0] = None
    for w in frame.winfo_children():
        w.destroy()

def titulo_pagina(texto):
    ctk.CTkLabel(
        frame, text=texto,
        font=("Segoe UI", 20, "bold"), text_color="#E6EDF3"
    ).pack(pady=(28, 4))
    ctk.CTkFrame(frame, height=1, fg_color="#21262D").pack(fill="x", padx=32, pady=(0, 20))

def entrada(placeholder, show=None):
    kw = dict(
        master=frame, placeholder_text=placeholder,
        width=420, height=44, font=("Segoe UI", 13),
        fg_color="#0D1117", border_color="#2D5F8A", border_width=1,
        corner_radius=10, text_color="#E6EDF3",
        placeholder_text_color="#484F58"
    )
    if show:
        kw["show"] = show
    e = ctk.CTkEntry(**kw)
    e.pack(pady=6)
    return e

def label_resultado():
    l = ctk.CTkLabel(frame, text="", font=("Segoe UI", 13), text_color="#8B949E")
    l.pack(pady=8)
    return l

def botao(texto, cmd):
    ctk.CTkButton(
        frame, text=texto, command=cmd,
        width=420, height=44,
        font=("Segoe UI", 13, "bold"),
        fg_color="#1C4E80", hover_color="#2563A8",
        corner_radius=10
    ).pack(pady=(4, 0))

def combobox(values):
    c = ctk.CTkComboBox(
        frame, values=values, width=420, height=44,
        font=("Segoe UI", 13),
        fg_color="#0D1117", border_color="#2D5F8A",
        button_color="#1C4E80", button_hover_color="#2563A8",
        dropdown_fg_color="#161B22",
        text_color="#E6EDF3"
    )
    c.pack(pady=6)
    return c

# ─── IMC ─────────────────────────────────────────────────────────────
def abrir_IMC():
    clear(); titulo_pagina("Calculadora de IMC")
    altura = entrada("Altura  ex: 1.75")
    peso   = entrada("Peso  ex: 70.5")
    res    = label_resultado()
    barra  = ctk.CTkProgressBar(frame, width=420, corner_radius=6); barra.pack(pady=6); barra.set(0)
    def calc():
        try:
            imc = float(peso.get()) / float(altura.get()) ** 2
            cor = "#E24B4A" if imc >= 30 else ("#FACC15" if imc >= 25 else ("#4ADE80" if imc >= 18.5 else "#FB923C"))
            res.configure(text=f"Seu IMC é: {imc:.2f}", text_color=cor)
            barra.set(min(imc / 40, 1.0))
        except ValueError:
            res.configure(text="Digite valores válidos!", text_color="#E24B4A")
    botao("Calcular IMC", calc)

# ─── TABUADA ─────────────────────────────────────────────────────────
def mutiplicacao():
    clear(); titulo_pagina("Tabuada")
    numero = entrada("Número da tabuada")
    res    = label_resultado()
    def calc():
        try:
            n   = int(numero.get())
            txt = "\n".join(f"{n} × {i} = {n*i}" for i in range(1, 11))
            res.configure(text=txt, text_color="#E6EDF3")
        except ValueError:
            res.configure(text="Digite um número válido!", text_color="#E24B4A")
    botao("Calcular Tabuada", calc)

# ─── CNPJ ────────────────────────────────────────────────────────────
def abrir_CNPJ():
    clear(); titulo_pagina("Buscador de CNPJ")
    cnpj = entrada("CNPJ  ex: 12345678000195")
    res  = label_resultado()
    def buscar():
        try:
            r = requests.get(f'https://api.opencnpj.org/{cnpj.get()}?dataset=receita').json()
            res.configure(text=f"CNPJ: {r['cnpj']}\nRazão Social: {r['razao_social']}\nFantasia: {r['nome_fantasia']}\nSituação: {r['situacao_cadastral']}", text_color="#E6EDF3")
        except Exception:
            res.configure(text="Erro ao buscar CNPJ!", text_color="#E24B4A")
    botao("Buscar CNPJ", buscar)

# ─── FATORIAL ────────────────────────────────────────────────────────
def abrir_fatorial():
    clear(); titulo_pagina("Calculadora de Fatorial")
    numero = entrada("Número para calcular o fatorial")
    res    = label_resultado()
    def calc():
        try:
            n = int(numero.get())
            if n < 0: res.configure(text="Fatorial não definido para negativos!", text_color="#E24B4A"); return
            fat = 1
            for i in range(1, n + 1): fat *= i
            res.configure(text=f"Fatorial de {n} = {fat}", text_color="#4ADE80")
        except ValueError:
            res.configure(text="Digite um número válido!", text_color="#E24B4A")
    botao("Calcular Fatorial", calc)

# ─── POTÊNCIA ────────────────────────────────────────────────────────
def abrir_potencia():
    clear(); titulo_pagina("Calculadora de Potência")
    base = entrada("Base"); exp = entrada("Expoente"); res = label_resultado()
    def calc():
        try:
            b, e = float(base.get()), float(exp.get())
            res.configure(text=f"{b} ^ {e} = {b**e}", text_color="#4ADE80")
        except ValueError:
            res.configure(text="Digite valores válidos!", text_color="#E24B4A")
    botao("Calcular Potência", calc)

# ─── RAIZ QUADRADA ───────────────────────────────────────────────────
def abrir_raiz():
    clear(); titulo_pagina("Raiz Quadrada")
    numero = entrada("Número"); res = label_resultado()
    def calc():
        try:
            n = float(numero.get())
            if n < 0: res.configure(text="Raiz não definida para negativos!", text_color="#E24B4A"); return
            res.configure(text=f"√{n} = {n**0.5:.4f}", text_color="#4ADE80")
        except ValueError:
            res.configure(text="Digite um número válido!", text_color="#E24B4A")
    botao("Calcular Raiz", calc)

# ─── ÁREA ────────────────────────────────────────────────────────────
def abrir_area():
    clear(); titulo_pagina("Calculadora de Área")
    base = entrada("Base"); alt = entrada("Altura"); raio = entrada("Raio (só para círculo)")
    combo = combobox(["Área do Triângulo", "Área do Retângulo", "Área do Círculo"])
    res   = label_resultado()
    def calc():
        try:
            op = combo.get()
            if op == "Área do Triângulo":   area = float(base.get()) * float(alt.get()) / 2
            elif op == "Área do Retângulo": area = float(base.get()) * float(alt.get())
            else:                           area = 3.14159 * float(raio.get()) ** 2
            res.configure(text=f"Área = {area:.4f}", text_color="#4ADE80")
        except ValueError:
            res.configure(text="Digite valores válidos!", text_color="#E24B4A")
    botao("Calcular Área", calc)

# ─── CEP ─────────────────────────────────────────────────────────────
def abrir_CEP():
    clear(); titulo_pagina("Busca de CEP")
    cep = entrada("CEP  ex: 01001000"); res = label_resultado()
    def buscar():
        try:
            d = requests.get(f"https://viacep.com.br/ws/{cep.get()}/json/").json()
            if "erro" not in d:
                res.configure(text=f"CEP: {d['cep']}\nLogradouro: {d['logradouro']}\nBairro: {d['bairro']}\nCidade: {d['localidade']} — {d['uf']}", text_color="#E6EDF3")
            else:
                res.configure(text="CEP não encontrado.", text_color="#E24B4A")
        except Exception:
            res.configure(text="Erro na busca!", text_color="#E24B4A")
    botao("Buscar CEP", buscar)

# ─── JUROS ───────────────────────────────────────────────────────────
def abrir_juros():
    clear(); titulo_pagina("Calculadora de Juros")
    principal = entrada("Valor principal (R$)")
    taxa      = entrada("Taxa de juros (% ao período)")
    periodo   = entrada("Número de períodos")
    combo     = combobox(["Juros Simples", "Juros Compostos"])
    res       = label_resultado()
    def calc():
        try:
            v, t, n = float(principal.get()), float(taxa.get()) / 100, float(periodo.get())
            if v <= 0 or t <= 0 or n <= 0: res.configure(text="Valores devem ser maiores que zero!", text_color="#E24B4A"); return
            j = v * t * n if combo.get() == "Juros Simples" else v * (1 + t) ** n - v
            res.configure(text=f"Principal: R${v:.2f}   Juros: R${j:.2f}   Total: R${v+j:.2f}", text_color="#4ADE80")
        except ValueError:
            res.configure(text="Digite valores válidos!", text_color="#E24B4A")
    botao("Calcular", calc)

# ─── PLANILHAS ───────────────────────────────────────────────────────
def abrir_planilhas():
    clear(); titulo_pagina("Análise de Planilhas")
    planilha = entrada("Caminho da planilha Excel"); res = label_resultado()
    def analisar():
        try:
            df = pd.read_excel(planilha.get())
            agrupado = df.groupby(['ID_Produto', 'Nome_Produto'])['Quantidade_Vendida'].sum()
            txt = "\n".join(f"ID: {i[0]} | {i[1]} | Qtd: {q}" for i, q in agrupado.items())
            res.configure(text=txt, text_color="#E6EDF3")
        except Exception as e:
            res.configure(text=f"Erro!\n{e}", text_color="#E24B4A")
    botao("Analisar Planilha", analisar)

# ─── GRÁFICO ─────────────────────────────────────────────────────────
def abrir_grafico():
    clear(); titulo_pagina("Gráfico de Planilhas")
    planilha = entrada("Caminho da planilha Excel"); res = label_resultado()
    def analisar():
        try:
            df = pd.read_excel(planilha.get())
            df['Data'] = pd.to_datetime(df['Data'])
            df.set_index('Data', inplace=True)
            df.resample('M').sum().plot(kind='bar', color='#2563A8')
            plt.tight_layout(); plt.show()
        except Exception as e:
            res.configure(text=f"Erro!\n{e}", text_color="#E24B4A")
    botao("Gerar Gráfico", analisar)

# ─── TEMAS ───────────────────────────────────────────────────────────
def abrir_temas():
    clear(); titulo_pagina("Configurações de Tema")
    opcoes = [
        ("escuro",   "🌙  Modo Escuro",     "#1C4E80", "#2563A8"),
        ("claro",    "☀️  Modo Claro",       "#1C4E80", "#2563A8"),
        ("vermelho", "🔴  Vermelho Maligno", "#8B0000", "#CC0000"),
    ]
    for valor, label, fg, hover in opcoes:
        ctk.CTkRadioButton(
            frame, text=label, variable=tema_var, value=valor,
            font=("Segoe UI", 14), text_color="#E6EDF3",
            fg_color=fg, hover_color=hover,
            command=on_tema_change, width=300, height=44
        ).pack(pady=10)
    caminho_img = ASSETS_DIR / "TIGRE_MALIGNO.jpg"
    if not os.path.exists(caminho_img):
        ctk.CTkLabel(
            frame, text="💡 Coloque 'TIGRE_MALIGNO.jpg' na mesma pasta para ativar o fundo vermelho.",
            font=("Segoe UI", 11), text_color="#484F58", justify="center"
        ).pack(pady=16)

# ─── BOTÕES DA SIDEBAR ───────────────────────────────────────────────
sections = [
    ("⚖  IMC",              abrir_IMC),
    ("🔢  Tabuada",          mutiplicacao),
    ("🏢  CNPJ",             abrir_CNPJ),
    ("!   Fatorial",         abrir_fatorial),
    ("^   Potência",         abrir_potencia),
    ("√   Raiz Quadrada",    abrir_raiz),
    ("📐  Área",             abrir_area),
    ("📮  CEP",              abrir_CEP),
    ("💰  Juros",            abrir_juros),
    ("📊  Planilhas",        abrir_planilhas),
    ("📈  Gráficos",         abrir_grafico),
    ("🎨  Temas",            abrir_temas),
]

for item, cmd in sections:
    ctk.CTkButton(
        side, text=item,
        fg_color="#1C4E80", hover_color="#2563A8",
        font=("Segoe UI", 12), height=38,
        corner_radius=10, anchor="w",
        command=cmd
    ).pack(pady=4, padx=10, fill="x")

janela.mainloop()