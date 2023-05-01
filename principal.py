from typing import TextIO

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
    bloco_try()
    bloco_with()
