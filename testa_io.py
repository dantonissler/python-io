if __name__ == "__main__":
    arquivo = open('dados/contatos.csv', encoding='latin_1')

    print(type(arquivo))
    print(type(arquivo.buffer))

    conteudo = arquivo.buffer.read()
    print(conteudo)

    texto_em_bytes = bytes('Esse é um texto em bytes', 'utf-8')
    print(texto_em_bytes)
    print(type(texto_em_bytes))
    arquivo.close()
