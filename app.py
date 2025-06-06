import customtkinter as ctk
import sqlite3
from datetime import datetime

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

            cursor.execute("INSERT INTO produtos (nome, lote, nota_fiscal, validade) VALUES (?, ?, ?, ?, ?)",
                           (nome, lote, nota, data_iso, quantidade))
            conn.commit()
            print("Produto cadastrado com sucesso.")
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

def janela_de_listas():
    cursor.execute("SELECT nome, lote, nota_fiscal, validade, quantidade FROM produtos")
    lista = cursor.fetchall()

    janela = ctk.CTk()
    janela.title("Lista dos Produtos")
    janela.geometry('1000x600')
    janela.attributes('-fullscreen', True)

    frame_listas = ctk.CTkFrame(master=janela)
    frame_listas.grid(row=0, column=0, padx=20, pady=20)

    # Cabeçalhos
    headers = ["Nome", "Lote", "Nota Fiscal", "Validade, Quantidade"]
    for idx, title in enumerate(headers):
        cabecalho = ctk.CTkLabel(frame_listas, text=title, font=("Arial", 14, "bold"))
        cabecalho.grid(row=0, column=idx, padx=10, pady=10, sticky="w")

    if lista:
        for i, (nome, lote, nota_fiscal, validade, quantidade) in enumerate(lista, start=1):
            nome_label = ctk.CTkLabel(frame_listas, text=nome)
            nome_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            lote_label = ctk.CTkLabel(frame_listas, text=lote)
            lote_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            nota_label = ctk.CTkLabel(frame_listas, text=nota_fiscal)
            nota_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")

            validade_label = ctk.CTkLabel(frame_listas, text=validade)
            validade_label.grid(row=i, column=3, padx=10, pady=5, sticky="w")

            quantidade_label = ctk.CTkLabel(frame_listas, text=quantidade)
            quantidade_label.grid(row=i, column=4, padx=10, pady=5, sticky="w")
    else:
        sem_dados_label = ctk.CTkLabel(frame_listas, text="Nenhum produto encontrado", font=("Arial", 16))
        sem_dados_label.grid(row=1, column=0, columnspan=4, pady=20)

    abrir_cadastro = ctk.CTkButton(janela, text="Abrir janela de cadastro", width=200, height=50, command=janela_cadastro)
    abrir_cadastro.grid(row=1, column=0, pady=20)

    janela.mainloop()

# Iniciar a aplicação
janela_de_listas()
