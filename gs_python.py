import re

def main():
    alimentos = []
    while True:
        try:
            print("""
            ------------------------------------------
                1 - Entrada de produtos
                2 - Exibir estoque
                3 - Vender estoque
                4 - Sair
            ------------------------------------------
                """)
            opcao = int(input())
            if not type(opcao) is int or opcao > 4 or opcao < 1:
                raise ValueError
            match opcao:
                case 1:
                    alimento = adicionar_alimento()
                    alimentos.append(alimento)

                case 2:
                    exibir_alimento(alimentos)

                case 3:
                    doar_alimento(alimentos)

                case 4:
                    print("Obrigado por usar o programa! Finalizando...")
                    break

        except ValueError:
            print("Digite um número válido e correspondente!")


#adicionando um alimento em uma lista
def adicionar_alimento():
    nome = input("Digite o nome do alimento para o estoque: ").capitalize()
    quantidade = int(input("Digite o número referente a quantidade em kg: "))
    while True:
        try:
            data_validade = input("Digite a data de validade (DD/MM/AAAA): ")
            day, month, year = map(int, data_validade.split('/'))
            
            if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 2025 or year < 2023:
                raise ValueError
                
            print(f"{nome} adicionado com sucesso!")
            return (nome, quantidade, data_validade)
        except ValueError:
            print("Formato inválido ou data fora do intervalo permitido.")


def exibir_alimento(alimentos):
    if len(alimentos) == 0:
        print("Não há alimentos cadastrados")
        return

    print("Estoque:")
    for i, alimento in enumerate(alimentos):
        print(f"{i+1}. {alimento[0]} - Estoque {alimento[1]}kg - Data de validade: {alimento[2]}")


def doar_alimento(alimentos):
    if len(alimentos) == 0:
        print("Não há alimentos no estoque.")
        return

    while True:
        try:
            print("\nSelecione um alimento para vender:")
            for i, alimento in enumerate(alimentos):
                print(f"{i+1}. {alimento[0]} - Estoque: {alimento[1]}kg - Data de validade: {alimento[2]}")

            opcao = int(input("Digite o número correspondente ao alimento: "))
            if opcao < 1 or opcao > len(alimentos) or not type(opcao) is int:
                raise ValueError

            alimento_selecionado = alimentos[opcao - 1]
            quantidade_vendida = int(input("Digite a quantidade a ser vendida em kg: "))
            # Check if the requested quantity is available
            if quantidade_vendida > alimento_selecionado[1]:
                print("Quantidade insuficiente em estoque.")
            else:
                # Update the stock quantity
                alimento_selecionado = list(alimento_selecionado)
                alimento_selecionado[1] -= quantidade_vendida
                if alimento_selecionado[1] == 0:
                    # Remove the food item from the stock if the quantity reaches zero
                    alimentos.pop(opcao - 1)
                else:
                    # Update the modified tuple back in the list
                    alimentos[opcao - 1] = tuple(alimento_selecionado)
                print(f"Foram vendidos {quantidade_vendida}kg de {alimento_selecionado[0]}.")

            return
        except ValueError:
            print("\nDigite um número correspondente ao alimento desejado!")


print("Banco de dados de produtos")
main()