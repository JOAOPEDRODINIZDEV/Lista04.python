class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0  

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_item = Item(value)
        if self.is_empty():
            self.tail = new_item
            self.head = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1  
        return value

    def get_size(self):
        return self.size
def verificar_palindromo(frase):
    fila = Queue()

    
    frase = frase.replace(" ", "").lower()

    
    for char in frase:
        fila.enqueue(char)

    while not fila.is_empty():
        char_inicio = fila.dequeue()
        if fila.is_empty():
            return True  
        char_fim = fila.dequeue()
        if char_inicio != char_fim:
            return False  

    return True 

frase = input("Digite uma frase: ")
if verificar_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
   