class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []

    def __str__(self):
        caixas = ", ".join([str(x) if x is not None else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    market = None
    while True:
        try:
            line = input().strip()
        except eE0FError:
            break
        if line == "":
            continue
        args =line.split()
        cmd + args[0]
        if cmd == "$end":
            break
        elif cmd == "$init":
            qtd = int(args{1})
            market = Market(qtd)
        elif cmd == "$show":
            print(market)
        elif cmd == "$arrive":
            market.arrive(args[1])
        elif cmd == "$call"
        
