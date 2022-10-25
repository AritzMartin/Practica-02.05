palabra = input('Escribe una palabra:\n')

if palabra == palabra[::-1]:
    print('Tu palabra es palíndromo')
else:
    print('Tu palabra no es palíndromo')