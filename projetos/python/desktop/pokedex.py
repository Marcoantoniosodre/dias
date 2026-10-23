# Autor: Marco Antonio
# Projeto: Pokédex Visual PRO (v2 — imagens corrigidas)

import customtkinter as ctk
import requests
from PIL import Image
from io import BytesIO
import threading

# ─────────────────────────────────────────────
# CORES POR TIPO
# ─────────────────────────────────────────────
CORES_TIPO = {
    "Fire":     "#e74c3c", "Water":    "#3498db", "Grass":    "#27ae60",
    "Electric": "#f1c40f", "Psychic":  "#9b59b6", "Ice":      "#74b9ff",
    "Dragon":   "#6c3483", "Dark":     "#2c3e50", "Fairy":    "#fd79a8",
    "Normal":   "#636e72", "Fighting": "#d35400", "Flying":   "#5dade2",
    "Poison":   "#8e44ad", "Ground":   "#f39c12", "Rock":     "#7f8c8d",
    "Bug":      "#a3cb38", "Ghost":    "#6c3483", "Steel":    "#95a5a6",
}

# ─────────────────────────────────────────────
# ESTADO GLOBAL
# ─────────────────────────────────────────────
pokemon_id_atual = 1
dados_cache = {}
# FIX: lista para manter referência FORTE da imagem e evitar GC deletar
_refs_imagem = []

# ─────────────────────────────────────────────
# JANELA
# ─────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("1000x720")
janela.title("Pokédex PRO")
janela.resizable(False, False)

# ─────────────────────────────────────────────
# FUNÇÕES AUXILIARES
# ─────────────────────────────────────────────

def carregar_imagem(url, tamanho=(240, 240)):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()

        img = Image.open(BytesIO(resp.content)).convert("RGBA")
        fundo = Image.new("RGBA", tamanho, "#1a1a2e")
        img.thumbnail(tamanho, Image.LANCZOS)
        x = (tamanho[0] - img.width) // 2
        y = (tamanho[1] - img.height) // 2
        fundo.alpha_composite(img, (x, y))

        return ctk.CTkImage(
            light_image=fundo,
            dark_image=fundo,
            size=tamanho
        )

    except Exception as e:
        print(f"[ERRO imagem] {e}")
        return None


def melhor_url(sprites, variante="normal"):
    other = sprites.get("other", {})
    art   = other.get("official-artwork", {})
    home  = other.get("home", {})

    if variante == "shiny":
        return (
            art.get("front_shiny")
            or home.get("front_shiny")
            or sprites.get("front_shiny")
            or sprites.get("front_default")
        )
    else:
        return (
            art.get("front_default")
            or home.get("front_default")
            or sprites.get("front_default")
        )


def cor_do_tipo(tipo_str):
    primeiro = tipo_str.split(",")[0].strip()
    return CORES_TIPO.get(primeiro, "#2d3436")


def mostrar_loading(ativo=True):
    if ativo:
        label_loading.configure(text="⏳ Carregando...")
        # FIX: ao mostrar loading, limpa a imagem corretamente
        label_imagem.configure(image=ctk.CTkImage(
            light_image=Image.new("RGBA", (240, 240), "#1a1a2e"),
            dark_image=Image.new("RGBA", (240, 240), "#1a1a2e"),
            size=(240, 240)
        ), text="")
    else:
        label_loading.configure(text="")


def atualizar_badges(tipos_str):
    for w in frame_tipos.winfo_children():
        w.destroy()
    for t in tipos_str.split(", "):
        cor = CORES_TIPO.get(t.strip(), "#636e72")
        ctk.CTkLabel(
            frame_tipos, text=f"  {t.strip()}  ",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=cor, corner_radius=8, text_color="white"
        ).pack(side="left", padx=4)


def atualizar_stats(stats):
    for w in frame_stats_inner.winfo_children():
        w.destroy()
    for i, stat in enumerate(stats):
        nome  = stat["stat"]["name"].upper().replace("-", " ")
        valor = stat["base_stat"]
        cor   = "#27ae60" if valor >= 80 else "#f39c12" if valor >= 50 else "#e74c3c"

        ctk.CTkLabel(
            frame_stats_inner, text=f"{nome:<13}", width=115,
            font=ctk.CTkFont(size=11), anchor="w"
        ).grid(row=i, column=0, sticky="w", padx=(5, 0))

        ctk.CTkLabel(
            frame_stats_inner, text=f"{valor:>3}",
            font=ctk.CTkFont(size=11, weight="bold"), width=35
        ).grid(row=i, column=1, padx=4)

        barra = ctk.CTkProgressBar(
            frame_stats_inner, width=160, height=12, progress_color=cor
        )
        barra.set(min(valor / 255, 1.0))
        barra.grid(row=i, column=2, padx=(0, 5), pady=2)


# ─────────────────────────────────────────────
# EXIBIÇÃO
# ─────────────────────────────────────────────

def exibir_pokemon(dados, variante="normal"):
    global pokemon_id_atual
    pokemon_id_atual = dados["id"]

    sprites   = dados.get("sprites", {})
    tipos_str = ", ".join([t["type"]["name"].capitalize() for t in dados["types"]])
    cor_tema  = cor_do_tipo(tipos_str)
    nome_disp = dados["name"].replace("-", " ").title()

    # Header
    label_id.configure(text=f"#{dados['id']:04d}", text_color="#fff")
    label_nome.configure(text=nome_disp, text_color="#fff")
    frame_header.configure(fg_color=cor_tema)

    # Badges e info
    atualizar_badges(tipos_str)
    altura = dados.get("height", 0) / 10
    peso   = dados.get("weight", 0) / 10
    label_info.configure(text=f"📏 {altura} m     ⚖️ {peso} kg", text_color="#fff")

    habs = [h["ability"]["name"].replace("-", " ").title()
            for h in dados.get("abilities", [])]
    label_habs.configure(text="🎯  " + "  •  ".join(habs))

    atualizar_stats(dados.get("stats", []))

    # Badge de variante
    badges = {
        "shiny": ("✨ SHINY",       "#f1c40f"),
        "mega":  ("⚡ MEGA",        "#9b59b6"),
        "gmax":  ("🌀 GIGANTAMAX",  "#e74c3c"),
    }
    if variante in badges:
        label_variante.configure(text=badges[variante][0],
                                  text_color=badges[variante][1])
    else:
        label_variante.configure(text="")

    url = melhor_url(sprites, variante)
    print(f"[DEBUG] #{dados['id']} {variante} → {url}")

    mostrar_loading(True)

    def _thread():
        foto = carregar_imagem(url) if url else None
        janela.after(0, lambda: _aplicar_imagem(foto))

    threading.Thread(target=_thread, daemon=True).start()


def _aplicar_imagem(foto):
    global _refs_imagem

    mostrar_loading(False)

    if foto:
        # FIX: guarda referência forte na lista global — impede o GC de deletar
        _refs_imagem = [foto]

        # FIX: configura image e text separadamente para evitar bug do CTkLabel
        label_imagem.configure(text="")
        label_imagem.configure(image=foto)

    else:
        label_imagem.configure(image=None, text="❌ Sem imagem")
        _refs_imagem = []


# ─────────────────────────────────────────────
# BUSCA E NAVEGAÇÃO
# ─────────────────────────────────────────────

def buscar_por_id_ou_nome(valor):
    chave = str(valor).strip().lower()
    if chave in dados_cache:
        return dados_cache[chave], None
    try:
        r = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{chave}", timeout=10
        )
        r.raise_for_status()
        d = r.json()
        dados_cache[chave]        = d
        dados_cache[str(d["id"])] = d
        return d, None
    except requests.HTTPError:
        if r.status_code == 404:
            return None, "Pokémon não encontrado."
        return None, f"Erro HTTP {r.status_code}"
    except Exception as e:
        return None, f"Erro: {e}"


def _pos_busca(dados, erro):
    if erro or not dados:
        mostrar_loading(False)
        label_nome.configure(text=erro or "Erro", text_color="#e74c3c")
        label_imagem.configure(image=None, text="")
        return
    exibir_pokemon(dados, "normal")


def buscar_pokemon():
    termo = entrada_busca.get().strip().lower()
    if not termo:
        return
    mostrar_loading(True)
    threading.Thread(
        target=lambda: janela.after(
            0, lambda: _pos_busca(*buscar_por_id_ou_nome(termo))
        ), daemon=True
    ).start()


def navegar(direcao):
    novo_id = pokemon_id_atual + direcao
    if novo_id < 1:    novo_id = 1010
    if novo_id > 1010: novo_id = 1
    mostrar_loading(True)
    threading.Thread(
        target=lambda: janela.after(
            0, lambda: _pos_busca(*buscar_por_id_ou_nome(str(novo_id)))
        ), daemon=True
    ).start()


def mudar_variante(variante):
    chave = str(pokemon_id_atual)
    if chave not in dados_cache:
        return

    dados_base = dados_cache[chave]
    nome_base  = dados_base["name"]

    if variante in ("mega", "gmax"):
        sufixo = "-mega" if variante == "mega" else "-gmax"
        mostrar_loading(True)

        def _thread():
            dados_var, _ = buscar_por_id_ou_nome(nome_base + sufixo)
            if dados_var:
                janela.after(0, lambda: exibir_pokemon(dados_var, variante))
            else:
                nome_v = "Mega" if variante == "mega" else "Gigantamax"
                janela.after(0, lambda: _sem_variante(nome_v))

        threading.Thread(target=_thread, daemon=True).start()
    else:
        exibir_pokemon(dados_base, variante)


def _sem_variante(nome_v):
    mostrar_loading(False)
    label_variante.configure(
        text=f"⚠️ Sem forma {nome_v}", text_color="#e74c3c"
    )


# ─────────────────────────────────────────────
# LAYOUT — PAINEL ESQUERDO
# ─────────────────────────────────────────────
frame_esq = ctk.CTkFrame(janela, width=230, corner_radius=14)
frame_esq.pack(side="left", fill="y", padx=(12, 6), pady=12)
frame_esq.pack_propagate(False)

frame_logo = ctk.CTkFrame(frame_esq, corner_radius=10,
                            fg_color="#cc0000", border_width=2, border_color="#ff4444")
ctk.CTkLabel(
    frame_logo, text="◉  Pokédex",
    font=ctk.CTkFont(size=22, weight="bold"), text_color="white"
).pack(pady=12)
frame_logo.pack(pady=(18, 8), padx=16, fill="x")

ctk.CTkLabel(frame_esq, text="Nome ou número:",
             font=ctk.CTkFont(size=12)).pack(pady=(14, 4))

entrada_busca = ctk.CTkEntry(
    frame_esq, placeholder_text="pikachu, 25...",
    width=190, height=34, font=ctk.CTkFont(size=13)
)
entrada_busca.pack(pady=4)
entrada_busca.bind("<Return>", lambda e: buscar_pokemon())

ctk.CTkButton(
    frame_esq, text="🔍  Buscar", width=190, height=34,
    font=ctk.CTkFont(size=13, weight="bold"),
    fg_color="#cc0000", hover_color="#e74c3c",
    command=buscar_pokemon
).pack(pady=(4, 16))

ctk.CTkFrame(frame_esq, height=2, fg_color="#444").pack(fill="x", padx=16)

ctk.CTkLabel(frame_esq, text="Navegar:",
             font=ctk.CTkFont(size=12)).pack(pady=(14, 6))

frame_nav = ctk.CTkFrame(frame_esq, fg_color="transparent")
frame_nav.pack()

ctk.CTkButton(
    frame_nav, text="◀️ Ant.", width=88, height=34,
    font=ctk.CTkFont(size=12, weight="bold"),
    command=lambda: navegar(-1)
).grid(row=0, column=0, padx=4)

ctk.CTkButton(
    frame_nav, text="Próx. ▶️", width=88, height=34,
    font=ctk.CTkFont(size=12, weight="bold"),
    command=lambda: navegar(1)
).grid(row=0, column=1, padx=4)

ctk.CTkFrame(frame_esq, height=2, fg_color="#444").pack(fill="x", padx=16, pady=16)

ctk.CTkLabel(frame_esq, text="Variantes:",
             font=ctk.CTkFont(size=12)).pack(pady=(0, 8))

VARIANTES = [
    ("⚪  Normal",      "normal",  "#2d3436", "#636e72"),
    ("✨  Shiny",       "shiny",   "#b7950b", "#f1c40f"),
    ("⚡  Mega",        "mega",    "#6c3483", "#9b59b6"),
    ("🌀  Gigantamax",  "gmax",    "#922b21", "#e74c3c"),
]
for texto, modo, cor, hover in VARIANTES:
    ctk.CTkButton(
        frame_esq, text=texto, width=190, height=32,
        font=ctk.CTkFont(size=12, weight="bold"),
        fg_color=cor, hover_color=hover,
        command=lambda m=modo: mudar_variante(m)
    ).pack(pady=3)

ctk.CTkLabel(
    frame_esq, text="PokeAPI  •  #1 – #1010",
    font=ctk.CTkFont(size=10), text_color="#555"
).pack(side="bottom", pady=10)

# ─────────────────────────────────────────────
# LAYOUT — PAINEL DIREITO
# ─────────────────────────────────────────────
frame_dir = ctk.CTkFrame(janela, corner_radius=14)
frame_dir.pack(side="left", fill="both", expand=True, padx=(6, 12), pady=12)

frame_header = ctk.CTkFrame(frame_dir, corner_radius=10, fg_color="#2d3436")
frame_header.pack(fill="x", padx=14, pady=(14, 6))

label_id = ctk.CTkLabel(
    frame_header, text="#0000",
    font=ctk.CTkFont(size=13), text_color="#aaa"
)
label_id.pack(side="right", padx=14)

label_nome = ctk.CTkLabel(
    frame_header, text="— Pokédex PRO —",
    font=ctk.CTkFont(size=26, weight="bold"), text_color="#fff"
)
label_nome.pack(side="left", padx=14, pady=10)

label_variante = ctk.CTkLabel(
    frame_dir, text="",
    font=ctk.CTkFont(size=13, weight="bold")
)
label_variante.pack(pady=(2, 0))

frame_tipos = ctk.CTkFrame(frame_dir, fg_color="transparent")
frame_tipos.pack(pady=6)

frame_img = ctk.CTkFrame(frame_dir, corner_radius=12, fg_color="#1a1a2e")
frame_img.pack(pady=8)

# FIX: inicia o label_imagem SEM image=None — passa uma imagem em branco
_img_placeholder = ctk.CTkImage(
    light_image=Image.new("RGBA", (240, 240), "#1a1a2e"),
    dark_image=Image.new("RGBA", (240, 240), "#1a1a2e"),
    size=(240, 240)
)
label_imagem = ctk.CTkLabel(
    frame_img,
    text="Busque um Pokémon 👆",
    image=_img_placeholder,
    compound="top",          # texto em cima da imagem placeholder
    font=ctk.CTkFont(size=14),
    fg_color="#1a1a2e"
)
label_imagem.pack(pady=16, padx=16)

label_loading = ctk.CTkLabel(
    frame_img, text="",
    font=ctk.CTkFont(size=13), text_color="#aaa"
)
label_loading.pack(pady=(0, 8))

label_info = ctk.CTkLabel(
    frame_dir, text="",
    font=ctk.CTkFont(size=12), text_color="#bbb"
)
label_info.pack(pady=3)

label_habs = ctk.CTkLabel(
    frame_dir, text="",
    font=ctk.CTkFont(size=12), text_color="#74b9ff"
)
label_habs.pack(pady=2)

ctk.CTkLabel(
    frame_dir, text="BASE STATS",
    font=ctk.CTkFont(size=11, weight="bold"), text_color="#666"
).pack(pady=(8, 2))

frame_stats_outer = ctk.CTkFrame(frame_dir, corner_radius=8, fg_color="#1e1e1e")
frame_stats_outer.pack(fill="x", padx=14, pady=(0, 10))

frame_stats_inner = ctk.CTkFrame(frame_stats_outer, fg_color="transparent")
frame_stats_inner.pack(padx=8, pady=8)

# ─────────────────────────────────────────────
# INICIA COM BULBASAUR
# ─────────────────────────────────────────────
def _inicio():
    dados, _ = buscar_por_id_ou_nome("1")
    if dados:
        janela.after(0, lambda: _pos_busca(dados, None))

threading.Thread(target=_inicio, daemon=True).start()

janela.mainloop()