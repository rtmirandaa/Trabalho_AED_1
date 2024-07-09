# Define a classe Torre
class Torre:
    # Inicializa a classe Torre com nome e endereco
    def __init__(self, nome, endereco):
        self.id = id  # Atribui um identificador à torre
        self.nome = nome  # Atribui o nome à torre
        self.endereco = endereco  # Atribui o endereco à torre

    # Define a representação em string da classe Torre
    def __str__(self):
        return f"Nome: {self.nome} \n Endereço:{self.endereco} \n"

    # Método para cadastrar a torre (ainda não implementado)
    def cadastrar(self):
        pass

    # Método para imprimir a representação da torre
    def imprimir(self):
        return str(self)

# Define a classe apartamento
class apartamento:
    # Inicializa a classe apartamento com um numero
    def __init__(self, numero):
        self.id = 0  # Atribui um identificador ao apartamento
        self.numero = numero  # Atribui o número ao apartamento
        self.torre = None  # Inicializa a torre como None
        self.vaga = int  # Inicializa a vaga como tipo inteiro

    # Método para cadastrar um apartamento em uma torre
    def cadastrar(self, torre):
        self.torre = torre  # Atribui a torre ao apartamento
        print("Cadastrado com sucesso")
        return

    # Define a representação em string da classe apartamento
    def __str__(self):
        vaga = ""  # Inicializa a string vaga
        if self.vaga > 10:  # Verifica se a vaga é maior que 10
            vaga = "Este apartamento está na fila"  # Atribui uma mensagem à vaga
        else:
            vaga = self.vaga  # Atribui o valor da vaga
        return f"Número: {self.numero} \n Torre: {str(self.torre)} \n Vaga: {self.vaga} \n"

    # Método para imprimir a representação do apartamento
    def imprimir(self):
        return str(self)

# Define a classe Fila
class Fila:
    # Define a classe nodo para os nós da fila
    class nodo:
        # Inicializa a classe nodo com um numero
        def __init__(self, numero):
            self.numero = numero  # Atribui o número ao nodo
            self.proximo = None  # Inicializa o próximo nodo como None

    # Inicializa a classe Fila
    def __init__(self):
        self.inicio = None  # Inicializa o início da fila como None
        self.fim = None  # Inicializa o fim da fila como None
        self.tamanho = 0  # Inicializa o tamanho da fila como 0

    # Define o iterador para a classe Fila
    def __iter__(self):
        atual = self.inicio  # Define o nodo atual como o início da fila
        while atual:  # Enquanto houver um nodo atual
            yield atual  # Retorna o nodo atual
            atual = atual.proximo  # Avança para o próximo nodo

    # Define a representação em string da classe Fila
    def __str__(self):
        return "\n".join([str(i) for i in self] + "\n")

    # Define o método len para a classe Fila
    def __len__(self):
        return self.tamanho

    # Método para inserir um novo nodo na fila
    def inserir(self, garagem):
        novo = self.nodo(garagem)  # Cria um novo nodo com o número da garagem
        if self.fim is None:  # Se o fim da fila é None
            self.fim = novo  # Define o novo nodo como o fim da fila
        else:
            self.fim.proximo = novo  # Define o próximo do fim da fila como o novo nodo
            self.ultimo = novo  # Atualiza o fim da fila para o novo nodo
        if self.inicio is None:  # Se o início da fila é None
            self.inicio = novo  # Define o novo nodo como o início da fila
        self.tamanho += 1  # Incrementa o tamanho da fila

    # Método para remover um nodo da fila
    def remover(self):
        if len(self) is not None:  # Se o tamanho da fila não é None
            garagem = self.inicio.numero  # Armazena o número do início da fila
            self.inicio = self.inicio.proximo  # Define o início da fila como o próximo nodo
            self.tamanho -= 1  # Decrementa o tamanho da fila
            return garagem  # Retorna o número do nodo removido
            raise IndexError("Fila vazia")  # Levanta um erro se a fila estiver vazia

# Define a classe lista
class lista:
    # Define a classe nodo para os nós da lista
    class nodo:
        # Inicializa a classe nodo com um valor
        def __init__(self, valor):
            self.valor = valor  # Atribui o valor ao nodo
            self.proximo = None  # Inicializa o próximo nodo como None

        # Define a representação em string da classe nodo
        def __str__(self):
            return str(self.valor)

    # Inicializa a classe lista
    def __init__(self):
        self.inicio = None  # Inicializa o início da lista como None
        self.fim = None  # Inicializa o fim da lista como None
        self.tamanho = 0  # Inicializa o tamanho da lista como 0

    # Define o método getitem para acessar itens na lista
    def __getitem__(self, posicao):
        if isinstance(posicao, slice):  # Verifica se a posição é um slice
            passo = posicao.step if posicao.step is not None else 1  # Define o passo do slice
            if passo == 0:
                raise ValueError("Passo não pode ser zero.")  # Levanta um erro se o passo for zero
            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0  # Define o início do slice
                fim = posicao.stop if posicao.stop is not None else len(self)  # Define o fim do slice
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1  # Define o início do slice
                fim = posicao.stop if posicao.stop is not None else -1  # Define o fim do slice
        if posicao < 0:
            posicao = len(self) + posicao  # Ajusta a posição se for negativa
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posicao inválida")  # Levanta um erro se a posição for inválida
        atual = self.inicio  # Define o nodo atual como o início da lista
        for i in range(posicao):
            atual = atual.proximo  # Avança para o próximo nodo
        return atual  # Retorna o nodo na posição especificada

    # Define o iterador para a classe lista
    def __iter__(self):
        atual = self.inicio  # Define o nodo atual como o início da lista
        while atual is not None:  # Enquanto houver um nodo atual
            yield atual  # Retorna o nodo atual
            atual = atual.proximo  # Avança para o próximo nodo

    # Define o método delitem para remover itens da lista
    def __delitem__(self, posicao):
        if isinstance(posicao, slice):  # Verifica se a posição é um slice
            passo = posicao.step if posicao.step is not None else 1  # Define o passo do slice
            if passo == 0:
                raise ValueError("Passo não pode ser zero.")  # Levanta um erro se o passo for zero
            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0  # Define o início do slice
                fim = posicao.stop if posicao.stop is not None else len(self)  # Define o fim do slice
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1  # Define o início do slice
                fim = posicao.stop if posicao.stop is not None else -1  # Define o fim do slice
        if posicao < 0:
            posicao = len(self) + posicao  # Ajusta a posição se for negativa
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posicao inválida")  # Levanta um erro se a posição for inválida
        atual = self.inicio  # Define o nodo atual como o início da lista
        for i in range(posicao):
            anterior = atual  # Armazena o nodo anterior
            atual = atual.proximo  # Avança para o próximo nodo
        anterior.proximo = atual.proximo  # Remove o nodo na posição especificada
        self.tamanho -= 1  # Decrementa o tamanho da lista

    # Define a representação em string da classe lista
    def __str__(self):
        return "\n".join([str(valor) for valor in self]) + "\n"

    # Define o método len para a classe lista
    def __len__(self):
        return self.tamanho

    # Método para inserir um nodo no final da lista
    def inserir_final(self, valor):
        novo = self.nodo(valor)  # Cria um novo nodo com o valor especificado
        self.tamanho += 1  # Incrementa o tamanho da lista
        if self.inicio is None:  # Se o início da lista é None
            self.inicio = novo  # Define o novo nodo como o início da lista
            self.fim = novo  # Define o novo nodo como o fim da lista
            return
        self.fim.proximo = novo  # Define o próximo do fim da lista como o novo nodo
        self.fim = novo  # Atualiza o fim da lista para o novo nodo

    # Método para inserir um nodo em uma posição específica na lista
    def inserir(self, posicao, valor):
        novo = self.nodo(valor)  # Cria um novo nodo com o valor especificado
        self.tamanho += 1  # Incrementa o tamanho da lista
        if self.inicio is None:  # Se o início da lista é None
            self.inicio = novo  # Define o novo nodo como o início da lista
            self.fim = novo  # Define o novo nodo como o fim da lista
            return
        if posicao <= 0:  # Se a posição é menor ou igual a 0
            novo.proximo = self.inicio  # Define o próximo do novo nodo como o início da lista
            self.inicio = novo  # Define o novo nodo como o início da lista
            return
        x = 0  # Inicializa o contador x
        atual = self.inicio  # Define o nodo atual como o início da lista
        while atual.proximo is not None and x < posicao - 1:
            atual = atual.proximo  # Avança para o próximo nodo
            x += 1  # Incrementa o contador x
        if atual.proximo is None:  # Se o próximo nodo é None
            self.fim = novo  # Define o novo nodo como o fim da lista
        novo.proximo = atual.proximo  # Define o próximo do novo nodo como o próximo do nodo atual
        atual.proximo = novo  # Define o próximo do nodo atual como o novo nodo