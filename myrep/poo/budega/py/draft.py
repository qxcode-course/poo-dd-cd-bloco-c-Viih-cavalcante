class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self._nome

    def __str__(self):
        return self._nome

class Market:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = [None] * num_caixas
        self.espera: list[Pessoa] = []

    def __str__(self):
        caixas = ", ".join([str(x) if x is not None else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

    def arrive(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if not self.espera:
            print("fail: sem clientes")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        self.caixas[index] = self.espera.pop(0)

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.caixas[index] = None

market = None

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    print("$" + line)

    parts = line.split()
    cmd = parts[0]

    if cmd == "$end":
        break

    if cmd == "$init":
        try:
            qtd = int(parts[1])
            market = Market(qtd)
        except (IndexError,ValueError):
            print(fail: inicializaçao invalida

    elif cmd == "$show":
        print(market)

    elif cmd == "$arrive":
        nome = parts[1]
        market.arrive(Pessoa(nome))

    elif cmd == "$call":
        market.call(int(parts[1]))

    elif cmd == "$finish":
        market.finish(int(parts[1]))
