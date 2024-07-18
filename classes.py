proximo_id_apartamento = 0

def gerar_proximo_id():
    global proximo_id_apartamento
    id_atual = proximo_id_apartamento
    proximo_id_apartamento += 1
    return id_atual

class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

class Apartamento:
    def __init__(self, id, numero_apartamento, numero_vaga, torre):
        self.id = id
        self.numero_apartamento = numero_apartamento
        self.numero_vaga = numero_vaga
        self.torre = torre

class FilaDeEspera:
    def __init__(self):
        self.fila = []

    def adicionar_apartamento(self, apartamento):
        self.fila.append(apartamento)
        print(f" {apartamento.numero_apartamento} adicionado à fila de espera.")

    def retirar_apartamento(self, numero_vaga):
        if self.fila:
            apartamento = self.fila.pop(0)
            apartamento.numero_vaga = numero_vaga
            print(f"Apartamento {apartamento.numero_apartamento} retirado da fila de espera e atribuído à vaga {numero_vaga}.")
            return apartamento
        else:
            print("A fila de espera está vazia.")
            return None

    def imprimir_fila(self):
        if self.fila:
            print("Fila de espera:")
            for apto in self.fila:
                print(f"Apartamento {apto.numero_apartamento}, {apto.torre.nome}")
        else:
            print("A fila de espera está vazia.")

class ListaApartamentosComVaga:
    def __init__(self):
        self.apartamentos = []

    def adicionar_apartamento(self, apartamento):
        self.apartamentos.append(apartamento)
        self.apartamentos.sort(key=lambda apto: apto.numero_vaga)
        print(f"Apartamento {apartamento.numero_apartamento} com vaga {apartamento.numero_vaga} adicionado à lista de apartamentos com vaga.")

    def liberar_vaga(self, numero_vaga, fila_de_espera):
        for apto in self.apartamentos:
            if apto.numero_vaga == numero_vaga:
                self.apartamentos.remove(apto)
                print(f"Vaga {numero_vaga} liberada pelo Apartamento {apto.numero_apartamento}.")
                fila_de_espera.adicionar_apartamento(apto)
                return numero_vaga
        print(f"Vaga {numero_vaga} não encontrada.")
        return None

    def imprimir_lista(self):
        if self.apartamentos:
            print("Apartamentos com vaga:")
            for apto in self.apartamentos:
                print(f"Apartamento {apto.numero_apartamento}, {apto.torre.nome}, Vaga {apto.numero_vaga}")
        else:
            print("Nenhum apartamento com vaga disponível.")
