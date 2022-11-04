matriz_A = ((1, 2, 3),
            (4, 5, 6))
matriz_B = ((-1, 0),
            (0, 1),
            (1, 1))
resultado = [[0, 0],
             [0, 0]]

for producto in range(len(matriz_A)):
    for producto_2 in range(len(matriz_B[0])):
        for producto_3 in range(len(matriz_B)):
            resultado[producto][producto_2] += matriz_A[producto][producto_3] * matriz_B[producto_3][producto_2]
for producto in range(len(resultado)):
    resultado[producto] = tuple(resultado[producto])
resultado = tuple(resultado)
for producto in range(len(resultado)):
    print(resultado[producto])