"Continuación de la parte uno"

"Metodos aplicados a listas"

# la función list() crea una lista, su mejor uso es para hacer listas vacias. De lo contrario es igual a una lista hecha simplemente con []
# la función len() puede ser util para saber la cantidad de elemntos de la lista.
lista_numero_uno = list(
    [
        "hola a todos",
        "elemento dos",
        43,
        345,
        54,
        True,
        "item beta",
        "la gorda",
        False,
        "not heavenly skies",
        False,
        349,
        True,
    ]
)
cantidad_de_elementos = len(lista_numero_uno)


# agregar elementos a la lista

lista_numero_uno.append("aguacate")
print(lista_numero_uno)
# no se llama a la variable agregado_con_append , sino a la lista

# con extend se le dice el indice en donde será agregado el nuevo elemento
lista_numero_uno.insert(2, "chocolate")

# Para agregar más elementos se debe pasar una lista al extend
lista_numero_uno.extend(
    [True, 35, "dross", "gaturro", "comiendo", 7865, 75409, True, True, False]
)


# pop elimina elementos de la lista por indices
lista_numero_uno.pop(1)
lista_numero_uno.pop(-1)  # elimina el ultimo elemento de la lista
lista_numero_uno.pop(-3)  # elimina la antepenultima

# Con .remove() se busca el valor dentro de la lista, luego lo elimina de la lista
lista_numero_uno.remove("gaturro")
# Si se da un string que no reconoce, salta una excepción

# Con .clear() se eliminan todos los elementos de la lista
print(lista_numero_uno)
ver_lista_vacia = lista_numero_uno.clear()
print(ver_lista_vacia)

lista_numero_dos = list(
    [78, 85, 64, 13, 24, 652, False, False, True, False, True, 787, 89, 9, True]
)
# Con .sort() sen ordenan las listas de nuemros y boleanos de menor a mayor. Primero false, true, y al final los numeros.
lista_numero_dos.sort()  # También existe la propiedad reverse = True que da vuelta el orden (mayor a menor)

# .reverse simplemente cambia el orden de la lista, a diferencia de .sort(reverse=true), .reverse no ordena la lista, solo cambia el indice.
lista_numero_dos.reverse()

# La función index busca elementos completos en listas. Igual a lo anterior lanza excepciones si no encuentra el elemento.
elemento_encontrado_en_l2 = lista_numero_dos.index(9)
print(elemento_encontrado_en_l2)


"Metodos a tuplas y conjuntos"

# Las tuplas al ser inalterables, solo se les puede aplicar .count() e .index()
tupla_uno = tuple(("hola", "me llamo", "isaac", 8))  # Tupla
# Solo se pueden buscar elementos y usar elementos.

print(dir(set[3, 2, True, False]))  # Conjunto
# En el conjunto solo se pueden sacar y remover elementos, pero no agregarlos, ni ver el indice. Pero si se puede hacer las otras cosas
# Nt: ahora hay metodos para agregar cosas, contar elementos dentro

"Metodos a los diccionarios"

diccionario_uno = {
    "nombre": "Walbert",
    "apellido": "Trejo",
    "user_name": "Walbert06",
    "edad": 17,
}
claves_de_diccionario_uno = diccionario_uno.keys()
print(
    claves_de_diccionario_uno
)  # las claves son el como el indice en las listas, es decir el primer elemnto
# nos devuelve un objeto dict_item que se puede iterar

# .get() te busca el elemento asociado a la key que pidas, se puede hacer también con [], pero estos, al no encontrar el elemento buscado lanzan una excepción. .get() solo respomde none
dame_el_ = diccionario_uno.get("edad")
print(dame_el_)
# ejemplo:
if diccionario_uno.get("edad") >= 17:
    print("No puedes pasar eres menor de edad")
else:
    print("Pásale, que te diviertas")

# .pop() elimina con la key que le pasamos, se pueden separar por comas
diccionario_uno.pop("nombre", "apellido")

# .items te da los valores del diccionario de manera que son iterables
diccionario_iterable = diccionario_uno.items()
print(diccionario_iterable)

# .clear() limpia el diccionario
diccionario_uno.clear()
print(diccionario_uno)


"Entrada de datos"

# Pedirle un dato al usuario
dame_tu_nombre = input("Hola usuario, dame tu nombre: ")
print(f"El nombre del usuario es {dame_tu_nombre}")


# input() siempre devuelve textos
# Para convertir a número, se usa la función int() o fload según sea conveniente
dame_un_numero = input("Pásame un número: ")
numero_resultado = 2 * int(dame_un_numero)
print(numero_resultado)


"Continua en la intermedio_1"
