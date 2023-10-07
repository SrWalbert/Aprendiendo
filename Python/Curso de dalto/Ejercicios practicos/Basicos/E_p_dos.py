# Texto del usuario
texto_del_usuario = input(
    "Dame cualquier texto, te diré cuanto tardarías en decirlo, cuantas palabras son, pero que no pase de un minuto. Tu texto es: "
)

# Mide la canitidad de palabras
separar_palabras = texto_del_usuario.split(" ")
cantidad_de_palabras = len(separar_palabras)

# Cuanto tardaría
se_tardaria = cantidad_de_palabras / 2
dalto_tardaria = cantidad_de_palabras / round((2 * 1.3), 2)
# Imprimir primeros datos
if se_tardaria > 60:
    print("Para flaco, tampoco te pedí tu testamento")
else:
    print(f"Te tardarías {se_tardaria} segundos en decir esa oración")
    print(f"Escribiste un total de {cantidad_de_palabras} palabras")
    print(f"Dalto se tardaría {dalto_tardaria} segundos")
