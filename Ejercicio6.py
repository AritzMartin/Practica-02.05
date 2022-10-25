lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia',  'Lengua']
lista_notas = []

for asignatura in lista_asignaturas:
    print('Cual es tu nota en:', asignatura)
    lista_notas.append(int(input()))
for lista in range(len(lista_asignaturas)):
    if lista_notas[lista] < 5:
        print('Tienes que recuperar:\n', lista_asignaturas[lista])