#   2. Escreva uma função que receba uma lista de números (informados pelo
#   usuário) e retorne um dicionário com as seguintes informações: média, valor
#   máximo, valor mínimo e quantidade de números na lista.



def adicionar(qtd_elemento):
    lista = []
    for i in range(qtd_elemento):
        item = int(input("Informe um número: "))
        lista.append(item)
    return lista


def operacoes(lista_numeros):
    if not lista_numeros:
        return None

    media = sum(lista_numeros) / len(lista_numeros)
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    quantidade = len(lista_numeros)


    dicionario = {"media": media, "maximo": maximo,"minimo":minimo, "quantidade":quantidade}
    return dicionario



def main():
    qtd_elemento = int(input("Informe o tamanho da lista: "))
    lista_numeros = adicionar(qtd_elemento)
    dict_result = operacoes(lista_numeros)
    print("Conteúdo do dicionário",qtd_elemento,lista_numeros)






if __name__=="__main__":
    main()
