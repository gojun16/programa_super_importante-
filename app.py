import customtkinter as ctk
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT nome,lote,nota_fiscal,validade FROM produtos")
lista = cursor.fetchall()


janela = ctk.CTk()
janela.title("listas dos Produtos")
janela.geometry('800x800')
janela.attributes('-fullscreen',True)

frame_listas = ctk.CTkFrame(master=janela,width=400,height=400)
frame_listas.pack(padx=20,pady=20,fill="both",expand=True)


if lista:
     for i, (nome,lote,nota_fiscal,validade) in enumerate(lista):
      nome_label = ctk.CTkLabel(frame_listas,text="nome")
      nome_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
     
      lote_label = ctk.CTkLabel(frame_listas,text="lote")
      lote_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")
 
      nota_label = ctk.CTkLabel(frame_listas,text="nota fiscal")
      nota_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")
     
      validade_label = ctk.CTkLabel(frame_listas,text="validade")
      validade_label.grid(row=i, column=3, padx=10, pady=5, sticky="w")
else:
    # Se não tiver dados, exibe uma mensagem
    sem_dados_label = ctk.CTkLabel(frame_listas, text="Nenhum produto encontrado", font=("Arial", 16))
    sem_dados_label.pack(pady=20)

janela.mainloop()
