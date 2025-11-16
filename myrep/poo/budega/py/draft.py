#PRATICA DA BUDEGA

class Pessoa:
    def __init__(self, nome :str):
        self.nome = nome
    def getNome(self):
        self.nome
    def __str__(self):
        return self.nome
class budega:
    def __init__(self, num_caixas :int):
        self.caixas: list[Pessoa | None] = []
        for _ in range (num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] =[]
    def __str__(self):
        caixas = ", ".join([str(x) for (x) in self.caixa])
        espera = ", ".join([str(x) for (x) in self.espera])
        return f"Caixas:{caixas}\nEspera:{espera}"

      
      
 pessoa = Pessoa("Maria")
 print("maria")

budega = Budega(5)
budega.caixas[2] + pessoa
 budega.espera.append(pessoa)
print(budega(

        )