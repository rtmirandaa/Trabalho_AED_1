from classes import Torre, Apartamento, FilaDeEspera, ListaApartamentosComVaga, gerar_proximo_id

def menu():
    fila_de_espera = FilaDeEspera()
    lista_apartamentos = ListaApartamentosComVaga()
    vagas_disponiveis = [i for i in range(1, 11)]

    torres = [
        Torre(id=1, nome="Torre: A", endereco="Rua 1, Nº 100"),
        Torre(id=2, nome="Torre: B", endereco="Rua 2, Nº 200"),
        Torre(id=3, nome="Torre: C", endereco="Rua 3, Nº 300"),
        Torre(id=4, nome="Torre: D", endereco="Rua 4, Nº 400")
    ]

    # for i in range(11):
    #     numero_apartamento = f" {i+1}"
    #     numero_vaga = None
    #     if vagas_disponiveis:
    #         numero_vaga = vagas_disponiveis.pop(0)
    #     torre = torres[i % len(torres)]
    #     id_apartamento = gerar_proximo_id()
    #     apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)

    #     if numero_vaga is not None:
    #         lista_apartamentos.adicionar_apartamento(apartamento)
    #     else:
    #         fila_de_espera.adicionar_apartamento(apartamento)

    while True:
        print("\nMenu:")
        print("1. Cadastrar apartamento")
        print("2. Liberar vaga")
        print("3. Imprimir lista de apartamentos com vaga")
        print("4. Imprimir fila de espera")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            numero_apartamento = input("Número do apartamento: ")
            numero_vaga = None
            if vagas_disponiveis:
                numero_vaga = vagas_disponiveis.pop(0)
                print(f"Apartamento será alocado na vaga {numero_vaga}.")
            print("Escolha uma torre:")
            for idx, torre in enumerate(torres, start=1):
                print(f"{idx}. {torre.nome} - {torre.endereco}")
            torre_opcao = int(input("Número da torre: "))
            torre = torres[torre_opcao - 1]
            id_apartamento = gerar_proximo_id()
            apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)

            if numero_vaga is not None:
                lista_apartamentos.adicionar_apartamento(apartamento)
            else:
                fila_de_espera.adicionar_apartamento(apartamento)

        elif opcao == 2:
            numero_vaga = int(input("Número da vaga a ser liberada: "))
            vaga_liberada = lista_apartamentos.liberar_vaga(numero_vaga, fila_de_espera)
            if vaga_liberada is not None:
                novo_apartamento = fila_de_espera.retirar_apartamento(vaga_liberada)
                if novo_apartamento is not None:
                    lista_apartamentos.adicionar_apartamento(novo_apartamento)
                vagas_disponiveis.append(vaga_liberada)
                vagas_disponiveis.sort()

        elif opcao == 3:
            lista_apartamentos.imprimir_lista()

        elif opcao == 4:
            fila_de_espera.imprimir_fila()

        elif opcao == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
