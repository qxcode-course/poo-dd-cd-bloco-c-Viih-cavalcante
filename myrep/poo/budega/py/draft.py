class Pessoa:
    def __init__(self, nome : str):
        self._nome = nome

    def __str__(self) -> str:
        return self._nome
    
    def enter(self, pessoa: str):
        self.espera.append(pessoa)

    def call(self, index: int):
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if index < 0 or index >= len(self.caixas):
            print("indice inexistente")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0]
    def finish 

class Budega:
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa | None] = []