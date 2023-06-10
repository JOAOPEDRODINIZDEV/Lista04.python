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


fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)


print("Elemento da frente:", fila.get_front())

print(fila.dequeue())  
print(fila.dequeue())
