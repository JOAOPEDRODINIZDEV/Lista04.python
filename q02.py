        
        
class Item:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,value):
        new_item = Item(value)
        if self.is_empty():
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("")
        else:
            value = self.head.next
            self.head = self.head.next
            self.size += 1
            return value
    def get_size(self):
        return self.size
                     
def exibir_menu():
    print("Selecione uma opção:")
    print("1. Adicionar número na fila")
    print("2. Remover número da fila")
    print("3. Tamanho da fila")
    print("4. Mostrar fila")
    print("5. Sair")

fila = Queue()

while True:
    exibir_menu()
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        numero = int(input("Digite o número a ser adicionado na fila: "))
        fila.enqueue(numero)
        print("Número adicionado na fila.")
    elif opcao == 2:
        try:
            numero_removido = fila.dequeue()
            print("Número removido da fila:", numero_removido)
        except IndexError as e:
            print("Erro:", str(e))
    elif opcao == 3:
        tamanho = fila.get_size()
        print("Tamanho da fila:", tamanho)
    elif opcao == 4:
        if fila.is_empty():
            print("A fila está vazia.")
        else:
            print("Elementos na fila:")
            temp = fila.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
    elif opcao == 5:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Digite um número válido.")

    print()  # Adiciona uma linha em branco para melhorar a legibilidade
