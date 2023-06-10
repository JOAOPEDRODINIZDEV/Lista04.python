class Item:
    def __init__(self,dado):
        self.dado.dado
        self.prox = None
    
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        
    def inseir(self,elemento):
        novo_item = Item(elemento)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            aux = self.inicio
            while aux.prox is not None:
                aux = aux.prox
            aux.prox = novo_item

def elementos_comuns(lista1, lista2):
    comuns = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in comuns:
            comuns.append(elemento)
    return comuns
num_elementos1 = int(input("Digite o número de elementos da primeira lista: "))
lista1 = []
for i in range(num_elementos1):
    elemento = int(input("Digite um número para a primeira lista: "))
    lista1.append(elemento)

num_elementos2 = int(input("Digite o número de elementos da segunda lista: "))
lista2 = []
for i in range(num_elementos2):
    elemento = int(input("Digite um número para a segunda lista: "))
    lista2.append(elemento)

resultado = elementos_comuns(lista1, lista2)
print(resultado)
