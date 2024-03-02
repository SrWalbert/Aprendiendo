"""Las funciones build-in 'map' y 'filter' pueden ser escritas de forma más pythonica"""

"En vez de all()"
print(all(["Ejemplo de lista", 5432, 42, 245, True, True, "texto"]))
print(
    True
    if False not in ["Ejemplo de lista", 5432, 42, 245, True, True, "texto"]
    else False
)
