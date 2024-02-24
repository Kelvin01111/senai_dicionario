
def adcionar_item(pessoas):
    nome = input("Informe o nome: ")
    idade = input("Informe a idade: ")
    pessoas[nome] = idade
    print("Adicionado com sucesso!")


def remover_item_por_nome(pessoas):
    nome = input("Informe o nome que deseja remover: ")
    chaves = list(pessoas.keys())
    
    for chave in chaves:
        if nome.lower() in chave.lower():
            del pessoas[chave]
            print(f"{nome} removido com sucesso!")
            break
        else:
            print(f"{nome} não encontrado!")


def remover_ultimo_item_adicionado(pessoas):
        chave, valor = pessoas.popitem()
        print(f"Chave removida {chave} e valor removido{valor}")
        print("Validar: ",pessoas)


def main():
    pessoas = {}
    continuar = True

    while continuar:
        print("\nCadastro de Pessoas")
        print("1 - Adicionar um novo item")
        print("2 - Remover item por nome")
        print("3 - Remover último item adicionado")
        print("4 - Exibir conteúdo do dicionário")
        print("5 - Sair")
   
        opcao = input("Informe a opção desejada (1-5): ") 
        if opcao == "1":
            adcionar_item(pessoas)
        elif opcao == "2":
            remover_item_por_nome(pessoas)
        elif opcao == "3":
            remover_ultimo_item_adicionado(pessoas)
        elif opcao == "4":
            print("Dicionário de pessoas: ",pessoas)
        elif opcao == "5":
            continuar = False
            print(" Saindo...")
        else:
            print("Opção Inválida")
            



if __name__=="__main__":
    main()