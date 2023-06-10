class Cliente:
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.prox = None

class ListaClientes:
    def __init__(self):
        self.head = None

    def inserir_cliente(self, cliente):
        novo_cliente = Cliente(cliente.nome, cliente.conta, cliente.saldo)
        if self.head is None:
            self.head = novo_cliente
        else:
            atual = self.head
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_cliente

    def remover_cliente(self, conta):
        if self.head is None:
            print("A lista está vazia")
            return

        if self.head.conta == conta:
            self.head = self.head.prox
            return

        atual = self.head
        while atual.prox:
            if atual.prox.conta == conta:
                atual.prox = atual.prox.prox
                return
            atual = atual.prox

        print("Cliente não encontrado")

    def pesquisar_cliente(self, conta):
        atual = self.head
        while atual:
            if atual.conta == conta:
                return atual
            atual = atual.prox
        return None

    def exibir_tabela(self):
        if self.head is None:
            print("A lista está vazia")
        else:
            print("Nome\t\tConta\t\tSaldo")
            atual = self.head
            while atual:
                print(f"{atual.nome}\t\t{atual.conta}\t\t{atual.saldo}")
                atual = atual.prox


clientes = ListaClientes()

while True:
    print("\nMenu:")
    print("1. Inserir cliente")
    print("2. Remover cliente")
    print("3. Pesquisar cliente")
    print("4. Exibir lista")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        conta = int(input("Digite o número da conta: "))
        saldo = float(input("Digite o saldo: "))
        clientes.inserir_cliente(Cliente(nome, conta, saldo))
        print("Cliente inserido com sucesso!")

    elif opcao == "2":
        conta = int(input("Digite o número da conta do cliente a ser removido: "))
        clientes.remover_cliente(conta)
        print("Cliente removido com sucesso!")

    elif opcao == "3":
        conta = int(input("Digite o número da conta do cliente a ser pesquisado: "))
        cliente_pesquisado = clientes.pesquisar_cliente(conta)
        if cliente_pesquisado:
            print(f"Cliente encontrado: {cliente_pesquisado.nome}, Conta: {cliente_pesquisado.conta}, Saldo: {cliente_pesquisado.saldo}")
        else:
            print("Cliente não encontrado")

    elif opcao == "4":
        clientes.exibir_tabela()

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Digite novamente.")

print("Programa encerrado.")
