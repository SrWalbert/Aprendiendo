import sys
import algoritmos as al


def main(*args: None) -> int:
    print(
        al.en_vigenere(
            "Ellas",
            "Lorem ipsum dolor sit amet",
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
