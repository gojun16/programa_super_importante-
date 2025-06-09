import customtkinter as ctk
import sqlite3
from datetime import datetime
from PIL import Image

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def janela_cadastro():

    cadastro_janela = ctk.CTkToplevel()
    cadastro_janela.title("Cadastre o item")
    cadastro_janela.geometry("600x400")

    def cadastrar():
        nome = nome_entry.get()
        lote = lote_entry.get()
        nota = nota_entry.get()
        validade = validade_entry.get()
        quantidade = quantidade_entry.get()

        try:
            # Tenta converter a validade para ISO, validando formato
            data_iso = datetime.strptime(validade, "%d%m%Y").date().isoformat()

            cursor.execute("INSERT INTO produtos (nome, lote, nota_fiscal, validade, quantidade) VALUES (?, ?, ?, ?, ?)",
                           (nome, lote, nota, data_iso, quantidade))
            conn.commit()
            print("Produto cadastrado com sucesso.")
            atualizar_lista()
            cadastro_janela.destroy()

        except ValueError:
            print("Data inválida. Use o formato DDMMAAAA.")

    info_frame = ctk.CTkFrame(cadastro_janela)
    info_frame.grid(row=0, column=0, padx=20, pady=20)

    nome_entry = ctk.CTkEntry(info_frame, placeholder_text="Nome do produto")
    nome_entry.grid(row=0, column=0, padx=5, pady=5)

    lote_entry = ctk.CTkEntry(info_frame, placeholder_text="Lote")
    lote_entry.grid(row=1, column=0, padx=5, pady=5)

    nota_entry = ctk.CTkEntry(info_frame, placeholder_text="Nota Fiscal")
    nota_entry.grid(row=2, column=0, padx=5, pady=5)

    validade_entry = ctk.CTkEntry(info_frame, placeholder_text="Validade (ex: 18092025)")
    validade_entry.grid(row=3, column=0, padx=5, pady=5)

    quantidade_entry = ctk.CTkEntry(info_frame, placeholder_text="Quantidade")
    quantidade_entry.grid(row=4, column=0, padx=5, pady=5)

    confirmar_button = ctk.CTkButton(info_frame, text="Cadastrar", command=cadastrar)
    confirmar_button.grid(row=5, column=0, padx=10, pady=15)
    




janela = ctk.CTk()
janela.title("Listas dos Produtos")
janela.geometry('800x600')
frame_listas = ctk.CTkFrame(janela)
frame_listas.grid(row=0, column=0, padx=20, pady=20)

def janela_de_listas():
   

    cursor.execute("SELECT nome, lote, nota_fiscal, validade, quantidade FROM produtos")
    lista = cursor.fetchall()

    # Cabeçalhos
    headers = ["Nome", "Lote", "Nota Fiscal", "Validade", "Quantidade"]
    for idx, title in enumerate(headers):
        cabecalho = ctk.CTkLabel(frame_listas, text=title, font=("Arial", 14, "bold"))
        cabecalho.grid(row=0, column=idx, padx=10, pady=10, sticky="w")

    if lista:
        for i, (nome, lote, nota_fiscal, validade, quantidade) in enumerate(lista, start=1):
            ctk.CTkLabel(frame_listas, text=nome).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=lote).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=nota_fiscal).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=validade).grid(row=i, column=3, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=quantidade).grid(row=i, column=4, padx=10, pady=5, sticky="w")
    else:
        sem_dados_label = ctk.CTkLabel(frame_listas, text="Nenhum produto encontrado", font=("Arial", 16))
        sem_dados_label.grid(row=1, column=0, columnspan=5, pady=20)

abrir_cadastro = ctk.CTkButton(janela, text="Abrir janela de cadastro", width=200, height=50, command=janela_cadastro)
abrir_cadastro.grid(row=1, column=0, pady=20)


def atualizar_lista():
    global frame_listas
    for widget in frame_listas.winfo_children():
        widget.destroy()

    cursor.execute("SELECT nome, lote, nota_fiscal, validade, quantidade FROM produtos")
    lista = cursor.fetchall()

    # Cabeçalhos
    headers = ["Nome", "Lote", "Nota Fiscal", "Validade", "Quantidade"]
    for idx, title in enumerate(headers):
        cabecalho = ctk.CTkLabel(frame_listas, text=title, font=("Arial", 14, "bold"))
        cabecalho.grid(row=1, column=idx, padx=10, pady=10, sticky="w")

    if lista:
        for i, (nome, lote, nota_fiscal, validade, quantidade) in enumerate(lista, start=1):
            ctk.CTkLabel(frame_listas, text=nome).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=lote).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=nota_fiscal).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=validade).grid(row=i, column=3, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(frame_listas, text=quantidade).grid(row=i, column=4, padx=10, pady=5, sticky="w")
            pass
    else:
       sem_dados_label = ctk.CTkLabel(frame_listas, text="Nenhum produto encontrado", font=("Arial", 16))
       sem_dados_label.grid(row=1, column=0, columnspan=5, pady=20)
    pass
refresh_img = ctk.CTkImage(Image.open("Refresh_icon.png"),size=(30,30))
botao_refresh = ctk.CTkButton(janela, text="", command=atualizar_lista,image=refresh_img,width=30,height=30)
botao_refresh.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky="e")

janela_de_listas()  # chama para montar a lista na inicialização
janela.mainloop()
