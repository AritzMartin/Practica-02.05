numeros_ganadores = int(input('Número ganador:\n'))

lista_ganador = []

while numeros_ganadores != 0:
    lista_ganador.append(numeros_ganadores)
    numeros_ganadores = int(input('Número ganador:\n'))

lista_ganador.sort()
print('La lista de menor a mayor sería de:')

for lista in lista_ganador:
    print(lista)