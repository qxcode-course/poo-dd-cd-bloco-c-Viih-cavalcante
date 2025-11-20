class Cliente:
    def __init__(self, id :str, phone : int):
        self.id = id
        self.phone = phone

    def getNome(self) -> str:
        return self.id
    
    def getPhone(self) -> int:
        return self.phone
    
    def setId(self, novo_id: str):
        self.id = novo_id

    def setphone(self, novo_phone: int):
        self.phone = novo_phone

    def __str__(self) -> str:
        return f"{self.id}:{self.phone}"

class SalaCinema:
    def __init__(self, capacidade :int):
        self.cadeiras: list[Cliente | None] = []
        for _ in range (capacidade):
            self.cadeiras.append(None)

    def procurar_cliente(self, id : str):
        for i, cliente in enumerate(self.cadeiras):
            if cliente is not None and cliente.id == id:
                return i
        return -1
    
    def verificar_indice(self, index: int) -> bool:
        return 0 <= index < len(self.cadeiras)
    
    def reserve(self, id: str, phone: int, index :int):
        if not self.verificar_indice(index):
            print("fail: cadeira nao existe")
            return
        
        if self.cadeiras[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        
        if self.procurar_cliente(id) != -1:
            print("fail: cliente ja esta no cinema")

        self.cadeiras[index] = Cliente(id, phone)

    def cancelar(self, id: str):
        posiçao = self.procurar_cliente(id)
        if posiçao == -1:
            print("fail: cliente nao esta no cinema")
            return
        self.cadeiras[posiçao] = None
    
    def getCadeiras(self):
        return self.cadeiras
    
    def __str__(self):
        return "[" + " ".join("-" if c is None else str (c) for c in self.cadeiras) + "]"
def main():
    sala = SalaCinema(0)
    while True:
        linha = input()
        print("$" + linha)
        args = linha.split()
        if len(args) == 0:
            continue

        if args[0] == "end":
            break

        elif args[0] == "init":
            sala = SalaCinema(int(args[1]))

        elif args[0] == "show":
            print(sala)

        elif args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            sala.reserve(id, phone, index)

        elif args[0] == "cancel":
            id = args[1]
            sala.cancelar(id)

        elif args[0] == "cancelar":
            id = args[1]
            sala.cancelar(id)

        else:
            print("fail: comando invalido")
            continue

main()
        
#Adorei essa atividade S2.