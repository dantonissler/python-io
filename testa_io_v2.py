if __name__ == "__main__":
    arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

    print(type(arquivo))
    print(type(arquivo.buffer))

    contato = bytes('14,Felipe,felipe@felipe.com.br\n', 'latin_1')
    arquivo.buffer.write(contato)
    arquivo.close()
