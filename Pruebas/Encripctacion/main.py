import sys
import algoritmios as al


def main(*args: None) -> int:
    print(
        al.en_viguenere(
            "MiVidaEsTuya",
            "Hola capitan, necesitamos refuerzos en las coordenadas quinentos sur, ochenta oeste; sector seiscientos ocho. Artilleria ya",
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
