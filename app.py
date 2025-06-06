import customtkinter as ctk
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def janela_de_listas():
    cursor.execute("SELECT nome,lote,nota_fiscal,validade FROM produtos")
    lista = cursor.fetchall()

    janela = ctk.CTk()
    janela.title("listas dos Produtos")
    janela.geometry('800x800')
    janela.attributes('-fullscreen',True)

    frame_listas = ctk.CTkFrame(master=janela,width=400,height=400)
    frame_listas.pack(padx=20,pady=20,fill="both",expand=True)
    
    def  text_holder_framelistas():
        

        cabecalho_nome = ctk.CTkLabel(frame_listas, text="Nome", font=("Arial", 14, "bold"))
        cabecalho_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        cabecalho_lote = ctk.CTkLabel(frame_listas, text="Lote", font=("Arial", 14, "bold"))
        cabecalho_lote.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        cabecalho_nota = ctk.CTkLabel(frame_listas, text="Nota Fiscal", font=("Arial", 14, "bold"))
        cabecalho_nota.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        cabecalho_validade = ctk.CTkLabel(frame_listas, text="Validade", font=("Arial", 14, "bold"))
        cabecalho_validade.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    text_holder_framelistas()

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
    abrir_cadastro = ctk.CTkButton(janela,text="abrir jenela de cadastro",width=100,height=100,command=janela_cadastro)
    abrir_cadastro.pack(padx=20,pady=20)
    janela.mainloop()

def janela_cadastro():
    cadastro_janela = ctk.CTk()
    cadastro_janela.title("cadestre o item")
    cadastro_janela.geometry("800x800")
    def cadastrar():
        nome = nome_label.get()
        lote = lote_label.get()
        nota = notafiscal_label.get()
        validade = validade_label.get()


    confirmar_button = ctk.CTkButton(cadastro_janela,text="cadastrar",command=cadastrar(),width=100,height=100)
    confirmar_button.pack(padx=20,pady=20)
    
    info_frame = ctk.CTkFrame(cadastro_janela,width=400,height=400)
    texto = ctk.StringVar()
    numero = ctk.IntVar()

    nome_label = ctk.CTkEntry(info_frame,placeholder_text="nome do produto",textvariable=texto)
    lote_label =  ctk.CTkEntry(info_frame,placeholder_text="lote do produto",textvariable=numero)
    notafiscal_label =  ctk.CTkEntry(info_frame,placeholder_text="nota fiscal do produto"textvariable=numero)
    validade_label =  ctk.CTkEntry(info_frame,placeholder_text="validade do produto Ex:18092025")
    cadastro_janela.mainloop()

janela_de_listas()


