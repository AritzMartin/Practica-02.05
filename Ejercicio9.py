palabra = input('Escribe una palabra:\n ')
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    tiempo = 0
    for letra in palabra.lower():
        if letra == vocal:
            tiempo += 1
    print('La vocal ' + vocal + ' se repite ' + str(tiempo) + ' veces')