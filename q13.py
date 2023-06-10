class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def esta_vazia(self):
        return self.head is None

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            novo_no.proximo = novo_no
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head
            self.head = novo_no

    def inserir_no_final(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            novo_no.proximo = novo_no
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("A lista está vazia")
        elif self.head.proximo == self.head:
            dado = self.head.dado
            self.head = None
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            dado = self.head.dado
            atual.proximo = self.head.proximo
            self.head = self.head.proximo
        return dado

    def remover_do_final(self):
        if self.esta_vazia():
            raise IndexError("A lista está vazia")
        elif self.head.proximo == self.head:
            dado = self.head.dado
            self.head = None
        else:
            atual = self.head
            anterior = None
            while atual.proximo != self.head:
                anterior = atual
                atual = atual.proximo
            dado = atual.dado
            anterior.proximo = self.head
        return dado

    def exibir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia")
        else:
            atual = self.head
            while True:
                print(atual.dado, end=" -> ")
                atual = atual.proximo
                if atual == self.head:
                    break
            print()


# Exemplo de uso
lista = ListaEncadeadaCircular()

lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)

lista.inserir_no_final(4)
lista.inserir_no_final(5)

lista.exibir_lista()  # Saída: 1 -> 2 -> 3 -> 4 -> 5 ->

lista.remover_do_inicio()
lista.remover_do_final()

lista.exibir_lista()  # Saída: 2 -> 3 -> 4 ->
