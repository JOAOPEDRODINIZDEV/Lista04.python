class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None

class Roleta:
    def __init__(self):
        self.head = None

    def adicionar_numero(self, numero):
        novo_no = No(numero)
        if self.head is None:
            self.head = novo_no
            novo_no.proximo = self.head
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head

    def girar_roleta(self):
        if self.head is None:
            print("A roleta está vazia")
            return

        import random
        numero_sorteado = random.randint(1, 37)

        atual = self.head
        while True:
            if atual.numero == numero_sorteado:
                print("Número sorteado:", numero_sorteado)
                print("Você ganhou!")
                break
            atual = atual.proximo
            if atual == self.head:
                print("Número sorteado:", numero_sorteado)
                print("Você perdeu!")
                break


roleta = Roleta()

for numero in range(1, 37):
    roleta.adicionar_numero(numero)

aposta = int(input("Faça sua aposta \n Digite um número de 1 a 37: "))

roleta.girar_roleta()
