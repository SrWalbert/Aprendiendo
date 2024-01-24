import sys
import algoritmios as al


def main(*args: None) -> int:
    print(
        al.en_vigenere(
            "MiVidaEsTuya",
            "Hola capitan, necesitamos refuerzos en las coordenadas quinentos sur, ochenta oeste; sector seiscientos ocho. Artilleria ya",
        )
    )
    print(
        al.desen_vigenere(
            "MiVidaEsTuya", "uxhj dficozo, jngfxbnvlpf nnjvjktjr rw uet vijqerwwmet jodmfackb tzk, ndunjce txmod; balxpw mzhtprawxpx ixgp. waxjqeymhb hw"
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
