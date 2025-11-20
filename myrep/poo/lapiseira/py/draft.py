class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def gasto(self):
        if self.dureza == "HB": return 1
        if self.dureza == "2B": return 2
        if self.dureza == "4B": return 4
        if self.dureza == "6B": return 6
        return 0
    
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    
class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []

    def inserir(self, g: Grafite):
        if g.calibre != self.calibre:
                print("fail: calibre incompatível")
                return False
        self.tambor.append(g)
        return True
    
    def puxar(self):
         if self.bico is not None:
              print("fail: ja existe grafite no bico")
              return False
         if len(self.tambor) == 0:
              print("fail: nao ha grafites no tambor")
              return False
         self.bico = self.tambor.pop(0)
         return True
    def remover(self):
         if self.bico is None:
              print("fail: nao existe grafite no bico")
              return None
         self.bico = None
    def escrever(self):
         if self.bico is None:
              print("fail: nao existe grafite no bico")
              return
         
         g = self.bico
         gasto = g.gasto()

         if g.tamanho <= 10:
              print("fail: tamanho insuficiente")
              return
         
         novo_tam = g.tamanho - gasto
         
         if novo_tam < 10:
              print("fail: folha incompleta")
              g.tamanho = 10
              return
         
         g.tamanho = novo_tam

    def __str__(self):
         if self.bico is None:
              bico_str = "[]"
         else:
              bico_str = f"[{self.bico}]"

         if len(self.tambor) == 0:
              tambor_str = " <>"
         else:
              tambor_str = " <" + "".join(f"[{g}]" for g in self.tambor) + ">"

         return f"calibre: {self.calibre}, bico: {bico_str}, tambor:{tambor_str}"

def main():
     lap: Lapiseira |None = None

     while True:
          line = input()
          print("$" + line)
          args = line.split()

          if len(args) == 0:
               continue
          if args[0] == "end":
               break
          elif args[0] == "init":
               calibre = float(args[1])
               lap = Lapiseira(calibre)
          elif args[0] == "show":
               if lap is None:
                    print("fail: lapiseira nao iniciada")
               else:
                    print(lap)
          elif args[0] == "insert":
               if lap is None:
                    print("fail: lapiseira nao iniciada")
                    continue
               
               calibre = float(args[1])
               dureza = args[2]
               tamanho = int(args[3])
               g = Grafite(calibre, dureza, tamanho)
               lap.inserir(g)

          elif args[0] == "pull":
               if lap is None:
                    print("fail: lapiseira nao iniciada")
                    continue
               lap.puxar()
          elif args[0] == "remove":
               if lap is None:
                    print("fail: lapiseira nao iniciada")
                    continue
               lap.remover()
          elif args[0] == "write":
               if lap is None:
                    print("fail: lapiseira nao iniciada")
                    continue
               lap.escrever()

          else:
               print("fail: comando invalido")

main()
               
