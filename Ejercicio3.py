lista_asignaturas = ['Matemática', 'Lengua', 'Historia', 'Física', 'Química']
nota_asignatura = []
for asignatura in lista_asignaturas:
    print('Cual es tu nota en:', asignatura)
    nota_asignatura.append(input())

for lista in range(len(lista_asignaturas)):
    print(lista_asignaturas[lista], ':', nota_asignatura[lista], sep='')