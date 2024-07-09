# Importa todas as classes do módulo classes
from classes import *
lista_AP = lista()  # Cria uma instância da classe lista
fila_Espera = Fila()  # Cria uma instância da classe Fila

# Define o menu do sistema
Menu = """
----------------------------------------
Sistema de Gerenciamento de condomínios
----------------------------------------
0 - Sair
1 - Cadastrar Torre
2 - Cadastrar apartamento
3 - Visualizar apartamentos com vaga de garagem
4 - Visualizar fila de espera
5 - Remover apartamento
"""

# Função para cadastrar uma torre
def cadastrar_torre():
    if len(lista_AP) == 0:  # Verifica se a lista de apartamentos está vazia
        print("Não podem ser cadastrados Torres sem apartamentos existentes")
        input("Clique Enter para continuar")
    else:
        nome = input("Nome da torre: ")  # Solicita o nome da torre
        endereco = input("Endereço da torre: ")  # Solicita o endereço da torre
        torre = Torre(nome, endereco)  # Cria uma nova instância da classe Torre
        if len(lista_AP) != 10:  # Verifica se a lista de apartamentos não está cheia
            print(str(lista_AP))  # Imprime a lista de apartamentos
            num_ap = int(input("Digite o indice do apartamento que você deseja nesta Torre: "))  # Solicita o índice do apartamento
            ap = lista_AP[num_ap]  # Obtém o apartamento na posição especificada
            ap.cadastrar(torre)  # Cadastra o apartamento na torre
        else:
            print(str(fila_Espera))  # Imprime a fila de espera
            num_ap = input("Número do apartamento nesta Torre: ")  # Solicita o número do apartamento
            ap = fila_Espera[num_ap]  # Obtém o apartamento na posição especificada
            ap.cadastrar(torre)  # Cadastra o apartamento na torre

# Função para cadastrar um apartamento
def cadastrar_ap():
    num_ap = int(input("Número do apartamento: "))  # Solicita o número do apartamento
    ap = apartamento(num_ap)  # Cria uma nova instância da classe apartamento
    if len(lista_AP) <= 10:  # Verifica se a lista de apartamentos não está cheia
        garagem = 0  # Inicializa o contador de garagem
        garagem += len(lista_AP) + 1  # Incrementa o contador de garagem
        ap.vaga = garagem  # Atribui a vaga ao apartamento
        lista_AP.inserir_final(ap)  # Insere o apartamento no final da lista
        print("Apartamento Cadastrado com sucesso")
    else:
        fila_Espera.inserir(ap)  # Insere o apartamento na fila de espera

# Função para exibir o menu do sistema
def menu():
    while True:  # Loop infinito para exibir o menu
        print(Menu)  # Imprime o menu
        op = int(input("Opção: "))  # Solicita a opção do usuário
        if op == 0:
            print("Saindo...")
            break  # Sai do loop
        elif op == 1:
            cadastrar_torre()  # Chama a função para cadastrar uma torre
        elif op == 2:
            cadastrar_ap()  # Chama a função para cadastrar um apartamento
        elif op == 3:
            print(str(lista_AP))  # Imprime a lista de apartamentos
            input("Clique Enter para continuar")
        elif op == 4:
            print(str(fila_Espera))  # Imprime a fila de espera
            input("Clique Enter para continuar")
        elif op == 5:
            excluir = int(input("Digite 1 para remover na fila de espera ou 2 para remover na lista de apartamentos: "))  # Solicita a opção de exclusão
            if excluir == 1:
                print("Será removido o primeiro da fila de espera")
                print(str(fila_Espera))  # Imprime a fila de espera
                fila_Espera.remover()  # Remove o primeiro da fila de espera
            elif excluir == 2:
                print(str(lista_AP))  # Imprime a lista de apartamentos
                num_ap = input("Digite o índice do apartamento que deseja excluir: ")  # Solicita o índice do apartamento
                del lista_AP[num_ap]  # Remove o apartamento na posição especificada
            else:
                print("Opcão inválida")  # Imprime uma mensagem de opção inválida

# Chama a função menu se o script for executado diretamente
if __name__ == "__main__":
    menu()
