import saludar as sald

saludo = sald.saludar_persona("Ana")
print(saludo)
# Se tienen que usar como métodos
# Se crea la caperta __pycache__
# Para cambiarle el apodo a algún modulo al hacer referencia a él, se usa "as", como en nuestro ejemplo

# Para importar algo muy concreto se puede usar from {modulo} import {lo que quieres saludar}, [puedes elegir qué más importar]
# as también fiuncionará con funciones, metodos, etc. que importes

# se puede importar todo con *
# Si tienes dos cosas con el mismo nombre (eg. función y variable) te lanzará un excepción. Para evitar esto hay muchas metodología, por ejemplo Mayuculas al pricipio para funciones, 

# accediendo al nombre del modulo actual, y al del modulo llamado
print(__name__)
print(sald.__name__)