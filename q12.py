class Contato:
    def __init__(self, nome, numero_telefone):
        self.nome = nome
        self.numero_telefone = numero_telefone
        self.anterior = None
        self.proximo = None

class AgendaTelefonica:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def adicionar_contato(self, nome, numero_telefone):
        novo_contato = Contato(nome, numero_telefone)

        if self.esta_vazia():
            self.inicio = novo_contato
            self.fim = novo_contato
        else:
            novo_contato.anterior = self.fim
            self.fim.proximo = novo_contato
            self.fim = novo_contato

    def remover_contato(self, nome):
        atual = self.inicio
        while atual:
            if atual.nome == nome:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                return

            atual = atual.proximo

    def exibir_contatos(self):
        if self.esta_vazia():
            print("A agenda está vazia")
        else:
            atual = self.inicio
            while atual:
                print("Nome:", atual.nome, "- Telefone:", atual.numero_telefone)
                atual = atual.proximo

# Programa principal
agenda = AgendaTelefonica()

while True:
    print("=== Agenda Telefônica ===")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Exibir contatos")
    print("4. Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        numero_telefone = input("Digite o número de telefone: ")
        agenda.adicionar_contato(nome, numero_telefone)
        print("Contato adicionado com sucesso!")

    elif escolha == "2":
        nome = input("Digite o nome do contato a ser removido: ")
        agenda.remover_contato(nome)
        print("Contato removido com sucesso!")

    elif escolha == "3":
        print("Contatos na agenda:")
        agenda.exibir_contatos()

    elif escolha == "4":
        break

    else:
        print("Opção inválida. Tente novamente.")
    print()

print("Fim do programa.")
