"MRO: method resolutio order"

# Cuando tenemos diferentes métodos que tienen el mismo nombre pero en diferentes clases, y hay una subclase que hereda esos métodos, cuál es el metodo que elegirá python al llamar al método
# Es el orden de las prioridades que se ejecutan, esto es escencial para entender la herencia


class A:
    def hablar(self):
        print("Hola, este es un texto de la clase A")


class B(A):
    def hablar(self):
        print("Hola, este es un texto de la clase B")


class C(A):
    def hablar(self):
        print("Hola, este es un texto de la clase C")


class D(B, C):
    def hablar(self):
        print("Hola, este es un texto de la clase D")


d = D()  # al D sobreescribir todo, esto sale por pura lógica
d.hablar()


class D(B, C):
    pass


d = D()
# Ahora que la clase D no está definida, pasa a clase que se menciona primiero, en este caso B
# Si fuese

# class D(C, B):
#     pass

# Entonces heredaría C
d.hablar()
# Si fuese un árbol más extenso, se busca de la rama principal al padre, si no existe, se busca de las secundarias (en este caso si C tuviese rama [superclase F], al no encontrar atributo en A, se buscaría en F)

print("-------------\n")


print(D.mro())
# Para ve la secuencia se usa la clase y se le aplica el método .mro() , como puedes var arriva


print("\n-------------")
# Para poder elejir la secuencia puedes escribir de la siguiente manera
# Clase.metodo(objeto)

B.hablar(d)

"Continúa en Intermedio_poo_1"
