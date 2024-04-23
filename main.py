import tkinter as tk
from tkinter import filedialog
import dividirPag
import os

def selecionarArquivoOrigem():
    arquivoOrigem = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if arquivoOrigem:
        entradaOrigem.delete(0, tk.END)
        entradaOrigem.insert(0, arquivoOrigem)

def selecionarPastaDestino():
    pastaDestino = filedialog.askdirectory()
    if pastaDestino:
        entradaDestino.delete(0, tk.END)
        entradaDestino.insert(0, pastaDestino)

def iniciar_processamento():
    origem = entradaOrigem.get()
    destino = entradaDestino.get()
    if origem and destino:
        if os.path.isfile(origem):  # Verifica se o caminho de origem é um arquivo
            if os.path.isdir(destino):  # Verifica se o caminho de destino é um diretório
                dividirPag.dividirPaginas(origem, destino)
                tk.messagebox.showinfo("Processamento Concluído", "O processamento foi concluído com sucesso!")
            else:
                tk.messagebox.showerror("Erro", "O destino precisa ser um diretório válido.")
        else:
            tk.messagebox.showerror("Erro", "A origem precisa ser um arquivo PDF.")

# Criando a janela principal
root = tk.Tk()
root.title("Processamento de PDFs do Holerite")

# Criando frames
frameOrigem = tk.Frame(root)
frameDestino = tk.Frame(root)
frameBotoes = tk.Frame(root)

# Labels
labelOrigem = tk.Label(frameOrigem, text="Arquivo de Origem:")
labelDestino = tk.Label(frameDestino, text="Pasta de Destino:")

# Entries
entradaOrigem = tk.Entry(frameOrigem, width=50)
entradaDestino = tk.Entry(frameDestino, width=50)

# Botões
botaoOrigem = tk.Button(frameOrigem, text="Selecionar Arquivo", command=selecionarArquivoOrigem)
botaoDestino = tk.Button(frameDestino, text="Selecionar Pasta", command=selecionarPastaDestino)
processarBotao = tk.Button(frameBotoes, text="Processar", command=iniciar_processamento)

# Colocando widgets na tela
labelOrigem.pack(side=tk.LEFT)
entradaOrigem.pack(side=tk.LEFT)
botaoOrigem.pack(side=tk.LEFT)

labelDestino.pack(side=tk.LEFT)
entradaDestino.pack(side=tk.LEFT)
botaoDestino.pack(side=tk.LEFT)

processarBotao.pack()

# Empacotando frames
frameOrigem.pack(pady=5)
frameDestino.pack(pady=5)
frameBotoes.pack(pady=5)

# Assinatura
labelAssinatura = tk.Label(root, text="Vida Veg - GustavoTI", font=("Arial", 10), fg="gray")
labelAssinatura.pack(side=tk.BOTTOM, pady=10)

# Iniciando o loop da interface
root.mainloop()
