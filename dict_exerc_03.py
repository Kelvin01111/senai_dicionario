#   3. Dada uma lista de palavra informadas pelo usuário, crie um dicionário com a
#   palavra como chave e o comprimento da palavra como valor, por fim exiba o
#   dicionário criado em tela.(estude o método split() e len())

def criar_dicionario(lista_palavras):
    dict = {}
    for palavra in lista_palavras:
        dict[palavra] = len(palavra)

    return dict       



def main():
    conteudo = input("Informe as palavras: ")
    lista_palavras = conteudo.split()
    print(lista_palavras)
    dict_saida = criar_dicionario(lista_palavras)
    print(dict_saida)

if __name__=="__main__":
    main()