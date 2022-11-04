vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
producto = 0

for lista in range(len(vector1)):
    producto += vector1[lista]*vector2[lista]

print('El producto de los vectores ' + str(vector1) + ' y ' + str(vector2) + ' es de ' + str(producto))