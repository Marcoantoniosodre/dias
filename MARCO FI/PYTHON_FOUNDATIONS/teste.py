import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"

resp = requests.get(url, timeout=10)
img = Image.open(BytesIO(resp.content)).convert("RGBA")

print("Modo:", img.mode)
print("Tamanho:", img.size)

# Criar fundo escuro e colar o sprite em cima
fundo = Image.new("RGBA", img.size, (30, 30, 46, 255))
fundo.paste(img, (0, 0), img)
fundo = fundo.resize((240, 240), Image.LANCZOS)

# Mostrar numa janela simples
root = tk.Tk()
foto = ImageTk.PhotoImage(fundo.convert("RGB"))
label = tk.Label(root, image=foto)
label.pack()
root.mainloop()