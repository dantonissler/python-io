from typing import TextIO

from contatos_leitura import csv_para_contato, contatos_para_json, json_para_contatos, contatos_para_pickle, pickle_para_contatos

def bloco_try():
    arquivo_contatos: TextIO
    try:
        arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')
        for linha in arquivo_contatos:
            print(linha, end='')
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Sem permissão para acessar o arquivo.")
    finally:
        arquivo_contatos.close()

def bloco_with():
    arquivo_contatos: TextIO
    try:
        with open('dados/contatos.csv', encoding='latin_1') as arquivo_contatos:
            for linha in arquivo_contatos:
                print(linha, end='')
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Sem permissão para acessar o arquivo.")

if __name__ == "__main__":
    # bloco_try()
    # bloco_with()
    try:
        contatos = csv_para_contato('dados/contatos.csv')
        contatos_para_pickle(contatos, 'dados/contatos.pickle')
        for contato in contatos:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

        contatos = pickle_para_contatos('dados/contatos.pickle')
        for contato in contatos:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

        contato = contatos_para_json(contatos, 'dados/contatos.json')
        for contato in contatos:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

        contato = json_para_contatos('dados/contatos.json')
        for contato in contatos:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Sem permissão para acessar o arquivo.")
