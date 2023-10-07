"Tipos de datos simples"
# """Existen varios tipos de datos, con comillas simples, que solo sirven para una linea, los de triple comilla, que son utiles para diferentes renglones, numeros entertos Int y flotantes fload. Además de los booleanos true o false. """

"Que son las variables"
# """Las variables son datos que se almacenan, pueden variar. se pueden operar números en las variables.
# Las variables se declaran y luego definen (se puede cambiar la definición)."
# "Las variables pueden tener datos simples o complejos"""


"Definiendo variables"


nombre = "aguacate"
c = 12 - 6
c = 33
c += 1
print(c)
# Se recomienda usar guiones bajos para variables de dos palabras
# Concadenaciones.
# Hay varias formas de hacerlo como
user = " Mario "
bienvenida = "Hola" + user + "como estás"  # concatenar con +
print(bienvenida)
# mejor usar:
bienvenida = f"Hola {user} cómo estás?"  # concatenar con f stings


"del borra datos"


del c
del nombre
del user

"In, not in dentro de print()"
# Para generar un booleano al buscar una secuencia de texto determinada se usan los operadores de pertenencia como los de abajo. Recordar que el lenguaje es sensible a mayusculas y minusculas
print("ola" in bienvenida)  # Esto da true. También existe   not in
print("ola" not in bienvenida)


"Datos complejos"
# Son datos simples u otros datos complejos agrupados


"Listas []"
ejemplo_de_lista = ["dato uno", "Pez", True, 1]
print(ejemplo_de_lista[0])
# recordar que en la lista, con el indice se cuenta desde cero.
# Las listas son un tipo de matrices
# Las listas sirven para datos más flexibles y cambiantes

# Las listas se pueden modificar, las tuplas no. Ambas se pueden redefinir
# Las tuplas se usan cuando son datos de solo lectura, pues maneja mejor la memoria
ejemplo_de_lista[1] = "Gato"
print(ejemplo_de_lista[1])

ejemplo_de_tupla = ("dato uno", "Pez", True, 1)  # ejemplo de tupla
print(ejemplo_de_tupla[0])

"Conjunto"
# Se pueden redefinir entero, pero no un solo elemnto del conjunto, los datos están desordenados, no se puede llamar a los elementos por índice, no permite repetir elementos,

ejemplo_de_conjunto = {"dato", False, 30, "dedo"}


"Diccionario"
# Es como un json, pues es una lista, pero en vez de numeros usa palabras
ejemplo_de_diccionario = {
    "dato_1": "agua",
    "animal": "gato",
    "valor": True,
    "numero": 4,
}
print(ejemplo_de_diccionario["valor"])


"Operadores aritméticos"

# suma +, resta -, multiplicación *, división /

suma = 5 + 5
resta = 7 - 5
división = 12 / 6  # siempre da como resultado un valor flotante
multiplicacion = 6 * 6
Potensiacion = 6**2
division_baja = 12 // 2  # devuelve entero redondeado hacia abajo

# resto o modulo %
resto = 6 % 2  # lo que queda de la división

"Operadores de comparación"

# Devuelven un valor Booleano
es_igual_que = 9 == 5
es_distinto_que = 9 != 8  # lo contrario a lo anterior

# y lo mismo para los que siguen: menor que <, mayor que >, menor o igual que <=, mayor igual >=
a = 10
b = 7
c = 20
comparacion = a + b == c
print(comparacion)
# Se pueden comparar textos con ==


"Condicionales"

# El if funciona con la siguiente gramática.
# If condición:
#   Acción
# else
# Acción en caso de que la condición de false
# si la condición es true, la acción se cumple

edad = 15
if edad >= 18:
    print("Puedes pasar, disfruta")
else:
    print("No puedes pasar")

# Elif (diminutivo de else if) Sirve por si tenemos dos "if"s y un else, pues en dicho caso, el else siempre se cumpliría, elif hará que la secuencia sea más ordenada

ingreso_mensual = 500
gasto_mensual = 700
# Se pueden hacer if's anidados
if ingreso_mensual - gasto_mensual >= 5000:
    print("Tu situación económica está bien")
elif ingreso_mensual - gasto_mensual <= 300:
    print("Estás yendo muy justo, intenta ahorrar más")
elif ingreso_mensual - gasto_mensual <= 0:
    print("Estás gastando demasiado")
elif ingreso_mensual >= 1000:
    print("...Pero estás bien en latinoamérica")
else:
    print("Eres pobre")

"Operadores lógicos"

# And
resultado_op_log_and_1 = True & True  # =True
resultado_op_log_and_2 = True & False  # =False
resultado_op_log_and_3 = False & True  # =False
resultado_op_log_and_4 = False & False  # =False
# Solo devuelve true si ambos son true


# Or
resultado_op_log_or_1 = True or True  # =True
resultado_op_log_or_2 = True or False  # =True
resultado_op_log_or_4 = False or True  # =True
resultado_op_log_or_3 = False or False  # =False
# Devuelve true si uno de los dos es true

# Not
resultado_op_log_not_1 = not True  # =False
resultado_op_log_not_2 = not False  # =True
# Lo contrario de lo que se le da


"Metodos de Cadenas"  # Los "métodos" son funciones aplicadas a objetos. Van seguidos de un "."
# En python muchas cosas pueden ser consideradas objetos, como una variable, lista o un texto

# Una función analiza pedasos de texto que nosotros les damos. Por ejemplo es print(), nombre_de_funcion("parametro"). Eg.
# Print(resultado), type(tipo de dato)


# La **fución** dir nos devuelve lo que le podemos hacer a su objeto (dir debe estar dentro de un print() )
cadena1 = "ejemplo de cadena"
cadena2 = "ejemplo de cadena dos"
cadena3 = "587795279845792"
# print(dir(cadena1))

Resultado_de_metodos = cadena1.upper()
print(Resultado_de_metodos)
# Los metodos siguen a la variable, despues de un punto (se pueden poner parametros entre parentesis), en este caso .upper cambia el texto a mayusculas.

Resultado_de_metodos = "AGUACATES".lower()
# funciona con strings como es logico, a minuscula
print(Resultado_de_metodos)

# Solo primera letra a mayuscula
Resultado_de_metodos = cadena2.capitalize()
print(Resultado_de_metodos)

#
# .find encuentra un caracter coincidente con su parametro y te da su posicion, si no existe devuelve -1
busqueda_find = cadena2.find("j")
print(busqueda_find)
# .index funciona casi igual que .find, pero si no encuentra resultados, index nos lanzará una excepción.
# busqueda_index = cadena2.index("j")

# .isnuemric verifica si el valor es numerico, con resultado booleano.
# Solo funcina con strings
es_numerico = cadena3.isnumeric()
print(es_numerico)
# igual que el anterior pero solo para letras, LOS ESPACIOS NO SON ALFANUMERICOS
es_alfanumerico = cadena2.isalpha()
print(es_alfanumerico)


# .count encuentra un caracter coincidente con su parametro y te da el numero de coincidencias encontradas
contar_coincidencias = cadena2.count("a")
print(contar_coincidencias)

# len es una función que cuenta caracteres
contar_caracteres = len(cadena1)
print(contar_caracteres)

# .startswith verifica si una cadena empieza con ciertos caracteres, devuelve booleanos
empieza_con = cadena1.startswith("hola")
print(empieza_con)
# .endswith verifica si una cadena termina con ciertos caracteres, devuelve booleanos
empieza_con = cadena1.endswith("hola")
print(empieza_con)


# .replace verifica si hay valores coincidentes en una cadena, se los hay, lo reemplaza por lo que se indique, si no deja dicha cadena sin modificar
cadena_nueva = cadena1.replace("ejemplo", "Nuevo ejemplo")
print(cadena_nueva)


# Va a separar cadenas con la cadena que le pasamos, devuelve una matriz (lista)
cadena4 = "Hola, como estás, tengo 34"
cadena_separada = cadena4.split(",")
print(cadena_separada)


"Continuará en Basicos 2. py"
