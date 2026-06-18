#Autor: Marco Antonio
#Snap tube do DIABOO

import customtkinter as ctk
from pytubefix import YouTube
from PIL import Image, ImageTk

# configurações visuais 

def baixar():
    link_youtube = link.get()
    yt= YouTube(link_youtube)
    yt.streams.first().download()
    status.configure(text='Baixou o Renato Garcia')

janela = ctk.CTk()
janela.title('BLOX FRUITS')
janela.geometry("400x500")

janela.iconbitmap('TIGRE_MALIGNO.ico')


bg_image = ctk.CTkImage(Image.open('TIGRE_MALIGNO.jpg'), size=(400, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text='')
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)




#Elementos da tela 
titulo = ctk.CTkLabel(janela, text='SNAPTUBE V2 MALÉFICO ', font=('Arial', 20), text_color= "#00070E", text_color_disabled= 'black')
titulo.pack(pady=20)

link = ctk.CTkEntry(janela, placeholder_text='Digite o link aqui paspalho: ', width=400, height=30, font=('Arial', 14), placeholder_text_color= "grey",)
link.pack(pady=20)

dowloand = ctk.CTkButton(janela, text= 'Baixar', command= baixar, fg_color= "green", hover_color= "blue")
dowloand.pack(pady=20)

status = ctk.CTkLabel(janela, text = '')
status.pack(pady=20)       

janela.mainloop()