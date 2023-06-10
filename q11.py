class Node:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.cabeca = None
        self.calda = None

    def esta_vazia(self):
        return self.cabeca is None

    def inserir_ordenado(self, dado):
        novo_no = Node(dado)

        if self.esta_vazia():
            self.cabeca = novo_no
            self.calda = novo_no
        elif dado < self.cabeca.dado:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
        elif dado >= self.calda.dado:
            novo_no.anterior = self.calda
            self.calda.proximo = novo_no
            self.calda = novo_no
        else:
            atual = self.cabeca
            while atual.proximo and dado >= atual.proximo.dado:
                atual = atual.proximo

            novo_no.anterior = atual
            novo_no.proximo = atual.proximo
            atual.proximo.anterior = novo_no
            atual.proximo = novo_no

    def exibir(self):
        if self.esta_vazia():
            print("A lista está vazia")
        else:
            atual = self.cabeca
            while atual:
                print(atual.dado, end=" <-> ")
                atual = atual.proximo
            print("None")

# Programa principal
lista = ListaEncadeadaDupla()

# Leitura dos nomes até que uma linha em branco seja digitada
print("Digite os nomes (pressione Enter para encerrar a entrada):")
while True:
    nome = input()
    if nome == "":
        break
    lista.inserir_ordenado(nome)

# Exibição da lista encadeada dupla em ordem alfabética
print("Lista em ordem alfabética:")
lista.exibir()
