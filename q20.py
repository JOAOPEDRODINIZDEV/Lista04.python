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


def aluno_com_maior_nota(lista_alunos):
    maior_nota = float('-inf')
    nome_aluno = ""
    for aluno in lista_alunos:
        if aluno["nota"] > maior_nota:
            maior_nota = aluno["nota"]
            nome_aluno = aluno["nome"]
    return nome_aluno


alunos = []

while True:
    print("\nMenu:")
    print("1. Inserir aluno")
    print("2. Obter aluno com maior nota")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        alunos.append({"nome": nome, "nota": nota})
        print("Aluno inserido com sucesso!")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Não há alunos cadastrados.")
        else:
            resultado = aluno_com_maior_nota(alunos)
            print(f"Aluno com maior nota: {resultado}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Digite novamente.")

print("Programa encerrado.")


