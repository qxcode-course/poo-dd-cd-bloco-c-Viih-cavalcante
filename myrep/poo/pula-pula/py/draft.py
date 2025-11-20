class Criança:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"


class PulaPula:
    def __init__(self):
        self.esperando: list[Criança] = []
        self.pulando: list[Criança] = []

    def procurar(self, nome: str, lista: list[Criança]):
        for i, c in enumerate(lista):
            if c.getNome() == nome:
                return i
        return -1

    def removeDaLista(self, nome: str, lista: list[Criança]):
        pos = self.procurar(nome, lista)
        if pos == -1:
            return None
        return lista.pop(pos)

    def chegar(self, criança: Criança):
        self.esperando.insert(0, criança)

    def entrar(self):
        if len(self.esperando) == 0:
            return
        criança = self.esperando.pop()
        self.pulando.insert(0, criança)

    def sair(self):
        if len(self.pulando) == 0:
            return
        criança = self.pulando.pop()
        self.esperando.insert(0, criança)

    def remover(self, nome: str):
        criança = self.removeDaLista(nome, self.pulando)
        if criança is not None:
            return True


        criança = self.removeDaLista(nome, self.esperando)
        if criança is not None:
            return True

        return False

    def __str__(self):
        esperando = ", ".join(str(c) for c in self.esperando)
        pulando = ", ".join(str(c) for c in self.pulando)
        return f"[{esperando}] => [{pulando}]"


def main():
    pp = PulaPula()

    while True:
        linha = input()
        print("$" + linha)
        args = linha.split()

        if len(args) == 0:
            continue

        if args[0] == "end":
            break

        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            pp.chegar(Criança(nome, idade))

        elif args[0] == "enter":
            pp.entrar()

        elif args[0] == "leave":
            pp.sair()

        elif args[0] == "remove":
            nome = args[1]
            if not pp.remover(nome):
                print(f"fail: {nome} nao esta no pula-pula")

        elif args[0] == "show":
            print(pp)

        else:
            print("Fail: comando invalido")

main()