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

    
def strings_com_mais_de_cinco_caracteres():
    lista_strings = []
    quantidade = int(input("Digite a quantidade de strings: "))

    for i in range(quantidade):
        string = input("Digite a string {}: ".format(i + 1))
        lista_strings.append(string)

    nova_lista = []
    for string in lista_strings:
        if len(string) > 5:
            nova_lista.append(string)

    return nova_lista


resultado = strings_com_mais_de_cinco_caracteres()
print(resultado)
