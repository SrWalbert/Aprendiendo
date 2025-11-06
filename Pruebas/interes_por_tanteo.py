import sys


def resolver_ecuacion_por_biseccion(
    C, n, limite_inferior=0.0, limite_superior=1.0, tolerancia=1e-4
):
    def f(x):
        if x == 0:
            return 0
        return (1 + x) ** n - 1 - C * x

    val_inf = f(limite_inferior)
    val_sup = f(limite_superior)

    if val_inf * val_sup > 0:
        limite_inferior_ajustado = 1e-9
        val_inf_ajustado = f(limite_inferior_ajustado)
        if val_inf_ajustado * val_sup > 0:
            print(
                f"No se puede garantizar una raíz en el intervalo [{limite_inferior}, {limite_superior}]."
            )
            return None
        else:
            limite_inferior = limite_inferior_ajustado
            val_inf = val_inf_ajustado

    while (limite_superior - limite_inferior) > tolerancia:
        punto_medio = (limite_inferior + limite_superior) / 2
        val_medio = f(punto_medio)
        if val_medio == 0:
            return punto_medio
        if val_inf * val_medio < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio
            val_inf = val_medio
    return (limite_inferior + limite_superior) / 2


def main(*args: None) -> int:

    C = 178550.21 / 25000
    n = 6
    exactitud = 1e-5

    print("--- BÚSQUEDA CON INTERVALO AJUSTADO [0, 0.1] ---")
    solucion_x = resolver_ecuacion_por_biseccion(
        C, n, limite_inferior=0.0, limite_superior=0.1, tolerancia=exactitud
    )

    if solucion_x is not None:
        print(f"RESULTADO:")
        print(f"La solución aproximada para x es: {solucion_x:.6f}")

        lado_izquierdo = C * solucion_x
        lado_derecho = (1 + solucion_x) ** n - 1
        diferencia = abs(lado_izquierdo - lado_derecho)

        print("\nVERIFICACIÓN:")
        print(f"Lado izquierdo ({C:.6f} * {solucion_x:.6f}): {lado_izquierdo:.6f}")
        print(f"Lado derecho ((1 + {solucion_x:.6f})^{n} - 1): {lado_derecho:.6f}")
        print(f"Diferencia absoluta: {diferencia:.8f}")
        if diferencia < exactitud:
            print("La solución es correcta dentro de la tolerancia especificada.")
        else:
            print("La solución tiene una diferencia mayor a la tolerancia.")
    else:
        print("No se pudo encontrar una solución en el intervalo especificado.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
