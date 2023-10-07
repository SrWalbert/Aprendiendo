# Definiendo clase


from ast import Return


class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.nombre = Nombre
        self.edad = Edad
        self.grado = Grado

    def estudiar(self):
        print(f"El alumno {self.nombre} está estudiando")


# Obteniendo datos
while True:
    Nombre = input("Dame tu nombre de pila: ")
    Edad = input("Escribe tu edad en números: ")
    Grado = input("Escribe tu grado en número: ")

    try:
        # Convirtiendo numeros
        Edad = int(Edad)
        Grado = int(Grado)
    except:
        print("Parece que has escrito algún dato de forma incorrecta")
    else:
        break

# Creando objeto alumno
alumno_x = Estudiante(Nombre, Edad, Grado)

# Imprimiendo los datos
print(
    f"Datos.\n\nNombre del alumno: {alumno_x.nombre}\nEdad: {alumno_x.edad}\nGrado: {alumno_x.grado}\n\n"
)

# estudiar input
respuesta = input("")
respuesta = respuesta.lower()
if respuesta == "estudiar":
    alumno_x.estudiar()
