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
for i in range(len(lista_preenchida)):
    temp = lista_preenchida[i]
    x = 3
    achou = False
    for v in lista_preenchida:
        if v == x:
            achou= True
            break
existe = x in lista_preenchida
pares = [v for v in lista_preenchida if v % 2 ==0]
dobro = [v * 2 for v in lista_preenchida]

def remover_primeira(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            lista.pop(i)
            return True
        return False
def remover_todos(lista,valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1
            funcoes_lista= dir(list)

def main ():
    if __name__ == "__name__":
        print("lista vazia:", lista_vazia)
        print("lista preenchida:", lista_preenchida)
        print("lista com objetos:", lista_preenchida_objetos)
        print("ultimo removido", ultimo)
        print("primeiro removido", primeiro)
        print("removido posiçao 2:", removido)
        print("join:", texto_formatado)
        print("sequencia:", sequencia)
        print("aleatorios", aleatorios)
        print("pares:", pares)
        print("dobro", dobro)
        print("3 existe na lista?", existe)        
        teste = [1, 2, 3, 2, 4]
        print("\nAntes remover primeira vez:", teste)
        remover_primeira(teste,2)
        print("Depois", teste)
        teste2 = [2, 2, 2, 3]
        print("\nAntes remover todos:", teste2)
        remover_todos(teste2, 2)
        print("depois:", teste2)
        print("\nFunçoes nativas de list:")
        print(funcoes_lista)
main ()