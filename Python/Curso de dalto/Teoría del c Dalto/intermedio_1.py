"Continuación de Basicos 2"


"Variables 2.0"
"desempaquetado de variables"
# Es una forma de crear multiples variables de forma más ordenada


datos_personales = ("Walbert", "Isaac", "Trejo", "Ayala")
nombre, s_nombre, apellido, s_apellido = datos_personales
print(nombre)
# Oviamente debe haber mismo numero de variables que de datos en la raiz (que puden ser listas, tuplas o conjuntos [este último no permite desempaquetar números]).
"creando tuplas"
tupla_uno = ("dato1", "dato2")  # Forma tradicional
tupla_dos = tuple(["dato1", "dato2"])  # Con función tuple() , que recive una lista.
tupla_tres = "dato1", "dato2"
# Sin parentesis, requiere la coma, también es posible:
# tupla_tres = "dato1",

# Recuerda que las tuplas se usan cuando son datos de solo lectura, pues maneja mejor la memoria

# Las listas sirven para datos más flexibles y cambiantes

"conjuntos"
# Creando conjunto con set()
conjunto_1 = set(["dato1", "dato2", ("dato en tupla1", "dato en tupla2")])
# le pasamos una lista a set, dentro hay una tupla, pues estas son perfectas para ir dentro de conjuntos, pues son inmutables.

# Conjunto dentro de conjunto
# Se necesita un conjunto inmutable, con frozenset()
conjunto_2 = frozenset(["dato1", "dato2"])
conjunto_3 = {conjunto_2, "dato3"}
print(conjunto_3)

"teoría de conjuntos"
# En teoría de conjuntos, teniendo a{1,2,3} y b{1,2,3,4,5}, dependiendo de la perspectiva y cuál tomemos de conjunto: a es subconjunto del conjunto b; ó b es un superconjunto del conjunto a

# Verificando si es subconjunto
conjunto_a = {1, 2, 3, 5, 7, -70}
conjunto_b = {1, 3, 7}
# tanto .issubset como <= harían lo mismo
es_sub_conjunto_de = conjunto_b.issubset(conjunto_a)
es_sub_conjunto_de = conjunto_b <= conjunto_a
print(es_sub_conjunto_de)  # Booleano

# Verificando si es super conjunto de
# tanto .issuperset como > harían lo mismo
es_super_conjunto_de = conjunto_b.issuperset(conjunto_a)
es_super_conjunto_de = conjunto_b > conjunto_a
print(es_super_conjunto_de)  # Booleano

# Verificando si los conjuntos son diferentes, si almenos hay un valor en común el resultado será false
son_conjuntos_diferentes = conjunto_a.isdisjoint(conjunto_b)
print(son_conjuntos_diferentes)

# con not hacemos que verifiqu si hay datos iguales, se es así da true (lo contrario a lo anterior)
tiene_al_menos_un_dato_igual = not conjunto_a.isdisjoint(conjunto_b)
print(tiene_al_menos_un_dato_igual)


"Diccionarios"
# recordar que para crear diccionarios vacios se usa dict() , pues con las {} no se puede
diccionario_1 = dict(titulo="Don", nombre="Walbert", apellido="Trejo")
# En dict se usa = , en {} se usan :
print(diccionario_1)
# Puedes poner tuplas como keys, pero listas, y conjuntos normales, no.
diccionario_2 = {("dato1", "dato2"): "ejemplo de tupla como key"}
print(diccionario_2)

# Para crear diccionarios con todos sus keys, pero valores en none se usa el método .fromkeys() , .fromkeys es iterable, recuerda pasarle una lista
diccionario_3 = dict.fromkeys(["nametag", "username", "more_info"])
print(diccionario_3)
print(diccionario_3["nametag"])
# .fromkekys(iterable, cosa a la que podemos igualar todos las keys)
diccionario_4 = dict.fromkeys("ABCDE", 10)
print(diccionario_4)


"Bucle for"
# Un bucle (loop) es repetir de forma controlada un código

# Los bucles son sentencias que nos permiten iterar un elemento, solo los elementos iterables se pueden iterar (valgame la redundancia, pero era necesario decirlo), los valores se vuelven iterables cuando tienen un iterador que defina cómo se van a iterar (saltando entre trozos de código)

# el bucle for nos permite iterar
# for va a iterar los datos de la lista en este caso, aunque las tuplas y conjuntos también sirven en estos casos
lista_de_animales = ["perro", "gato", "loro", "cocodrilo"]
for animal in lista_de_animales:
    print(f"ahora la variable animal es igual a {animal}")

# otro ejemplo, recorriendo la lista lista_de_numeros y multiplicando por dos
lista_de_numeros = [
    643,
    3425,
    62,
    254,
]
for numero in lista_de_numeros:
    resultado = numero * 2
    print(resultado)

# Cuando tienes dos o más listas del mismo tamaño y quieres recorrerlas a la vez usas zip()
for (
    numero,
    animal,
) in zip(lista_de_numeros, lista_de_animales):
    print(f"el elemnto de la lista animal es: {animal}")
    print(f"el elemnto de la lista numeros es: {numero}")

# la función range() recorre elementos desde un rango (], si solo se se le da un número, inicia desde ahí
for num in range(3, 11):
    print(num)


print("---------------------")


# Forma NO OPTIMA de recorrer una lista con su indice, pues no funciona en conjuntos
for num in range(len(lista_de_numeros)):
    print(lista_de_numeros[num])

# Forma correcta de recorrer una lista con su indice
for num in enumerate(lista_de_numeros):
    # print(num)  # es una tupla con el indice y el valor.
    indice = num[0]
    valor = num[1]
    print(f"El indice es {indice} y su valor es {valor}")


# Usando el for/else
# Else siempre se va ejecutar al final del for
for num in lista_de_numeros:
    print(num)
else:
    print("El programa ha acabado")


"iterando conjuntos, recorriendo con enumerate"
# La forma INCORRECTA de recorrer conjuntos con su indice:

# for num in range(len(conjunto_de_numeros)):
#     print(lista_de_numeros[num])

# NO FUNCIONA EN CONJUNTOS, POR ESO SE USA enumerate()
"Iterando diccionarios"

print("-------------")

diccionario_5 = {"identificador": "ASDSDJKS", "buscador": "google"}

for datos in diccionario_5:
    print(datos)
# en este caso al decir print(datos) nos esta devolviendo las keys, para obtener las tuplas de los ejemplos anteriores se usa .items()

for datos in diccionario_5.items():
    key = datos[0]
    valor = datos[1]
    print(f"la key son {key} y el valor asociados son {valor}")

"Más iteraciones"
frutas = ["platano", "manzana", "naranja", "pera", "mango", "uva", "durazno"]
# El if seguido de la sentencia continue hace que, si es verdadero el bucle lo ignora
for fruta in frutas:
    if fruta == "uva":
        continue
    print(f"Me voy a comer un {fruta}")
print("---------")
# Si quieres que termine cuando llegue a un punto especifico usa la sentencia break
# La posición del if influye, pues este es un lenguaje que se ejecuta de arriba a abajo
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"Te estás comiendo {fruta}")
print("Bucle termindado")
# else no se ejecuta si hay una sentencia break

"Iterando textos"

cadena_1 = "Hola, qué tal estás"

for letra in cadena_1:
    print(letra)

"Matematicas aplicadas a listas en una sola linea"
numeros_1 = [1, 5, 8, 528, 47, 6, 6864, 3, 2, 77]
multiplicar_lista_por_dos = [x * 2 for x in numeros_1]
print(multiplicar_lista_por_dos)


"bucle while"
# Si la condición se cumple, el codigo sigue en bucle
contador = 0
while contador <= 5:
    print(contador)
    contador += 1
print("while llegó a su fin")


"Continua en intermedio_2"
