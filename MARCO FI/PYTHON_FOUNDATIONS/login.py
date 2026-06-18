# Autor: Marco Antonio
# Tela de login multitools

import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    btn_login.configure(state="disabled", text="Entrando...")
    janela.after(400, lambda: verificar_login(usuario, senha))


def verificar_login(usuario, senha):
    if usuario == 'Marco' and senha == '1312007ma':
        janela.destroy()
        import PALHAÇADINHA14
    else:
        label_erro.configure(text="Usuário ou senha incorretos")
        entry_usuario.configure(border_color="white")
        entry_senha.configure(border_color="white")
        btn_login.configure(state="normal", text="Entrar")
        janela.after(2500, limpar_erro)


def limpar_erro():
    label_erro.configure(text="")
    entry_usuario.configure(border_color="#444444")
    entry_senha.configure(border_color="#444444")


def on_enter_key(event):
    login()


# ─── Janela ──────────────────────────────────────────────────────────
janela = ctk.CTk()
janela.geometry('420x420')
janela.title('Multi Ferramentas')
janela.resizable(False, False)
janela.configure(fg_color="#0D1117")

# ─── Card central ────────────────────────────────────────────────────
card = ctk.CTkFrame(
    janela,
    fg_color="#161B22",
    corner_radius=12,
    border_width=1,
    border_color="white"
)
card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85)

# ─── Título ──────────────────────────────────────────────────────────
ctk.CTkLabel(
    card,
    text="Multi Ferramentas",
    font=("Segoe UI", 20, "bold"),
    text_color="#E6EDF3"
).pack(pady=(30, 4))

ctk.CTkLabel(
    card,
    text="Faça login para continuar",
    font=("Segoe UI", 12),
    text_color="#8B949E"
).pack(pady=(0, 20))

# ─── Separador ───────────────────────────────────────────────────────
ctk.CTkFrame(card, height=1, fg_color="white").pack(fill="x", padx=28, pady=(0, 20))

# ─── Usuário ─────────────────────────────────────────────────────────
frame_u = ctk.CTkFrame(card, fg_color="transparent")
frame_u.pack(padx=28, fill="x")

ctk.CTkLabel(frame_u, text="USUÁRIO", font=("Segoe UI", 10, "bold"),
             text_color="#8B949E", anchor="w").pack(fill="x", pady=(0, 5))

entry_usuario = ctk.CTkEntry(
    frame_u, height=42, font=("Segoe UI", 13),
    fg_color="#0D1117", border_color="#444444", border_width=1,
    corner_radius=8, text_color="#E6EDF3",
    placeholder_text="Digite seu usuário", placeholder_text_color="#484F58"
)
entry_usuario.pack(fill="x")
entry_usuario.bind("<Return>", on_enter_key)

# ─── Senha ───────────────────────────────────────────────────────────
frame_s = ctk.CTkFrame(card, fg_color="transparent")
frame_s.pack(padx=28, fill="x", pady=(14, 0))

ctk.CTkLabel(frame_s, text="SENHA", font=("Segoe UI", 10, "bold"),
             text_color="#8B949E", anchor="w").pack(fill="x", pady=(0, 5))

entry_senha = ctk.CTkEntry(
    frame_s, height=42, font=("Segoe UI", 13),
    fg_color="#0D1117", border_color="#444444", border_width=1,
    corner_radius=8, text_color="#E6EDF3",
    placeholder_text="Digite sua senha", placeholder_text_color="#484F58",
    show="*"
)
entry_senha.pack(fill="x")
entry_senha.bind("<Return>", on_enter_key)

# ─── Erro ────────────────────────────────────────────────────────────
label_erro = ctk.CTkLabel(card, text="", font=("Segoe UI", 12), text_color="#E24B4A")
label_erro.pack(pady=(10, 0))

# ─── Botão ───────────────────────────────────────────────────────────
btn_login = ctk.CTkButton(
    card, text="Entrar",
    font=("Segoe UI", 13, "bold"),
    height=44, corner_radius=8,
    fg_color="#1C4E80", hover_color="#2563A8",
    text_color="#FFFFFF", command=login
)
btn_login.pack(padx=28, fill="x", pady=(8, 0))

# ─── Rodapé ──────────────────────────────────────────────────────────
ctk.CTkLabel(card, text="v1.0  ·  Marco Antonio",
             font=("Segoe UI", 10), text_color="#484F58").pack(pady=(16, 24))

entry_usuario.focus()
janela.mainloop()