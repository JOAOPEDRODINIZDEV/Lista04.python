class Item:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    def inserir(self, elemento):
        novo_item = Item(elemento)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            aux = self.inicio
            while aux.prox is not None:
                aux = aux.prox
            aux.prox = novo_item

    def exibir(self):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            aux = self.inicio
            while aux is not None:
                print(aux.dado, end=" -> ")
                aux = aux.prox
            print("None")


lista = ListaEncadeada()


numeros = [5, 4, 3, 2, 1]
for num in numeros:
    lista.inserir(num)

lista.exibir()
