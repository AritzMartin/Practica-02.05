muestra_numeros = input('Introduce una muestra de números separados por comas:\n')
muestra_numeros = muestra_numeros.split(',')
numeros = len(muestra_numeros)

for lista in range(numeros):
    muestra_numeros[lista] = int(muestra_numeros[lista])
muestra_numeros = tuple(muestra_numeros)
suma = 0
suma_al_cuadrado = 0

for lista in muestra_numeros:
    suma += lista
    suma_al_cuadrado += lista**2

media = suma/numeros
desviacion = (suma_al_cuadrado/numeros-media**2)**(1/2)

print('La media es de: ', media, 'y la desviación es de: ', desviacion)