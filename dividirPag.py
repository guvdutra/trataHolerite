import os
from PyPDF2 import PdfReader, PdfWriter
import nomearArq

def dividirPaginas(arquivoEntrada, pastaSaida):
    # Abre o arquivo PDF
    with open(arquivoEntrada, 'rb') as file:
        pdf_reader = PdfReader(file)
        # Itera sobre as páginas do PDF
        for page_number in range(len(pdf_reader.pages)):
            # Obtém o texto da página
            texto_pagina = pdf_reader.pages[page_number].extract_text()
            # Obtém o nome do colaborador da página
            nome_colaborador = nomearArq.extrairNome(texto_pagina)
            if nome_colaborador:
                # Cria um novo objeto PdfWriter
                pdf_writer = PdfWriter()
                # Adiciona a página atual ao objeto PdfWriter
                pdf_writer.add_page(pdf_reader.pages[page_number])
                # Constrói o nome do arquivo de saída com o nome do colaborador
                output_filename = os.path.join(pastaSaida, f'{nome_colaborador}.pdf')
                # Escreve a página atual em um novo arquivo PDF
                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
            else:
                print(f'Nome não encontrado na página {page_number + 1} do arquivo {arquivoEntrada}.')

