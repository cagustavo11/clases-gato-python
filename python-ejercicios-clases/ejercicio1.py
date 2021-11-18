"""
1. Defina la clase Libro con los atributos isbn, autor, titulo y número de páginas, a continuación, cree tres objetos: lib, miLibrito, quijote. Implementar un método que defina si el libro está en calidad de préstamo.
"""


class Libro():
    isbn = ""
    autor = ""
    titulo = ""
    numero_de_paginas = ""
    calidad_de_prestamo = False

    def __init__(self, isbn, autor, titulo, numero_de_paginas):
        self.isbn = isbn
        self.autor = autor
        self.titulo = titulo
        self.numero_de_paginas = numero_de_paginas

    def estar_calidad_de_prestamo(self):
        self.calidad_de_prestamo = True


libro_isbn = input("ingrese el código del libro: ")
libro_autor = input("ingrese el nombre del autor del libro: ")
titulo_libro = input("ingrese el el titulo del libro: ")
paginas_libro = input("ingrese las paginas del libro: ")

lib = Libro(libro_isbn, libro_autor, titulo_libro, paginas_libro)
miLibrito = Libro(libro_isbn, libro_autor, titulo_libro, paginas_libro)
quijote = Libro(libro_isbn, libro_autor, titulo_libro, paginas_libro)
