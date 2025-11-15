espera: list[str] = []

espera.append("joao")
espera.append("bruxa")
espera.append("bruxa")

del espera [1]

espera = ["maria"] + espera
del espera [0]

espera.append("lobo")
espera.append("caçador")

del espera [2]

espera.insert(2,"lobo")

espera_texto = "-".join(espera)

print(espera_texto)
#PRATICA DA BUDEGA

class Pessoa:
    def __init__(self, nome :str):
        self.nome = nome
    def __str__(self):
        return self.nome
    
class budega:
    def __init__(self, num_caixas :int):
        self.caixas: list[Pessoa | None] = []
        for _ in range (num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] =[]
    def __str__(self):
        return f"Caixas:{num_caixas

        pessoa = Pessoa("Maria")
        print("maria")

        budega = Budega(3)
        print(budega)