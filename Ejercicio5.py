numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print('Esta es la lista: ')
for lista in numeros:
    print(lista, end=", ")

print('\n')
print('Esta es la lista en orden inverso: ')
numeros.reverse()
for lista2 in numeros:
    print(lista2, end=', ')
