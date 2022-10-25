import string
abcd = list(string.ascii_lowercase)

for fila in range(len(abcd), 1, -1):
    if fila % 3 == 0:
        abcd.pop(fila-1)
for lista in abcd:
    print(lista, end=', ')
