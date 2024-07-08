from classes import *
lista_AP = lista()
fila_Espera = Fila()


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

def cadastrar_torre():
    if len(lista_AP) == 0:
        print("Não podem ser cadastratods Torres sem apartamentos existentes")
        input("Clique Enter para continuar")
    else:
        nome = input("Nome da torre: ")
        endereco = input("Endereço da torre: ")
        torre = Torre(nome, endereco)
        if len(lista_AP) != 10:
            print(str(lista_AP))
            num_ap = int(input("Digite o indice do apartamento que você deseja nesta Torre: "))
            ap = lista_AP[num_ap]
            ap.cadastrar(torre)
            
        else:
            print(str(fila_Espera))
            num_ap = input("Número do apartamento nesta Torre: ")
            ap = fila_Espera[num_ap]
            ap.cadastrar(torre)

def cadastrar_ap():

    num_ap = int(input("Número do apartamento: "))
    ap = apartamento(num_ap)
    if len(lista_AP) <= 10:
        garagem = 0
        garagem += len(lista_AP) + 1
        ap.vaga = garagem
        lista_AP.inserir_final(ap)
        print("Apartamento Cadastrado com sucesso")
    else:
        fila_Espera.inserir(ap)

def menu():
    while True:
        print(Menu)
        op = int(input("Opção: "))
        if op == 0:
            print("Saindo...")
            break
        elif op == 1:
            cadastrar_torre()
        elif op == 2:
            cadastrar_ap()
        elif op == 3:
            print(str(lista_AP))
            input("Clique Enter para continuar")
        elif op == 4:
            print(str(fila_Espera))
            input("Clique Enter para continuar")
        elif op == 5:
            excluir = int(input("Digite 1 para remover na fila de espera ou 2 para remover na lista de apartamentos: "))
            if excluir == 1:
                print ("Será removido o primeiro da fila de espera")
                print(str(fila_Espera))
                fila_Espera.remover()
            elif excluir == 2:
                print(str(lista_AP))
                num_ap = input("Digite o índice do apartamento que deseja excluir: ")
                del lista_AP[num_ap]
            else:
                print("Opcão inválida")

if __name__ == "__main__":
    menu()