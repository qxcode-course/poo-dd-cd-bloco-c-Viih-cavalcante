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
