"Continuación de intermedio_1"

"Funciones"
# Son fragmentos de codigo que podemos usar cada vez que querramos sin necesidad de volver a escribirlo todo desde cero
# A las funciones integradas por python se les llama built-in

"funciones built in"
# Para conjuntos, listas y tuplas con numeros existen max y min para encontrar los valores más altos o bajos del conjunto en cuestión


numeros_1 = (1, 35, 65, 7, 3, 245, 6, 763, 73, 478, 686, 2462, 754)
minimo_en_numeros_1 = min(numeros_1)  # devuelven excepciones si no se les da números
maximo_en_numeros_1 = max(numeros_1)
print(minimo_en_numeros_1)
print(maximo_en_numeros_1)

# Para redondear usas round, pero si quieres un numero de decimales lo escribes como segundo valo de la función
redondear_decimales = round(7 / 3, 3)
print(redondear_decimales)

# bool() devuelve falso si: se le da 0, vacio, False, None. Y True si se le da: distinto de 0, True, cadena, datos no vacíos.
print(bool())
# all() trabaja con lo anterior mencionado, si todo es verdadero es True, si hay un solo elemento de las caracteristicas de falso, devuelve False.
print(all(["Ejemplo de lista", 5432, 42, 245, True, True, "texto"]))

# sum() devuelve la suma de todos los iterables
print(sum(numeros_1))  # devuelven excepciones si no se les da números


"Creando funciones propias"


# Se usa def para esto, luego el nombre y los parentesis son importantes
# Creando función
def saludar():
    print("Hola amigo, ¿cómo andas?")


saludar()


# Si quieres añadir variables es así
def saludar(nombre, sexo):
    nombre = nombre.capitalize()
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titán"
    else:
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo}, ¿cómo estás?")


saludar("camila", "mujer")


# Para el back end, la sentencia return es muy util, pues así se guarda lo que retorna de la función. Return puede retornar más valores, en una tupla o lista por ejemplo
def n_contrasena(num):
    chars = "LoremIpsumDolorSitAmet"
    num_entero = str(num)
    num = int(num_entero)
    c1 = num - 2
    c2 = num + 7
    c3 = num + 5
    c4 = num
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{num*56}"
    return contrasena


# Para mostrar lo oculto, podemos trabajar conlo que pusimos en return fuera de la función
def p_n_contrasena(num):
    print(f"Tu nueva contraseña es {n_contrasena(num)}")


p_n_contrasena(5)


# Forma NO OPTIMA de sumar valores o hacer otras cosas
def suma_noptima(lista):
    numeros_sumados = 0
    for numeros_f in lista:
        numeros_sumados = numeros_sumados + numeros_f
    return numeros_sumados


resultado_suma = suma_noptima([5, 3, 9, 90, 8])
print(resultado_suma)


# forma óptima usando el operador * como parametro en (*args); este parametro debe de ir al final
def suma(*numeros_sum):
    return sum(numeros_sum)


# recordemos que sum() suma iterables


# De esta manera args no requiere ir al último de los datos de entrada, pero en este caso necesitará una lista como valor de entrada
def suma2(numeros_sum_2):
    return sum([*numeros_sum_2])


# Se debe pasar un lista, usando la forma dos
print(suma(5, 3, 9, 90, 8))
print(suma2([5, 3, 9, 90, 8]))


# Forzando argumentos con palabras clave
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"


print(frase("Walbert", "Trejo", "inteligente"))
# De esta manera se fuerzan los argumentos, una vez forzado uno, se deben de escribir todos de la misma forma (keyword arguments)
print(frase(adjetivo="grade", apellido="Ayala", nombre="Isaac"))

# También puede haber parametros opcionles predefinidos en la función, que podrías cambiar de la forma anterior, o simplemente rellenando el espacio vacío, si dejas el espacio vacío se ejecutará el parametro opcional


"Funciones lambda"
# Lambda crea funciones anónimas
# así como los strings y listas, las cuales no son asignadas a una variable, las funciones lambda no tienen nombre

multiplicar_por_dos = lambda x: x * 2

print(multiplicar_por_dos(2))


# De esta manera nos evitamos hacer este bloque de coodigo
def multiplicar_por_dos_def(x):
    return x * 2


print(multiplicar_por_dos_def(2))

# Las funciones lambda son muy útiles cuando se tienen que dar instrucciones sencillas, no requieren sentencia return, pero son malas cuando se necesita más de un instrucción

# La función filter manda su segundo parametro (iterables) a la función del primer parametro, los valores que sean True se agregan a una lista. Es como un bucle
numeros_posible_par = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 162, 85, 74, 33, 73]


# Ejemplo de filter y forma NO OPTIMA
def es_par(num):
    if num % 2 == 0:
        return True


numeros_pares = filter(es_par, numeros_posible_par)
print(list(numeros_pares))


# Forma optima con funciones lambda
numeros_pares_lambda = list(
    filter(lambda numeros: numeros % 2 == 0, numeros_posible_par)
)
print(numeros_pares_lambda)

"Continua en intermedio_3"
# C:\Users\gertr\OneDrive\Escritorio\Walbert\VS Code\Aprendiendo\Python\Curso de dalto\Teoría del c Dalto\Intermedio_3\intermedio_3.py
