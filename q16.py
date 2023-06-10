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
    
def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma
num_elementos = int(input("Digite o número de elementos da lista: "))
numeros = []
for i in range(num_elementos):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

resultado = soma_elementos(numeros)
print(resultado)

