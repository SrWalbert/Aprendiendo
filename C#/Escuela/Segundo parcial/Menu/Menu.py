# Vamos a hacer un restaurante, escribe el menu


# Información
print(
    "|__________Menu de amburguesas__________|\n|1.Haburguesas.......................$50|\n|2.Pizza.............................$30|\n|3.Agua..............................$50|\n|4.Refresco..........................$15|\n|5.papas.............................$15|)"
)


# Para que seleccionen que van a pedir
print("¿Qué vas a pedir?\n")


while True:
    pedido: int = input("Ingresa el NÚMERO que deseas pedir: ")
    try:
        pedido = int(pedido)
        if pedido > 5:
            raise
        break
    except Exception as e:
        if e == ValueError:
            print("Introduce el dato correctamente")
        else:
            print("Tu numero es superior a 5")

print("Estamos procesando tu pedido")
match pedido:
    case 1:
        print("Se están preparando tus haburguesas")
    case 2:
        print("Se está preparando tu pizza")
    case 3:
        print("Aquí está tu agua")
    case 4:
        print("Aquí está tu refresco")
    case 5:
        print("Aquí están tus papas")
