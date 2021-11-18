"""
3. Crea la clase Fracción. Los atributos serán numerador y denominador. Y
algunos de los métodos pueden ser invierte, simplifica, multiplica, divide, etc. Implementar los métodos invierte, multiplica (con otra fracción ), divide.
"""


class Fraccion():
    numerador = ""
    denominador = ""

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def invertir(self):
        numerador = self.denominador
        denominador = self.numerador
        return [numerador, denominador]

    # def simplificar(self):
    #     pass

    def multiplicar(self, otra_fraccion_numerador, otra_fraccion_denominador):
        res_numerador = self.numerador * otra_fraccion_numerador
        res_denominador = self.denominador * otra_fraccion_denominador
        return [res_numerador, res_denominador]

    def dividir(self):
        return self.numerador / self.denominador

    def get_numerador(self):
        return self.numerador

    def get_denominador(self):
        return self.numerador


numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))

fraccion1 = Fraccion(numerador, denominador)


fraccion_invertida = fraccion1.invertir()
print(
    f"La fraccion invertida es: { fraccion_invertida[0] } / { fraccion_invertida[1] }")

print("--------")
print("ingrese otra fraccion para multiplicar")
numerador1 = int(input("Ingrese el numerador: "))
denominador2 = int(input("Ingrese el denominador: "))
print("--------")
fraccion_multiplicada = fraccion1.multiplicar(numerador1, denominador2)


print(
    f'La fracción multiplicada es: { fraccion_multiplicada[0] } / { fraccion_multiplicada[1] }')


print(f'La fracción dividida es: { fraccion1.dividir() }')
