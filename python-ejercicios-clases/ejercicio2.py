class Gato():

    def __init__(self, color, raza, edad, sexo, peso_kg):
        self.color = color
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso_kg = peso_kg

    def maullar(self):
        return "Meowth, Meowth, Meowth"

    def ronronear(self):
        return "Estoy ronroneando..."

    def comer(self, alimento):
        if alimento.lower() == "pez":
            return "Estoy comiendo mi pescado"

    def pelear(self, contrincante):
        if self.sexo == "hembra":
            return f"No me gusta pelear"
        else:
            if contrincante.get_sexo() == "hembra":
                return f"No peleo contra gatitas"
            else:
                return f'¡venga pa ca!'

    def get_sexo(self):
        return self.sexo


listaColores = []
listaRaza = []
listaEdades = []
listaPesos = []

for i in range(1, 4):
    colorGato = input(f"ingrese el color del gato{i}: ")
    razaGato = input(f"ingrese la raza del gato{i}: ")
    edadGato = input(f"ingrese la edad del gato{i}: ")
    pesoGato = input(f"ingrese el peso del gato{i}: ")
    print("------------")
    listaColores.append(colorGato)
    listaRaza.append(razaGato)
    listaEdades.append(edadGato)
    listaPesos.append(pesoGato)

gato1 = Gato(listaColores[0], listaRaza[0],
             listaEdades[0], "macho", listaPesos[0])
gato2 = Gato(listaColores[1], listaRaza[1],
             listaEdades[1], "macho", listaPesos[1])
gato3 = Gato(listaColores[2], listaRaza[2],
             listaEdades[2], "hembra", listaPesos[2])

print(gato1.pelear(gato2))
print(gato1.ronronear())
print(gato1.comer("pez"))
print(gato1.maullar())
