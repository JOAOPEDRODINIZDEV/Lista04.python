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

    def get_front(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self.head.value
fila = Queue()

print("Digite uma sequência de números inteiros (digite um número 0 para parar):")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    fila.enqueue(numero)

print("Os elementos da fila (na ordem em que foram inseridos):")
while not fila.is_empty():
    elemento = fila.dequeue()
    print(elemento)

