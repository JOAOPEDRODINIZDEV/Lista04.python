class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def esta_vazia(self):
        return self.head is None

    def inserir_em_ordem(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            novo_no.proximo = novo_no
            self.head = novo_no
        elif dado < self.head.dado:
            novo_no.proximo = self.head
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head and dado > atual.proximo.dado:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def exibir_primeiro_elemento(self):
        if self.esta_vazia():
            print("A lista está vazia")
        else:
            print("Primeiro elemento:", self.head.dado)

    def exibir_ultimo_elemento(self):
        if self.esta_vazia():
            print("A lista está vazia")
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            print("Último elemento:", atual.dado)


# Programa principal
lista = ListaEncadeadaCircular()

numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()

for numero in numeros:
    lista.inserir_em_ordem(int(numero))

lista.exibir_primeiro_elemento()
lista.exibir_ultimo_elemento()
