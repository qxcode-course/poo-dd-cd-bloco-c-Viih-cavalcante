class Foo:
    def __init__(self, x: int):
        self.x = x
    def __str__(self):
        return f"FFoo({self.x})"
    
lista_vazia: list[int] = []
lista_preenchida: list [int] = [1, 2, 3, 4, 5]
lista_preenchida_objetos: list[Foo]= [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lista_vazia.append(10)
lista_preenchida.append(6)
ultimo = lista_preenchida.pop()
lista_preenchida.insert(0,99)
primeiro = lista_preenchida.pop(0)
lista_preenchida.insert(2, 777)
removido = lista_preenchida.pop(2)
palavras = ["ola", "mundo", "python"]
texto_formatado = " | ".join(palavras)
n = 5
sequencia = list(range(n + 1))
import random
aleatorios = [random.randint(1, 10) for _ in range(5)]
primeiro_elemento = lista_preenchida[0] if len(lista_preenchida) > 0 else None
for valor in lista_preenchida:
    pass
for i in range(len(lista_prenchida)):
    temp = lista_preenchida[i]
    x = 3
    achou = False
    for v in lista_preenchida:
        if v == x:
            achou= True
            break
existe = x in lista_preenchida