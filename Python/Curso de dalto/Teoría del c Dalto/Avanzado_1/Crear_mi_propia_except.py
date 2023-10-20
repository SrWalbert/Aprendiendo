# Como vimos en POO las clases se crean con semi camelCase
# Va a heredar la clase Exception
class MiExeception(Exception):
    def __init__(self, err):
        print(f"Comentiste el siguiente error: {err}")


# raise lanza excepciones

try:
    raise
except:
    MiExeception("Error code w1e")
