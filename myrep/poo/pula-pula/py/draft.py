class Criança:
    def __init__(self, nome : str, tempo: int):
        self.nome = nome
        self.twmpo = tempo

    def __str__(self):
        return self.nome

class PulaPula:
    def __init__(self, capacidade : int):
        self.capacidade = capacidade
        self.dentro: list[Criança] = []

    def entrar(self, criança: Criança):
        if len(self.dentro) < self.capacidade:
            self.dentro.append(criança)
            return True
        return False
    
    def sair_primeiro(self):
        if self.dentro:
            return self.dentro.pop(0)
        return None
    
    class GestorPulaPula:
        def __init__(self, capacidade_pulapula: int):
            self.fila: list[Criança] = []
            self.pulapula = PulaPula(capacidade_pulapula)

        def adcionar_na_fila(self, criança: Criança):
            self.fila.append(criança)
        def mover_fila_para_pulapula(self):
            if self.fila:
                primeira = self.fila.pop(0)
                if self.pulapula.entrar(primeira):
                    return True
                else:
                 self.fila.insert(0,primeira)
                return False
            return False