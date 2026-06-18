#Autor: Marco Antonio
import customtkinter as ctk
from PIL import Image
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela= ctk.CTk()
janela.title("Busca de CNPJ e CPF")
janela.geometry('450x500')

bg_image = ctk.CTkImage(Image.open('finados.jpg'), size=(450, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


tabviewcpf = ctk.CTkTabview(janela)
tabviewcpf.pack(pady=10, padx=10, fill='both', expand=True)
tabviewcpf.add("CPF")
tabviewcpf.add("CNPJ")
tabviewcpf.set("CPF")

aba_cpf = tabviewcpf.tab("CPF")

titulo = ctk.CTkLabel(aba_cpf, text="Busca de CPF", font=("Arial", 20))
titulo.pack(pady=10)
entrada = ctk.CTkEntry(aba_cpf, placeholder_text="Digite o CPF aqui", width=200, height=30, font=("Arial", 14))
entrada.pack(pady=10)

def busca():
    try:     
        cpf = entrada.get()
        url = f'https://api.cpfhub.io/cpf/{cpf}'
        token = '15fb9829763702195c4dd71892817a0dc6f864dd49da2ca26c22c4c4fd721bed'
        headers = {'x-api-key': token}
        res = requests.get(url, headers=headers)
        dados = res.json()
        label1cpf.configure(text=f"CPF: {dados['data'].get('cpf', 'N/A')}")
        label2cpf.configure(text=f"Nome: {dados['data'].get('name', 'N/A')}")
        label3cpf.configure(text=f"Data de Nascimento: {dados['data'].get('birthDate', 'N/A')}")
        label4cpf.configure(text=f"Sexo: {dados['data'].get('gender', 'N/A')}")
    except Exception as e:
        label1cpf.configure(text=f"Errooooouuu KKKKKKKKKKKKKKKKK")


botao = ctk.CTkButton(aba_cpf, text='Buscar', command=busca)
botao.pack(pady=10)


label1cpf = ctk.CTkLabel(tabviewcpf.tab("CPF"), text="")
label1cpf.pack(pady=10, padx=10)
label2cpf = ctk.CTkLabel(tabviewcpf.tab("CPF"), text="")
label2cpf.pack(pady=10, padx=10)
label3cpf = ctk.CTkLabel(tabviewcpf.tab("CPF"), text="")
label3cpf.pack(pady=10, padx=10)
label4cpf = ctk.CTkLabel(tabviewcpf.tab("CPF"), text="")
label4cpf.pack(pady=10, padx=10)

aba_cnpj = tabviewcpf.tab("CNPJ")
titulo_cnpj = ctk.CTkLabel(aba_cnpj, text="Busca de CNPJ", font=("Arial", 20))
titulo_cnpj.pack(pady=10)

entrada_cnpj = ctk.CTkEntry(aba_cnpj, placeholder_text="Digite o CNPJ aqui", width=200, height=30, font=("Arial", 14))
entrada_cnpj.pack(pady=10)


def busca_cnpj():
    try:
        cnpj = entrada_cnpj.get()
        url = f'https://api.opencnpj.org/{cnpj}?dataset=receita'
        res = requests.get(url)
        dados = res.json()
        label1cnpj.configure(text=f"CNPJ: {dados['cnpj']}")
        label2cnpj.configure(text=f"Razão Social: {dados['razao_social']}")
        label3cnpj.configure(text=f"Nome Fantasia: {dados['nome_fantasia']}")
        label4cnpj.configure(text=f"Situação Cadastral: {dados['situacao_cadastral']}")
    except Exception as e:
        label1cnpj.configure(text=f"Errooooouuu KKKKKKKKKKKKKKKKK")

     
botao_cnpj = ctk.CTkButton(aba_cnpj, text='Buscar', command=busca_cnpj)
botao_cnpj.pack(pady=10)

label1cnpj = ctk.CTkLabel(tabviewcpf.tab("CNPJ"), text="")
label1cnpj.pack(pady=10, padx=10)
label2cnpj = ctk.CTkLabel(tabviewcpf.tab("CNPJ"), text="")
label2cnpj.pack(pady=10, padx=10)
label3cnpj = ctk.CTkLabel(tabviewcpf.tab("CNPJ"), text="")
label3cnpj.pack(pady=10, padx=10)
label4cnpj = ctk.CTkLabel(tabviewcpf.tab("CNPJ"), text="")
label4cnpj.pack(pady=10, padx=10)

janela.mainloop()