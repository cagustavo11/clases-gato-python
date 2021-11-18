"""
Crear una clase Alumno, implementar una Lista de N alumnos identificados por su código de 
estudiante, apellidos y nombres y edad; después mostrar una lista ordenada por la edad.
"""


class Alumno():

    def __init__(self, codigo_estudiante, apellidos, nombres):
        self.codigo_estudiante = codigo_estudiante
        self.apellidos = apellidos
        self.nombres = nombres

    def get_nombres(self):
        return self.nombres


alumnos = []

n = int(input("ingrese la cantidad de alumnos: "))

for i in range(n):
    codigo_estudiante = int(input("ingrese su código de estudiante: "))
    apellidos = input("ingrese sus apellidos: ")
    nombres = input("Ingrese sus nombres: ")

    alumnos.append(Alumno(codigo_estudiante, apellidos, nombres))

print("----------")
for i in range(n):
    print(f'Estudiante: { alumnos[i].get_nombres() }')
    print("----------")
