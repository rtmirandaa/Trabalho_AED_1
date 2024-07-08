    

class Torre:
    def __init__(self, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
    def __str__(self):
        return f"Nome: {self.nome} \n Endereço:{self.endereco} \n"
    def cadastrar(self):
        pass    
    def imprimir(self):
        return str(self)

class apartamento:
    def __init__(self, numero):
        self.id = 0
        self.numero = numero
        self.torre = None
        self.vaga = int
    def cadastrar(self, torre):
        self.torre = torre
        print("Cadastrado com sucesso")
        return
    def __str__(self):
        vaga =""
        if self.vaga > 10:
            vaga ="Este apartamento está na fila"
        else:
            vaga = self.vaga
        return f"Número: {self.numero} \n Torre: {str(self.torre)} \n Vaga: {self.vaga} \n"
        
    def imprimir(self):
        return str(self)
    
class Fila:
    class nodo:
        def __init__(self, numero):
            self.numero = numero
            self.proximo = None

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
            
    def __iter__(self):
        atual = self.inicio
        while atual:
            yield atual
            atual = atual.proximo
    def __str__(self):
        return "\n".join([str(i) for i in self]+ "\n")

    def __len__(self):
        return self.tamanho

    def inserir(self, garagem):
        novo = self.nodo(garagem)
        if self.fim is None:
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.ultimo = novo
        if self.inicio is None:
            self.inicio = novo
        self.tamanho += 1
            
    def remover(self):
        if len(self) is not None:
            garagem = self.inicio.numero
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return garagem
            raise IndexError("Fila vazia")




class lista:
    class nodo:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
        def __str__(self):
            return str(self.valor)

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __getitem__(self, posicao):
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1
            if passo == 0:
                raise ValueError("Passo não pode ser zero.")
            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1
                fim = posicao.stop if posicao.stop is not None else -1
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posicao inválida")
        atual = self.inicio
        for i in range(posicao):
            atual = atual.proximo
        return atual

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual
            atual = atual.proximo
    
    def __delitem__(self, posicao):
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1
            if passo == 0:
                raise ValueError("Passo não pode ser zero.")
            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1
                fim = posicao.stop if posicao.stop is not None else -1
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posicao inválida")
        atual = self.inicio
        for i in range(posicao):
            anterior = atual
            atual = atual.proximo
        anterior.proximo = atual.proximo
        self.tamanho -= 1

    def __str__(self):
        return  "\n".join([str(valor) for valor in self]) + "\n"

    def __len__(self):
        return self.tamanho

    def inserir_final(self, valor):
        novo = self.nodo(valor)
        self.tamanho += 1
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return
        self.fim.proximo = novo
        self.fim = novo

    def inserir(self,posicao, valor):
        novo = self.nodo(valor)
        self.tamanho += 1
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return
        if posicao <= 0:
            novo.proximo = self.inicio
            self.inicio = novo
            return
        x = 0
        atual = self.inicio
        while atual.proximo is not None and x < posicao - 1:
            atual = atual.proximo
            x += 1

        if atual.proximo is None:
            self.fim = novo
        novo.proximo = atual.proximo
        atual.proximo = novo 