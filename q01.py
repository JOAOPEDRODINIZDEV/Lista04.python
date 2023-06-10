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

opcao = 0

while opcao != 4:
    print("----- MENU -----")
    print("1. Enfileirar")
    print("2. Desenfileirar")
    print("3. Elemento da frente")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = int(input("Digite o valor a ser enfileirado: "))
        fila.enqueue(valor)
        print("Valor enfileirado com sucesso!")
    elif opcao == 2:
        if fila.is_empty():
            print("A fila está vazia")
        else:
            valor = fila.dequeue()
            print("Valor desenfileirado:", valor)
    elif opcao == 3:
        try:
            valor = fila.get_front()
            print("Elemento da frente:", valor)
        except IndexError as e:
            print(str(e))
    elif opcao == 4:
        print("Saindo...")
    else:
        print("Opção inválida! Digite uma opção válida.")

print(fila.dequeue())  
print(fila.dequeue())
