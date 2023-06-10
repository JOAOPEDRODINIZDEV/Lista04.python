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
            
def palavra_mais_longa(lista_palavras):
    palavra_longa = ""
    for palavra in lista_palavras:
        if len(palavra) > len(palavra_longa):
            palavra_longa = palavra
    return palavra_longa

palavras = []
num_palavras = int(input("Digite o número de palavras: "))

for i in range(num_palavras):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)

resultado = palavra_mais_longa(palavras)
print("A palavra mais longa é:", resultado)

