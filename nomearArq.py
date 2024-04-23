import re
from PyPDF2 import PdfReader

def extrairNome(texto):
    padrao = r'Nº Reg. Chapa Nome\s*\d+\s*([\w\s]+)\s*Cód'
    resultado = re.search(padrao, texto)
    if resultado:
        nome = resultado.group(1).strip()
        # Remover caracteres inválidos e caracteres de nova linha do nome do arquivo
        nome = re.sub(r'[\\/:*?"<>|\n]', '', nome)
        return nome
    else:
        return None

def extrairTextoPDF(caminhoArquivo):
    with open(caminhoArquivo, 'rb') as arquivo_pdf:
        leitorPDF = PdfReader(arquivo_pdf)
        texto = ''
        for numeroPag in range(len(leitorPDF.pages)):
            texto += leitorPDF.pages[numeroPag].extract_text()
        return texto

def obterNomeColaborador(caminhoArquivo):
    texto = extrairTextoPDF(caminhoArquivo)
    nome = extrairNome(texto)
    if nome:
        return nome
    else:
        print(f'Nome não encontrado no arquivo {caminhoArquivo}.')
        return None
