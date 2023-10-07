import re

texto = """Mira esta linea de texto capitán, cámara, podemos hacer muchas cosas.
Esta es la segunda linea de texto mi capitán.
afkajkfjakofj, iaejr if,figgodfijt
baba aaa a a  aa aa aa a aaa a aa aa aa aa aa abab ba ba ab
h
4
4352
562
7
87
af gg
ab abababbabab
abababbabaabab
"""

# Haciendo búsquedas simples
res_1 = re.search("Mira", texto)
res_2 = re.findall("capitán", texto)
res_3 = re.findall("esta", texto, flags=re.IGNORECASE)
print(res_1)
print(res_2)
print(res_3)

print("-------------")
# \d busca digitos numéricos del cero al nueve, los separa en una lista (aunque estén juntos)
res_4 = re.findall(r"\d", texto)
# \D busca todo, menos su contraparte minuscula
res_5 = re.findall(r"\D", texto)

# \w busca alfanumericos (a-z, A-Z, y el _)
res_6 = re.findall(r"\w", texto)
# \W ... menos alfanumericos
res_7 = re.findall(r"\W", texto)

# Con \n buscamos saltos de linea
res_8 = re.findall(r"\n", texto)
# Con . buscamos todo MENOS saltos de linea
res_9 = re.findall(r".", texto)

# \s busca los espacios en blanco (espacios, tabs y saltos de linea)
res_10 = re.findall(r"\s", texto)
# \S lo contrario
res_10 = re.findall(r"\S", texto)

# la barra cancela caraceres especiales
res_11 = re.findall(r"\.", texto)  # Cancela funcion de . y busca . tos


# E.G. Cadena que busque un numero, punto y espacio
resultado_ejemplo_1 = re.findall(r"\d\.\s", texto)
# Busca una cadena que coincida con la estructura
print(resultado_ejemplo_1)


# ^ Busca el comienzo de una linea, si lo encuentra lo añade a una lista
res_12 = re.findall(r"^Hola", texto)
print(res_12)
# Con flags=re.M se buscará en todas las lineas
res_13 = re.findall(r"^h", texto, flags=re.M)
# $ busca el final de una linea
res_14 = re.findall(r"\.$", texto, flags=re.M)
print(res_14)

# Si queremos repetir una cadena podemos usar {n}
# Por ejemplo, si queremos que nos de la cadena con tres números juntos con un salto de linea usamos:
resultado_ejemplo_2 = re.findall(r"\d{3}\n", texto)
print(resultado_ejemplo_2)

# {n,m} También sirve para rangos de coincidencias, n = minimo y m = maximo
resultado_ejemplo_3 = re.findall(r"\d{1,3}\n", texto)
print(resultado_ejemplo_3)

# Buscar en grupos
res_15 = re.findall(r"ab{2,4}", texto)  # solo busca b
# Si queremos que la busqueda se aplique a un conjunto de elementos
res_16 = re.findall(r"(ab){2,4}", texto)
print(res_15)
print(res_16)

res_17 = re.findall(r"(ab){2}", texto)  # Si encuentras abab devuelveme ab

# Con corchetes busca "aa", "ab", "bb", "ba" y si lo encuentra lo añade a la lista
print("------------")
res_18 = re.findall(r"[ab]{2}", texto)
print(res_18)
# | funciona como el operador or, es como hacer dos operaciones en una

res_19 = re.findall(r"\d{1,4}|^Mira", texto)
print(res_19)


print("------------------")


text_2 = "The brown fox jumps over the lazy dog"
x = re.search(r"^The.*dog$", text_2)
# Inicia con The, el asterisco actua retroactivamente para señalar que dé todo lo anterior (. es decir sin saltos de linea), si no existe, aún así todo bien. Y que termina con dog

if x:
    print("Es 'true'")
else:
    print("Es 'false'")

print("-----------------")
# El texto dado
text_3 = "La fecha es 30/09/2023 y el teléfono es +1-555-555-5555"
# El patrón a buscar
patron_texto_3 = r"\d{2}/\d{2}/\d{4}"
# Texto que remplazará al patrón
remplazador = "Fecha oculta"

new_text_3 = re.sub(patron_texto_3, remplazador, text_3)
print("El nuevo texto es:", new_text_3)
print("-----------------")

text_4 = "Remplaznado todas las vocales por asteriscos"
new_text_4 = re.sub("[aeiou]", "*", text_4)
# El [] sirve para que pueda ser en cualquier orden de esos caracteres
print(new_text_4)

print("-----------------")

eg_email = "Example@example.com"
patron_email = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# - sirve para separar de uno a otro valor
# %,@ NO TIENEN significado espcial, son literales
# + busca una o más coincidencias (como el asterisco pero envez de 0 o más)
# el + fuera del conjunto modifica todo el conjunto
# Lo mismo para lo que está después del arrova

es_valido_email = re.match(patron_email, eg_email)
if es_valido_email:
    print("¡Tu email es válido!")
else:
    print("Tu email no es válido, intenta otro")


eg_web_dom = "Esta es un sitio web cualquiera de internet https://www.example.com"
patron_web_dom = "https?://[a-z]{3,4}\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# el ? busca cero coincidencias o una
es_una_url_validad = re.findall(patron_web_dom, eg_web_dom)
if es_una_url_validad:
    print("¡Es una URL válida!")
else:
    print("No es una URL válida")
