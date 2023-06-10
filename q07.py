class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeça = None

    def está_vazia(self):
        return self.cabeça is None

    def inserir_no_início(self, valor):
        novo_nó = No(valor)
        novo_nó.proximo = self.cabeça
        self.cabeça = novo_nó

    def inserir_no_final(self, valor):
        novo_nó = No(valor)
        if self.está_vazia():
            self.cabeça = novo_nó
        else:
            atual = self.cabeça
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nó

    def remover_do_início(self):
        if self.está_vazia():
            raise IndexError("A lista está vazia")

        valor = self.cabeça.valor
        self.cabeça = self.cabeça.proximo
        return valor

    def remover_do_final(self):
        if self.está_vazia():
            raise IndexError("A lista está vazia")

        if self.cabeça.proximo is None:
            valor = self.cabeça.valor
            self.cabeça = None
            return valor

        atual = self.cabeça
        while atual.proximo.proximo:
            atual = atual.proximo
        valor = atual.proximo.valor
        atual.proximo = None
        return valor

    def exibir(self):
        if self.está_vazia():
            print("A lista está vazia")
        else:
            atual = self.cabeça
            while atual:
                print(atual.valor, end=" -> ")
                atual = atual.proximo
            print("None")
