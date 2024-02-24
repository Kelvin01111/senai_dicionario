#  5. Crie um dicionário que represente um inventário de produtos em uma loja.
#  Cada chave deve ser o código do produto, e cada valor deve ser um dicionário
#  contendo informações como nome, preço e quantidade em estoque. Crie um
#  menu que permita com que o usuário atualize as informações ou mesmo remova
#  um produto específico.

def adicionar_produto(inventario):
    codigo = input("Informe o código do produto: ")
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    quantidade = int(input("Informe a quantidade de produto: "))
    
    inventario[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
    print("Produto adicionado com sucesso!")

def atualizar_produto(inventario):
    codigo = input("Informe o código do produto que deseja atualizar: ")
    if codigo in inventario:
        print("Atualize as informações do produto que desejar ou pressione Enter: ")
        novo_nome = input("Informe o novo nome do produto: ")
        if novo_nome != "":
            inventario[codigo]['nome'] = novo_nome

        novo_preco = input("Informe o novo preço do produto: ")
        if novo_nome != "":
            inventario[codigo]['preco'] = novo_preco

        nova_qtd = input("Informe a nova quantidade do produto: ")
        if nova_qtd != "":
            inventario[codigo]['quantidade'] = nova_qtd

    else:
        print("Produto não encontrado")


def remover_produto(inventario):
    codigo = input("Informe o código do produto que deseja remover: ")
    if codigo in inventario:
        del inventario[codigo]
    else:
        print("Produto não encontrado")

def main():
    continuar = True
    inventario = {}

    while continuar:
        print(" Menu de opções ")
        print("1. Adicionar produto")
        print("2. Exibir produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Sair")

        opcao = input("Entre com uma das opções(1-5): ")
        if opcao == "1":
            adicionar_produto(inventario)
        elif opcao == "2":
            print("Exibir Inventário: ",inventario)
        elif opcao == "3":
            atualizar_produto(inventario)
        elif opcao == "4":
            remover_produto(inventario)
        elif opcao == "5":
            continuar = False
        else:
            print("Opção inválida!")


if __name__=="__main__":
    main()